---
name: bash-history
description: "Program the history command: Show and manipulate the shell command history."
version: 1.0.0
tags: [bash, cli, command-line, shell]
---

    # Command: `history`

    ## Overview

    Show and manipulate the shell command history.

    ## When to use

    Use `history` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
history
```
```bash
history 20
```
```bash
!42
```

    ## Structuring it in a program

    `history` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if history ... ; then
        echo "ok"
    else
        echo "history failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man history` on a POSIX system.

    ## Related

    `fc`
