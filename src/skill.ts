/**
 * Skill discovery and loading.
 *
 * A skill lives in a directory and is identified by a primary instruction file.
 * By convention this is `SKILL.md`, but `skill.md` and a lone `*.md` file in a
 * directory are also recognized.
 */

import * as fs from "node:fs";
import * as path from "node:path";
import { parseFrontmatter, type FrontmatterDocument } from "./frontmatter.js";

/** Candidate names for a skill's primary instruction file, in priority order. */
export const PRIMARY_FILE_NAMES = ["SKILL.md", "skill.md", "README.md"];

export interface LoadedSkill {
  /** Absolute path to the primary markdown file. */
  filePath: string;
  /** Absolute path to the skill's root directory. */
  dir: string;
  /** Parsed frontmatter + body. */
  doc: FrontmatterDocument;
  /** Raw source of the primary file. */
  source: string;
}

/**
 * Resolve the primary instruction file for a path that may be either a
 * directory or a markdown file. Returns null if none can be found.
 */
export function resolvePrimaryFile(target: string): string | null {
  const stat = safeStat(target);
  if (!stat) return null;

  if (stat.isFile()) {
    return path.resolve(target);
  }

  if (stat.isDirectory()) {
    // Preferred well-known names first.
    for (const name of PRIMARY_FILE_NAMES) {
      const candidate = path.join(target, name);
      if (safeStat(candidate)?.isFile()) {
        return path.resolve(candidate);
      }
    }
    // Fall back to a single markdown file in the directory.
    const mds = fs
      .readdirSync(target)
      .filter((f) => f.toLowerCase().endsWith(".md"));
    if (mds.length === 1) {
      return path.resolve(path.join(target, mds[0]));
    }
  }

  return null;
}

/** Load a skill from a directory or a markdown file path. */
export function loadSkill(target: string): LoadedSkill {
  const filePath = resolvePrimaryFile(target);
  if (!filePath) {
    throw new Error(
      `No skill instruction file found at "${target}" (looked for ${PRIMARY_FILE_NAMES.join(", ")} or a single *.md)`,
    );
  }
  const source = fs.readFileSync(filePath, "utf8");
  const doc = parseFrontmatter(source);
  return {
    filePath,
    dir: path.dirname(filePath),
    doc,
    source,
  };
}

/**
 * Discover skills under a root directory. A subdirectory is treated as a skill
 * if it contains a resolvable primary file. Non-recursive beyond one level by
 * default; pass `recursive` to walk deeper.
 */
export function discoverSkills(root: string, recursive = false): LoadedSkill[] {
  const stat = safeStat(root);
  if (!stat || !stat.isDirectory()) {
    throw new Error(`Skills root "${root}" is not a directory`);
  }

  const found: LoadedSkill[] = [];
  const seen = new Set<string>();

  const visit = (dir: string, depth: number): void => {
    const primary = resolvePrimaryFile(dir);
    if (primary && !seen.has(primary)) {
      seen.add(primary);
      try {
        found.push(loadSkill(dir));
      } catch {
        // Ignore unloadable dirs during discovery.
      }
    }

    if (depth <= 0 && !recursive) return;

    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
      if (!entry.isDirectory()) continue;
      if (entry.name === "node_modules" || entry.name.startsWith(".")) continue;
      visit(path.join(dir, entry.name), depth - 1);
    }
  };

  // Visit each immediate subdirectory (depth controls recursion).
  const entries = fs.readdirSync(root, { withFileTypes: true });
  for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    if (entry.name === "node_modules" || entry.name.startsWith(".")) continue;
    visit(path.join(root, entry.name), recursive ? Infinity : 0);
  }

  return found.sort((a, b) => a.dir.localeCompare(b.dir));
}

function safeStat(p: string): fs.Stats | null {
  try {
    return fs.statSync(p);
  } catch {
    return null;
  }
}
