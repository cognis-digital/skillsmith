---
name: bash-cron
description: "Program the cron command: Time-based job scheduler — run commands on a schedule."
version: 1.0.0
tags: [bash, cli, command-line, schedule]
---

    # Command: `cron`

    ## Overview

    Time-based job scheduler — run commands on a schedule.

    ## When to use

    Use `cron` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
crontab -e
```
```bash
crontab -l
```

    ## Structuring it in a program

    `cron` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if cron ... ; then
        echo "ok"
    else
        echo "cron failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man cron` on a POSIX system.

    ## Related

    `at`, `systemd`
