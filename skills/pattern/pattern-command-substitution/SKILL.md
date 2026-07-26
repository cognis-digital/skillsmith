---
name: pattern-command-substitution
description: "Capture a command's output into a variable or another command with $(...)."
version: 1.0.0
tags: [bash, command-structure, pattern, shell]
---

# Pattern: Command substitution (`$(...)`)

## Overview

`$(command)` runs a command and substitutes its stdout in place, with trailing
newlines stripped. It is how you feed one command's result into another.

## Worked examples

```bash
today=$(date +%Y-%m-%d)
files=$(find . -name '*.log')
echo "commit $(git rev-parse --short HEAD)"
cd "$(dirname "$0")"            # move to the script's directory
```

## Structuring it in a program

- Always quote the expansion: `"$(...)"` — unquoted, the result is word-split and
  glob-expanded.
- Prefer `$( )` over backticks: it nests cleanly and is readable.
- For large output, pipe instead of substituting to avoid holding it all in memory.

## Pitfalls

- Command substitution runs in a subshell; variable assignments inside it do not
  leak out.
- Trailing newlines are trimmed — fine for scalars, surprising for exact bytes.
