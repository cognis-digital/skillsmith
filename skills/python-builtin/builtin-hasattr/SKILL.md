---
name: builtin-hasattr
description: "Program with Python's built-in hasattr: Return whether the object has an attribute with the given name."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `hasattr`

    ## Overview

    `hasattr` is a Python built-in function — always available, no import required.

    Return whether the object has an attribute with the given name.

This is done by calling getattr(obj, name) and catching AttributeError.

    ## Signature

    ```python
    hasattr(obj, name, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `hasattr` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = hasattr(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function hasattr in module builtins

hasattr(obj, name, /)
    Return whether the object has an attribute with the given name.

    This is done by calling getattr(obj, name) and catching AttributeError.

    ```
