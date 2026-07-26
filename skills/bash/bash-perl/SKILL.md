---
name: bash-perl
description: "Program the perl command: Powerful text-processing language; a one-liner Swiss army knife."
version: 1.0.0
tags: [bash, cli, command-line, language, text]
---

    # Command: `perl`

    ## Overview

    Powerful text-processing language; a one-liner Swiss army knife.

    ## When to use

    Use `perl` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
perl -pe 's/a/b/g' file
```
```bash
perl -ne 'print if /re/' file
```
```bash
perl -e 'print 1+2'
```

    ## Structuring it in a program

    `perl` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if perl ... ; then
        echo "ok"
    else
        echo "perl failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`perl --help` on this machine)

```
Usage: perl [switches] [--] [programfile] [arguments]
  -0[octal/hexadecimal] specify record separator (\0, if no argument)
  -a                    autosplit mode with -n or -p (splits $_ into @F)
  -C[number/list]       enables the listed Unicode features
  -c                    check syntax only (runs BEGIN and CHECK blocks)
  -d[t][:MOD]           run program under debugger or module Devel::MOD
  -D[number/letters]    set debugging flags (argument is a bit mask or alphabets)
  -e commandline        one line of program (several -e's allowed, omit programfile)
  -E commandline        like -e, but enables all optional features
  -f                    don't do $sitelib/sitecustomize.pl at startup
  -F/pattern/           split() pattern for -a switch (//'s are optional)
  -i[extension]         edit <> files in place (makes backup if extension supplied)
  -Idirectory           specify @INC/#include directory (several -I's allowed)
  -l[octnum]            enable line ending processing, specifies line terminator
  -[mM][-]module        execute "use/no module..." before executing program
  -n                    assume "while (<>) { ... }" loop around program
  -p                    assume loop like -n but print line also, like sed
  -s                    enable rudimentary parsing for switches after programfile
  -S                    look for programfile using PATH environment variable
  -t                    enable tainting warnings
  -T                    enable tainting checks
  -u                    dump core after parsing program
  -U                    allow unsafe operations
  -v                    print version, patchlevel and license
  -V[:configvar]        print configuration summary (or a single Config.pm variable)
  -w                    enable many useful warnings
  -W                    enable all warnings
  -x[directory]         ignore text before #!perl line (optionally cd to directory)
  -X                    disable all warnings

Run 'perldoc perl' for more help with Perl.
```

    ## Related

    `awk`, `sed`
