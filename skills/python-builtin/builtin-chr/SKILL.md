---
name: builtin-chr
description: "Program with Python's built-in chr: Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `chr`

    ## Overview

    `chr` is a Python built-in function — always available, no import required.

    Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.

    ## Signature

    ```python
    chr(i, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `chr` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = chr(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function chr in module builtins

chr(i, /)
    Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.

    ```
