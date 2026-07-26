---
name: python-dataclasses
description: "Program with Python's dataclasses module: The Python standard-library module `dataclasses`."
version: 1.0.0
tags: [dataclasses, programming, python, stdlib]
---

# Python: `dataclasses`

## Overview

`dataclasses` is part of the Python standard library.

## When to use

Reach for `dataclasses` when your task calls for The Python standard-library module `dataclasses`. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import dataclasses
```

## Key functions

- `dataclasses.asdict(obj, *, dict_factory=<class 'dict'>)`
- `dataclasses.astuple(obj, *, tuple_factory=<class 'tuple'>)`
- `dataclasses.dataclass(cls=None, /, *, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=False, weakref_slot=False)`
- `dataclasses.field(*, default=<dataclasses._MISSING_TYPE object at 0x000001FE37A18AD0>, default_factory=<dataclasses._MISSING_TYPE object at 0x000001FE37A18AD0>, init=True, repr=True, hash=None, compare=True, metadata=None, kw_only=<dataclasses._MISSING_TYPE object at 0x000001FE37A18AD0>, doc=None)`
- `dataclasses.fields(class_or_instance)`
- `dataclasses.is_dataclass(obj)`
- `dataclasses.make_dataclass(cls_name, fields, *, bases=(), namespace=None, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=False, weakref_slot=False, module=None, decorator=<function dataclass at 0x000001FE37A0E1F0>)`
- `dataclasses.recursive_repr(fillvalue='...')`
- `dataclasses.replace(obj, /, **changes)`

## Key classes

`Field`, `FrozenInstanceError`, `InitVar`

## Constants / attributes

`KW_ONLY`, `MISSING`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import dataclasses

def do_work(...):
    """Use dataclasses to accomplish one well-defined task."""
    result = dataclasses.asdict(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `dataclasses` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module dataclasses

NAME
    dataclasses

MODULE REFERENCE
    https://docs.python.org/3.14/library/dataclasses.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.AttributeError(builtins.Exception)
        FrozenInstanceError
    builtins.object
        Field
        InitVar

    class Field(builtins.object)
     |  Field(
     |      default,
     |      default_factory,
     |      init,
     |      repr,
     |      hash,
     |      compare,
     |      metadata,
     |      kw_only,
     |      doc
     |  )
     |
     |  # Instances of Field are only ever created from within this module,
     |  # and only from the field() function, although Field instances are
     |  # exposed externally as (conceptually) read-only objects.
     |  #
     |  # name and type are filled in after the fact, not in __init__.
     |  # They're not known at the time this class is instantiated, but it's
     |  # convenient if they're available later.
     |  #
     |  # When cls._FIELDS is filled in with a list of Field objects, the name
     |  # and type fields will have been populated.
     |
     |  Methods defined here:
     |
     |  __init__(
     |      self,
     |      default,
     |      default_factory,
     |      init,
     |      repr,
     |      hash,
     |      compare,
     |      metadata,
     |      kw_only,
     |      doc
     |  )
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __set_name__(self, owner, name)
     |      # This is used to support the PEP 487 __set_name__ protocol in the
     |      # case where we're using a field that contains a descriptor as a
     |      # default value.  For details on __set_name__, see
     |      # https://peps.python.org/pep-0487/#implementation-details.
     |      #
     |      # Note that in _process_class, this Field object is overwritten
     |      # with the default value, so the end result is a descriptor that
     |      # had __set_name__ called on it at the right time.
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
     |  compare
     |
     |  default
     |
     |  default_factory
     |
     |  doc
     |
     |  hash
     |
     |  init
     |
     |  kw_only
     |
     |  metadata
     |
     |  name
     |
     |  repr
     |
     |  type

    class FrozenInstanceError(builtins.AttributeError)
     |  # Raised when an attempt is made to modify a frozen class.
     |
     |  Method resolution order:
     |      FrozenInstanceError
     |      builtins.AttributeError
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
     |  Methods inherited from builtins.AttributeError:
     |
     |  __getstate__(self, /)
     |      Helper for pickle.
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__(self, /)
     |      Helper for pickle.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.AttributeError:
     |
     |  name
     |      attribute name
     |
     |  obj
     |      object
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

    class InitVar(builtins.object)
     |  InitVar(type)
     |
     |  Methods defined here:
     |
     |  __init__(self, type)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  __class_getitem__(type)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  type

FUNCTIONS
    asdict(obj, *, dict_factory=<class 'dict'>)
        Return the fields of a dataclass instance as a new dictionary mapping
        field names to
```

## Related

Other standard-library modules pair well with `dataclasses`; explore the `python` domain of this catalog.
