---
name: builtin-next
description: "Program with Python's built-in next: next(iterator[, default]) Return the next item from the iterator."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `next`

    ## Overview

    `next` is a Python built-in function — always available, no import required.

    next(iterator[, default])

Return the next item from the iterator. If default is given and the iterator
is exhausted, it is returned instead of raising StopIteration.

    ## Signature

    ```python
    next
    ```

    ## When to use

    Built-ins are the first tool to reach for: `next` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = next(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function next in module builtins

next(...)
    next(iterator[, default])

    Return the next item from the iterator. If default is given and the iterator
    is exhausted, it is returned instead of raising StopIteration.

    ```
