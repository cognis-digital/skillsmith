---
name: bash-ps
description: "Program the ps command: Report a snapshot of current processes."
version: 1.0.0
tags: [bash, cli, command-line, process]
---

    # Command: `ps`

    ## Overview

    Report a snapshot of current processes.

    ## When to use

    Use `ps` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
ps aux
```
```bash
ps -ef
```
```bash
ps -o pid,%cpu,cmd
```

    ## Structuring it in a program

    `ps` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if ps ... ; then
        echo "ok"
    else
        echo "ps failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`ps --help` on this machine)

```
Usage: ps [-aefls] [-u UID] [-p PID]

Report process status

 -a, --all       show processes of all users
 -e, --everyone  show processes of all users
 -f, --full      show process uids, ppids
 -h, --help      output usage information and exit
 -l, --long      show process uids, ppids, pgids, winpids
 -p, --process   show information for specified PID
 -s, --summary   show process summary
 -u, --user      list processes owned by UID
 -V, --version   output version information and exit
 -W, --windows   show windows as well as cygwin processes

With no options, ps outputs the long format by default
```

    ## Related

    `top`, `pgrep`
