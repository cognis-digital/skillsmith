---
name: builtin-unicodeencodeerror
description: "Program with Python's built-in UnicodeEncodeError: Unicode encoding error."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `UnicodeEncodeError`

    ## Overview

    `UnicodeEncodeError` is a Python built-in class — always available, no import required.

    Unicode encoding error.

    ## Signature

    ```python
    UnicodeEncodeError
    ```

    ## When to use

    Built-ins are the first tool to reach for: `UnicodeEncodeError` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = UnicodeEncodeError(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class UnicodeEncodeError in module builtins

class UnicodeEncodeError(UnicodeError)
 |  Unicode encoding error.
 |
 |  Method resolution order:
 |      UnicodeEncodeError
 |      UnicodeError
 |      ValueError
 |      Exception
 |      BaseException
 |      object
 |
 |  Methods defined here:
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __str__(self, /)
 |      Return str(self).
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  encoding
 |      exception encoding
 |
 |  end
 |      exception end
 |
 |  object
 |      exception object
 |
 |  reason
 |      exception reason
 |
 |  start
 |      exception start
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from BaseException:
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
