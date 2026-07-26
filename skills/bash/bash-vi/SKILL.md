---
name: bash-vi
description: "Program the vi command: The classic modal editor (usually vim in disguise)."
version: 1.0.0
tags: [bash, cli, command-line, editor]
---

    # Command: `vi`

    ## Overview

    The classic modal editor (usually vim in disguise).

    ## When to use

    Use `vi` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
vi file
```

    ## Structuring it in a program

    `vi` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if vi ... ; then
        echo "ok"
    else
        echo "vi failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man vi` on a POSIX system.

    ## Related

    `vim`, `nano`
