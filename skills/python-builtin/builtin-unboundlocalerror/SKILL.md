---
name: builtin-unboundlocalerror
description: "Program with Python's built-in UnboundLocalError: Local name referenced but not bound to a value."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `UnboundLocalError`

    ## Overview

    `UnboundLocalError` is a Python built-in class — always available, no import required.

    Local name referenced but not bound to a value.

    ## Signature

    ```python
    UnboundLocalError
    ```

    ## When to use

    Built-ins are the first tool to reach for: `UnboundLocalError` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = UnboundLocalError(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class UnboundLocalError in module builtins

class UnboundLocalError(NameError)
 |  Local name referenced but not bound to a value.
 |
 |  Method resolution order:
 |      UnboundLocalError
 |      NameError
 |      Exception
 |      BaseException
 |      object
 |
 |  Methods inherited from NameError:
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from NameError:
 |
 |  name
 |      name
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
