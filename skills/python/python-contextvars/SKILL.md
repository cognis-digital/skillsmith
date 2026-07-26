---
name: python-contextvars
description: "Program with Python's contextvars module: The Python standard-library module `contextvars`."
version: 1.0.0
tags: [contextvars, programming, python, stdlib]
---

# Python: `contextvars`

## Overview

`contextvars` is part of the Python standard library.

## When to use

Reach for `contextvars` when your task calls for The Python standard-library module `contextvars`. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import contextvars
```

## Key functions

- `contextvars.copy_context()`

## Key classes

`Context`, `ContextVar`, `Token`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import contextvars

def do_work(...):
    """Use contextvars to accomplish one well-defined task."""
    result = contextvars.copy_context(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `contextvars` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module contextvars

NAME
    contextvars

MODULE REFERENCE
    https://docs.python.org/3.14/library/contextvars.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.object
        _contextvars.Context
        _contextvars.ContextVar
        _contextvars.Token

    class Context(builtins.object)
     |  Methods defined here:
     |
     |  __contains__(self, key, /)
     |      Return bool(key in self).
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getitem__(self, key, /)
     |      Return self[key].
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __len__(self, /)
     |      Return len(self).
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  copy(self, /)
     |      Return a shallow copy of the context object.
     |
     |  get(self, key, default=None, /)
     |      Return the value for `key` if `key` has the value in the context object.
     |
     |      If `key` does not exist, return `default`. If `default` is not given,
     |      return None.
     |
     |  items(self, /)
     |      Return all variables and their values in the context object.
     |
     |      The result is returned as a list of 2-tuples (variable, value).
     |
     |  keys(self, /)
     |      Return a list of all variables in the context object.
     |
     |  run(...)
     |
     |  values(self, /)
     |      Return a list of all variables' values in the context object.
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs)
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __hash__ = None

    class ContextVar(builtins.object)
     |  Methods defined here:
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  get(self, default=<unrepresentable>, /)
     |      Return a value for the context variable for the current context.
     |
     |      If there is no value for the variable in the current context, the method will:
     |       * return the value of the default argument of the method, if provided; or
     |       * return the default value for the context variable, if it was created
     |         with one; or
     |       * raise a LookupError.
     |
     |  reset(self, token, /)
     |      Reset the context variable.
     |
     |      The variable is reset to the value it had before the `ContextVar.set()` that
     |      created the token was used.
     |
     |  set(self, value, /)
     |      Call to set a new value for the context variable in the current context.
     |
     |      The required value argument is the new value for the context variable.
     |
     |      Returns a Token object that can be used to restore the variable to its previous
     |      value via the `ContextVar.reset()` method.
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  __class_getitem__(object, /)
     |      See PEP 585
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
     |  name

    class Token(builtins.object)
     |  Methods defined here:
     |
     |  __enter__(self, /)
     |      Enter into Token context manager.
     |
     |  __exit__(self, type, val, tb, /)
     |      Exit from Token context manager, restore the linked ContextVar.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  __class_getitem__(object, /)
     |      See PEP 585
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
     |  old_value
     |
     |  var
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  MISSING = <Token.MISSING>
     |
     |  __hash__ = None

FUNCTIONS
    copy_context()

DATA
    __all__ = ('Context', 'ContextVar', 'Token', 'copy_context')

FILE
    c:\python314\lib\contextvars.py


```

## Related

Other standard-library modules pair well with `contextvars`; explore the `python` domain of this catalog.
