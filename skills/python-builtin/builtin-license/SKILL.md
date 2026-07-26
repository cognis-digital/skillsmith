---
name: builtin-license
description: "Program with Python's built-in license: interactive prompt objects for printing the license text, a list of contributors and the copyright notice."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `license`

    ## Overview

    `license` is a Python built-in function — always available, no import required.

    interactive prompt objects for printing the license text, a list of
contributors and the copyright notice.

    ## Signature

    ```python
    license()
    ```

    ## When to use

    Built-ins are the first tool to reach for: `license` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = license(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: _Printer in module _sitebuiltins object

class _Printer(builtins.object)
 |  _Printer(name, data, files=(), dirs=())
 |
 |  interactive prompt objects for printing the license text, a list of
 |  contributors and the copyright notice.
 |
 |  Methods defined here:
 |
 |  __call__(self)
 |      Call self as a function.
 |
 |  __init__(self, name, data, files=(), dirs=())
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
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  MAXLINES = 23

    ```
