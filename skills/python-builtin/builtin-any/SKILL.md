---
name: builtin-any
description: "Program with Python's built-in any: Return True if bool(x) is True for any x in the iterable."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `any`

    ## Overview

    `any` is a Python built-in function — always available, no import required.

    Return True if bool(x) is True for any x in the iterable.

If the iterable is empty, return False.

    ## Signature

    ```python
    any(iterable, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `any` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = any(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function any in module builtins

any(iterable, /)
    Return True if bool(x) is True for any x in the iterable.

    If the iterable is empty, return False.

    ```
