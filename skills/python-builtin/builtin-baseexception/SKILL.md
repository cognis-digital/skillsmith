---
name: builtin-baseexception
description: "Program with Python's built-in BaseException: Common base class for all exceptions"
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `BaseException`

    ## Overview

    `BaseException` is a Python built-in class — always available, no import required.

    Common base class for all exceptions

    ## Signature

    ```python
    BaseException
    ```

    ## When to use

    Built-ins are the first tool to reach for: `BaseException` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = BaseException(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class BaseException in module builtins

class BaseException(object)
 |  Common base class for all exceptions
 |
 |  Built-in subclasses:
 |      BaseExceptionGroup
 |      Exception
 |      GeneratorExit
 |      KeyboardInterrupt
 |      ... and 1 other subclasses
 |
 |  Methods defined here:
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
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
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
