---
name: bash-tput
description: "Program the tput command: Query the terminfo database — colors, cursor moves, terminal size."
version: 1.0.0
tags: [bash, cli, command-line, terminal]
---

    # Command: `tput`

    ## Overview

    Query the terminfo database — colors, cursor moves, terminal size.

    ## When to use

    Use `tput` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
tput cols
```
```bash
tput setaf 2
```
```bash
tput bold
```

    ## Structuring it in a program

    `tput` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if tput ... ; then
        echo "ok"
    else
        echo "tput failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`tput --help` on this machine)

```
tput: unknown option -- -
Usage: tput [options] [command]

Options:
  -S <<       read commands from standard input
  -T TERM     use this instead of $TERM
  -V          print curses-version
  -x          do not try to clear scrollback

Commands:
  clear       clear the screen
  init        initialize the terminal
  reset       reinitialize the terminal
  capname     unlike clear/init/reset, print value for capability "capname"
```

    ## Related

    `stty`
