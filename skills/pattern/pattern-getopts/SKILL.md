---
name: pattern-getopts
description: "Parse short command-line options in a script with getopts."
version: 1.0.0
tags: [bash, command-structure, pattern, shell]
---

# Pattern: Option parsing (`getopts`)

## Overview

`getopts` is the shell builtin for parsing short options (`-v`, `-o file`) in a
portable, predictable way — better than hand-rolled `$1` inspection.

## Worked example

```bash
verbose=0 out=""
while getopts ":vo:h" opt; do
    case $opt in
        v) verbose=1 ;;
        o) out=$OPTARG ;;
        h) echo "usage: $0 [-v] [-o FILE]"; exit 0 ;;
        \?) echo "unknown option -$OPTARG" >&2; exit 2 ;;
        :)  echo "-$OPTARG needs an argument" >&2; exit 2 ;;
    esac
done
shift $((OPTIND - 1))          # remaining args are positional
```

## Structuring it in a program

- A trailing `:` in the optstring (`o:`) means that option takes an argument, found
  in `$OPTARG`.
- A leading `:` enables silent error handling so you can print your own messages.
- `shift $((OPTIND-1))` leaves `$@` holding the positional arguments.

## Pitfalls

- `getopts` handles only single-dash short options; for `--long` options use a
  manual `case` loop or a tool like `getopt`.
