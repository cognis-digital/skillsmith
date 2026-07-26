---
name: builtin-min
description: "Program with Python's built-in min: min(iterable, *[, default=obj, key=func]) -> value min(arg1, arg2, *args, *[, key=func]) -> value With a single iterable argument, return its smallest item."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `min`

    ## Overview

    `min` is a Python built-in function — always available, no import required.

    min(iterable, *[, default=obj, key=func]) -> value
min(arg1, arg2, *args, *[, key=func]) -> value

With a single iterable argument, return its smallest item. The
default keyword-only argument specifies an object to return if
the provided iterable is empty.
With two or more positional arguments, return the smallest argument.

    ## Signature

    ```python
    min
    ```

    ## When to use

    Built-ins are the first tool to reach for: `min` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = min(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function min in module builtins

min(...)
    min(iterable, *[, default=obj, key=func]) -> value
    min(arg1, arg2, *args, *[, key=func]) -> value

    With a single iterable argument, return its smallest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more positional arguments, return the smallest argument.

    ```
