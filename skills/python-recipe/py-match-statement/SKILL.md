---
name: py-match-statement
description: "Branch on the shape of data with match/case, destructuring as you go (Python 3.10+)."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Structural pattern matching (match)

    ## Overview

    `match` compares a value against structural patterns and binds parts of it — cleaner than long if/elif chains for tagged data, sequences, and mappings.

    ## When to use

    Branch on the shape of data with match/case, destructuring as you go (Python 3.10+).

    ## Worked examples

    **Literals + capture**

```python
match command.split():
    case ['go', direction]:
        move(direction)
    case ['quit']:
        raise SystemExit
    case _:
        print('unknown')
```

**Mappings / classes**

```python
match event:
    case {'type': 'click', 'x': x, 'y': y}:
        click(x, y)
    case Point(x=0, y=0):
        origin()
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - `case _` is the wildcard/default — put it last.
- A bare name in a pattern binds (captures), it does not compare; use dotted names or guards to compare.

    ## Related

    `enum`, `unpacking`
