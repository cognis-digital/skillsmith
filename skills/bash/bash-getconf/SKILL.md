---
name: bash-getconf
description: "Program the getconf command: Query system configuration values."
version: 1.0.0
tags: [bash, cli, command-line, system]
---

    # Command: `getconf`

    ## Overview

    Query system configuration values.

    ## When to use

    Use `getconf` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
getconf PAGE_SIZE
```
```bash
getconf -a
```

    ## Structuring it in a program

    `getconf` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if getconf ... ; then
        echo "ok"
    else
        echo "getconf failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`getconf --help` on this machine)

```
Usage: getconf [-v specification] variable_name [pathname]
       getconf -a [pathname]

Get configuration values

  -v specification     Indicate specific version for which configuration
                       values shall be fetched.
  -a, --all            Print all known configuration values

Other options:

  -h, --help           This text
  -V, --version        Print program version and exit
```

    ## Related

    `ulimit`
