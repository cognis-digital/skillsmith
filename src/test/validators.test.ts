import { test } from "node:test";
import assert from "node:assert/strict";
import {
  validateFrontmatter,
  extractLocalLinks,
  DEFAULT_OPTIONS,
} from "../validators.js";

function errorRules(data: Record<string, unknown>): string[] {
  return validateFrontmatter(data as never)
    .filter((d) => d.level === "error")
    .map((d) => d.rule);
}

test("valid frontmatter has no errors", () => {
  const data = {
    name: "good-skill",
    description: "A sufficiently long description for the skill.",
    version: "1.0.0",
  };
  assert.deepEqual(errorRules(data), []);
});

test("missing required fields flagged", () => {
  const rules = errorRules({});
  assert.ok(rules.includes("required-field"));
});

test("non-kebab name flagged", () => {
  const rules = errorRules({
    name: "BadName",
    description: "A sufficiently long description here.",
  });
  assert.ok(rules.includes("name-format"));
});

test("short description flagged", () => {
  const rules = errorRules({ name: "ok-name", description: "too short" });
  assert.ok(rules.includes("description-length"));
});

test("over-long description flagged", () => {
  const rules = errorRules({
    name: "ok-name",
    description: "x".repeat(DEFAULT_OPTIONS.descriptionMaxLength + 1),
  });
  assert.ok(rules.includes("description-length"));
});

test("bad version is warning not error", () => {
  const diags = validateFrontmatter({
    name: "ok-name",
    description: "A sufficiently long description here.",
    version: "not-semver",
  } as never);
  assert.equal(diags.filter((d) => d.level === "error").length, 0);
  assert.ok(diags.some((d) => d.rule === "version-format" && d.level === "warning"));
});

test("extracts local links and skips external/anchors", () => {
  const body = `
See [local](./other.md) and [deep](docs/guide.md).
Also [site](https://example.com) and [top](#section) and [mail](mailto:a@b.c).
`;
  const links = extractLocalLinks(body);
  assert.deepEqual(
    links.map((l) => l.target),
    ["./other.md", "docs/guide.md"],
  );
});
