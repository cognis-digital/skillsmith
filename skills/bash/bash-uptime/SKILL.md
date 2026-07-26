---
name: bash-uptime
description: "Program the uptime command: Show how long the system has been running and load averages."
version: 1.0.0
tags: [bash, cli, command-line, system]
---

    # Command: `uptime`

    ## Overview

    Show how long the system has been running and load averages.

    ## When to use

    Use `uptime` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
uptime
```

    ## Structuring it in a program

    `uptime` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if uptime ... ; then
        echo "ok"
    else
        echo "uptime failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man uptime` on a POSIX system.

    ## Related

    `top`, `w`
