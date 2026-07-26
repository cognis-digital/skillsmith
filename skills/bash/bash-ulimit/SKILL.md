---
name: bash-ulimit
description: "Program the ulimit command: Show or set shell resource limits."
version: 1.0.0
tags: [bash, cli, command-line, limits, shell]
---

    # Command: `ulimit`

    ## Overview

    Show or set shell resource limits.

    ## When to use

    Use `ulimit` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
ulimit -n
```
```bash
ulimit -c unlimited
```

    ## Structuring it in a program

    `ulimit` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if ulimit ... ; then
        echo "ok"
    else
        echo "ulimit failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man ulimit` on a POSIX system.

    ## Related

    `getconf`
