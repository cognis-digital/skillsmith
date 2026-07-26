---
name: pattern-functions
description: "Package reusable shell logic into named functions with local scope."
version: 1.0.0
tags: [bash, command-structure, pattern, shell]
---

# Pattern: Functions

## Overview

Functions name a block of shell code so you can reuse it, test it, and give your
script structure. Arguments arrive as `$1`, `$2`, ...; the return value is an exit
code.

## Worked examples

```bash
log() { printf '[%s] %s\n' "$(date +%T)" "$*" >&2; }

retry() {
    local n=$1; shift
    local i
    for ((i=1; i<=n; i++)); do
        "$@" && return 0
        sleep "$i"
    done
    return 1
}

retry 3 curl -fsS https://flaky/endpoint
```

## Structuring it in a program

- Declare loop and temp variables `local` so functions do not clobber globals.
- Return status with `return N`; "return" data by printing it and capturing with
  `$(func)`.
- Keep functions small and single-purpose; compose them.

## Pitfalls

- Without `local`, every assignment is global — a classic source of action-at-a-
  distance bugs.
