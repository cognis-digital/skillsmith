---
name: builtin-sorted
description: "Program with Python's built-in sorted: Return a new list containing all items from the iterable in ascending order."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `sorted`

    ## Overview

    `sorted` is a Python built-in function — always available, no import required.

    Return a new list containing all items from the iterable in ascending order.

A custom key function can be supplied to customize the sort order, and the
reverse flag can be set to request the result in descending order.

    ## Signature

    ```python
    sorted(iterable, /, *, key=None, reverse=False)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `sorted` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = sorted(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function sorted in module builtins

sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.

    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.

    ```
