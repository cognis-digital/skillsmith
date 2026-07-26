---
name: pattern-quoting
description: "Control word-splitting and expansion with single quotes, double quotes, and escaping."
version: 1.0.0
tags: [bash, command-structure, pattern, shell]
---

# Pattern: Quoting

## Overview

Quoting decides what the shell expands and how it splits words. Getting it right is
the difference between a robust script and one that breaks on a space or a `*`.

## Rules

- `'single'` — fully literal; nothing expands.
- `"double"` — expands `$var`, `$(cmd)`, `` `cmd` ``, but keeps the result as one
  word and prevents globbing.
- `\` — escape the next character.
- Unquoted — expands **and** word-splits **and** globs. Rarely what you want for
  variables.

## Worked examples

```bash
echo "$HOME/my file"      # one argument, expanded
echo '$HOME stays literal'
rm -- "$path"             # survives spaces; -- stops option parsing
find . -name '*.py'       # quote the glob so find (not the shell) expands it
```

## The one rule to remember

> Quote every variable expansion — `"$var"`, `"${arr[@]}"`, `"$(cmd)"` — unless you
> have a specific reason to want splitting or globbing.

## Pitfalls

- Unquoted `$var` with an empty value can vanish entirely, shifting arguments.
