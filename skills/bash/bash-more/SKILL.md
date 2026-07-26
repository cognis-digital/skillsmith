---
name: bash-more
description: "Program the more command: Simple pager: view text one screen at a time."
version: 1.0.0
tags: [bash, cli, command-line, pager, text]
---

    # Command: `more`

    ## Overview

    Simple pager: view text one screen at a time.

    ## When to use

    Use `more` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
more file
```
```bash
ls | more
```

    ## Structuring it in a program

    `more` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if more ... ; then
        echo "ok"
    else
        echo "more failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man more` on a POSIX system.

    ## Related

    `less`
