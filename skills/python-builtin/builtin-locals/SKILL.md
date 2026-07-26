---
name: builtin-locals
description: "Program with Python's built-in locals: Return a dictionary containing the current scope's local variables."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `locals`

    ## Overview

    `locals` is a Python built-in function — always available, no import required.

    Return a dictionary containing the current scope's local variables.

NOTE: Whether or not updates to this dictionary will affect name lookups in
the local scope and vice-versa is *implementation dependent* and not
covered by any backwards compatibility guarantees.

    ## Signature

    ```python
    locals()
    ```

    ## When to use

    Built-ins are the first tool to reach for: `locals` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = locals(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function locals in module builtins

locals()
    Return a dictionary containing the current scope's local variables.

    NOTE: Whether or not updates to this dictionary will affect name lookups in
    the local scope and vice-versa is *implementation dependent* and not
    covered by any backwards compatibility guarantees.

    ```
