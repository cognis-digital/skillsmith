import { test } from "node:test";
import assert from "node:assert/strict";
import { parseFrontmatter, FrontmatterError } from "../frontmatter.js";

test("parses basic scalars", () => {
  const doc = parseFrontmatter(
    `---\nname: my-skill\ndescription: A test skill\nversion: 1.2.3\n---\n# Body\n`,
  );
  assert.equal(doc.hasFrontmatter, true);
  assert.equal(doc.data.name, "my-skill");
  assert.equal(doc.data.description, "A test skill");
  assert.equal(doc.data.version, "1.2.3");
  assert.equal(doc.body.trim(), "# Body");
});

test("coerces numbers and booleans and null", () => {
  const doc = parseFrontmatter(`---\nweight: 42\nratio: 0.5\nenabled: true\noff: false\nempty:\n---\n`);
  assert.equal(doc.data.weight, 42);
  assert.equal(doc.data.ratio, 0.5);
  assert.equal(doc.data.enabled, true);
  assert.equal(doc.data.off, false);
  assert.equal(doc.data.empty, null);
});

test("parses block lists", () => {
  const doc = parseFrontmatter(`---\ntags:\n  - alpha\n  - beta\n  - gamma\n---\n`);
  assert.deepEqual(doc.data.tags, ["alpha", "beta", "gamma"]);
});

test("parses inline flow lists", () => {
  const doc = parseFrontmatter(`---\ntags: [one, "two", 'three']\n---\n`);
  assert.deepEqual(doc.data.tags, ["one", "two", "three"]);
});

test("empty inline list", () => {
  const doc = parseFrontmatter(`---\ntags: []\n---\n`);
  assert.deepEqual(doc.data.tags, []);
});

test("handles quoted strings with colons", () => {
  const doc = parseFrontmatter(`---\ndescription: "uses a: colon inside"\n---\n`);
  assert.equal(doc.data.description, "uses a: colon inside");
});

test("strips trailing comments but not inside quotes", () => {
  const doc = parseFrontmatter(
    `---\nname: foo # this is a comment\nlabel: "has # hash"\n---\n`,
  );
  assert.equal(doc.data.name, "foo");
  assert.equal(doc.data.label, "has # hash");
});

test("skips full-line comments and blanks", () => {
  const doc = parseFrontmatter(`---\n# a comment\n\nname: bar\n---\n`);
  assert.equal(doc.data.name, "bar");
});

test("no frontmatter yields empty data", () => {
  const doc = parseFrontmatter(`# Just markdown\nNo frontmatter here.\n`);
  assert.equal(doc.hasFrontmatter, false);
  assert.deepEqual(doc.data, {});
});

test("CRLF normalization", () => {
  const doc = parseFrontmatter(`---\r\nname: crlf-skill\r\n---\r\nbody\r\n`);
  assert.equal(doc.data.name, "crlf-skill");
});

test("throws on unterminated block", () => {
  assert.throws(() => parseFrontmatter(`---\nname: x\nno closing fence\n`), FrontmatterError);
});

test("throws on duplicate key", () => {
  assert.throws(() => parseFrontmatter(`---\nname: a\nname: b\n---\n`), FrontmatterError);
});

test("throws on missing colon", () => {
  assert.throws(() => parseFrontmatter(`---\nthisIsNotValid\n---\n`), FrontmatterError);
});
