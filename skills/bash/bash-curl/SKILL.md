---
name: bash-curl
description: "Program the curl command: Transfer data to/from a URL — the universal HTTP client for scripts."
version: 1.0.0
tags: [bash, cli, command-line, http, network]
---

    # Command: `curl`

    ## Overview

    Transfer data to/from a URL — the universal HTTP client for scripts.

    ## When to use

    Use `curl` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
curl -s https://api/x
```
```bash
curl -O https://host/file
```
```bash
curl -X POST -d @body url
```

    ## Structuring it in a program

    `curl` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if curl ... ; then
        echo "ok"
    else
        echo "curl failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`curl --help` on this machine)

```
Usage: curl [options...] <url>
 -d, --data <data>           HTTP POST data
 -f, --fail                  Fail fast with no output on HTTP errors
 -h, --help <subject>        Get help for commands
 -o, --output <file>         Write to file instead of stdout
 -O, --remote-name           Write output to file named as remote file
 -i, --show-headers          Show response headers in output
 -s, --silent                Silent mode
 -T, --upload-file <file>    Transfer local FILE to destination
 -u, --user <user:password>  Server user and password
 -A, --user-agent <name>     Send User-Agent <name> to server
 -v, --verbose               Make the operation more talkative
 -V, --version               Show version number and quit

This is not the full help; this menu is split into categories.
Use "--help category" to get an overview of all categories, which are:
auth, connection, curl, deprecated, dns, file, ftp, global, http, imap, ldap, 
output, pop3, post, proxy, scp, sftp, smtp, ssh, telnet, tftp, timeout, tls, 
upload, verbose.
Use "--help all" to list all options
```

    ## Related

    `wget`, `http`, `jq`
