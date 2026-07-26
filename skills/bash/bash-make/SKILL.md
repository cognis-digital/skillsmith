---
name: bash-make
description: "Program the make command: Build automation: run targets whose prerequisites changed."
version: 1.0.0
tags: [bash, build, cli, command-line]
---

    # Command: `make`

    ## Overview

    Build automation: run targets whose prerequisites changed.

    ## When to use

    Use `make` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
make
```
```bash
make -j4
```
```bash
make test
```

    ## Structuring it in a program

    `make` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if make ... ; then
        echo "ok"
    else
        echo "make failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man make` on a POSIX system.

    ## Related

    `cmake`, `ninja`
