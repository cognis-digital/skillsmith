---
name: bash-mapfile
description: "Program the mapfile command: Read lines of input into a bash array (aka readarray)."
version: 1.0.0
tags: [bash, cli, command-line, shell]
---

    # Command: `mapfile`

    ## Overview

    Read lines of input into a bash array (aka readarray).

    ## When to use

    Use `mapfile` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
mapfile -t lines < file
```
```bash
mapfile -t arr < <(ls)
```

    ## Structuring it in a program

    `mapfile` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if mapfile ... ; then
        echo "ok"
    else
        echo "mapfile failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man mapfile` on a POSIX system.

    ## Related

    `read`, `arrays`
