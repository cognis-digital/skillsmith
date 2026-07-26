---
name: builtin-hash
description: "Program with Python's built-in hash: Return the hash value for the given object."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `hash`

    ## Overview

    `hash` is a Python built-in function — always available, no import required.

    Return the hash value for the given object.

Two objects that compare equal must also have the same hash value, but the
reverse is not necessarily true.

    ## Signature

    ```python
    hash(obj, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `hash` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = hash(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function hash in module builtins

hash(obj, /)
    Return the hash value for the given object.

    Two objects that compare equal must also have the same hash value, but the
    reverse is not necessarily true.

    ```
