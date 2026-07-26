---
name: builtin-repr
description: "Program with Python's built-in repr: Return the canonical string representation of the object."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `repr`

    ## Overview

    `repr` is a Python built-in function — always available, no import required.

    Return the canonical string representation of the object.

For many object types, including most builtins, eval(repr(obj)) == obj.

    ## Signature

    ```python
    repr(obj, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `repr` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = repr(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function repr in module builtins

repr(obj, /)
    Return the canonical string representation of the object.

    For many object types, including most builtins, eval(repr(obj)) == obj.

    ```
