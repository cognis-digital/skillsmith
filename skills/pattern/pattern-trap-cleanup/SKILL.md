---
name: pattern-trap-cleanup
description: "Run cleanup and handle signals reliably with trap."
version: 1.0.0
tags: [bash, command-structure, pattern, shell]
---

# Pattern: Traps and cleanup (`trap`)

## Overview

`trap` registers commands to run when the shell receives a signal or on specific
pseudo-signals like `EXIT` and `ERR`. It is how you guarantee cleanup no matter how
a script ends.

## Worked examples

```bash
tmpdir=$(mktemp -d)
trap 'rm -rf "$tmpdir"' EXIT           # runs on normal exit, error, or Ctrl-C

trap 'echo "interrupted" >&2; exit 130' INT TERM

trap 'echo "failed at line $LINENO" >&2' ERR
```

## Structuring it in a program

- Put an `EXIT` trap right after you create a temp resource, so cleanup is bound to
  the resource's lifetime.
- Combine with strict mode: `ERR` reports, `EXIT` cleans up.
- Keep trap handlers short and non-failing.

## Pitfalls

- Later `trap` calls for the same signal replace earlier ones — set the full
  handler you want.
