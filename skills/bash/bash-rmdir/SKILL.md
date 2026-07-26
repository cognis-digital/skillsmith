---
name: bash-rmdir
description: "Program the rmdir command: Remove empty directories."
version: 1.0.0
tags: [bash, cli, command-line, files]
---

    # Command: `rmdir`

    ## Overview

    Remove empty directories.

    ## When to use

    Use `rmdir` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
rmdir emptydir
```

    ## Structuring it in a program

    `rmdir` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if rmdir ... ; then
        echo "ok"
    else
        echo "rmdir failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`rmdir --help` on this machine)

```
Usage: rmdir [OPTION]... DIRECTORY...
Remove the DIRECTORY(ies), if they are empty.

      --ignore-fail-on-non-empty
                  ignore each failure that is solely because a directory
                    is non-empty
  -p, --parents   remove DIRECTORY and its ancestors; e.g., 'rmdir -p a/b/c' is
                    similar to 'rmdir a/b/c a/b a'
  -v, --verbose   output a diagnostic for every directory processed
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/rmdir>
or available locally via: info '(coreutils) rmdir invocation'
```

    ## Related

    `rm`, `mkdir`
