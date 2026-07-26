---
name: bash-set
description: "Program the set command: Set shell options and positional parameters."
version: 1.0.0
tags: [bash, cli, command-line, shell]
---

    # Command: `set`

    ## Overview

    Set shell options and positional parameters.

    ## When to use

    Use `set` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
set -euo pipefail
```
```bash
set -- a b c
```
```bash
set -x
```

    ## Structuring it in a program

    `set` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if set ... ; then
        echo "ok"
    else
        echo "set failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man set` on a POSIX system.

    ## Related

    `shopt`, `export`
