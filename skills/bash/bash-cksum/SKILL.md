---
name: bash-cksum
description: "Program the cksum command: Compute a CRC checksum and byte count."
version: 1.0.0
tags: [bash, cli, command-line, hash]
---

    # Command: `cksum`

    ## Overview

    Compute a CRC checksum and byte count.

    ## When to use

    Use `cksum` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
cksum file
```

    ## Structuring it in a program

    `cksum` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if cksum ... ; then
        echo "ok"
    else
        echo "cksum failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`cksum --help` on this machine)

```
Usage: cksum [FILE]...
  or:  cksum [OPTION]
Print CRC checksum and byte counts of each FILE.

      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/cksum>
or available locally via: info '(coreutils) cksum invocation'
```

    ## Related

    `md5sum`
