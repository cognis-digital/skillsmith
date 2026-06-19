/**
 * Validation rules for skill frontmatter and structure.
 *
 * A "skill" is a directory containing a markdown instruction file (SKILL.md by
 * convention) with YAML frontmatter carrying at minimum `name` and
 * `description`.
 */

import type { FrontmatterValue } from "./frontmatter.js";

/** A single diagnostic produced by a check. */
export interface Diagnostic {
  level: "error" | "warning";
  rule: string;
  message: string;
}

/** Tunable limits for description-length checks. */
export interface ValidationOptions {
  descriptionMinLength: number;
  descriptionMaxLength: number;
  nameMaxLength: number;
}

export const DEFAULT_OPTIONS: ValidationOptions = {
  descriptionMinLength: 20,
  descriptionMaxLength: 1024,
  nameMaxLength: 64,
};

/** kebab-case: lowercase alphanumerics separated by single hyphens. */
const KEBAB_CASE = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

const REQUIRED_FIELDS = ["name", "description"] as const;

/**
 * Validate a frontmatter data object. Returns diagnostics (errors + warnings).
 */
export function validateFrontmatter(
  data: Record<string, FrontmatterValue>,
  options: ValidationOptions = DEFAULT_OPTIONS,
): Diagnostic[] {
  const diags: Diagnostic[] = [];

  // Required fields present and non-empty.
  for (const field of REQUIRED_FIELDS) {
    const value = data[field];
    if (value === undefined || value === null || value === "") {
      diags.push({
        level: "error",
        rule: "required-field",
        message: `Missing required frontmatter field "${field}"`,
      });
    }
  }

  // name: must be a kebab-case string within length bound.
  const name = data["name"];
  if (typeof name === "string" && name !== "") {
    if (!KEBAB_CASE.test(name)) {
      diags.push({
        level: "error",
        rule: "name-format",
        message: `"name" must be kebab-case (got "${name}")`,
      });
    }
    if (name.length > options.nameMaxLength) {
      diags.push({
        level: "error",
        rule: "name-length",
        message: `"name" exceeds ${options.nameMaxLength} characters (got ${name.length})`,
      });
    }
  } else if (name !== undefined && name !== null && name !== "") {
    diags.push({
      level: "error",
      rule: "name-type",
      message: `"name" must be a string`,
    });
  }

  // description: string within bounds.
  const description = data["description"];
  if (typeof description === "string" && description !== "") {
    if (description.length < options.descriptionMinLength) {
      diags.push({
        level: "error",
        rule: "description-length",
        message: `"description" is too short (${description.length} < ${options.descriptionMinLength})`,
      });
    }
    if (description.length > options.descriptionMaxLength) {
      diags.push({
        level: "error",
        rule: "description-length",
        message: `"description" is too long (${description.length} > ${options.descriptionMaxLength})`,
      });
    }
  } else if (description !== undefined && description !== null && description !== "") {
    diags.push({
      level: "error",
      rule: "description-type",
      message: `"description" must be a string`,
    });
  }

  // version (optional): if present, must look like semver-ish.
  const version = data["version"];
  if (version !== undefined && version !== null) {
    const vstr = String(version);
    if (!/^\d+\.\d+\.\d+(?:[-+].+)?$/.test(vstr)) {
      diags.push({
        level: "warning",
        rule: "version-format",
        message: `"version" should be semver (e.g. 1.0.0); got "${vstr}"`,
      });
    }
  }

  // tags (optional): if present, must be a list of kebab-ish strings.
  const tags = data["tags"];
  if (tags !== undefined && tags !== null) {
    if (!Array.isArray(tags)) {
      diags.push({
        level: "warning",
        rule: "tags-type",
        message: `"tags" should be a list`,
      });
    } else {
      for (const tag of tags) {
        if (typeof tag !== "string" || tag.trim() === "") {
          diags.push({
            level: "warning",
            rule: "tags-entry",
            message: `"tags" entries should be non-empty strings`,
          });
          break;
        }
      }
    }
  }

  return diags;
}

/** Local markdown links of the form [text](path) where path is not a URL/anchor. */
export interface LocalLink {
  text: string;
  target: string;
}

/** Extract local (non-URL, non-anchor) markdown links from body text. */
export function extractLocalLinks(body: string): LocalLink[] {
  const links: LocalLink[] = [];
  const re = /\[([^\]]*)\]\(([^)]+)\)/g;
  let m: RegExpExecArray | null;
  while ((m = re.exec(body)) !== null) {
    const target = m[2].trim();
    // Skip external URLs, protocol-relative, mailto, and pure anchors.
    if (
      /^[a-z][a-z0-9+.-]*:\/\//i.test(target) ||
      target.startsWith("//") ||
      target.startsWith("mailto:") ||
      target.startsWith("#")
    ) {
      continue;
    }
    links.push({ text: m[1], target });
  }
  return links;
}
