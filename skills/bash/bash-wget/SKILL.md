---
name: bash-wget
description: "Program the wget command: Download files over HTTP/FTP, with recursion and resume."
version: 1.0.0
tags: [bash, cli, command-line, download, network]
---

    # Command: `wget`

    ## Overview

    Download files over HTTP/FTP, with recursion and resume.

    ## When to use

    Use `wget` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
wget https://host/file
```
```bash
wget -c bigfile
```
```bash
wget -r -np site
```

    ## Structuring it in a program

    `wget` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if wget ... ; then
        echo "ok"
    else
        echo "wget failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man wget` on a POSIX system.

    ## Related

    `curl`
