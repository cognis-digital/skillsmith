---
name: bash-rg
description: "Program the rg command: ripgrep: extremely fast recursive regex search that respects .gitignore."
version: 1.0.0
tags: [bash, cli, command-line, search, text]
---

    # Command: `rg`

    ## Overview

    ripgrep: extremely fast recursive regex search that respects .gitignore.

    ## When to use

    Use `rg` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
rg TODO
```
```bash
rg -t py 'def '
```
```bash
rg -l pattern
```

    ## Structuring it in a program

    `rg` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if rg ... ; then
        echo "ok"
    else
        echo "rg failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man rg` on a POSIX system.

    ## Related

    `grep`, `ag`, `fd`
