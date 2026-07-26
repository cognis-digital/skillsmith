---
name: bash-alias
description: "Program the alias command: Create a shorthand name for a command."
version: 1.0.0
tags: [bash, cli, command-line, shell]
---

    # Command: `alias`

    ## Overview

    Create a shorthand name for a command.

    ## When to use

    Use `alias` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
alias ll='ls -la'
```
```bash
alias -p
```

    ## Structuring it in a program

    `alias` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if alias ... ; then
        echo "ok"
    else
        echo "alias failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man alias` on a POSIX system.

    ## Related

    `type`, `function`
