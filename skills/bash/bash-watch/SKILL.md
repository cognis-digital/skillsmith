---
name: bash-watch
description: "Program the watch command: Run a command periodically and show the output."
version: 1.0.0
tags: [bash, cli, command-line, monitor]
---

    # Command: `watch`

    ## Overview

    Run a command periodically and show the output.

    ## When to use

    Use `watch` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
watch -n1 df -h
```
```bash
watch 'ps aux | head'
```

    ## Structuring it in a program

    `watch` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if watch ... ; then
        echo "ok"
    else
        echo "watch failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man watch` on a POSIX system.

    ## Related

    `top`
