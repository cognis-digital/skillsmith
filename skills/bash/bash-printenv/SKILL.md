---
name: bash-printenv
description: "Program the printenv command: Print environment variable values."
version: 1.0.0
tags: [bash, cli, command-line, env]
---

    # Command: `printenv`

    ## Overview

    Print environment variable values.

    ## When to use

    Use `printenv` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
printenv PATH
```
```bash
printenv
```

    ## Structuring it in a program

    `printenv` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if printenv ... ; then
        echo "ok"
    else
        echo "printenv failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`printenv --help` on this machine)

```
Usage: printenv [OPTION]... [VARIABLE]...
Print the values of the specified environment VARIABLE(s).
If no VARIABLE is specified, print name and value pairs for them all.

  -0, --null     end each output line with NUL, not newline
      --help     display this help and exit
      --version  output version information and exit

NOTE: your shell may have its own version of printenv, which usually supersedes
the version described here.  Please refer to your shell's documentation
for details about the options it supports.

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/printenv>
or available locally via: info '(coreutils) printenv invocation'
```

    ## Related

    `env`
