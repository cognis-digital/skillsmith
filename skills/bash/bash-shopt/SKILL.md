---
name: bash-shopt
description: "Program the shopt command: Toggle bash-specific shell behaviors."
version: 1.0.0
tags: [bash, cli, command-line, shell]
---

    # Command: `shopt`

    ## Overview

    Toggle bash-specific shell behaviors.

    ## When to use

    Use `shopt` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
shopt -s globstar
```
```bash
shopt -s nullglob
```
```bash
shopt
```

    ## Structuring it in a program

    `shopt` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if shopt ... ; then
        echo "ok"
    else
        echo "shopt failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man shopt` on a POSIX system.

    ## Related

    `set`
