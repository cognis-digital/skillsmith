---
name: bash-pushd
description: "Program the pushd command: Change directory and push the old one onto a stack."
version: 1.0.0
tags: [bash, cli, command-line, navigation, shell]
---

    # Command: `pushd`

    ## Overview

    Change directory and push the old one onto a stack.

    ## When to use

    Use `pushd` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
pushd /tmp
```
```bash
popd
```

    ## Structuring it in a program

    `pushd` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if pushd ... ; then
        echo "ok"
    else
        echo "pushd failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man pushd` on a POSIX system.

    ## Related

    `popd`, `cd`, `dirs`
