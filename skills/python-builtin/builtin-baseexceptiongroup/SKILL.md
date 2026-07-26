---
name: builtin-baseexceptiongroup
description: "Program with Python's built-in BaseExceptionGroup: A combination of multiple unrelated exceptions."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `BaseExceptionGroup`

    ## Overview

    `BaseExceptionGroup` is a Python built-in class — always available, no import required.

    A combination of multiple unrelated exceptions.

    ## Signature

    ```python
    BaseExceptionGroup
    ```

    ## When to use

    Built-ins are the first tool to reach for: `BaseExceptionGroup` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = BaseExceptionGroup(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class BaseExceptionGroup in module builtins

class BaseExceptionGroup(BaseException)
 |  A combination of multiple unrelated exceptions.
 |
 |  Method resolution order:
 |      BaseExceptionGroup
 |      BaseException
 |      object
 |
 |  Built-in subclasses:
 |      ExceptionGroup
 |
 |  Methods defined here:
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __str__(self, /)
 |      Return str(self).
 |
 |  derive(self, excs, /)
 |
 |  split(self, matcher_value, /)
 |
 |  subgroup(self, matcher_value, /)
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __class_getitem__(object, /)
 |      See PEP 585
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
 |  exceptions
 |      nested exceptions
 |
 |  message
 |      exception message
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
