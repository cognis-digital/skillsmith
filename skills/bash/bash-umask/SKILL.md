---
name: bash-umask
description: "Program the umask command: Set the default permission mask for newly created files."
version: 1.0.0
tags: [bash, cli, command-line, perms, shell]
---

    # Command: `umask`

    ## Overview

    Set the default permission mask for newly created files.

    ## When to use

    Use `umask` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
umask
```
```bash
umask 022
```

    ## Structuring it in a program

    `umask` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if umask ... ; then
        echo "ok"
    else
        echo "umask failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man umask` on a POSIX system.

    ## Related

    `chmod`
