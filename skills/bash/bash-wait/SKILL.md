---
name: bash-wait
description: "Program the wait command: Wait for background jobs to finish (builtin)."
version: 1.0.0
tags: [bash, cli, command-line, process, shell]
---

    # Command: `wait`

    ## Overview

    Wait for background jobs to finish (builtin).

    ## When to use

    Use `wait` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
long & wait
```
```bash
wait $pid
```

    ## Structuring it in a program

    `wait` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if wait ... ; then
        echo "ok"
    else
        echo "wait failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man wait` on a POSIX system.

    ## Related

    `jobs`, `bg`
