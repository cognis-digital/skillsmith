---
name: builtin-issubclass
description: "Program with Python's built-in issubclass: Return whether 'cls' is derived from another class or is the same class."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `issubclass`

    ## Overview

    `issubclass` is a Python built-in function — always available, no import required.

    Return whether 'cls' is derived from another class or is the same class.

A tuple, as in ``issubclass(x, (A, B, ...))``, may be given as the target to
check against. This is equivalent to ``issubclass(x, A) or issubclass(x, B)
or ...``.

    ## Signature

    ```python
    issubclass(cls, class_or_tuple, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `issubclass` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = issubclass(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function issubclass in module builtins

issubclass(cls, class_or_tuple, /)
    Return whether 'cls' is derived from another class or is the same class.

    A tuple, as in ``issubclass(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``issubclass(x, A) or issubclass(x, B)
    or ...``.

    ```
