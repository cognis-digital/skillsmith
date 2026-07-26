---
name: python-weakref
description: "Program with Python's weakref module: Weak reference support for Python."
version: 1.0.0
tags: [programming, python, stdlib, weakref]
---

# Python: `weakref`

## Overview

Weak reference support for Python.

This module is an implementation of PEP 205:

https://peps.python.org/pep-0205/

## When to use

Reach for `weakref` when your task calls for Weak reference support for Python. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import weakref
```

## Key functions

- `weakref.getweakrefcount(object, /)`
- `weakref.getweakrefs(object, /)`
- `weakref.proxy(object, callback=None, /)`

## Key classes

`CallableProxyType`, `KeyedRef`, `ProxyType`, `ReferenceType`, `WeakKeyDictionary`, `WeakMethod`, `WeakSet`, `WeakValueDictionary`, `finalize`, `ref`

## Constants / attributes

`ProxyTypes`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import weakref

def do_work(...):
    """Use weakref to accomplish one well-defined task."""
    result = weakref.getweakrefcount(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `weakref` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module weakref

NAME
    weakref - Weak reference support for Python.

MODULE REFERENCE
    https://docs.python.org/3.14/library/weakref.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module is an implementation of PEP 205:

    https://peps.python.org/pep-0205/

CLASSES
    builtins.object
        _weakrefset.WeakSet
        CallableProxyType
        ProxyType
        ReferenceType
            WeakMethod
        finalize
    collections.abc.MutableMapping(collections.abc.Mapping)
        WeakKeyDictionary
        WeakValueDictionary

    class CallableProxyType(builtins.object)
     |  Methods defined here:
     |
     |  __abs__(self, /)
     |      abs(self)
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __and__(self, value, /)
     |      Return self&value.
     |
     |  __bool__(self, /)
     |      True if self else False
     |
     |  __call__(self, /, *args, **kwargs)
     |      Call self as a function.
     |
     |  __contains__(self, key, /)
     |      Return bool(key in self).
     |
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |
     |  __delitem__(self, key, /)
     |      Delete self[key].
     |
     |  __divmod__(self, value, /)
     |      Return divmod(self, value).
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __float__(self, /)
     |      float(self)
     |
     |  __floordiv__(self, value, /)
     |      Return self//value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __getitem__(self, key, /)
     |      Return self[key].
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __iadd__(self, value, /)
     |      Return self+=value.
     |
     |  __iand__(self, value, /)
     |      Return self&=value.
     |
     |  __ifloordiv__(self, value, /)
     |      Return self//=value.
     |
     |  __ilshift__(self, value, /)
     |      Return self<<=value.
     |
     |  __imatmul__(self, value, /)
     |      Return self@=value.
     |
     |  __imod__(self, value, /)
     |      Return self%=value.
     |
     |  __imul__(self, value, /)
     |      Return self*=value.
     |
     |  __index__(self, /)
     |      Return self converted to an integer, if self is suitable for use as an index into a list.
     |
     |  __int__(self, /)
     |      int(self)
     |
     |  __invert__(self, /)
     |      ~self
     |
     |  __ior__(self, value, /)
     |      Return self|=value.
     |
     |  __ipow__(self, value, /)
     |      Return self**=value.
     |
     |  __irshift__(self, value, /)
     |      Return self>>=value.
     |
     |  __isub__(self, value, /)
     |      Return self-=value.
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __itruediv__(self, value, /)
     |      Return self/=value.
     |
     |  __ixor__(self, value, /)
     |      Return self^=value.
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __len__(self, /)
     |      Return len(self).
     |
     |  __lshift__(self, value, /)
     |      Return self<<value.
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __matmul__(self, value, /)
     |      Return self@value.
     |
     |  __mod__(self, value, /)
     |      Return self%value.
     |
     |  __mul__(self, value, /)
     |      Return self*value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __neg__(self, /)
     |      -self
     |
     |  __next__(self, /)
     |      Implement next(self).
     |
     |  __or__(self, value, /)
     |      Return self|value.
     |
     |  __pos__(self, /)
     |      +self
     |
     |  __pow__(self, value, mod=None, /)
     |      Return pow(self, value, mod).
     |
     |  __radd__(self, value, /)
     |      Return value+self.
     |
     |  __rand__(self, value, /)
     |      Return value&self.
     |
     |  __rdivmod__(self, value, /)
     |      Return divmod(value, self).
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __rfloordiv__(self, value, /)
     |      Return value//self.
     |
     |  __rlshift__(self, value, /)
     |      Return value<<self.
     |
     |  __rmatmul__(self, value, /)
     |      Return value@self.
     |
     |  __rmod__(self, value, /)
     |      Return value%self.
     |
     |  __rmul__(self, value, /)
     |      Return value*self.
     |
     |  __ror__(self, value, /)
     |      Return value|self.
     |
     |  __rpow__(self, value, mod=None, /)
     |      Return pow(value, self, mod).
     |
     |  __rrshift__(self, value, /)
     |      Return value>>self.
     |
     |  __rshift__(self, value, /)
     |      Return self>>value.
     |
     |  __rsub__(self, value, /)
     |      Return value-self.
     |
     |  __rtruediv__(self, value, /)
     |      Return value/self.
     |
     |  __rxor__(self, value, /)
     |      Return value^self.
     |
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setitem__(self, key, value, /)
     |      Set self[key] to value.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  __sub__(self, value, /)
     |      Return self-value.
     |
     |  __truediv__(self, value, /)
     |      Return self/value.
     |
     |  __xor__(self, value, /)
     |      Return self^value.
     |
     |  ----------------------------------------------------------------------
  
```

## Related

Other standard-library modules pair well with `weakref`; explore the `python` domain of this catalog.
