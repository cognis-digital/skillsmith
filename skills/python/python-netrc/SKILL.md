---
name: python-netrc
description: "Program with Python's netrc module: An object-oriented interface to .netrc files."
version: 1.0.0
tags: [netrc, programming, python, stdlib]
---

# Python: `netrc`

## Overview

An object-oriented interface to .netrc files.

## When to use

Reach for `netrc` when your task calls for An object-oriented interface to .netrc files. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import netrc
```

## Key classes

`NetrcParseError`, `netrc`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import netrc

def do_work(...):
    """Use netrc to accomplish one well-defined task."""
    result = netrc.NetrcParseError(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `netrc` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module netrc

NAME
    netrc - An object-oriented interface to .netrc files.

MODULE REFERENCE
    https://docs.python.org/3.14/library/netrc.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.Exception(builtins.BaseException)
        NetrcParseError
    builtins.object
        netrc

    class NetrcParseError(builtins.Exception)
     |  NetrcParseError(msg, filename=None, lineno=None)
     |
     |  Exception raised on syntax errors in the .netrc file.
     |
     |  Method resolution order:
     |      NetrcParseError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, msg, filename=None, lineno=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __str__(self)
     |      Return str(self).
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

    class netrc(builtins.object)
     |  netrc(file=None)
     |
     |  Methods defined here:
     |
     |  __init__(self, file=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __repr__(self)
     |      Dump the class data in the format of a .netrc file.
     |
     |  authenticators(self, host)
     |      Return a (user, account, password) tuple for given host.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

DATA
    __all__ = ['netrc', 'NetrcParseError']

FILE
    c:\python314\lib\netrc.py


```

## Related

Other standard-library modules pair well with `netrc`; explore the `python` domain of this catalog.
