/**
 * Skill packager: produces a versioned package manifest describing a skill
 * directory's files and their content hashes. This is a manifest (no actual
 * tarball compression) suitable for integrity verification and distribution.
 */

import * as fs from "node:fs";
import * as path from "node:path";
import * as crypto from "node:crypto";
import { loadSkill } from "./skill.js";

export interface PackagedFile {
  /** Path relative to the skill directory, using forward slashes. */
  path: string;
  /** Byte size of the file. */
  size: number;
  /** Hex-encoded hash digest of the file contents. */
  hash: string;
}

export interface PackageManifest {
  manifestVersion: 1;
  name: string;
  version: string;
  description: string | null;
  /** Algorithm used for file hashes. */
  hashAlgorithm: string;
  /** Sorted list of packaged files. */
  files: PackagedFile[];
  /** Total byte size across all files. */
  totalSize: number;
  /** Hash over the file list (an integrity digest for the whole package). */
  integrity: string;
  /** ISO timestamp the manifest was generated. */
  createdAt: string;
}

export interface PackOptions {
  /** Override version when frontmatter lacks one. Defaults to "0.0.0". */
  defaultVersion?: string;
  hashAlgorithm?: string;
  /** Names to skip during packaging. */
  ignore?: string[];
}

const DEFAULT_IGNORE = ["node_modules", ".git", ".DS_Store"];

/** Build a package manifest for a skill directory. */
export function packSkill(target: string, options: PackOptions = {}): PackageManifest {
  const skill = loadSkill(target);
  const algo = options.hashAlgorithm ?? "sha256";
  const ignore = new Set([...DEFAULT_IGNORE, ...(options.ignore ?? [])]);

  const name = typeof skill.doc.data["name"] === "string"
    ? (skill.doc.data["name"] as string)
    : path.basename(skill.dir);

  const versionRaw = skill.doc.data["version"];
  const version =
    versionRaw !== undefined && versionRaw !== null
      ? String(versionRaw)
      : options.defaultVersion ?? "0.0.0";

  const description =
    typeof skill.doc.data["description"] === "string"
      ? (skill.doc.data["description"] as string)
      : null;

  const files = collectFiles(skill.dir, ignore, algo);
  const totalSize = files.reduce((sum, f) => sum + f.size, 0);

  // Integrity digest: hash of "path:hash" lines, deterministic & order-stable.
  const integrityInput = files.map((f) => `${f.path}:${f.hash}`).join("\n");
  const integrity = `${algo}-${hash(algo, Buffer.from(integrityInput, "utf8"))}`;

  return {
    manifestVersion: 1,
    name,
    version,
    description,
    hashAlgorithm: algo,
    files,
    totalSize,
    integrity,
    createdAt: new Date().toISOString(),
  };
}

/** Recursively collect files under `dir`, hashing each. */
function collectFiles(
  dir: string,
  ignore: Set<string>,
  algo: string,
): PackagedFile[] {
  const out: PackagedFile[] = [];

  const walk = (current: string): void => {
    const entries = fs.readdirSync(current, { withFileTypes: true });
    for (const entry of entries) {
      if (ignore.has(entry.name)) continue;
      const abs = path.join(current, entry.name);
      if (entry.isDirectory()) {
        walk(abs);
      } else if (entry.isFile()) {
        const data = fs.readFileSync(abs);
        const rel = path.relative(dir, abs).split(path.sep).join("/");
        out.push({ path: rel, size: data.length, hash: hash(algo, data) });
      }
    }
  };

  walk(dir);
  out.sort((a, b) => a.path.localeCompare(b.path));
  return out;
}

function hash(algo: string, data: Buffer): string {
  return crypto.createHash(algo).update(data).digest("hex");
}
