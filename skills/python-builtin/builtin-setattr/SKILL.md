---
name: builtin-setattr
description: "Program with Python's built-in setattr: Sets the named attribute on the given object to the specified value."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `setattr`

    ## Overview

    `setattr` is a Python built-in function — always available, no import required.

    Sets the named attribute on the given object to the specified value.

setattr(x, 'y', v) is equivalent to ``x.y = v``

    ## Signature

    ```python
    setattr(obj, name, value, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `setattr` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = setattr(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function setattr in module builtins

setattr(obj, name, value, /)
    Sets the named attribute on the given object to the specified value.

    setattr(x, 'y', v) is equivalent to ``x.y = v``

    ```
