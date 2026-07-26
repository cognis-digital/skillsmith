---
name: builtin-bin
description: "Program with Python's built-in bin: Return the binary representation of an integer."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `bin`

    ## Overview

    `bin` is a Python built-in function — always available, no import required.

    Return the binary representation of an integer.

>>> bin(2796202)
'0b1010101010101010101010'

    ## Signature

    ```python
    bin(number, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `bin` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = bin(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function bin in module builtins

bin(number, /)
    Return the binary representation of an integer.

    >>> bin(2796202)
    '0b1010101010101010101010'

    ```
