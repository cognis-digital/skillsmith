---
name: bash-read
description: "Program the read command: Read a line of input into shell variables."
version: 1.0.0
tags: [bash, cli, command-line, input, shell]
---

    # Command: `read`

    ## Overview

    Read a line of input into shell variables.

    ## When to use

    Use `read` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
read -r line
```
```bash
read -p 'name: ' n
```
```bash
while read -r l; do :; done < f
```

    ## Structuring it in a program

    `read` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if read ... ; then
        echo "ok"
    else
        echo "read failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man read` on a POSIX system.

    ## Related

    `mapfile`
