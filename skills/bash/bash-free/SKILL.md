---
name: bash-free
description: "Program the free command: Show memory usage."
version: 1.0.0
tags: [bash, cli, command-line, memory, system]
---

    # Command: `free`

    ## Overview

    Show memory usage.

    ## When to use

    Use `free` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
free -h
```
```bash
free -m
```

    ## Structuring it in a program

    `free` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if free ... ; then
        echo "ok"
    else
        echo "free failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man free` on a POSIX system.

    ## Related

    `top`, `vmstat`
