---
name: bash-csplit
description: "Program the csplit command: Split a file into sections determined by context lines/patterns."
version: 1.0.0
tags: [bash, cli, command-line, files, text]
---

    # Command: `csplit`

    ## Overview

    Split a file into sections determined by context lines/patterns.

    ## When to use

    Use `csplit` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
csplit file '/^CHAPTER/' '{*}'
```

    ## Structuring it in a program

    `csplit` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if csplit ... ; then
        echo "ok"
    else
        echo "csplit failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`csplit --help` on this machine)

```
Usage: csplit [OPTION]... FILE PATTERN...
Output pieces of FILE separated by PATTERN(s) to files 'xx00', 'xx01', ...,
and output byte counts of each piece to standard output.

Read standard input if FILE is -

Mandatory arguments to long options are mandatory for short options too.
  -b, --suffix-format=FORMAT  use sprintf FORMAT instead of %02d
  -f, --prefix=PREFIX        use PREFIX instead of 'xx'
  -k, --keep-files           do not remove output files on errors
      --suppress-matched     suppress the lines matching PATTERN
  -n, --digits=DIGITS        use specified number of digits instead of 2
  -s, --quiet, --silent      do not print counts of output file sizes
  -z, --elide-empty-files    remove empty output files
      --help     display this help and exit
      --version  output version information and exit

Each PATTERN may be:
  INTEGER            copy up to but not including specified line number
  /REGEXP/[OFFSET]   copy up to but not including a matching line
  %REGEXP%[OFFSET]   skip to, but not including a matching line
  {INTEGER}          repeat the previous pattern specified number of times
  {*}                repeat the previous pattern as many times as possible

A line OFFSET is a required '+' or '-' followed by a positive integer.

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/csplit>
or available locally via: info '(coreutils) csplit invocation'
```

    ## Related

    `split`
