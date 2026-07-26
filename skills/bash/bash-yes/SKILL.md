---
name: bash-yes
description: "Program the yes command: Repeat a string until killed — feed prompts or generate load."
version: 1.0.0
tags: [bash, cli, command-line, shell]
---

    # Command: `yes`

    ## Overview

    Repeat a string until killed — feed prompts or generate load.

    ## When to use

    Use `yes` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
yes | rm -i *
```
```bash
yes hello | head
```

    ## Structuring it in a program

    `yes` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if yes ... ; then
        echo "ok"
    else
        echo "yes failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`yes --help` on this machine)

```
Usage: yes [STRING]...
  or:  yes OPTION
Repeatedly output a line with all specified STRING(s), or 'y'.

      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/yes>
or available locally via: info '(coreutils) yes invocation'
```

    ## Related

    `seq`
