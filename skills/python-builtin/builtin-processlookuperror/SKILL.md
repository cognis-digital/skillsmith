---
name: builtin-processlookuperror
description: "Program with Python's built-in ProcessLookupError: Process not found."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `ProcessLookupError`

    ## Overview

    `ProcessLookupError` is a Python built-in class — always available, no import required.

    Process not found.

    ## Signature

    ```python
    ProcessLookupError
    ```

    ## When to use

    Built-ins are the first tool to reach for: `ProcessLookupError` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = ProcessLookupError(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class ProcessLookupError in module builtins

class ProcessLookupError(OSError)
 |  Process not found.
 |
 |  Method resolution order:
 |      ProcessLookupError
 |      OSError
 |      Exception
 |      BaseException
 |      object
 |
 |  Methods inherited from OSError:
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
 |  Static methods inherited from OSError:
 |
 |  __new__(*args, **kwargs) class method of builtins.OSError
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from OSError:
 |
 |  characters_written
 |
 |  errno
 |      POSIX exception code
 |
 |  filename
 |      exception filename
 |
 |  filename2
 |      second exception filename
 |
 |  strerror
 |      exception strerror
 |
 |  winerror
 |      Win32 exception code
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
