---
name: builtin-divmod
description: "Program with Python's built-in divmod: Return the tuple (x//y, x%y)."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `divmod`

    ## Overview

    `divmod` is a Python built-in function — always available, no import required.

    Return the tuple (x//y, x%y).  Invariant: div*y + mod == x.

    ## Signature

    ```python
    divmod(x, y, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `divmod` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = divmod(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function divmod in module builtins

divmod(x, y, /)
    Return the tuple (x//y, x%y).  Invariant: div*y + mod == x.

    ```
