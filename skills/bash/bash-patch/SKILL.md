---
name: bash-patch
description: "Program the patch command: Apply a diff/patch to files."
version: 1.0.0
tags: [bash, cli, command-line, files]
---

    # Command: `patch`

    ## Overview

    Apply a diff/patch to files.

    ## When to use

    Use `patch` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
patch -p1 < fix.patch
```

    ## Structuring it in a program

    `patch` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if patch ... ; then
        echo "ok"
    else
        echo "patch failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`patch --help` on this machine)

```
Usage: patch [OPTION]... [ORIGFILE [PATCHFILE]]

Input options:

  -p NUM  --strip=NUM  Strip NUM leading components from file names.
  -F LINES  --fuzz LINES  Set the fuzz factor to LINES for inexact matching.
  -l  --ignore-whitespace  Ignore white space changes between patch and input.

  -c  --context  Interpret the patch as a context difference.
  -e  --ed  Interpret the patch as an ed script.
  -n  --normal  Interpret the patch as a normal difference.
  -u  --unified  Interpret the patch as a unified difference.

  -N  --forward  Ignore patches that appear to be reversed or already applied.
  -R  --reverse  Assume patches were created with old and new files swapped.

  -i PATCHFILE  --input=PATCHFILE  Read patch from PATCHFILE instead of stdin.

Output options:

  -o FILE  --output=FILE  Output patched files to FILE.
  -r FILE  --reject-file=FILE  Output rejects to FILE.

  -D NAME  --ifdef=NAME  Make merged if-then-else output using NAME.
  --merge  Merge using conflict markers instead of creating reject files.
  -E  --remove-empty-files  Remove output files that are empty after patching.

  -Z  --set-utc  Set times of patched files, assuming diff uses UTC (GMT).
  -T  --set-time  Likewise, assuming local time.

  --quoting-style=WORD   output file names using quoting style WORD.
    Valid WORDs are: literal, shell, shell-always, c, escape.
    Default is taken from QUOTING_STYLE env variable, or 'shell' if unset.

Backup and version control options:

  -b  --backup  Back up the original contents of each file.
  --backup-if-mismatch  Back up if the patch does not match exactly.
  --no-backup-if-mismatch  Back up mismatches only if otherwise requested.

  -V STYLE  --version-control=STYLE  Use STYLE version control.
	STYLE is either 'simple', 'numbered', or 'existing'.
  -B PREFIX  --prefix=PREFIX  Prepend PREFIX to backup file names.
  -Y PREFIX  --basename-prefix=PREFIX  Prepend PREFIX to backup file basenames.
  -z SUFFIX  --suffix=SUFFIX  Append SUFFIX to backup file names.

  -g NUM  --get=NUM  Get files from RCS etc. if positive; ask if negative.

Miscellaneous options:

  -t  --batch  Ask no questions; skip bad-Prereq patches; assume reversed.
  -f  --force  Like -t, but ignore bad-Prereq patches, and assume unreversed.
  -s  --quiet  --silent  Work silently unless an error occurs.
  --verbose  Output extra information about the work being done.
  --dry-run  Do not actually change any files; just print what would happen.
  --posix  Conform to the POSIX standard.

  -d DIR  --directory=DIR  Change the working directory to DIR first.
  --reject-format=FORMAT  Create 'context' or 'unified' rejects.
  --binary  Read data in binary mode.  Writing data is always binary.
  --read-only=BEHAVIOR  How to handle read-only input files: 'ignore' that they
                        are read-only, 'warn' (default), or 'fail'.

  -v  --version  Output version info.
  --help  Output this help.

Report bugs to <bug-patch@gnu.org>.
```

    ## Related

    `diff`, `git`
