---
name: builtin-sum
description: "Program with Python's built-in sum: Return the sum of a 'start' value (default: 0) plus an iterable of numbers When the iterable is empty, return the start value."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `sum`

    ## Overview

    `sum` is a Python built-in function — always available, no import required.

    Return the sum of a 'start' value (default: 0) plus an iterable of numbers

When the iterable is empty, return the start value.
This function is intended specifically for use with numeric values and may
reject non-numeric types.

    ## Signature

    ```python
    sum(iterable, /, start=0)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `sum` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = sum(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function sum in module builtins

sum(iterable, /, start=0)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers

    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.

    ```
