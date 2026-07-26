---
name: bash-scp
description: "Program the scp command: Copy files securely between hosts over SSH."
version: 1.0.0
tags: [bash, cli, command-line, network]
---

    # Command: `scp`

    ## Overview

    Copy files securely between hosts over SSH.

    ## When to use

    Use `scp` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
scp file host:/path
```
```bash
scp -r dir host:~
```

    ## Structuring it in a program

    `scp` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if scp ... ; then
        echo "ok"
    else
        echo "scp failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`scp --help` on this machine)

```
scp: unknown option -- -
usage: scp [-346ABCOpqRrsTv] [-c cipher] [-D sftp_server_path] [-F ssh_config]
           [-i identity_file] [-J destination] [-l limit]
           [-o ssh_option] [-P port] [-S program] source ... target
```

    ## Related

    `ssh`, `rsync`
