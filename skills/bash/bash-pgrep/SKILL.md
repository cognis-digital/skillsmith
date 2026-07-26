---
name: bash-pgrep
description: "Program the pgrep command: Find process IDs by name pattern."
version: 1.0.0
tags: [bash, cli, command-line, process]
---

    # Command: `pgrep`

    ## Overview

    Find process IDs by name pattern.

    ## When to use

    Use `pgrep` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
pgrep -fl python
```
```bash
pgrep nginx
```

    ## Structuring it in a program

    `pgrep` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if pgrep ... ; then
        echo "ok"
    else
        echo "pgrep failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man pgrep` on a POSIX system.

    ## Related

    `ps`, `pkill`
