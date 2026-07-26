---
name: builtin-round
description: "Program with Python's built-in round: Round a number to a given precision in decimal digits."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `round`

    ## Overview

    `round` is a Python built-in function — always available, no import required.

    Round a number to a given precision in decimal digits.

The return value is an integer if ndigits is omitted or None.  Otherwise
the return value has the same type as the number.  ndigits may be negative.

    ## Signature

    ```python
    round(number, ndigits=None)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `round` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = round(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function round in module builtins

round(number, ndigits=None)
    Round a number to a given precision in decimal digits.

    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.

    ```
