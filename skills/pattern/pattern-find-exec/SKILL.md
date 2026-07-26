---
name: pattern-find-exec
description: "Act on many files precisely by combining find with -exec or -print0."
version: 1.0.0
tags: [bash, command-structure, pattern, shell]
---

# Pattern: `find -exec` and safe batch actions

## Overview

`find` locates files by rich criteria; `-exec` (or piping `-print0` to `xargs -0`)
runs a command on each match. Together they are the safe way to act on many files.

## Worked examples

```bash
find . -name '*.bak' -delete
find . -type f -mtime +30 -exec gzip {} \;      # one process per file
find . -type f -name '*.js' -exec eslint {} +   # batched, faster
find . -name '*.tmp' -print0 | xargs -0 rm      # NUL-safe pipeline
```

## Structuring it in a program

- `-exec cmd {} \;` runs once per file; `-exec cmd {} +` batches many files per
  invocation (much faster).
- Combine predicates: `-type f -name '*.log' -size +1M -mtime -7`.
- Use `-print0 | xargs -0` when you also want parallelism (`-P`).

## Pitfalls

- Plain `find ... | xargs` breaks on spaces/newlines in names — always use
  `-print0`/`-0`.
- Test destructive finds first by swapping the action for `-print`.
