---
name: python-tomllib
description: "Program with Python's tomllib module: The Python standard-library module `tomllib`."
version: 1.0.0
tags: [programming, python, stdlib, tomllib]
---

# Python: `tomllib`

## Overview

`tomllib` is part of the Python standard library.

## When to use

Reach for `tomllib` when your task calls for The Python standard-library module `tomllib`. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import tomllib
```

## Key functions

- `tomllib.load(fp: 'IO[bytes]', /, *, parse_float: 'ParseFloat' = <class 'float'>) -> 'dict[str, Any]'`
- `tomllib.loads(s: 'str', /, *, parse_float: 'ParseFloat' = <class 'float'>) -> 'dict[str, Any]'`

## Key classes

`TOMLDecodeError`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import tomllib

def do_work(...):
    """Use tomllib to accomplish one well-defined task."""
    result = tomllib.load(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `tomllib` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: package tomllib

NAME
    tomllib

MODULE REFERENCE
    https://docs.python.org/3.14/library/tomllib.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    # SPDX-License-Identifier: MIT
    # SPDX-FileCopyrightText: 2021 Taneli Hukkinen
    # Licensed to PSF under a Contributor Agreement.

PACKAGE CONTENTS
    _parser
    _re
    _types

CLASSES
    builtins.ValueError(builtins.Exception)
        TOMLDecodeError

    class TOMLDecodeError(builtins.ValueError)
     |  TOMLDecodeError(
     |      msg: str = <class 'tomllib._parser.DEPRECATED_DEFAULT'>,
     |      doc: str = <class 'tomllib._parser.DEPRECATED_DEFAULT'>,
     |      pos: Pos = <class 'tomllib._parser.DEPRECATED_DEFAULT'>,
     |      *args: Any
     |  )
     |
     |  An error raised if a document is not valid TOML.
     |
     |  Adds the following attributes to ValueError:
     |  msg: The unformatted error message
     |  doc: The TOML document being parsed
     |  pos: The index of doc where parsing failed
     |  lineno: The line corresponding to pos
     |  colno: The column corresponding to pos
     |
     |  Method resolution order:
     |      TOMLDecodeError
     |      builtins.ValueError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(
     |      self,
     |      msg: str = <class 'tomllib._parser.DEPRECATED_DEFAULT'>,
     |      doc: str = <class 'tomllib._parser.DEPRECATED_DEFAULT'>,
     |      pos: Pos = <class 'tomllib._parser.DEPRECATED_DEFAULT'>,
     |      *args: Any
     |  ) from tomllib._parser.TOMLDecodeError
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
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
    load(fp: IO[bytes], /, *, parse_float: ParseFloat = <class 'float'>) -> dict[str, Any]
        Parse TOML from a binary file object.

    loads(s: str, /, *, parse_float: ParseFloat = <class 'float'>) -> dict[str, Any]
        Parse TOML from a string.

DATA
    __all__ = ('loads', 'load', 'TOMLDecodeError')

FILE
    c:\python314\lib\tomllib\__init__.py


```

## Related

Other standard-library modules pair well with `tomllib`; explore the `python` domain of this catalog.
