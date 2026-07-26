---
name: bash-whoami
description: "Program the whoami command: Print the effective username."
version: 1.0.0
tags: [bash, cli, command-line, system]
---

    # Command: `whoami`

    ## Overview

    Print the effective username.

    ## When to use

    Use `whoami` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
whoami
```

    ## Structuring it in a program

    `whoami` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if whoami ... ; then
        echo "ok"
    else
        echo "whoami failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`whoami --help` on this machine)

```
ERROR: Invalid argument/option - '--help'.
Type "WHOAMI /?" for usage.
```

    ## Related

    `id`
