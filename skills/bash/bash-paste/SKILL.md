---
name: bash-paste
description: "Program the paste command: Merge lines of files side by side, delimited."
version: 1.0.0
tags: [bash, cli, command-line, text]
---

    # Command: `paste`

    ## Overview

    Merge lines of files side by side, delimited.

    ## When to use

    Use `paste` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
paste a b
```
```bash
paste -d, col1 col2
```
```bash
paste -s -d+ nums
```

    ## Structuring it in a program

    `paste` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if paste ... ; then
        echo "ok"
    else
        echo "paste failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`paste --help` on this machine)

```
Usage: paste [OPTION]... [FILE]...
Write lines consisting of the sequentially corresponding lines from
each FILE, separated by TABs, to standard output.

With no FILE, or when FILE is -, read standard input.

Mandatory arguments to long options are mandatory for short options too.
  -d, --delimiters=LIST   reuse characters from LIST instead of TABs
  -s, --serial            paste one file at a time instead of in parallel
  -z, --zero-terminated    line delimiter is NUL, not newline
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/paste>
or available locally via: info '(coreutils) paste invocation'
```

    ## Related

    `cut`, `join`
