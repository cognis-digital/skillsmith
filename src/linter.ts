/**
 * Skill linter: combines frontmatter validation, structure checks, and
 * broken-local-link detection into a single report.
 */

import * as fs from "node:fs";
import * as path from "node:path";
import { parseFrontmatter, FrontmatterError } from "./frontmatter.js";
import { loadSkill, type LoadedSkill } from "./skill.js";
import {
  validateFrontmatter,
  extractLocalLinks,
  DEFAULT_OPTIONS,
  type Diagnostic,
  type ValidationOptions,
} from "./validators.js";

export interface LintReport {
  target: string;
  filePath: string | null;
  diagnostics: Diagnostic[];
  errorCount: number;
  warningCount: number;
  ok: boolean;
}

/** Lint a single skill (directory or file). */
export function lintSkill(
  target: string,
  options: ValidationOptions = DEFAULT_OPTIONS,
): LintReport {
  const diagnostics: Diagnostic[] = [];
  let skill: LoadedSkill | null = null;

  try {
    skill = loadSkill(target);
  } catch (err) {
    diagnostics.push({
      level: "error",
      rule: "load",
      message: err instanceof Error ? err.message : String(err),
    });
    return finalize(target, null, diagnostics);
  }

  // Frontmatter presence.
  if (!skill.doc.hasFrontmatter) {
    diagnostics.push({
      level: "error",
      rule: "frontmatter-missing",
      message: "No YAML frontmatter block (file must start with '---')",
    });
  } else {
    diagnostics.push(...validateFrontmatter(skill.doc.data, options));
  }

  // Body must contain something beyond frontmatter.
  if (skill.doc.body.trim() === "") {
    diagnostics.push({
      level: "warning",
      rule: "empty-body",
      message: "Skill body is empty; add instructions below the frontmatter",
    });
  }

  // Broken local links.
  diagnostics.push(...checkLocalLinks(skill));

  return finalize(target, skill.filePath, diagnostics);
}

/** Parse frontmatter purely to surface syntax errors with line numbers. */
export function lintFrontmatterSyntax(source: string): Diagnostic[] {
  try {
    parseFrontmatter(source);
    return [];
  } catch (err) {
    if (err instanceof FrontmatterError) {
      return [{ level: "error", rule: "frontmatter-syntax", message: err.message }];
    }
    return [
      {
        level: "error",
        rule: "frontmatter-syntax",
        message: err instanceof Error ? err.message : String(err),
      },
    ];
  }
}

function checkLocalLinks(skill: LoadedSkill): Diagnostic[] {
  const diags: Diagnostic[] = [];
  const links = extractLocalLinks(skill.doc.body);
  for (const link of links) {
    // Strip any anchor fragment before resolving.
    const cleanTarget = link.target.split("#")[0];
    if (cleanTarget === "") continue; // pure in-page anchor
    const resolved = path.resolve(skill.dir, cleanTarget);
    if (!fs.existsSync(resolved)) {
      diags.push({
        level: "error",
        rule: "broken-link",
        message: `Broken local link: "${link.target}" -> ${resolved} not found`,
      });
    }
  }
  return diags;
}

function finalize(
  target: string,
  filePath: string | null,
  diagnostics: Diagnostic[],
): LintReport {
  const errorCount = diagnostics.filter((d) => d.level === "error").length;
  const warningCount = diagnostics.filter((d) => d.level === "warning").length;
  return {
    target,
    filePath,
    diagnostics,
    errorCount,
    warningCount,
    ok: errorCount === 0,
  };
}
