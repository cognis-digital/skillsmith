---
name: bash-factor
description: "Program the factor command: Print the prime factors of numbers."
version: 1.0.0
tags: [bash, cli, command-line, math]
---

    # Command: `factor`

    ## Overview

    Print the prime factors of numbers.

    ## When to use

    Use `factor` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
factor 360
```
```bash
seq 100 | factor
```

    ## Structuring it in a program

    `factor` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if factor ... ; then
        echo "ok"
    else
        echo "factor failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`factor --help` on this machine)

```
Usage: factor [NUMBER]...
  or:  factor OPTION
Print the prime factors of each specified integer NUMBER.  If none
are specified on the command line, read them from standard input.

      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/factor>
or available locally via: info '(coreutils) factor invocation'
```

    ## Related

    `bc`
