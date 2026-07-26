---
name: builtin-len
description: "Program with Python's built-in len: Return the number of items in a container."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `len`

    ## Overview

    `len` is a Python built-in function — always available, no import required.

    Return the number of items in a container.

    ## Signature

    ```python
    len(obj, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `len` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = len(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function len in module builtins

len(obj, /)
    Return the number of items in a container.

    ```
