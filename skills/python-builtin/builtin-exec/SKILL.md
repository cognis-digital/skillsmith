---
name: builtin-exec
description: "Program with Python's built-in exec: Execute the given source in the context of globals and locals."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `exec`

    ## Overview

    `exec` is a Python built-in function — always available, no import required.

    Execute the given source in the context of globals and locals.

The source may be a string representing one or more Python statements
or a code object as returned by compile().
The globals must be a dictionary and locals can be any mapping,
defaulting to the current globals and locals.
If only globals is given, locals defaults to it.
The closure must be a tuple of cellvars, and can only be used
when source is a code object requiring exactly that many cellvars.

    ## Signature

    ```python
    exec(source, /, globals=None, locals=None, *, closure=None)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `exec` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = exec(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function exec in module builtins

exec(source, /, globals=None, locals=None, *, closure=None)
    Execute the given source in the context of globals and locals.

    The source may be a string representing one or more Python statements
    or a code object as returned by compile().
    The globals must be a dictionary and locals can be any mapping,
    defaulting to the current globals and locals.
    If only globals is given, locals defaults to it.
    The closure must be a tuple of cellvars, and can only be used
    when source is a code object requiring exactly that many cellvars.

    ```
