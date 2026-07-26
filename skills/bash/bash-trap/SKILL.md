---
name: bash-trap
description: "Program the trap command: Register handlers for signals and shell events (builtin)."
version: 1.0.0
tags: [bash, cli, command-line, shell, signal]
---

    # Command: `trap`

    ## Overview

    Register handlers for signals and shell events (builtin).

    ## When to use

    Use `trap` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
trap 'rm -f $tmp' EXIT
```
```bash
trap 'echo INT' INT
```

    ## Structuring it in a program

    `trap` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if trap ... ; then
        echo "ok"
    else
        echo "trap failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man trap` on a POSIX system.

    ## Related

    `kill`, `signal`
