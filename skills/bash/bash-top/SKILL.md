---
name: bash-top
description: "Program the top command: Live view of processes and resource usage."
version: 1.0.0
tags: [bash, cli, command-line, monitor, process]
---

    # Command: `top`

    ## Overview

    Live view of processes and resource usage.

    ## When to use

    Use `top` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
top
```
```bash
top -o %MEM
```

    ## Structuring it in a program

    `top` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if top ... ; then
        echo "ok"
    else
        echo "top failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man top` on a POSIX system.

    ## Related

    `htop`, `ps`
