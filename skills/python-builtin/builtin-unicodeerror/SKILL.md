---
name: builtin-unicodeerror
description: "Program with Python's built-in UnicodeError: Unicode related error."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `UnicodeError`

    ## Overview

    `UnicodeError` is a Python built-in class — always available, no import required.

    Unicode related error.

    ## Signature

    ```python
    UnicodeError
    ```

    ## When to use

    Built-ins are the first tool to reach for: `UnicodeError` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = UnicodeError(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class UnicodeError in module builtins

class UnicodeError(ValueError)
 |  Unicode related error.
 |
 |  Method resolution order:
 |      UnicodeError
 |      ValueError
 |      Exception
 |      BaseException
 |      object
 |
 |  Built-in subclasses:
 |      UnicodeDecodeError
 |      UnicodeEncodeError
 |      UnicodeTranslateError
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
