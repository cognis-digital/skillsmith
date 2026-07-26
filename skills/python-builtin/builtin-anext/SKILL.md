---
name: builtin-anext
description: "Program with Python's built-in anext: Return the next item from the async iterator."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `anext`

    ## Overview

    `anext` is a Python built-in function — always available, no import required.

    Return the next item from the async iterator.

If default is given and the async iterator is exhausted,
it is returned instead of raising StopAsyncIteration.

    ## Signature

    ```python
    anext
    ```

    ## When to use

    Built-ins are the first tool to reach for: `anext` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = anext(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function anext in module builtins

anext(aiterator, default=<unrepresentable>, /)
    Return the next item from the async iterator.

    If default is given and the async iterator is exhausted,
    it is returned instead of raising StopAsyncIteration.

    ```
