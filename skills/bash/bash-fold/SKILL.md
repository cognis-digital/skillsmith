---
name: bash-fold
description: "Program the fold command: Wrap input lines to a given width."
version: 1.0.0
tags: [bash, cli, command-line, text]
---

    # Command: `fold`

    ## Overview

    Wrap input lines to a given width.

    ## When to use

    Use `fold` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
fold -w 72 file
```

    ## Structuring it in a program

    `fold` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if fold ... ; then
        echo "ok"
    else
        echo "fold failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`fold --help` on this machine)

```
Usage: fold [OPTION]... [FILE]...
Wrap input lines in each FILE, writing to standard output.

With no FILE, or when FILE is -, read standard input.

Mandatory arguments to long options are mandatory for short options too.
  -b, --bytes         count bytes rather than columns
  -s, --spaces        break at spaces
  -w, --width=WIDTH   use WIDTH columns instead of 80
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/fold>
or available locally via: info '(coreutils) fold invocation'
```

    ## Related

    `fmt`
