---
name: python-operator
description: "Program with Python's operator module: Operator interface."
version: 1.0.0
tags: [operator, programming, python, stdlib]
---

# Python: `operator`

## Overview

Operator interface.

This module exports a set of functions implemented in C corresponding
to the intrinsic operators of Python.  For example, operator.add(x, y)
is equivalent to the expression x+y.  The function names are those
used for special methods; variants without leading and trailing
'__' are also provided for convenience.

## When to use

Reach for `operator` when your task calls for Operator interface. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import operator
```

## Key functions

- `operator.abs(a, /)`
- `operator.add(a, b, /)`
- `operator.and_(a, b, /)`
- `operator.call(obj, /, *args, **kwargs)`
- `operator.concat(a, b, /)`
- `operator.contains(a, b, /)`
- `operator.countOf(a, b, /)`
- `operator.delitem(a, b, /)`
- `operator.eq(a, b, /)`
- `operator.floordiv(a, b, /)`
- `operator.ge(a, b, /)`
- `operator.getitem(a, b, /)`
- `operator.gt(a, b, /)`
- `operator.iadd(a, b, /)`
- `operator.iand(a, b, /)`
- `operator.iconcat(a, b, /)`
- `operator.ifloordiv(a, b, /)`
- `operator.ilshift(a, b, /)`
- `operator.imatmul(a, b, /)`
- `operator.imod(a, b, /)`
- `operator.imul(a, b, /)`
- `operator.index(a, /)`
- `operator.indexOf(a, b, /)`
- `operator.inv(a, /)`
- `operator.invert(a, /)`
- `operator.ior(a, b, /)`
- `operator.ipow(a, b, /)`
- `operator.irshift(a, b, /)`
- `operator.is_(a, b, /)`
- `operator.is_none(a, /)`

## Key classes

`attrgetter`, `itemgetter`, `methodcaller`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import operator

def do_work(...):
    """Use operator to accomplish one well-defined task."""
    result = operator.abs(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `operator` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module operator

NAME
    operator - Operator interface.

MODULE REFERENCE
    https://docs.python.org/3.14/library/operator.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module exports a set of functions implemented in C corresponding
    to the intrinsic operators of Python.  For example, operator.add(x, y)
    is equivalent to the expression x+y.  The function names are those
    used for special methods; variants without leading and trailing
    '__' are also provided for convenience.

CLASSES
    builtins.object
        attrgetter
        itemgetter
        methodcaller

    class attrgetter(builtins.object)
     |  attrgetter(attr, /, *attrs)
     |
     |  Return a callable object that fetches the given attribute(s) from its operand.
     |  After f = attrgetter('name'), the call f(r) returns r.name.
     |  After g = attrgetter('name', 'date'), the call g(r) returns (r.name, r.date).
     |  After h = attrgetter('name.first', 'name.last'), the call h(r) returns
     |  (r.name.first, r.name.last).
     |
     |  Methods defined here:
     |
     |  __call__(self, /, *args, **kwargs)
     |      Call self as a function.
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __reduce__(self, /)
     |      Return state information for pickling
     |
     |  __repr__(self, /)
     |      Return repr(self).
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
     |  __vectorcalloffset__
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __text_signature__ = '(attr, /, *attrs)'

    class itemgetter(builtins.object)
     |  itemgetter(item, /, *items)
     |
     |  Return a callable object that fetches the given item(s) from its operand.
     |  After f = itemgetter(2), the call f(r) returns r[2].
     |  After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])
     |
     |  Methods defined here:
     |
     |  __call__(self, /, *args, **kwargs)
     |      Call self as a function.
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __reduce__(self, /)
     |      Return state information for pickling
     |
     |  __repr__(self, /)
     |      Return repr(self).
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
     |  __vectorcalloffset__
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __text_signature__ = '(item, /, *items)'

    class methodcaller(builtins.object)
     |  methodcaller(name, /, *args, **kwargs)
     |
     |  Return a callable object that calls the given method on its operand.
     |  After f = methodcaller('name'), the call f(r) returns r.name().
     |  After g = methodcaller('name', 'date', foo=1), the call g(r) returns
     |  r.name('date', foo=1).
     |
     |  Methods defined here:
     |
     |  __call__(self, /, *args, **kwargs)
     |      Call self as a function.
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __reduce__(self, /)
     |      Return state information for pickling
     |
     |  __repr__(self, /)
     |      Return repr(self).
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
     |  __vectorcalloffset__
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __text_signature__ = '(name, /, *args, **kwargs)'

FUNCTIONS
    __abs__ = abs(a, /)
        Same as abs(a).

    __add__ = add(a, b, /)
        Same as a + b.

    __and__ = and_(a, b, /)
        Same as a & b.

    __call__ = call(obj, /, *args, **kwargs)
        Same as obj(*args, **kwargs).

    __concat__ = concat(a, b, /)
        Same as a + b, for a and b sequences.

    __contains__ = contains(a, b, /)
        Same as b in a (note reversed operands).

    __delitem__ = delitem(a, b, /)
        Same as del a[b].

    __eq__ = eq(a, b, /)
        Same as a == b.

    __floordiv__ = floordiv(a, b, /)
        Same as a // b.

    __ge__ = ge(a, b, /)
        Same as a >= b.

    __getitem__ = getitem(a, b, /)
        Same as a[b].

    __gt__ = gt(a, b, /)
        Same as a > b.

    __iadd__ = iadd(a, b, /)
        Same as a += b.

    __iand__ = iand(a, b, /)
        Same as a &= b.

    __iconcat__ = iconcat(a, b, /)
        Same as a += b, for a and b sequences.

    __ifloordiv__ = ifloordiv(a, b, /)
        Same as a //= b.

    __ilshift__ = ilshift(a, b, /)
        Same as a <<= b.

    __imatmul__ = imatmul(a, b, /)
        Sa
```

## Related

Other standard-library modules pair well with `operator`; explore the `python` domain of this catalog.
