---
name: pattern-xargs-parallel
description: "Turn a list into many commands and run them in parallel with xargs -P."
version: 1.0.0
tags: [bash, command-structure, pattern, shell]
---

# Pattern: Parallelism with `xargs -P`

## Overview

`xargs` reads items from stdin and runs a command with them as arguments; `-P N`
runs up to N invocations concurrently. It is the simplest way to parallelize a
batch of independent tasks.

## Worked examples

```bash
# resize every image, 8 at a time, one file per invocation
ls *.png | xargs -P8 -n1 -I{} convert {} -resize 50% small/{}

# fetch many URLs concurrently
xargs -P4 -n1 curl -sO < urls.txt

# NUL-safe against weird filenames
find . -name '*.log' -print0 | xargs -0 -P4 gzip
```

## Structuring it in a program

- `-n1` gives one item per command; `-I{}` places the item explicitly.
- `-P0` uses as many processes as possible; pick a bound near your core count.
- Use `-print0` / `-0` to survive spaces and newlines in filenames.

## Pitfalls

- Parallel output interleaves; write to per-item files or add locking if order
  matters.
- Each parallel job's failure does not stop the others — check results afterward.
