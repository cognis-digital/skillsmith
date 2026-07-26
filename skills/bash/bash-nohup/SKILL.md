---
name: bash-nohup
description: "Program the nohup command: Run a command immune to hangups, detached from the terminal."
version: 1.0.0
tags: [bash, cli, command-line, process]
---

    # Command: `nohup`

    ## Overview

    Run a command immune to hangups, detached from the terminal.

    ## When to use

    Use `nohup` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
nohup ./run.sh &
```

    ## Structuring it in a program

    `nohup` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if nohup ... ; then
        echo "ok"
    else
        echo "nohup failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`nohup --help` on this machine)

```
Usage: nohup COMMAND [ARG]...
  or:  nohup OPTION
Run COMMAND, ignoring hangup signals.

      --help     display this help and exit
      --version  output version information and exit

If standard input is a terminal, redirect it from an unreadable file.
If standard output is a terminal, append output to 'nohup.out' if possible,
'$HOME/nohup.out' otherwise.
If standard error is a terminal, redirect it to standard output.
To save output to FILE, use 'nohup COMMAND > FILE'.

NOTE: your shell may have its own version of nohup, which usually supersedes
the version described here.  Please refer to your shell's documentation
for details about the options it supports.

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/nohup>
or available locally via: info '(coreutils) nohup invocation'
```

    ## Related

    `disown`, `setsid`
