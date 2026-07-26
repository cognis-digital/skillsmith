---
name: bash-kill
description: "Program the kill command: Send a signal to a process by PID."
version: 1.0.0
tags: [bash, cli, command-line, process, signal]
---

    # Command: `kill`

    ## Overview

    Send a signal to a process by PID.

    ## When to use

    Use `kill` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
kill 1234
```
```bash
kill -9 1234
```
```bash
kill -TERM $(pgrep app)
```

    ## Structuring it in a program

    `kill` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if kill ... ; then
        echo "ok"
    else
        echo "kill failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`kill --help` on this machine)

```
Usage: kill [-fW] [-signal] [-s signal] pid1 [pid2 ...]
       kill -l [signal]

Send signals to processes

 -f, --force     force, using win32 interface if necessary
 -l, --list      print a list of signal names
 -s, --signal    send signal (use kill --list for a list)
 -W, --winpid    specified pids are windows PIDs, not Cygwin PIDs
                 (use with extreme caution!)
 -h, --help      output usage information and exit
 -V, --version   output version information and exit
```

    ## Related

    `pkill`, `killall`
