---
name: bash-ssh
description: "Program the ssh command: Open a secure shell to a remote host and run commands."
version: 1.0.0
tags: [bash, cli, command-line, network, remote]
---

    # Command: `ssh`

    ## Overview

    Open a secure shell to a remote host and run commands.

    ## When to use

    Use `ssh` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
ssh user@host
```
```bash
ssh -i key host 'uptime'
```
```bash
ssh -L 8080:localhost:80 host
```

    ## Structuring it in a program

    `ssh` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if ssh ... ; then
        echo "ok"
    else
        echo "ssh failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`ssh --help` on this machine)

```
ssh: unknown option -- -
usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface]
           [-b bind_address] [-c cipher_spec] [-D [bind_address:]port]
           [-E log_file] [-e escape_char] [-F configfile] [-I pkcs11]
           [-i identity_file] [-J [user@]host[:port]] [-L address]
           [-l login_name] [-m mac_spec] [-O ctl_cmd] [-o option] [-p port]
           [-Q query_option] [-R address] [-S ctl_path] [-W host:port]
           [-w local_tun[:remote_tun]] destination [command [argument ...]]
```

    ## Related

    `scp`, `sftp`, `ssh-keygen`
