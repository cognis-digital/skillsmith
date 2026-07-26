---
name: bash-realpath
description: "Program the realpath command: Resolve a path to its absolute, canonical form."
version: 1.0.0
tags: [bash, cli, command-line, paths]
---

    # Command: `realpath`

    ## Overview

    Resolve a path to its absolute, canonical form.

    ## When to use

    Use `realpath` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
realpath ./link
```

    ## Structuring it in a program

    `realpath` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if realpath ... ; then
        echo "ok"
    else
        echo "realpath failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`realpath --help` on this machine)

```
Usage: realpath [OPTION]... FILE...
Print the resolved absolute file name;
all but the last component must exist

  -e, --canonicalize-existing  all components of the path must exist
  -m, --canonicalize-missing   no path components need exist or be a directory
  -L, --logical                resolve '..' components before symlinks
  -P, --physical               resolve symlinks as encountered (default)
  -q, --quiet                  suppress most error messages
      --relative-to=DIR        print the resolved path relative to DIR
      --relative-base=DIR      print absolute paths unless paths below DIR
  -s, --strip, --no-symlinks   don't expand symlinks
  -z, --zero                   end each output line with NUL, not newline

      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/realpath>
or available locally via: info '(coreutils) realpath invocation'
```

    ## Related

    `readlink`
