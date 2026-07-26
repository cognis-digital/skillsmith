---
name: builtin-exit
description: "Program with Python's built-in exit: The built-in function `exit`."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `exit`

    ## Overview

    `exit` is a Python built-in function — always available, no import required.



    ## Signature

    ```python
    exit(code=None)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `exit` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = exit(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: Quitter in module _sitebuiltins object

class Quitter(builtins.object)
 |  Quitter(name, eof)
 |
 |  Methods defined here:
 |
 |  __call__(self, code=None)
 |      Call self as a function.
 |
 |  __init__(self, name, eof)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __repr__(self)
 |      Return repr(self).
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object

    ```
