---
name: python-reprlib
description: "Program with Python's reprlib module: Redo the builtin repr() (representation) but with limits on most sizes."
version: 1.0.0
tags: [programming, python, reprlib, stdlib]
---

# Python: `reprlib`

## Overview

Redo the builtin repr() (representation) but with limits on most sizes.

## When to use

Reach for `reprlib` when your task calls for Redo the builtin repr() (representation) but with limits on most sizes. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import reprlib
```

## Key functions

- `reprlib.get_ident()`
- `reprlib.recursive_repr(fillvalue='...')`
- `reprlib.repr(x)`

## Key classes

`Repr`, `islice`

## Constants / attributes

`aRepr`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import reprlib

def do_work(...):
    """Use reprlib to accomplish one well-defined task."""
    result = reprlib.get_ident(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `reprlib` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module reprlib

NAME
    reprlib - Redo the builtin repr() (representation) but with limits on most sizes.

MODULE REFERENCE
    https://docs.python.org/3.14/library/reprlib.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.object
        Repr

    class Repr(builtins.object)
     |  Repr(
     |      *,
     |      maxlevel=6,
     |      maxtuple=6,
     |      maxlist=6,
     |      maxarray=5,
     |      maxdict=4,
     |      maxset=6,
     |      maxfrozenset=6,
     |      maxdeque=6,
     |      maxstring=30,
     |      maxlong=40,
     |      maxother=30,
     |      fillvalue='...',
     |      indent=None
     |  )
     |
     |  Methods defined here:
     |
     |  __init__(
     |      self,
     |      *,
     |      maxlevel=6,
     |      maxtuple=6,
     |      maxlist=6,
     |      maxarray=5,
     |      maxdict=4,
     |      maxset=6,
     |      maxfrozenset=6,
     |      maxdeque=6,
     |      maxstring=30,
     |      maxlong=40,
     |      maxother=30,
     |      fillvalue='...',
     |      indent=None
     |  )
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  repr(self, x)
     |
     |  repr1(self, x, level)
     |
     |  repr_array(self, x, level)
     |
     |  repr_deque(self, x, level)
     |
     |  repr_dict(self, x, level)
     |
     |  repr_frozenset(self, x, level)
     |
     |  repr_instance(self, x, level)
     |
     |  repr_int(self, x, level)
     |
     |  repr_list(self, x, level)
     |
     |  repr_set(self, x, level)
     |
     |  repr_str(self, x, level)
     |
     |  repr_tuple(self, x, level)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

FUNCTIONS
    recursive_repr(fillvalue='...')
        Decorator to make a repr function return fillvalue for a recursive call

    repr(x) method of Repr instance

DATA
    __all__ = ['Repr', 'repr', 'recursive_repr']

FILE
    c:\python314\lib\reprlib.py


```

## Related

Other standard-library modules pair well with `reprlib`; explore the `python` domain of this catalog.
