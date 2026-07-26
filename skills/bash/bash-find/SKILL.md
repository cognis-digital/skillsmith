---
name: bash-find
description: "Program the find command: Recursively search a directory tree by name, type, size, time, and run actions."
version: 1.0.0
tags: [bash, cli, command-line, files, search]
---

    # Command: `find`

    ## Overview

    Recursively search a directory tree by name, type, size, time, and run actions.

    ## When to use

    Use `find` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
find . -name '*.py'
```
```bash
find . -type f -mtime -1
```
```bash
find . -name '*.tmp' -delete
```

    ## Structuring it in a program

    `find` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if find ... ; then
        echo "ok"
    else
        echo "find failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man find` on a POSIX system.

    ## Related

    `fd`, `grep`, `xargs`
