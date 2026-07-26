---
name: builtin-callable
description: "Program with Python's built-in callable: Return whether the object is callable (i.e., some kind of function)."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `callable`

    ## Overview

    `callable` is a Python built-in function — always available, no import required.

    Return whether the object is callable (i.e., some kind of function).

Note that classes are callable, as are instances of classes with a
__call__() method.

    ## Signature

    ```python
    callable(obj, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `callable` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = callable(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function callable in module builtins

callable(obj, /)
    Return whether the object is callable (i.e., some kind of function).

    Note that classes are callable, as are instances of classes with a
    __call__() method.

    ```
