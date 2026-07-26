---
name: builtin-pow
description: "Program with Python's built-in pow: Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments Some types, such as ints, are able to use a more efficient algorithm when invoked using the three argument form."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `pow`

    ## Overview

    `pow` is a Python built-in function — always available, no import required.

    Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments

Some types, such as ints, are able to use a more efficient algorithm when
invoked using the three argument form.

    ## Signature

    ```python
    pow(base, exp, mod=None)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `pow` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = pow(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function pow in module builtins

pow(base, exp, mod=None)
    Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments

    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.

    ```
