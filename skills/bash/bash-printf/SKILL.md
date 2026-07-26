---
name: bash-printf
description: "Program the printf command: Formatted output — more predictable than echo."
version: 1.0.0
tags: [bash, cli, command-line, io, shell]
---

    # Command: `printf`

    ## Overview

    Formatted output — more predictable than echo.

    ## When to use

    Use `printf` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
printf '%s=%d\n' k 3
```
```bash
printf '%.2f\n' 3.14159
```

    ## Structuring it in a program

    `printf` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if printf ... ; then
        echo "ok"
    else
        echo "printf failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`printf --help` on this machine)

```
Usage: printf FORMAT [ARGUMENT]...
  or:  printf OPTION
Print ARGUMENT(s) according to FORMAT, or execute according to OPTION:

      --help     display this help and exit
      --version  output version information and exit

FORMAT controls the output as in C printf.  Interpreted sequences are:

  \"      double quote
  \\      backslash
  \a      alert (BEL)
  \b      backspace
  \c      produce no further output
  \e      escape
  \f      form feed
  \n      new line
  \r      carriage return
  \t      horizontal tab
  \v      vertical tab
  \NNN    byte with octal value NNN (1 to 3 digits)
  \xHH    byte with hexadecimal value HH (1 to 2 digits)
  \uHHHH  Unicode (ISO/IEC 10646) character with hex value HHHH (4 digits)
  \UHHHHHHHH  Unicode character with hex value HHHHHHHH (8 digits)
  %%      a single %
  %b      ARGUMENT as a string with '\' escapes interpreted,
          except that octal escapes are of the form \0 or \0NNN
  %q      ARGUMENT is printed in a format that can be reused as shell input,
          escaping non-printable characters with the proposed POSIX $'' syntax.

and all C format specifications ending with one of diouxXfeEgGcs, with
ARGUMENTs converted to proper type first.  Variable widths are handled.

NOTE: your shell may have its own version of printf, which usually supersedes
the version described here.  Please refer to your shell's documentation
for details about the options it supports.

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/printf>
or available locally via: info '(coreutils) printf invocation'
```

    ## Related

    `echo`
