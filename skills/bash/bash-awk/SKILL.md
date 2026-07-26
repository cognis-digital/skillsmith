---
name: bash-awk
description: "Program the awk command: Pattern-action language for structured text: split into fields and compute per-line."
version: 1.0.0
tags: [bash, cli, command-line, fields, reporting, text]
---

    # Command: `awk`

    ## Overview

    Pattern-action language for structured text: split into fields and compute per-line.

    ## When to use

    Use `awk` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
awk '{print $1}' file
```
```bash
awk -F, '{sum+=$3} END{print sum}' data.csv
```
```bash
df | awk 'NR>1{print $5, $6}'
```

    ## Structuring it in a program

    `awk` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if awk ... ; then
        echo "ok"
    else
        echo "awk failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`awk --help` on this machine)

```
Usage: awk [POSIX or GNU style options] -f progfile [--] file ...
Usage: awk [POSIX or GNU style options] [--] 'program' file ...
POSIX options:		GNU long options: (standard)
	-f progfile		--file=progfile
	-F fs			--field-separator=fs
	-v var=val		--assign=var=val
Short options:		GNU long options: (extensions)
	-b			--characters-as-bytes
	-c			--traditional
	-C			--copyright
	-d[file]		--dump-variables[=file]
	-D[file]		--debug[=file]
	-e 'program-text'	--source='program-text'
	-E file			--exec=file
	-g			--gen-pot
	-h			--help
	-i includefile		--include=includefile
	-l library		--load=library
	-L[fatal|invalid]	--lint[=fatal|invalid]
	-M			--bignum
	-N			--use-lc-numeric
	-n			--non-decimal-data
	-o[file]		--pretty-print[=file]
	-O			--optimize
	-p[file]		--profile[=file]
	-P			--posix
	-r			--re-interval
	-s			--no-optimize
	-S			--sandbox
	-t			--lint-old
	-V			--version

To report bugs, see node `Bugs' in `gawk.info'
which is section `Reporting Problems and Bugs' in the
printed version.  This same information may be found at
https://www.gnu.org/software/gawk/manual/html_node/Bugs.html.
PLEASE do NOT try to report bugs by posting in comp.lang.awk,
or by using a web forum such as Stack Overflow.

gawk is a pattern scanning and processing language.
By default it reads standard input and writes standard output.

Examples:
	gawk '{ sum += $1 }; END { print sum }' file
	gawk -F: '{ print $1 }' /etc/passwd
```

    ## Related

    `sed`, `cut`, `grep`
