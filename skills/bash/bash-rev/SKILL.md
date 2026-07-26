---
name: bash-rev
description: "Program the rev command: Reverse the characters of each line."
version: 1.0.0
tags: [bash, cli, command-line, text]
---

    # Command: `rev`

    ## Overview

    Reverse the characters of each line.

    ## When to use

    Use `rev` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
echo abc | rev
```

    ## Structuring it in a program

    `rev` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if rev ... ; then
        echo "ok"
    else
        echo "rev failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man rev` on a POSIX system.

    ## Related

    `tac`
