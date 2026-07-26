---
name: builtin-stopiteration
description: "Program with Python's built-in StopIteration: Signal the end from iterator.__next__()."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `StopIteration`

    ## Overview

    `StopIteration` is a Python built-in class — always available, no import required.

    Signal the end from iterator.__next__().

    ## Signature

    ```python
    StopIteration
    ```

    ## When to use

    Built-ins are the first tool to reach for: `StopIteration` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = StopIteration(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class StopIteration in module builtins

class StopIteration(Exception)
 |  Signal the end from iterator.__next__().
 |
 |  Method resolution order:
 |      StopIteration
 |      Exception
 |      BaseException
 |      object
 |
 |  Methods defined here:
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  value
 |      generator return value
 |
 |  ----------------------------------------------------------------------
 |  Static methods inherited from Exception:
 |
 |  __new__(*args, **kwargs) class method of builtins.Exception
 |      Create and return a new object.  See help(type) for accurate signature.
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
