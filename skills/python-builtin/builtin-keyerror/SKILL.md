---
name: builtin-keyerror
description: "Program with Python's built-in KeyError: Mapping key not found."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `KeyError`

    ## Overview

    `KeyError` is a Python built-in class — always available, no import required.

    Mapping key not found.

    ## Signature

    ```python
    KeyError
    ```

    ## When to use

    Built-ins are the first tool to reach for: `KeyError` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = KeyError(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class KeyError in module builtins

class KeyError(LookupError)
 |  Mapping key not found.
 |
 |  Method resolution order:
 |      KeyError
 |      LookupError
 |      Exception
 |      BaseException
 |      object
 |
 |  Methods defined here:
 |
 |  __str__(self, /)
 |      Return str(self).
 |
 |  ----------------------------------------------------------------------
 |  Static methods inherited from LookupError:
 |
 |  __new__(*args, **kwargs) class method of builtins.LookupError
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
