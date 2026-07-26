---
name: pattern-process-substitution
description: "Feed a command's output as if it were a file with <(...) and >(...)."
version: 1.0.0
tags: [bash, command-structure, pattern, shell]
---

# Pattern: Process substitution (`<(...)`, `>(...)`)

## Overview

Process substitution presents a command's output (or input) as a filename, so tools
that expect files can consume streams — and you avoid subshell variable loss.

## Worked examples

```bash
diff <(sort a) <(sort b)            # compare two pipelines as files
comm -12 <(sort x) <(sort y)
while read -r line; do count=$((count+1)); done < <(grep foo file)
tee >(gzip > out.gz) >(wc -l) < input
```

## Structuring it in a program

- Use `< <(producer)` to feed a `while read` loop without a pipe, so variables set
  in the loop survive.
- Combine multiple `>(...)` consumers with `tee` to fan one stream out.

## Pitfalls

- Bash/zsh only (not POSIX `sh`).
- The substituted filename (e.g. `/dev/fd/63`) is valid only while the command runs.
