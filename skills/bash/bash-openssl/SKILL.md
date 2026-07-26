---
name: bash-openssl
description: "Program the openssl command: Cryptography toolkit: keys, certs, hashing, encryption, TLS testing."
version: 1.0.0
tags: [bash, cli, command-line, crypto, security]
---

    # Command: `openssl`

    ## Overview

    Cryptography toolkit: keys, certs, hashing, encryption, TLS testing.

    ## When to use

    Use `openssl` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
openssl rand -hex 16
```
```bash
openssl x509 -in cert.pem -text
```
```bash
openssl s_client -connect host:443
```

    ## Structuring it in a program

    `openssl` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if openssl ... ; then
        echo "ok"
    else
        echo "openssl failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`openssl --help` on this machine)

```
Invalid command '--help'; type "help" for a list.
```

    ## Related

    `gpg`, `ssh-keygen`
