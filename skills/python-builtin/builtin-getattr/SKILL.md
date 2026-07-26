---
name: builtin-getattr
description: "Program with Python's built-in getattr: getattr(object, name[, default]) -> value Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `getattr`

    ## Overview

    `getattr` is a Python built-in function — always available, no import required.

    getattr(object, name[, default]) -> value

Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
When a default argument is given, it is returned when the attribute doesn't
exist; without it, an exception is raised in that case.

    ## Signature

    ```python
    getattr
    ```

    ## When to use

    Built-ins are the first tool to reach for: `getattr` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = getattr(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function getattr in module builtins

getattr(...)
    getattr(object, name[, default]) -> value

    Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
    When a default argument is given, it is returned when the attribute doesn't
    exist; without it, an exception is raised in that case.

    ```
