---
name: python-getpass
description: "Program with Python's getpass module: Utilities to get a password and/or the current user name."
version: 1.0.0
tags: [getpass, programming, python, stdlib]
---

# Python: `getpass`

## Overview

Utilities to get a password and/or the current user name.

getpass(prompt[, stream[, echo_char]]) - Prompt for a password, with echo
turned off and optional keyboard feedback.
getuser() - Get the user name from the environment or password database.

GetPassWarning - This UserWarning is issued when getpass() cannot prevent
                 echoing of the password contents while reading.

On Windows, the msvcrt module will be used.

## When to use

Reach for `getpass` when your task calls for Utilities to get a password and/or the current user name. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import getpass
```

## Key functions

- `getpass.fallback_getpass(prompt='Password: ', stream=None, *, echo_char=None)`
- `getpass.getpass(prompt='Password: ', stream=None, *, echo_char=None)`
- `getpass.getuser()`
- `getpass.unix_getpass(prompt='Password: ', stream=None, *, echo_char=None)`
- `getpass.win_getpass(prompt='Password: ', stream=None, *, echo_char=None)`

## Key classes

`GetPassWarning`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import getpass

def do_work(...):
    """Use getpass to accomplish one well-defined task."""
    result = getpass.fallback_getpass(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `getpass` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module getpass

NAME
    getpass - Utilities to get a password and/or the current user name.

MODULE REFERENCE
    https://docs.python.org/3.14/library/getpass.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    getpass(prompt[, stream[, echo_char]]) - Prompt for a password, with echo
    turned off and optional keyboard feedback.
    getuser() - Get the user name from the environment or password database.

    GetPassWarning - This UserWarning is issued when getpass() cannot prevent
                     echoing of the password contents while reading.

    On Windows, the msvcrt module will be used.

CLASSES
    builtins.UserWarning(builtins.Warning)
        GetPassWarning

    class GetPassWarning(builtins.UserWarning)
     |  Method resolution order:
     |      GetPassWarning
     |      builtins.UserWarning
     |      builtins.Warning
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors defined here:
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.UserWarning:
     |
     |  __new__(*args, **kwargs) class method of builtins.UserWarning
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
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
    getpass = win_getpass(prompt='Password: ', stream=None, *, echo_char=None)
        Prompt for password with echo off, using Windows getwch().

    getuser()
        Get the username from the environment or password database.

        First try various environment variables, then the password
        database.  This works on Windows as long as USERNAME is set.
        Any failure to find a username raises OSError.

        .. versionchanged:: 3.13
            Previously, various exceptions beyond just :exc:`OSError`
            were raised.

DATA
    __all__ = ['getpass', 'getuser', 'GetPassWarning']

FILE
    c:\python314\lib\getpass.py


```

## Related

Other standard-library modules pair well with `getpass`; explore the `python` domain of this catalog.
