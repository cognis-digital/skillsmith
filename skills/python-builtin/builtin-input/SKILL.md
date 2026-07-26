---
name: builtin-input
description: "Program with Python's built-in input: Read a string from standard input."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `input`

    ## Overview

    `input` is a Python built-in function — always available, no import required.

    Read a string from standard input.  The trailing newline is stripped.

The prompt string, if given, is printed to standard output without a
trailing newline before reading input.

If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
On *nix systems, readline is used if available.

    ## Signature

    ```python
    input(prompt='', /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `input` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = input(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function input in module builtins

input(prompt='', /)
    Read a string from standard input.  The trailing newline is stripped.

    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.

    ```
