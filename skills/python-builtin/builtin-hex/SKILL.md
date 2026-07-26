---
name: builtin-hex
description: "Program with Python's built-in hex: Return the hexadecimal representation of an integer."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `hex`

    ## Overview

    `hex` is a Python built-in function — always available, no import required.

    Return the hexadecimal representation of an integer.

>>> hex(12648430)
'0xc0ffee'

    ## Signature

    ```python
    hex(number, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `hex` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = hex(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function hex in module builtins

hex(number, /)
    Return the hexadecimal representation of an integer.

    >>> hex(12648430)
    '0xc0ffee'

    ```
