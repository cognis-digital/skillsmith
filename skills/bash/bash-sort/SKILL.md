---
name: bash-sort
description: "Program the sort command: Sort lines of text, numerically or lexically, with keys and uniqueness."
version: 1.0.0
tags: [bash, cli, command-line, ordering, text]
---

    # Command: `sort`

    ## Overview

    Sort lines of text, numerically or lexically, with keys and uniqueness.

    ## When to use

    Use `sort` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
sort -n nums
```
```bash
sort -k2,2 -t, data.csv
```
```bash
sort -u names
```

    ## Structuring it in a program

    `sort` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if sort ... ; then
        echo "ok"
    else
        echo "sort failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`sort --help` on this machine)

```
--helpThe system cannot find the file specified.
```

    ## Related

    `uniq`, `comm`, `shuf`
