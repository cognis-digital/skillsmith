---
name: bash-true
description: "Program the true command: Do nothing, successfully (exit 0) — loops and defaults."
version: 1.0.0
tags: [bash, cli, command-line, shell]
---

    # Command: `true`

    ## Overview

    Do nothing, successfully (exit 0) — loops and defaults.

    ## When to use

    Use `true` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
while true; do :; done
```

    ## Structuring it in a program

    `true` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if true ... ; then
        echo "ok"
    else
        echo "true failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`true --help` on this machine)

```
Usage: true [ignored command line arguments]
  or:  true OPTION
Exit with a status code indicating success.

      --help     display this help and exit
      --version  output version information and exit

NOTE: your shell may have its own version of true, which usually supersedes
the version described here.  Please refer to your shell's documentation
for details about the options it supports.

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/true>
or available locally via: info '(coreutils) true invocation'
```

    ## Related

    `false`, `yes`
