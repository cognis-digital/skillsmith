---
name: bash-test
description: "Program the test command: Evaluate a conditional expression (the [ ] command)."
version: 1.0.0
tags: [bash, cli, command-line, logic, shell]
---

    # Command: `test`

    ## Overview

    Evaluate a conditional expression (the [ ] command).

    ## When to use

    Use `test` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
[ -f file ] && echo yes
```
```bash
[ "$a" = "$b" ]
```

    ## Structuring it in a program

    `test` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if test ... ; then
        echo "ok"
    else
        echo "test failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man test` on a POSIX system.

    ## Related

    `case`, `expr`
