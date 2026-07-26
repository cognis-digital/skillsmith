---
name: builtin-vars
description: "Program with Python's built-in vars: vars([object]) -> dictionary Without arguments, equivalent to locals()."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `vars`

    ## Overview

    `vars` is a Python built-in function — always available, no import required.

    vars([object]) -> dictionary

Without arguments, equivalent to locals().
With an argument, equivalent to object.__dict__.

    ## Signature

    ```python
    vars
    ```

    ## When to use

    Built-ins are the first tool to reach for: `vars` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = vars(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function vars in module builtins

vars(...)
    vars([object]) -> dictionary

    Without arguments, equivalent to locals().
    With an argument, equivalent to object.__dict__.

    ```
