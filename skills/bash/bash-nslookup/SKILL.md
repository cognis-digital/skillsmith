---
name: bash-nslookup
description: "Program the nslookup command: Query DNS name servers interactively or in batch."
version: 1.0.0
tags: [bash, cli, command-line, dns, network]
---

    # Command: `nslookup`

    ## Overview

    Query DNS name servers interactively or in batch.

    ## When to use

    Use `nslookup` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
nslookup example.com
```
```bash
nslookup -type=MX domain
```

    ## Structuring it in a program

    `nslookup` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if nslookup ... ; then
        echo "ok"
    else
        echo "nslookup failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`nslookup --help` on this machine)

```
Default Server:  dns1.nextdns.io
Address:  45.90.28.231

>
```

    ## Related

    `dig`, `host`
