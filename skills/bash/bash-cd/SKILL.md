---
name: bash-cd
description: "Program the cd command: Change the shell's current directory (a builtin)."
version: 1.0.0
tags: [bash, cli, command-line, navigation, shell]
---

    # Command: `cd`

    ## Overview

    Change the shell's current directory (a builtin).

    ## When to use

    Use `cd` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
cd /path
```
```bash
cd -
```
```bash
cd ~
```

    ## Structuring it in a program

    `cd` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if cd ... ; then
        echo "ok"
    else
        echo "cd failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man cd` on a POSIX system.

    ## Related

    `pushd`, `popd`
