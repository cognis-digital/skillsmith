---
name: python-copy
description: "Program with Python's copy module: Generic (shallow and deep) copying operations."
version: 1.0.0
tags: [copy, programming, python, stdlib]
---

# Python: `copy`

## Overview

Generic (shallow and deep) copying operations.

Interface summary:

        import copy

        x = copy.copy(y)                # make a shallow copy of y
        x = copy.deepcopy(y)            # make a deep copy of y
        x = copy.replace(y, a=1, b=2)   # new object with fields replaced, as defined by `__replace__`

For module specific errors, copy.Error is raised.

The difference between shallow and deep copying is only relevant for
compound objects (objects that contain other objects, like lists or
class instances).

- A shallow copy constructs a new compound object and then (to the
  extent possible) inserts *the same objects* into it that the
  original contains.

- A deep copy constructs a new compound object and then, recursively,
  inserts *copies* into it of the objects found in the original.

Two problems often exist with deep copy operations that don't exist
with shallow copy operations:

 a) recursive objects (compound objects that, directly or indirectly,
    contain a reference to themselves) may cause a recursive loop

 b) because deep copy copies *everything* it may copy too much, e.g.
    administrative data structures that should be shared even between
    copies

Python's deep copy operation avoids these problems by:

 a) keeping a table of objects already copied during the current
    copying pass

 b) letting user-defined classes override the copying operation or the
    set of components copied

This version does not copy types like module, class, function, method,
nor stack trace, stack frame, nor file, socket, window, nor any
similar types.

Classes can use the same interfaces to control copying that they use
to control pickling: they can define methods called __getinitargs__(),
__getstate__() and __setstate__().  See the documentation for module
"pickle" for information on these methods.

## When to use

Reach for `copy` when your task calls for Generic (shallow and deep) copying operations. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import copy
```

## Key functions

- `copy.copy(x)`
- `copy.deepcopy(x, memo=None, _nil=[])`
- `copy.replace(obj, /, **changes)`

## Key classes

`Error`, `error`

## Constants / attributes

`dispatch_table`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import copy

def do_work(...):
    """Use copy to accomplish one well-defined task."""
    result = copy.copy(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `copy` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module copy

NAME
    copy - Generic (shallow and deep) copying operations.

MODULE REFERENCE
    https://docs.python.org/3.14/library/copy.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Interface summary:

            import copy

            x = copy.copy(y)                # make a shallow copy of y
            x = copy.deepcopy(y)            # make a deep copy of y
            x = copy.replace(y, a=1, b=2)   # new object with fields replaced, as defined by `__replace__`

    For module specific errors, copy.Error is raised.

    The difference between shallow and deep copying is only relevant for
    compound objects (objects that contain other objects, like lists or
    class instances).

    - A shallow copy constructs a new compound object and then (to the
      extent possible) inserts *the same objects* into it that the
      original contains.

    - A deep copy constructs a new compound object and then, recursively,
      inserts *copies* into it of the objects found in the original.

    Two problems often exist with deep copy operations that don't exist
    with shallow copy operations:

     a) recursive objects (compound objects that, directly or indirectly,
        contain a reference to themselves) may cause a recursive loop

     b) because deep copy copies *everything* it may copy too much, e.g.
        administrative data structures that should be shared even between
        copies

    Python's deep copy operation avoids these problems by:

     a) keeping a table of objects already copied during the current
        copying pass

     b) letting user-defined classes override the copying operation or the
        set of components copied

    This version does not copy types like module, class, function, method,
    nor stack trace, stack frame, nor file, socket, window, nor any
    similar types.

    Classes can use the same interfaces to control copying that they use
    to control pickling: they can define methods called __getinitargs__(),
    __getstate__() and __setstate__().  See the documentation for module
    "pickle" for information on these methods.

CLASSES
    builtins.Exception(builtins.BaseException)
        Error

    class Error(builtins.Exception)
     |  Method resolution order:
     |      Error
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
     |  Static methods inherited from builtins.Exception:
     |
     |  __new__(*args, **kwargs) class method of builtins.Exception
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
    copy(x)
        Shallow copy operation on arbitrary Python objects.

        See the module's __doc__ string for more info.

    deepcopy(x, memo=None, _nil=[])
        Deep copy operation on arbitrary Python objects.

        See the module's __doc__ string for more info.

    replace(obj, /, **changes)
        Return a new object replacing specified fields with new values.

        This is especially useful for immutable objects, like named tuples or
        frozen dataclasses.

DATA
    __all__ = ['Error', 'copy', 'deepcopy', 'replace']

FILE
    c:\python314\lib\copy.py


```

## Related

Other standard-library modules pair well with `copy`; explore the `python` domain of this catalog.
