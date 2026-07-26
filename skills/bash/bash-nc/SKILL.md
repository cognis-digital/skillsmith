---
name: bash-nc
description: "Program the nc command: netcat: read/write raw TCP/UDP — test ports, move bytes."
version: 1.0.0
tags: [bash, cli, command-line, network]
---

    # Command: `nc`

    ## Overview

    netcat: read/write raw TCP/UDP — test ports, move bytes.

    ## When to use

    Use `nc` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
nc -zv host 22
```
```bash
nc -l 9000
```

    ## Structuring it in a program

    `nc` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if nc ... ; then
        echo "ok"
    else
        echo "nc failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man nc` on a POSIX system.

    ## Related

    `socat`, `curl`
