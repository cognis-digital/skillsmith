---
name: bash-export
description: "Program the export command: Mark a shell variable for export to child processes."
version: 1.0.0
tags: [bash, cli, command-line, env, shell]
---

    # Command: `export`

    ## Overview

    Mark a shell variable for export to child processes.

    ## When to use

    Use `export` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
export PATH=$PATH:/opt/bin
```
```bash
export EDITOR=vim
```

    ## Structuring it in a program

    `export` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if export ... ; then
        echo "ok"
    else
        echo "export failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man export` on a POSIX system.

    ## Related

    `env`, `set`
