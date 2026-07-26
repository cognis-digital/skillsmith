---
name: builtin-iter
description: "Program with Python's built-in iter: iter(iterable) -> iterator iter(callable, sentinel) -> iterator Get an iterator from an object."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `iter`

    ## Overview

    `iter` is a Python built-in function — always available, no import required.

    iter(iterable) -> iterator
iter(callable, sentinel) -> iterator

Get an iterator from an object.  In the first form, the argument must
supply its own iterator, or be a sequence.
In the second form, the callable is called until it returns the sentinel.

    ## Signature

    ```python
    iter
    ```

    ## When to use

    Built-ins are the first tool to reach for: `iter` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = iter(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function iter in module builtins

iter(...)
    iter(iterable) -> iterator
    iter(callable, sentinel) -> iterator

    Get an iterator from an object.  In the first form, the argument must
    supply its own iterator, or be a sequence.
    In the second form, the callable is called until it returns the sentinel.

    ```
