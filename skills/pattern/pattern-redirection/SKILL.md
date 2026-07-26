---
name: pattern-redirection
description: "Redirect a command's input and output to and from files and other descriptors."
version: 1.0.0
tags: [bash, command-structure, pattern, shell]
---

# Pattern: Redirection (`>`, `>>`, `<`, `2>`, `&>`)

## Overview

Redirection wires a command's file descriptors to files instead of the terminal.
Descriptor 0 is stdin, 1 is stdout, 2 is stderr.

## Operators

- `> file` — send stdout to file (truncate).
- `>> file` — append stdout to file.
- `< file` — read stdin from file.
- `2> file` — send stderr to file.
- `2>&1` — send stderr to wherever stdout currently goes.
- `&> file` — send both stdout and stderr to file (bash).
- `2>/dev/null` — discard stderr.

## Worked examples

```bash
make > build.log 2>&1          # capture everything
./job 2>errors.log             # keep stderr separate
sort < unsorted > sorted       # both ends redirected
grep foo file 2>/dev/null      # silence permission noise
```

## Structuring it in a program

- Order matters: `>file 2>&1` differs from `2>&1 >file`. Redirections are applied
  left to right; `2>&1` copies the *current* target of fd 1.
- Log to a file and the screen at once with `... 2>&1 | tee run.log`.
- Use `exec > logfile 2>&1` at the top of a script to redirect everything after it.

## Pitfalls

- `>` truncates the file immediately, even if the command later fails — write to a
  temp file and `mv` on success when that matters.
