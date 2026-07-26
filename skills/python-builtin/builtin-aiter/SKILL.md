---
name: builtin-aiter
description: "Program with Python's built-in aiter: Return an AsyncIterator for an AsyncIterable object."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `aiter`

    ## Overview

    `aiter` is a Python built-in function — always available, no import required.

    Return an AsyncIterator for an AsyncIterable object.

    ## Signature

    ```python
    aiter(async_iterable, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `aiter` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = aiter(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function aiter in module builtins

aiter(async_iterable, /)
    Return an AsyncIterator for an AsyncIterable object.

    ```
