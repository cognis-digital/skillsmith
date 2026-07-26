---
name: builtin-lookuperror
description: "Program with Python's built-in LookupError: Base class for lookup errors."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `LookupError`

    ## Overview

    `LookupError` is a Python built-in class — always available, no import required.

    Base class for lookup errors.

    ## Signature

    ```python
    LookupError
    ```

    ## When to use

    Built-ins are the first tool to reach for: `LookupError` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = LookupError(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class LookupError in module builtins

class LookupError(Exception)
 |  Base class for lookup errors.
 |
 |  Method resolution order:
 |      LookupError
 |      Exception
 |      BaseException
 |      object
 |
 |  Built-in subclasses:
 |      IndexError
 |      KeyError
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
