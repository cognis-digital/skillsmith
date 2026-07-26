---
name: pattern-globbing
description: "Match sets of filenames with shell wildcard patterns."
version: 1.0.0
tags: [bash, command-structure, pattern, shell]
---

# Pattern: Globbing (`*`, `?`, `[...]`, `**`)

## Overview

The shell expands wildcard patterns into matching filenames before the command
runs. This is filename generation, distinct from regular expressions.

## Operators

- `*` — any run of characters (not `/`).
- `?` — any single character.
- `[abc]` / `[a-z]` — one character from a set/range.
- `**` — recursive match (requires `shopt -s globstar` in bash).
- `{a,b}` — brace expansion (not a glob, but often used together).

## Worked examples

```bash
ls *.py                 # every python file here
cp img_?.png backup/    # single-digit variants
shopt -s globstar; ls **/*.md   # recursive
rm -- *.tmp             # -- guards against filenames starting with -
```

## Pitfalls

- An unmatched glob is passed through **literally** by default; set
  `shopt -s nullglob` to expand to nothing instead.
- Globs are not regex: `*.txt` is anchored to whole names, `.` is literal.
- Always quote variables; never quote the glob you want expanded.
