---
name: bash-pdftotext
description: "Program the pdftotext command: Extract plain text from a PDF."
version: 1.0.0
tags: [bash, cli, command-line, documents]
---

    # Command: `pdftotext`

    ## Overview

    Extract plain text from a PDF.

    ## When to use

    Use `pdftotext` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
pdftotext doc.pdf -
```
```bash
pdftotext -layout doc.pdf out.txt
```

    ## Structuring it in a program

    `pdftotext` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if pdftotext ... ; then
        echo "ok"
    else
        echo "pdftotext failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`pdftotext --help` on this machine)

```
pdftotext version 4.00
Copyright 1996-2017 Glyph & Cog, LLC
Usage: pdftotext [options] <PDF-file> [<text-file>]
  -f <int>             : first page to convert
  -l <int>             : last page to convert
  -layout              : maintain original physical layout
  -simple              : simple one-column page layout
  -table               : similar to -layout, but optimized for tables
  -lineprinter         : use strict fixed-pitch/height layout
  -raw                 : keep strings in content stream order
  -fixed <number>      : assume fixed-pitch (or tabular) text
  -linespacing <number>: fixed line spacing for LinePrinter mode
  -clip                : separate clipped text
  -nodiag              : discard diagonal text
  -enc <string>        : output text encoding name
  -eol <string>        : output end-of-line convention (unix, dos, or mac)
  -nopgbrk             : don't insert page breaks between pages
  -bom                 : insert a Unicode BOM at the start of the text file
  -opw <string>        : owner password (for encrypted files)
  -upw <string>        : user password (for encrypted files)
  -q                   : don't print any messages or errors
  -cfg <string>        : configuration file to use in place of .xpdfrc
  -v                   : print copyright and version info
  -h                   : print usage information
  -help                : print usage information
  --help               : print usage information
  -?                   : print usage information
```

    ## Related

    `pandoc`
