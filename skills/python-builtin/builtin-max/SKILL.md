---
name: builtin-max
description: "Program with Python's built-in max: max(iterable, *[, default=obj, key=func]) -> value max(arg1, arg2, *args, *[, key=func]) -> value With a single iterable argument, return its biggest item."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `max`

    ## Overview

    `max` is a Python built-in function — always available, no import required.

    max(iterable, *[, default=obj, key=func]) -> value
max(arg1, arg2, *args, *[, key=func]) -> value

With a single iterable argument, return its biggest item. The
default keyword-only argument specifies an object to return if
the provided iterable is empty.
With two or more positional arguments, return the largest argument.

    ## Signature

    ```python
    max
    ```

    ## When to use

    Built-ins are the first tool to reach for: `max` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = max(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function max in module builtins

max(...)
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value

    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more positional arguments, return the largest argument.

    ```
