---
name: builtin-oct
description: "Program with Python's built-in oct: Return the octal representation of an integer."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `oct`

    ## Overview

    `oct` is a Python built-in function — always available, no import required.

    Return the octal representation of an integer.

>>> oct(342391)
'0o1234567'

    ## Signature

    ```python
    oct(number, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `oct` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = oct(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function oct in module builtins

oct(number, /)
    Return the octal representation of an integer.

    >>> oct(342391)
    '0o1234567'

    ```
