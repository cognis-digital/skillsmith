---
name: bash-expand
description: "Program the expand command: Convert tabs to spaces."
version: 1.0.0
tags: [bash, cli, command-line, text]
---

    # Command: `expand`

    ## Overview

    Convert tabs to spaces.

    ## When to use

    Use `expand` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
expand -t4 file
```

    ## Structuring it in a program

    `expand` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if expand ... ; then
        echo "ok"
    else
        echo "expand failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`expand --help` on this machine)

```
Microsoft (R) File Expansion Utility
Copyright (c) Microsoft Corporation. All rights reserved.

Unrecognized switch --.
```

    ## Related

    `unexpand`
