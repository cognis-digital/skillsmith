---
name: bash-tsort
description: "Program the tsort command: Topologically sort a partial order given as pairs."
version: 1.0.0
tags: [bash, cli, command-line, graph, order]
---

    # Command: `tsort`

    ## Overview

    Topologically sort a partial order given as pairs.

    ## When to use

    Use `tsort` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
tsort deps.txt
```

    ## Structuring it in a program

    `tsort` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if tsort ... ; then
        echo "ok"
    else
        echo "tsort failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`tsort --help` on this machine)

```
Usage: tsort [OPTION] [FILE]
Write totally ordered list consistent with the partial ordering in FILE.

With no FILE, or when FILE is -, read standard input.

      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/tsort>
or available locally via: info '(coreutils) tsort invocation'
```

    ## Related

    `sort`
