/**
 * Skill scaffolder: create a new skill directory with a SKILL.md containing
 * valid frontmatter and a section skeleton.
 */

import * as fs from "node:fs";
import * as path from "node:path";

export interface ScaffoldOptions {
  /** Description to embed; a placeholder is used when omitted. */
  description?: string;
  /** Skill version. Defaults to "0.1.0". */
  version?: string;
  /** Overwrite an existing SKILL.md if present. */
  force?: boolean;
}

export interface ScaffoldResult {
  dir: string;
  filePath: string;
  created: string[];
}

const KEBAB_CASE = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

/**
 * Scaffold a new skill named `name` under `parentDir`. The directory is named
 * after the skill and contains a SKILL.md.
 */
export function scaffoldSkill(
  name: string,
  parentDir: string,
  options: ScaffoldOptions = {},
): ScaffoldResult {
  if (!KEBAB_CASE.test(name)) {
    throw new Error(`Skill name "${name}" must be kebab-case (e.g. my-skill)`);
  }

  const dir = path.resolve(parentDir, name);
  const filePath = path.join(dir, "SKILL.md");
  const created: string[] = [];

  if (fs.existsSync(filePath) && !options.force) {
    throw new Error(`${filePath} already exists (use force to overwrite)`);
  }

  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
    created.push(dir);
  }

  const description =
    options.description ??
    "Describe what this skill does and when an agent should use it (at least 20 characters).";
  const version = options.version ?? "0.1.0";

  const content = renderTemplate(name, description, version);
  fs.writeFileSync(filePath, content, "utf8");
  created.push(filePath);

  return { dir, filePath, created };
}

/** Render the SKILL.md template body. */
export function renderTemplate(
  name: string,
  description: string,
  version: string,
): string {
  const title = name
    .split("-")
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
    .join(" ");

  return `---
name: ${name}
description: ${quoteIfNeeded(description)}
version: ${version}
tags: []
---

# ${title}

## Overview

Briefly explain the purpose of this skill.

## When to use

Describe the situations in which an agent should invoke this skill.

## Instructions

1. Step one.
2. Step two.
3. Step three.

## Notes

Add any constraints, caveats, or references here.
`;
}

/** Quote a YAML scalar when it contains characters that would break parsing. */
function quoteIfNeeded(value: string): string {
  if (/[:#"']/.test(value) || value.trim() !== value) {
    return JSON.stringify(value);
  }
  return value;
}
