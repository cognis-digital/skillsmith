---
name: bash-pkill
description: "Program the pkill command: Signal processes by name pattern."
version: 1.0.0
tags: [bash, cli, command-line, process]
---

    # Command: `pkill`

    ## Overview

    Signal processes by name pattern.

    ## When to use

    Use `pkill` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
pkill -f server.py
```
```bash
pkill -9 chrome
```

    ## Structuring it in a program

    `pkill` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if pkill ... ; then
        echo "ok"
    else
        echo "pkill failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man pkill` on a POSIX system.

    ## Related

    `kill`, `pgrep`
