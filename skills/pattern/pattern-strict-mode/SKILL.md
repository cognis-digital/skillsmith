---
name: pattern-strict-mode
description: "Make scripts fail fast and loud with set -euo pipefail and a trap."
version: 1.0.0
tags: [bash, command-structure, pattern, shell]
---

# Pattern: Strict mode (`set -euo pipefail`)

## Overview

By default the shell plows on after errors and treats unset variables as empty.
Strict mode turns silent failures into loud, early ones — the single biggest
robustness win for a script.

## The incantation

```bash
#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'
trap 'echo "error on line $LINENO (exit $?)" >&2' ERR
```

- `set -e` — exit on any unhandled non-zero command.
- `set -u` — error on use of an unset variable.
- `set -o pipefail` — a pipeline fails if any stage fails, not just the last.
- `trap ... ERR` — report where it died; add cleanup here too.

## Worked example

```bash
set -euo pipefail
tmp=$(mktemp)
trap 'rm -f "$tmp"' EXIT        # always clean up
process > "$tmp"
mv "$tmp" result.txt
```

## Pitfalls

- Under `set -e`, a command whose failure you *expect* must be guarded:
  `cmd || true`, or put it in an `if`.
- `set -u` breaks `$1` when no arg is passed; use `${1:-default}`.
