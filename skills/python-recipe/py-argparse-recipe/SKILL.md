---
name: py-argparse-recipe
description: "Build a real CLI — positional args, options, subcommands, help — with the standard argparse module."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Command-line interfaces with argparse

    ## Overview

    `argparse` turns a function into a proper command-line tool with `--help`, type conversion, defaults, and subcommands. It is the standard, dependency-free way to accept arguments.

    ## When to use

    Build a real CLI — positional args, options, subcommands, help — with the standard argparse module.

    ## Worked examples

    **Basic**

```python
import argparse
p = argparse.ArgumentParser(description='do a thing')
p.add_argument('path')
p.add_argument('-n', '--num', type=int, default=1)
p.add_argument('-v', '--verbose', action='store_true')
args = p.parse_args()
```

**Subcommands**

```python
sub = p.add_subparsers(dest='cmd')
b = sub.add_parser('build'); b.add_argument('target')
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Give every option a sensible default and a help string.
- Use type= for conversion and validation instead of parsing strings yourself.

    ## Related

    `python-argparse`, `star-args`
