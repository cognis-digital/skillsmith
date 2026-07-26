---
name: bash-hostname
description: "Program the hostname command: Show or set the system hostname."
version: 1.0.0
tags: [bash, cli, command-line, system]
---

    # Command: `hostname`

    ## Overview

    Show or set the system hostname.

    ## When to use

    Use `hostname` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
hostname
```
```bash
hostname -I
```

    ## Structuring it in a program

    `hostname` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if hostname ... ; then
        echo "ok"
    else
        echo "hostname failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`hostname --help` on this machine)

```
sethostname: Use the Network Control Panel Applet to set hostname.
hostname -s is not supported.
```

    ## Related

    `uname`
