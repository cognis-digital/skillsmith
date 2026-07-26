---
name: bash-dig
description: "Program the dig command: Query DNS records."
version: 1.0.0
tags: [bash, cli, command-line, dns, network]
---

    # Command: `dig`

    ## Overview

    Query DNS records.

    ## When to use

    Use `dig` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
dig example.com
```
```bash
dig +short A host
```
```bash
dig MX domain
```

    ## Structuring it in a program

    `dig` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if dig ... ; then
        echo "ok"
    else
        echo "dig failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man dig` on a POSIX system.

    ## Related

    `nslookup`, `host`
