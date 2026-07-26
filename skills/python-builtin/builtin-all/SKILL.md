---
name: builtin-all
description: "Program with Python's built-in all: Return True if bool(x) is True for all values x in the iterable."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `all`

    ## Overview

    `all` is a Python built-in function — always available, no import required.

    Return True if bool(x) is True for all values x in the iterable.

If the iterable is empty, return True.

    ## Signature

    ```python
    all(iterable, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `all` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = all(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function all in module builtins

all(iterable, /)
    Return True if bool(x) is True for all values x in the iterable.

    If the iterable is empty, return True.

    ```
