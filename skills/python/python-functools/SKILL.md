---
name: python-functools
description: "Program with Python's functools module: functools.py - Tools for working with functions and callable objects"
version: 1.0.0
tags: [functools, programming, python, stdlib]
---

# Python: `functools`

## Overview

functools.py - Tools for working with functions and callable objects

## When to use

Reach for `functools` when your task calls for functools.py - Tools for working with functions and callable objects. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import functools
```

## Key functions

- `functools.cache(user_function, /)`
- `functools.cmp_to_key(mycmp)`
- `functools.get_cache_token()`
- `functools.lru_cache(maxsize=128, typed=False)`
- `functools.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)`
- `functools.recursive_repr(fillvalue='...')`
- `functools.reduce(...)`
- `functools.singledispatch(func)`
- `functools.total_ordering(cls)`
- `functools.update_wrapper(wrapper, wrapped, assigned=('__module__', '__name__', '__qualname__', '__doc__', '__annotate__', '__type_params__'), updated=('__dict__',))`
- `functools.wraps(wrapped, assigned=('__module__', '__name__', '__qualname__', '__doc__', '__annotate__', '__type_params__'), updated=('__dict__',))`

## Key classes

`GenericAlias`, `MappingProxyType`, `MethodType`, `RLock`, `UnionType`, `cached_property`, `itemgetter`, `partial`, `partialmethod`, `singledispatchmethod`

## Constants / attributes

`Placeholder`, `WRAPPER_ASSIGNMENTS`, `WRAPPER_UPDATES`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import functools

def do_work(...):
    """Use functools to accomplish one well-defined task."""
    result = functools.cache(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `functools` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module functools

NAME
    functools - functools.py - Tools for working with functions and callable objects

MODULE REFERENCE
    https://docs.python.org/3.14/library/functools.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.object
        cached_property
        partial
        partialmethod
        singledispatchmethod

    class cached_property(builtins.object)
     |  cached_property(func)
     |
     |  Methods defined here:
     |
     |  __get__(self, instance, owner=None)
     |
     |  __init__(self, func)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __set_name__(self, owner, name)
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  __class_getitem__ = GenericAlias(args, /)
     |      Represent a PEP 585 generic type
     |
     |      E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class partial(builtins.object)
     |  partial(func, /, *args, **keywords)
     |
     |  Create a new function with partial application of the given arguments
     |  and keywords.
     |
     |  Methods defined here:
     |
     |  __call__(self, /, *args, **kwargs)
     |      Call self as a function.
     |
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |
     |  __get__(self, instance, owner=None, /)
     |      Return an attribute of instance, which is of type owner.
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __reduce__(self, /)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(self, object, /)
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
     |  __dict__
     |
     |  __vectorcalloffset__
     |
     |  args
     |      tuple of arguments to future partial calls
     |
     |  func
     |      function object to use in future partial calls
     |
     |  keywords
     |      dictionary of keyword arguments to future partial calls

    class partialmethod(builtins.object)
     |  partialmethod(func, /, *args, **keywords)
     |
     |  Method descriptor with partial application of the given arguments
     |  and keywords.
     |
     |  Supports wrapping existing descriptors and handles non-descriptor
     |  callables as instance methods.
     |
     |  Methods defined here:
     |
     |  __get__(self, obj, cls=None)
     |
     |  __repr__ = _partial_repr(self)
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  __class_getitem__ = GenericAlias(args, /)
     |      Represent a PEP 585 generic type
     |
     |      E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__ = _partial_new(cls, func, /, *args, **keywords)
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  __isabstractmethod__
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class singledispatchmethod(builtins.object)
     |  singledispatchmethod(func)
     |
     |  Single-dispatch generic method descriptor.
     |
     |  Supports wrapping existing descriptors and handles non-descriptor
     |  callables as instance methods.
     |
     |  Methods defined here:
     |
     |  __get__(self, obj, cls=None)
     |
     |  __init__(self, func)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  register(self, cls, method=None)
     |      generic_method.register(cls, func) -> func
     |
     |      Registers a new implementation for the given *cls* on a *generic_method*.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  __isabstractmethod__
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
    cache(user_function, /)
        Simple lightweight unbounded cache.  Sometimes called "memoize".

    cmp_to_key(mycmp)
        Convert a cmp= fu
```

## Related

Other standard-library modules pair well with `functools`; explore the `python` domain of this catalog.
