---
name: builtin-ascii
description: "Program with Python's built-in ascii: Return an ASCII-only representation of an object."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `ascii`

    ## Overview

    `ascii` is a Python built-in function — always available, no import required.

    Return an ASCII-only representation of an object.

As repr(), return a string containing a printable representation of an
object, but escape the non-ASCII characters in the string returned by
repr() using \\x, \\u or \\U escapes. This generates a string similar
to that returned by repr() in Python 2.

    ## Signature

    ```python
    ascii(obj, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `ascii` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = ascii(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function ascii in module builtins

ascii(obj, /)
    Return an ASCII-only representation of an object.

    As repr(), return a string containing a printable representation of an
    object, but escape the non-ASCII characters in the string returned by
    repr() using \\x, \\u or \\U escapes. This generates a string similar
    to that returned by repr() in Python 2.

    ```
