---
name: bash-tac
description: "Program the tac command: Concatenate and print files in reverse line order."
version: 1.0.0
tags: [bash, cli, command-line, text]
---

    # Command: `tac`

    ## Overview

    Concatenate and print files in reverse line order.

    ## When to use

    Use `tac` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
tac file
```
```bash
tac log | grep -m1 START
```

    ## Structuring it in a program

    `tac` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if tac ... ; then
        echo "ok"
    else
        echo "tac failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`tac --help` on this machine)

```
Usage: tac [OPTION]... [FILE]...
Write each FILE to standard output, last line first.

With no FILE, or when FILE is -, read standard input.

Mandatory arguments to long options are mandatory for short options too.
  -b, --before             attach the separator before instead of after
  -r, --regex              interpret the separator as a regular expression
  -s, --separator=STRING   use STRING as the separator instead of newline
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/tac>
or available locally via: info '(coreutils) tac invocation'
```

    ## Related

    `cat`, `rev`
