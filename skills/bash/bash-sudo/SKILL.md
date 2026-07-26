---
name: bash-sudo
description: "Program the sudo command: Execute a command as another user (usually root)."
version: 1.0.0
tags: [bash, cli, command-line, perms, system]
---

    # Command: `sudo`

    ## Overview

    Execute a command as another user (usually root).

    ## When to use

    Use `sudo` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
sudo apt update
```
```bash
sudo -u www cmd
```

    ## Structuring it in a program

    `sudo` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if sudo ... ; then
        echo "ok"
    else
        echo "sudo failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man sudo` on a POSIX system.

    ## Related

    `su`, `doas`
