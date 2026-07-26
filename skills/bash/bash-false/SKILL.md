---
name: bash-false
description: "Program the false command: Do nothing, unsuccessfully (exit 1)."
version: 1.0.0
tags: [bash, cli, command-line, shell]
---

    # Command: `false`

    ## Overview

    Do nothing, unsuccessfully (exit 1).

    ## When to use

    Use `false` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
false || echo failed
```

    ## Structuring it in a program

    `false` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if false ... ; then
        echo "ok"
    else
        echo "false failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`false --help` on this machine)

```
Usage: false [ignored command line arguments]
  or:  false OPTION
Exit with a status code indicating failure.

      --help     display this help and exit
      --version  output version information and exit

NOTE: your shell may have its own version of false, which usually supersedes
the version described here.  Please refer to your shell's documentation
for details about the options it supports.

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/false>
or available locally via: info '(coreutils) false invocation'
```

    ## Related

    `true`
