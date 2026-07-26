---
name: bash-popd
description: "Program the popd command: Pop a directory off the stack and change to it."
version: 1.0.0
tags: [bash, cli, command-line, navigation, shell]
---

    # Command: `popd`

    ## Overview

    Pop a directory off the stack and change to it.

    ## When to use

    Use `popd` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
popd
```

    ## Structuring it in a program

    `popd` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if popd ... ; then
        echo "ok"
    else
        echo "popd failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man popd` on a POSIX system.

    ## Related

    `pushd`, `dirs`
