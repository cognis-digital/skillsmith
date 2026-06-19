#!/usr/bin/env node
/**
 * skillsmith CLI.
 *
 * Commands:
 *   lint <skill-dir|file> [--strict]   Lint a skill; non-zero exit on error.
 *   new  <name> [--dir <d>] [--desc <text>] [--version <v>] [--force]
 *   pack <skill-dir> [--out <file>] [--version <v>]
 *   list <skills-root> [--recursive] [--json]
 *   help | --help | -h
 *   version | --version | -v
 */

import * as fs from "node:fs";
import * as path from "node:path";
import { lintSkill } from "./linter.js";
import { packSkill } from "./packager.js";
import { discoverSkills } from "./skill.js";
import { scaffoldSkill } from "./scaffold.js";

const PROG = "skillsmith";
const VERSION = "0.1.0";

interface ParsedArgs {
  positionals: string[];
  flags: Record<string, string | boolean>;
}

/** Minimal arg parser: `--flag`, `--flag value`, `--flag=value`. */
function parseArgs(argv: string[]): ParsedArgs {
  const positionals: string[] = [];
  const flags: Record<string, string | boolean> = {};
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg.startsWith("--")) {
      const eq = arg.indexOf("=");
      if (eq !== -1) {
        flags[arg.slice(2, eq)] = arg.slice(eq + 1);
      } else {
        const key = arg.slice(2);
        const next = argv[i + 1];
        if (next !== undefined && !next.startsWith("--")) {
          flags[key] = next;
          i++;
        } else {
          flags[key] = true;
        }
      }
    } else {
      positionals.push(arg);
    }
  }
  return { positionals, flags };
}

function main(): number {
  const [, , command, ...rest] = process.argv;
  const { positionals, flags } = parseArgs(rest);

  switch (command) {
    case "lint":
      return cmdLint(positionals, flags);
    case "new":
      return cmdNew(positionals, flags);
    case "pack":
      return cmdPack(positionals, flags);
    case "list":
      return cmdList(positionals, flags);
    case "version":
    case "--version":
    case "-v":
      process.stdout.write(`${PROG} ${VERSION}\n`);
      return 0;
    case "help":
    case "--help":
    case "-h":
    case undefined:
      printHelp();
      return command === undefined ? 1 : 0;
    default:
      process.stderr.write(`${PROG}: unknown command "${command}"\n\n`);
      printHelp();
      return 1;
  }
}

function cmdLint(positionals: string[], flags: Record<string, string | boolean>): number {
  const target = positionals[0];
  if (!target) {
    process.stderr.write(`${PROG} lint: missing <skill-dir|file>\n`);
    return 2;
  }
  const strict = Boolean(flags["strict"]);
  const report = lintSkill(target);

  const header = report.filePath ?? target;
  process.stdout.write(`${header}\n`);

  if (report.diagnostics.length === 0) {
    process.stdout.write("  OK — no issues found\n");
  }
  for (const d of report.diagnostics) {
    const tag = d.level === "error" ? "error" : "warn ";
    process.stdout.write(`  ${tag} [${d.rule}] ${d.message}\n`);
  }

  process.stdout.write(
    `\n${report.errorCount} error(s), ${report.warningCount} warning(s)\n`,
  );

  if (report.errorCount > 0) return 1;
  if (strict && report.warningCount > 0) return 1;
  return 0;
}

function cmdNew(positionals: string[], flags: Record<string, string | boolean>): number {
  const name = positionals[0];
  if (!name) {
    process.stderr.write(`${PROG} new: missing <name>\n`);
    return 2;
  }
  const parentDir =
    typeof flags["dir"] === "string" ? (flags["dir"] as string) : process.cwd();
  try {
    const result = scaffoldSkill(name, parentDir, {
      description: typeof flags["desc"] === "string" ? (flags["desc"] as string) : undefined,
      version: typeof flags["version"] === "string" ? (flags["version"] as string) : undefined,
      force: Boolean(flags["force"]),
    });
    process.stdout.write(`Created skill "${name}"\n`);
    for (const c of result.created) {
      process.stdout.write(`  + ${c}\n`);
    }
    return 0;
  } catch (err) {
    process.stderr.write(`${PROG} new: ${errMsg(err)}\n`);
    return 1;
  }
}

function cmdPack(positionals: string[], flags: Record<string, string | boolean>): number {
  const target = positionals[0];
  if (!target) {
    process.stderr.write(`${PROG} pack: missing <skill-dir>\n`);
    return 2;
  }
  try {
    const manifest = packSkill(target, {
      defaultVersion:
        typeof flags["version"] === "string" ? (flags["version"] as string) : undefined,
    });
    const json = JSON.stringify(manifest, null, 2);
    const out = flags["out"];
    if (typeof out === "string") {
      fs.writeFileSync(out, json + "\n", "utf8");
      process.stdout.write(
        `Packaged "${manifest.name}" v${manifest.version} (${manifest.files.length} files) -> ${out}\n`,
      );
    } else {
      process.stdout.write(json + "\n");
    }
    return 0;
  } catch (err) {
    process.stderr.write(`${PROG} pack: ${errMsg(err)}\n`);
    return 1;
  }
}

function cmdList(positionals: string[], flags: Record<string, string | boolean>): number {
  const root = positionals[0];
  if (!root) {
    process.stderr.write(`${PROG} list: missing <skills-root>\n`);
    return 2;
  }
  try {
    const skills = discoverSkills(root, Boolean(flags["recursive"]));
    const rows = skills.map((s) => {
      const name =
        typeof s.doc.data["name"] === "string"
          ? (s.doc.data["name"] as string)
          : path.basename(s.dir);
      const version =
        s.doc.data["version"] !== undefined && s.doc.data["version"] !== null
          ? String(s.doc.data["version"])
          : "-";
      const description =
        typeof s.doc.data["description"] === "string"
          ? (s.doc.data["description"] as string)
          : "";
      return { name, version, description, dir: s.dir };
    });

    if (flags["json"]) {
      process.stdout.write(JSON.stringify(rows, null, 2) + "\n");
      return 0;
    }

    if (rows.length === 0) {
      process.stdout.write(`No skills found under ${root}\n`);
      return 0;
    }

    process.stdout.write(renderTable(rows));
    process.stdout.write(`\n${rows.length} skill(s)\n`);
    return 0;
  } catch (err) {
    process.stderr.write(`${PROG} list: ${errMsg(err)}\n`);
    return 1;
  }
}

interface TableRow {
  name: string;
  version: string;
  description: string;
  dir: string;
}

/** Render a simple fixed-width text table. */
function renderTable(rows: TableRow[]): string {
  const headers = { name: "NAME", version: "VERSION", description: "DESCRIPTION" };
  const truncate = (s: string, n: number): string =>
    s.length > n ? s.slice(0, n - 1) + "…" : s;

  const descMax = 60;
  const display = rows.map((r) => ({
    name: r.name,
    version: r.version,
    description: truncate(r.description.replace(/\s+/g, " ").trim(), descMax),
  }));

  const nameW = Math.max(headers.name.length, ...display.map((r) => r.name.length));
  const verW = Math.max(headers.version.length, ...display.map((r) => r.version.length));
  const descW = Math.max(
    headers.description.length,
    ...display.map((r) => r.description.length),
  );

  const pad = (s: string, w: number): string => s + " ".repeat(w - s.length);
  const line = (n: string, v: string, d: string): string =>
    `${pad(n, nameW)}  ${pad(v, verW)}  ${pad(d, descW)}\n`;

  let out = line(headers.name, headers.version, headers.description);
  out += `${"-".repeat(nameW)}  ${"-".repeat(verW)}  ${"-".repeat(descW)}\n`;
  for (const r of display) {
    out += line(r.name, r.version, r.description);
  }
  return out;
}

function printHelp(): void {
  process.stdout.write(
    `${PROG} ${VERSION} — authoring toolkit for AI-agent skills

Usage:
  ${PROG} lint <skill-dir|file> [--strict]
  ${PROG} new  <name> [--dir <d>] [--desc <text>] [--version <v>] [--force]
  ${PROG} pack <skill-dir> [--out <file>] [--version <v>]
  ${PROG} list <skills-root> [--recursive] [--json]
  ${PROG} version
  ${PROG} help

Commands:
  lint   Validate frontmatter, structure, and local links. Exits non-zero on
         error (use as a CI gate). --strict also fails on warnings.
  new    Scaffold a new skill directory with a SKILL.md skeleton.
  pack   Produce a versioned package manifest (file list + content hashes).
  list   Discover and tabulate skills under a root directory.

License: COCL 1.0
`,
  );
}

function errMsg(err: unknown): string {
  return err instanceof Error ? err.message : String(err);
}

process.exit(main());
