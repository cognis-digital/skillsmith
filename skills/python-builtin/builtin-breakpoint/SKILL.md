---
name: builtin-breakpoint
description: "Program with Python's built-in breakpoint: Call sys.breakpointhook(*args, **kws)."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `breakpoint`

    ## Overview

    `breakpoint` is a Python built-in function — always available, no import required.

    Call sys.breakpointhook(*args, **kws).  sys.breakpointhook() must accept
whatever arguments are passed.

By default, this drops you into the pdb debugger.

    ## Signature

    ```python
    breakpoint(*args, **kws)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `breakpoint` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = breakpoint(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function breakpoint in module builtins

breakpoint(*args, **kws)
    Call sys.breakpointhook(*args, **kws).  sys.breakpointhook() must accept
    whatever arguments are passed.

    By default, this drops you into the pdb debugger.

    ```
