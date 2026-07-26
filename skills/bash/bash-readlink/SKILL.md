---
name: bash-readlink
description: "Program the readlink command: Print the target of a symbolic link."
version: 1.0.0
tags: [bash, cli, command-line, paths]
---

    # Command: `readlink`

    ## Overview

    Print the target of a symbolic link.

    ## When to use

    Use `readlink` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
readlink -f link
```

    ## Structuring it in a program

    `readlink` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if readlink ... ; then
        echo "ok"
    else
        echo "readlink failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`readlink --help` on this machine)

```
Usage: readlink [OPTION]... FILE...
Print value of a symbolic link or canonical file name

  -f, --canonicalize            canonicalize by following every symlink in
                                every component of the given name recursively;
                                all but the last component must exist
  -e, --canonicalize-existing   canonicalize by following every symlink in
                                every component of the given name recursively,
                                all components must exist
  -m, --canonicalize-missing    canonicalize by following every symlink in
                                every component of the given name recursively,
                                without requirements on components existence
  -n, --no-newline              do not output the trailing delimiter
  -q, --quiet
  -s, --silent                  suppress most error messages (on by default)
  -v, --verbose                 report error messages
  -z, --zero                    end each output line with NUL, not newline
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/readlink>
or available locally via: info '(coreutils) readlink invocation'
```

    ## Related

    `realpath`, `ln`
