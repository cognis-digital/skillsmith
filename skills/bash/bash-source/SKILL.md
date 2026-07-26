---
name: bash-source
description: "Program the source command: Execute a script in the current shell (so its variables persist)."
version: 1.0.0
tags: [bash, cli, command-line, shell]
---

    # Command: `source`

    ## Overview

    Execute a script in the current shell (so its variables persist).

    ## When to use

    Use `source` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
source .env
```
```bash
. ./lib.sh
```

    ## Structuring it in a program

    `source` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if source ... ; then
        echo "ok"
    else
        echo "source failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man source` on a POSIX system.

    ## Related

    `export`, `exec`
