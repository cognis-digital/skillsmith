---
name: builtin-ord
description: "Program with Python's built-in ord: Return the ordinal value of a character."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `ord`

    ## Overview

    `ord` is a Python built-in function — always available, no import required.

    Return the ordinal value of a character.

If the argument is a one-character string, return the Unicode code
point of that character.

If the argument is a bytes or bytearray object of length 1, return its
single byte value.

    ## Signature

    ```python
    ord(character, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `ord` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = ord(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function ord in module builtins

ord(character, /)
    Return the ordinal value of a character.

    If the argument is a one-character string, return the Unicode code
    point of that character.

    If the argument is a bytes or bytearray object of length 1, return its
    single byte value.

    ```
