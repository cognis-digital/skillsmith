---
name: bash-time
description: "Program the time command: Measure how long a command takes."
version: 1.0.0
tags: [bash, bench, cli, command-line, process]
---

    # Command: `time`

    ## Overview

    Measure how long a command takes.

    ## When to use

    Use `time` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
time make
```
```bash
time ./script.sh
```

    ## Structuring it in a program

    `time` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if time ... ; then
        echo "ok"
    else
        echo "time failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man time` on a POSIX system.

    ## Related

    `hyperfine`
