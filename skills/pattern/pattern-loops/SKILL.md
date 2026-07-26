---
name: pattern-loops
description: "Repeat work with for, while, and until loops over lists and streams."
version: 1.0.0
tags: [bash, command-structure, pattern, shell]
---

# Pattern: Loops (`for`, `while`, `until`)

## Overview

Loops repeat a body over a list of items or until a condition changes. Choose the
form that fits the source of iteration.

## Worked examples

```bash
for f in *.log; do gzip "$f"; done          # over a glob
for i in $(seq 1 5); do echo "$i"; done     # over a sequence

while read -r line; do                       # over lines of input
    process "$line"
done < input.txt

until ping -c1 host &>/dev/null; do          # until a condition holds
    sleep 1
done
```

## Structuring it in a program

- Prefer `while read -r line; do ...; done < file` (or `< <(cmd)`) over
  `for x in $(cmd)` when items may contain spaces.
- Use `continue` to skip and `break` to exit early.
- For parallelism over a list, pipe into `xargs -P` instead of a serial loop.

## Pitfalls

- `for x in $(cat file)` splits on whitespace and globs — almost never what you
  want for lines. Read line by line instead.
