---
name: builtin-syntaxerror
description: "Program with Python's built-in SyntaxError: Invalid syntax."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `SyntaxError`

    ## Overview

    `SyntaxError` is a Python built-in class — always available, no import required.

    Invalid syntax.

    ## Signature

    ```python
    SyntaxError
    ```

    ## When to use

    Built-ins are the first tool to reach for: `SyntaxError` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = SyntaxError(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class SyntaxError in module builtins

class SyntaxError(Exception)
 |  Invalid syntax.
 |
 |  Method resolution order:
 |      SyntaxError
 |      Exception
 |      BaseException
 |      object
 |
 |  Built-in subclasses:
 |      IndentationError
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
 |  Data descriptors defined here:
 |
 |  end_lineno
 |      exception end lineno
 |
 |  end_offset
 |      exception end offset
 |
 |  filename
 |      exception filename
 |
 |  lineno
 |      exception lineno
 |
 |  msg
 |      exception msg
 |
 |  offset
 |      exception offset
 |
 |  print_file_and_line
 |      exception print_file_and_line
 |
 |  text
 |      exception text
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
