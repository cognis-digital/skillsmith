# skillsmith

An authoring toolkit for AI-agent **skills**. A skill is a directory containing
a markdown instruction file (`SKILL.md` by convention) with YAML frontmatter
carrying at minimum a `name` and a `description`, plus optional metadata such as
`version` and `tags`.

`skillsmith` helps you author and ship those skills with confidence:

- **lint** — validate frontmatter, structure, and local links (CI gate).
- **new** — scaffold a new skill from a template.
- **pack** — produce a versioned package manifest with per-file content hashes.
- **list** — discover and tabulate skills under a root directory.

It is written in TypeScript, compiles to ESM with `tsc`, and has **zero runtime
dependencies** (the YAML-frontmatter reader is implemented in-house).

## Install / build

Requires Node.js >= 20.

```bash
npm install
npm run build      # tsc -> dist/
npm test           # node --test "dist/test/*.test.js"
```

Run the CLI from the build output:

```bash
node dist/cli.js <command> ...
```

Once published, the `skillsmith` bin is available globally after a global
install.

## Usage

### Lint a skill (CI gate)

`lint` checks that the frontmatter is present and well-formed, that required
fields exist, that `name` is kebab-case and within length bounds, that
`description` is within length bounds, and that every local markdown link
resolves. It exits non-zero when there are errors, so it slots straight into CI.
Add `--strict` to also fail on warnings.

```text
$ skillsmith lint examples/skills/summarize-document
.../examples/skills/summarize-document/SKILL.md
  OK — no issues found

0 error(s), 0 warning(s)
```

A skill with a broken local link:

```text
$ skillsmith lint ./my-skill
.../my-skill/SKILL.md
  error [broken-link] Broken local link: "./nope.md" -> .../my-skill/nope.md not found

1 error(s), 0 warning(s)
# exit code: 1
```

### Scaffold a new skill

```text
$ skillsmith new summarize-document --desc "Summarize a long document faithfully."
Created skill "summarize-document"
  + /cwd/summarize-document
  + /cwd/summarize-document/SKILL.md
```

Flags: `--dir <parent>`, `--desc <text>`, `--version <v>`, `--force`.

### Package a skill

`pack` walks the skill directory, hashes each file, and emits a deterministic
JSON manifest. An `integrity` digest is computed over the file list so the whole
package can be verified.

```text
$ skillsmith pack examples/skills/summarize-document
{
  "manifestVersion": 1,
  "name": "summarize-document",
  "version": "1.0.0",
  "description": "Produce a faithful, concise summary of a long document ...",
  "hashAlgorithm": "sha256",
  "files": [
    { "path": "SKILL.md", "size": 985, "hash": "6bbb0dc8..." },
    { "path": "STYLE.md", "size": 268, "hash": "c866066a..." }
  ],
  "totalSize": 1253,
  "integrity": "sha256-3e2f030f...",
  "createdAt": "2026-06-19T19:45:00.000Z"
}
```

Write to a file with `--out manifest.json`, or override the version when the
frontmatter has none with `--version <v>`.

### List skills under a root

```text
$ skillsmith list examples/skills
NAME                VERSION  DESCRIPTION
------------------  -------  ------------------------------------------------------------
summarize-document  1.0.0    Produce a faithful, concise summary of a long document whil…

1 skill(s)
```

Flags: `--recursive` (walk nested directories), `--json` (machine-readable
output).

## Library

The package also exports a small, reusable library (see `src/index.ts`):

- `parseFrontmatter(source)` — minimal in-house YAML-frontmatter reader.
- `validateFrontmatter(data, options?)` / `extractLocalLinks(body)` — validators.
- `loadSkill(target)` / `discoverSkills(root, recursive?)` — discovery.
- `lintSkill(target, options?)` — full lint report.
- `packSkill(target, options?)` — package manifest.
- `scaffoldSkill(name, parentDir, options?)` — scaffolder.

## Features

- Dependency-free YAML-frontmatter parser: scalars, quoted strings, block lists,
  inline flow lists, comments, CRLF normalization, and clear syntax errors with
  line numbers.
- Frontmatter validation: required fields, kebab-case `name`, length bounds for
  `name`/`description`, semver-ish `version` (warning), `tags` shape (warning).
- Structure validation: locates the primary instruction file
  (`SKILL.md`/`skill.md`/`README.md` or a single `*.md`), flags empty bodies.
- Broken local-link detection (skips external URLs, `mailto:`, and anchors).
- Versioned package manifest with per-file content hashes and a stable
  package-level integrity digest.
- Skill scaffolding with a section skeleton and valid frontmatter.
- Skill discovery and tabular/JSON listing.
- Tests with Node's built-in `node:test`, run over the compiled
  `dist/test/*.test.js`.

## Examples

`examples/skills/summarize-document/` is a complete, lint-clean sample skill you
can lint, list, and pack out of the box.

## License

License: COCL 1.0

Maintainer: Cognis Digital
