---
name: python-zipapp
description: "Program with Python's zipapp module: The Python standard-library module `zipapp`."
version: 1.0.0
tags: [programming, python, stdlib, zipapp]
---

# Python: `zipapp`

## Overview

`zipapp` is part of the Python standard library.

## When to use

Reach for `zipapp` when your task calls for The Python standard-library module `zipapp`. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import zipapp
```

## Key functions

- `zipapp.create_archive(source, target=None, interpreter=None, main=None, filter=None, compressed=False)`
- `zipapp.get_interpreter(archive)`
- `zipapp.main(args=None)`

## Key classes

`ZipAppError`

## Constants / attributes

`MAIN_TEMPLATE`, `shebang_encoding`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import zipapp

def do_work(...):
    """Use zipapp to accomplish one well-defined task."""
    result = zipapp.create_archive(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `zipapp` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module zipapp

NAME
    zipapp

MODULE REFERENCE
    https://docs.python.org/3.14/library/zipapp.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.ValueError(builtins.Exception)
        ZipAppError

    class ZipAppError(builtins.ValueError)
     |  Method resolution order:
     |      ZipAppError
     |      builtins.ValueError
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
     |  Static methods inherited from builtins.ValueError:
     |
     |  __new__(*args, **kwargs) class method of builtins.ValueError
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
    create_archive(
        source,
        target=None,
        interpreter=None,
        main=None,
        filter=None,
        compressed=False
    )
        Create an application archive from SOURCE.

        The SOURCE can be the name of a directory, or a filename or a file-like
        object referring to an existing archive.

        The content of SOURCE is packed into an application archive in TARGET,
        which can be a filename or a file-like object.  If SOURCE is a directory,
        TARGET can be omitted and will default to the name of SOURCE with .pyz
        appended.

        The created application archive will have a shebang line specifying
        that it should run with INTERPRETER (there will be no shebang line if
        INTERPRETER is None), and a __main__.py which runs MAIN (if MAIN is
        not specified, an existing __main__.py will be used).  It is an error
        to specify MAIN for anything other than a directory source with no
        __main__.py, and it is an error to omit MAIN if the directory has no
        __main__.py.

    get_interpreter(archive)

DATA
    __all__ = ['ZipAppError', 'create_archive', 'get_interpreter']

FILE
    c:\python314\lib\zipapp.py


```

## Related

Other standard-library modules pair well with `zipapp`; explore the `python` domain of this catalog.
