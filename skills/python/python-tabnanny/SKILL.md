---
name: python-tabnanny
description: "Program with Python's tabnanny module: The Tab Nanny despises ambiguous indentation."
version: 1.0.0
tags: [programming, python, stdlib, tabnanny]
---

# Python: `tabnanny`

## Overview

The Tab Nanny despises ambiguous indentation.  She knows no mercy.

tabnanny -- Detection of ambiguous indentation

For the time being this module is intended to be called as a script.
However it is possible to import it into an IDE and use the function
check() described below.

Warning: The API provided by this module is likely to change in future
releases; such changes may not be backward compatible.

## When to use

Reach for `tabnanny` when your task calls for The Tab Nanny despises ambiguous indentation. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import tabnanny
```

## Key functions

- `tabnanny.check(file)`
- `tabnanny.errprint(*args)`
- `tabnanny.format_witnesses(w)`
- `tabnanny.main()`
- `tabnanny.process_tokens(tokens)`

## Key classes

`NannyNag`, `Whitespace`

## Constants / attributes

`filename_only`, `verbose`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import tabnanny

def do_work(...):
    """Use tabnanny to accomplish one well-defined task."""
    result = tabnanny.check(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `tabnanny` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module tabnanny

NAME
    tabnanny - The Tab Nanny despises ambiguous indentation.  She knows no mercy.

MODULE REFERENCE
    https://docs.python.org/3.14/library/tabnanny.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    tabnanny -- Detection of ambiguous indentation

    For the time being this module is intended to be called as a script.
    However it is possible to import it into an IDE and use the function
    check() described below.

    Warning: The API provided by this module is likely to change in future
    releases; such changes may not be backward compatible.

CLASSES
    builtins.Exception(builtins.BaseException)
        NannyNag

    class NannyNag(builtins.Exception)
     |  NannyNag(lineno, msg, line)
     |
     |  Raised by process_tokens() if detecting an ambiguous indent.
     |  Captured and handled in check().
     |
     |  Method resolution order:
     |      NannyNag
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, lineno, msg, line)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  get_line(self)
     |
     |  get_lineno(self)
     |
     |  get_msg(self)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |
     |  __new__(*args, **kwargs) class method of builtins.Exception
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
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
     |  Data descriptors inherited from builtins.BaseException:
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

FUNCTIONS
    check(file)
        check(file_or_dir)

        If file_or_dir is a directory and not a symbolic link, then recursively
        descend the directory tree named by file_or_dir, checking all .py files
        along the way. If file_or_dir is an ordinary Python source file, it is
        checked for whitespace related problems. The diagnostic messages are
        written to standard output using the print statement.

    process_tokens(tokens)

DATA
    __all__ = ['check', 'NannyNag', 'process_tokens']

VERSION
    6

FILE
    c:\python314\lib\tabnanny.py


```

## Related

Other standard-library modules pair well with `tabnanny`; explore the `python` domain of this catalog.
