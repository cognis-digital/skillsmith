---
name: bash-jobs
description: "Program the jobs command: List shell background jobs."
version: 1.0.0
tags: [bash, cli, command-line, process, shell]
---

    # Command: `jobs`

    ## Overview

    List shell background jobs.

    ## When to use

    Use `jobs` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
jobs -l
```

    ## Structuring it in a program

    `jobs` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if jobs ... ; then
        echo "ok"
    else
        echo "jobs failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man jobs` on a POSIX system.

    ## Related

    `bg`, `fg`, `kill`
