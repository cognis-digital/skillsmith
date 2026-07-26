---
name: builtin-globals
description: "Program with Python's built-in globals: Return the dictionary containing the current scope's global variables."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `globals`

    ## Overview

    `globals` is a Python built-in function — always available, no import required.

    Return the dictionary containing the current scope's global variables.

NOTE: Updates to this dictionary *will* affect name lookups in the current
global scope and vice-versa.

    ## Signature

    ```python
    globals()
    ```

    ## When to use

    Built-ins are the first tool to reach for: `globals` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = globals(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function globals in module builtins

globals()
    Return the dictionary containing the current scope's global variables.

    NOTE: Updates to this dictionary *will* affect name lookups in the current
    global scope and vice-versa.

    ```
