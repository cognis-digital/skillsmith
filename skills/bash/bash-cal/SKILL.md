---
name: bash-cal
description: "Program the cal command: Display a calendar."
version: 1.0.0
tags: [bash, cli, command-line, time]
---

    # Command: `cal`

    ## Overview

    Display a calendar.

    ## When to use

    Use `cal` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
cal
```
```bash
cal 2026
```
```bash
cal -3
```

    ## Structuring it in a program

    `cal` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if cal ... ; then
        echo "ok"
    else
        echo "cal failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man cal` on a POSIX system.

    ## Related

    `date`
