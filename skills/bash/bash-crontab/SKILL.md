---
name: bash-crontab
description: "Program the crontab command: Manage per-user cron schedules."
version: 1.0.0
tags: [bash, cli, command-line, schedule]
---

    # Command: `crontab`

    ## Overview

    Manage per-user cron schedules.

    ## When to use

    Use `crontab` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
crontab -l
```
```bash
crontab -e
```

    ## Structuring it in a program

    `crontab` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if crontab ... ; then
        echo "ok"
    else
        echo "crontab failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man crontab` on a POSIX system.

    ## Related

    `cron`, `at`
