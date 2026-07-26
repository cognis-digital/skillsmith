---
name: builtin-importerror
description: "Program with Python's built-in ImportError: Import can't find module, or can't find name in module."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `ImportError`

    ## Overview

    `ImportError` is a Python built-in class — always available, no import required.

    Import can't find module, or can't find name in module.

    ## Signature

    ```python
    ImportError
    ```

    ## When to use

    Built-ins are the first tool to reach for: `ImportError` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = ImportError(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class ImportError in module builtins

class ImportError(Exception)
 |  Import can't find module, or can't find name in module.
 |
 |  Method resolution order:
 |      ImportError
 |      Exception
 |      BaseException
 |      object
 |
 |  Built-in subclasses:
 |      ModuleNotFoundError
 |
 |  Methods defined here:
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __reduce__(self, /)
 |      Helper for pickle.
 |
 |  __str__(self, /)
 |      Return str(self).
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  msg
 |      exception message
 |
 |  name
 |      module name
 |
 |  name_from
 |      name imported from module
 |
 |  path
 |      module path
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
