---
name: bash-type
description: "Program the type command: Show how a name would be interpreted (builtin, alias, file)."
version: 1.0.0
tags: [bash, cli, command-line, shell]
---

    # Command: `type`

    ## Overview

    Show how a name would be interpreted (builtin, alias, file).

    ## When to use

    Use `type` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
type -a ls
```
```bash
type cd
```

    ## Structuring it in a program

    `type` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if type ... ; then
        echo "ok"
    else
        echo "type failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man type` on a POSIX system.

    ## Related

    `which`, `command`
