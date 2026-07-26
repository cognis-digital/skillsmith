---
name: bash-ss
description: "Program the ss command: Modern socket statistics (replaces netstat)."
version: 1.0.0
tags: [bash, cli, command-line, network]
---

    # Command: `ss`

    ## Overview

    Modern socket statistics (replaces netstat).

    ## When to use

    Use `ss` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
ss -tulpn
```
```bash
ss -s
```

    ## Structuring it in a program

    `ss` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if ss ... ; then
        echo "ok"
    else
        echo "ss failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man ss` on a POSIX system.

    ## Related

    `netstat`
