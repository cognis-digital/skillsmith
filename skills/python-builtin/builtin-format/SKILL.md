---
name: builtin-format
description: "Program with Python's built-in format: Return type(value).__format__(value, format_spec) Many built-in types implement format_spec according to the Format Specification Mini-language."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `format`

    ## Overview

    `format` is a Python built-in function — always available, no import required.

    Return type(value).__format__(value, format_spec)

Many built-in types implement format_spec according to the
Format Specification Mini-language. See help('FORMATTING').

If type(value) does not supply a method named __format__
and format_spec is empty, then str(value) is returned.
See also help('SPECIALMETHODS').

    ## Signature

    ```python
    format(value, format_spec='', /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `format` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = format(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function format in module builtins

format(value, format_spec='', /)
    Return type(value).__format__(value, format_spec)

    Many built-in types implement format_spec according to the
    Format Specification Mini-language. See help('FORMATTING').

    If type(value) does not supply a method named __format__
    and format_spec is empty, then str(value) is returned.
    See also help('SPECIALMETHODS').

    ```
