---
name: builtin-warning
description: "Program with Python's built-in Warning: Base class for warning categories."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `Warning`

    ## Overview

    `Warning` is a Python built-in class — always available, no import required.

    Base class for warning categories.

    ## Signature

    ```python
    Warning
    ```

    ## When to use

    Built-ins are the first tool to reach for: `Warning` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = Warning(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class Warning in module builtins

class Warning(Exception)
 |  Base class for warning categories.
 |
 |  Method resolution order:
 |      Warning
 |      Exception
 |      BaseException
 |      object
 |
 |  Built-in subclasses:
 |      BytesWarning
 |      DeprecationWarning
 |      EncodingWarning
 |      FutureWarning
 |      ... and 7 other subclasses
 |
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from BaseException:
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __reduce__(self, /)
 |      Helper for pickle.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __setstate__(self, state, /)
 |
 |  __str__(self, /)
 |      Return str(self).
 |
 |  add_note(self, note, /)
 |      Add a note to the exception
 |
 |  with_traceback(self, tb, /)
 |      Set self.__traceback__ to tb and return self.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from BaseException:
 |
 |  __cause__
 |
 |  __context__
 |
 |  __dict__
 |
 |  __suppress_context__
 |
 |  __traceback__
 |
 |  args

    ```
