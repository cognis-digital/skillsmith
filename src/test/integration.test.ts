import { test } from "node:test";
import assert from "node:assert/strict";
import * as fs from "node:fs";
import * as os from "node:os";
import * as path from "node:path";
import { scaffoldSkill } from "../scaffold.js";
import { lintSkill } from "../linter.js";
import { packSkill } from "../packager.js";
import { discoverSkills, loadSkill } from "../skill.js";

function tmpdir(): string {
  return fs.mkdtempSync(path.join(os.tmpdir(), "skillsmith-test-"));
}

test("scaffold produces a lint-clean skill", () => {
  const root = tmpdir();
  try {
    const result = scaffoldSkill("sample-skill", root, {
      description: "A scaffolded sample skill that does something useful for agents.",
    });
    assert.ok(fs.existsSync(result.filePath));

    const report = lintSkill(result.dir);
    assert.equal(report.errorCount, 0, JSON.stringify(report.diagnostics));
    assert.equal(report.ok, true);
  } finally {
    fs.rmSync(root, { recursive: true, force: true });
  }
});

test("scaffold refuses non-kebab names", () => {
  const root = tmpdir();
  try {
    assert.throws(() => scaffoldSkill("Bad_Name", root));
  } finally {
    fs.rmSync(root, { recursive: true, force: true });
  }
});

test("lint flags a broken local link", () => {
  const root = tmpdir();
  try {
    const dir = path.join(root, "linky");
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(
      path.join(dir, "SKILL.md"),
      `---\nname: linky\ndescription: A skill with a broken link reference inside.\n---\nSee [missing](./nope.md).\n`,
      "utf8",
    );
    const report = lintSkill(dir);
    assert.ok(report.diagnostics.some((d) => d.rule === "broken-link"));
    assert.equal(report.ok, false);
  } finally {
    fs.rmSync(root, { recursive: true, force: true });
  }
});

test("lint reports missing frontmatter", () => {
  const root = tmpdir();
  try {
    const dir = path.join(root, "nofm");
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(path.join(dir, "SKILL.md"), `# No frontmatter\n`, "utf8");
    const report = lintSkill(dir);
    assert.ok(report.diagnostics.some((d) => d.rule === "frontmatter-missing"));
  } finally {
    fs.rmSync(root, { recursive: true, force: true });
  }
});

test("pack produces a deterministic manifest with hashes", () => {
  const root = tmpdir();
  try {
    scaffoldSkill("packable", root, {
      description: "A packable skill used to verify the manifest generator output.",
      version: "2.3.4",
    });
    const dir = path.join(root, "packable");
    fs.writeFileSync(path.join(dir, "extra.txt"), "hello", "utf8");

    const m1 = packSkill(dir);
    assert.equal(m1.name, "packable");
    assert.equal(m1.version, "2.3.4");
    assert.equal(m1.files.length, 2);
    assert.ok(m1.files.every((f) => /^[0-9a-f]{64}$/.test(f.hash)));
    assert.ok(m1.integrity.startsWith("sha256-"));

    const m2 = packSkill(dir);
    assert.equal(m1.integrity, m2.integrity, "integrity should be stable");
  } finally {
    fs.rmSync(root, { recursive: true, force: true });
  }
});

test("discover finds multiple skills under a root", () => {
  const root = tmpdir();
  try {
    scaffoldSkill("alpha-one", root, { description: "Alpha skill description goes here now." });
    scaffoldSkill("beta-two", root, { description: "Beta skill description goes here now." });
    const skills = discoverSkills(root);
    assert.equal(skills.length, 2);
    const names = skills.map((s) => s.doc.data.name).sort();
    assert.deepEqual(names, ["alpha-one", "beta-two"]);
  } finally {
    fs.rmSync(root, { recursive: true, force: true });
  }
});

test("loadSkill resolves a single markdown file in a dir", () => {
  const root = tmpdir();
  try {
    const dir = path.join(root, "single");
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(
      path.join(dir, "anything.md"),
      `---\nname: single\ndescription: A single markdown skill file resolved by fallback.\n---\nbody\n`,
      "utf8",
    );
    const skill = loadSkill(dir);
    assert.equal(skill.doc.data.name, "single");
  } finally {
    fs.rmSync(root, { recursive: true, force: true });
  }
});
