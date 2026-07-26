---
name: bash-zip
description: "Program the zip command: Create and update zip archives."
version: 1.0.0
tags: [archive, bash, cli, command-line]
---

    # Command: `zip`

    ## Overview

    Create and update zip archives.

    ## When to use

    Use `zip` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
zip -r out.zip dir
```
```bash
zip out.zip a b
```

    ## Structuring it in a program

    `zip` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if zip ... ; then
        echo "ok"
    else
        echo "zip failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man zip` on a POSIX system.

    ## Related

    `unzip`, `tar`
