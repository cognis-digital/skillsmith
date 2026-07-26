---
name: builtin-id
description: "Program with Python's built-in id: Return the identity of an object."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `id`

    ## Overview

    `id` is a Python built-in function — always available, no import required.

    Return the identity of an object.

This is guaranteed to be unique among simultaneously existing objects.
(CPython uses the object's memory address.)

    ## Signature

    ```python
    id(obj, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `id` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = id(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function id in module builtins

id(obj, /)
    Return the identity of an object.

    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)

    ```
