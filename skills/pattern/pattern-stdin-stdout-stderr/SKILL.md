---
name: pattern-stdin-stdout-stderr
description: "Understand the three standard streams and route them deliberately."
version: 1.0.0
tags: [bash, command-structure, pattern, shell]
---

# Pattern: The three standard streams

## Overview

Every process starts with three open file descriptors: stdin (0) for input, stdout
(1) for normal output, stderr (2) for diagnostics. Keeping data on stdout and
messages on stderr is what makes tools composable.

## Worked examples

```bash
echo "result"           # -> stdout (fd 1), part of the data
echo "warning" >&2      # -> stderr (fd 2), not part of the data
program < input         # feed stdin from a file
program > out 2> err    # separate the streams

data=$(program 2>/dev/null)   # capture data, discard diagnostics
```

## Structuring it in a program

- Print **results** to stdout so they flow through pipes; print **logs, prompts,
  and errors** to stderr so they do not pollute the data.
- A well-behaved filter reads stdin, writes stdout, and reports problems on stderr
  with a non-zero exit.

## Pitfalls

- Mixing logs into stdout corrupts downstream parsing — the most common reason a
  pipeline "randomly" breaks.
