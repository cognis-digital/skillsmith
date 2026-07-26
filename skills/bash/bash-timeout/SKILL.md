---
name: bash-timeout
description: "Program the timeout command: Run a command with a time limit, killing it if it overruns."
version: 1.0.0
tags: [bash, cli, command-line, process]
---

    # Command: `timeout`

    ## Overview

    Run a command with a time limit, killing it if it overruns.

    ## When to use

    Use `timeout` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
timeout 10 ./slow
```
```bash
timeout -s KILL 5 cmd
```

    ## Structuring it in a program

    `timeout` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if timeout ... ; then
        echo "ok"
    else
        echo "timeout failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`timeout --help` on this machine)

```
ERROR: Invalid value for timeout (/T) specified. Valid range is -1 to 99999.
```

    ## Related

    `sleep`, `kill`
