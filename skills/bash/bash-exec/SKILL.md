---
name: bash-exec
description: "Program the exec command: Replace the shell with a command, or reassign its file descriptors."
version: 1.0.0
tags: [bash, cli, command-line, process, shell]
---

    # Command: `exec`

    ## Overview

    Replace the shell with a command, or reassign its file descriptors.

    ## When to use

    Use `exec` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
exec bash
```
```bash
exec > log 2>&1
```

    ## Structuring it in a program

    `exec` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if exec ... ; then
        echo "ok"
    else
        echo "exec failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man exec` on a POSIX system.

    ## Related

    `source`
