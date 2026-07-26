---
name: builtin-environmenterror
description: "Program with Python's built-in EnvironmentError: Base class for I/O related errors."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `EnvironmentError`

    ## Overview

    `EnvironmentError` is a Python built-in class — always available, no import required.

    Base class for I/O related errors.

    ## Signature

    ```python
    EnvironmentError
    ```

    ## When to use

    Built-ins are the first tool to reach for: `EnvironmentError` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = EnvironmentError(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class OSError in module builtins

class OSError(Exception)
 |  Base class for I/O related errors.
 |
 |  Method resolution order:
 |      OSError
 |      Exception
 |      BaseException
 |      object
 |
 |  Built-in subclasses:
 |      BlockingIOError
 |      ChildProcessError
 |      ConnectionError
 |      FileExistsError
 |      ... and 7 other subclasses
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
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
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
