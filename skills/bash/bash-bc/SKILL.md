---
name: bash-bc
description: "Program the bc command: Arbitrary-precision calculator language."
version: 1.0.0
tags: [bash, cli, command-line, math]
---

    # Command: `bc`

    ## Overview

    Arbitrary-precision calculator language.

    ## When to use

    Use `bc` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
echo '3/4' | bc -l
```
```bash
bc <<< '2^10'
```

    ## Structuring it in a program

    `bc` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if bc ... ; then
        echo "ok"
    else
        echo "bc failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man bc` on a POSIX system.

    ## Related

    `expr`, `awk`
