---
name: builtin-delattr
description: "Program with Python's built-in delattr: Deletes the named attribute from the given object."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `delattr`

    ## Overview

    `delattr` is a Python built-in function — always available, no import required.

    Deletes the named attribute from the given object.

delattr(x, 'y') is equivalent to ``del x.y``

    ## Signature

    ```python
    delattr(obj, name, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `delattr` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = delattr(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function delattr in module builtins

delattr(obj, name, /)
    Deletes the named attribute from the given object.

    delattr(x, 'y') is equivalent to ``del x.y``

    ```
