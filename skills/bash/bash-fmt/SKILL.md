---
name: bash-fmt
description: "Program the fmt command: Reformat/rewrap paragraphs to a target width."
version: 1.0.0
tags: [bash, cli, command-line, text]
---

    # Command: `fmt`

    ## Overview

    Reformat/rewrap paragraphs to a target width.

    ## When to use

    Use `fmt` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
fmt -w 80 notes
```

    ## Structuring it in a program

    `fmt` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if fmt ... ; then
        echo "ok"
    else
        echo "fmt failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`fmt --help` on this machine)

```
Usage: fmt [-WIDTH] [OPTION]... [FILE]...
Reformat each paragraph in the FILE(s), writing to standard output.
The option -WIDTH is an abbreviated form of --width=DIGITS.

With no FILE, or when FILE is -, read standard input.

Mandatory arguments to long options are mandatory for short options too.
  -c, --crown-margin        preserve indentation of first two lines
  -p, --prefix=STRING       reformat only lines beginning with STRING,
                              reattaching the prefix to reformatted lines
  -s, --split-only          split long lines, but do not refill
  -t, --tagged-paragraph    indentation of first line different from second
  -u, --uniform-spacing     one space between words, two after sentences
  -w, --width=WIDTH         maximum line width (default of 75 columns)
  -g, --goal=WIDTH          goal width (default of 93% of width)
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/fmt>
or available locally via: info '(coreutils) fmt invocation'
```

    ## Related

    `fold`
