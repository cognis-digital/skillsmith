---
name: pattern-exit-codes
description: "Use command exit status to drive control flow and signal success or failure."
version: 1.0.0
tags: [bash, command-structure, pattern, shell]
---

# Pattern: Exit codes and `$?`

## Overview

Every command returns an integer exit status: `0` means success, non-zero means
failure. Shell control flow (`&&`, `||`, `if`, `set -e`) is built on it.

## Worked examples

```bash
mkdir -p out && cd out          # only cd if mkdir succeeded
grep -q pattern file || echo "not found"   # run on failure
command; echo "exited $?"       # inspect the last status
```

## Structuring it in a program

```bash
set -euo pipefail   # exit on error, unset var, or pipeline failure

deploy() {
    build   || return 1
    upload  || return 2
    verify  || return 3
}
deploy; echo "deploy returned $?"
```

- Return meaningful codes from functions and scripts so callers can branch.
- Reserve `0` for success; use small distinct non-zero codes for distinct failures.
- `set -e` stops on the first error; combine with `trap` for cleanup.

## Pitfalls

- `$?` reflects only the **most recent** command — capture it immediately.
- Inside `if cmd; then`, `set -e` does not trigger on `cmd`'s failure by design.
