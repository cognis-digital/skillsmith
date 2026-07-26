---
name: bash-sleep
description: "Program the sleep command: Pause for a given duration."
version: 1.0.0
tags: [bash, cli, command-line, time]
---

    # Command: `sleep`

    ## Overview

    Pause for a given duration.

    ## When to use

    Use `sleep` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
sleep 5
```
```bash
sleep 0.5
```

    ## Structuring it in a program

    `sleep` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if sleep ... ; then
        echo "ok"
    else
        echo "sleep failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`sleep --help` on this machine)

```
Usage: sleep NUMBER[SUFFIX]...
  or:  sleep OPTION
Pause for NUMBER seconds.  SUFFIX may be 's' for seconds (the default),
'm' for minutes, 'h' for hours or 'd' for days.  NUMBER need not be an
integer.  Given two or more arguments, pause for the amount of time
specified by the sum of their values.

      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/sleep>
or available locally via: info '(coreutils) sleep invocation'
```

    ## Related

    `timeout`, `watch`
