---
name: builtin-isinstance
description: "Program with Python's built-in isinstance: Return whether an object is an instance of a class or of a subclass thereof."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `isinstance`

    ## Overview

    `isinstance` is a Python built-in function — always available, no import required.

    Return whether an object is an instance of a class or of a subclass thereof.

A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
or ...`` etc.

    ## Signature

    ```python
    isinstance(obj, class_or_tuple, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `isinstance` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = isinstance(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function isinstance in module builtins

isinstance(obj, class_or_tuple, /)
    Return whether an object is an instance of a class or of a subclass thereof.

    A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
    or ...`` etc.

    ```
