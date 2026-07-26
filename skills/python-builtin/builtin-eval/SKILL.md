---
name: builtin-eval
description: "Program with Python's built-in eval: Evaluate the given source in the context of globals and locals."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `eval`

    ## Overview

    `eval` is a Python built-in function — always available, no import required.

    Evaluate the given source in the context of globals and locals.

The source may be a string representing a Python expression
or a code object as returned by compile().
The globals must be a dictionary and locals can be any mapping,
defaulting to the current globals and locals.
If only globals is given, locals defaults to it.

    ## Signature

    ```python
    eval(source, /, globals=None, locals=None)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `eval` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = eval(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function eval in module builtins

eval(source, /, globals=None, locals=None)
    Evaluate the given source in the context of globals and locals.

    The source may be a string representing a Python expression
    or a code object as returned by compile().
    The globals must be a dictionary and locals can be any mapping,
    defaulting to the current globals and locals.
    If only globals is given, locals defaults to it.

    ```
