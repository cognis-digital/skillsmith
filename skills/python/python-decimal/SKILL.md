---
name: python-decimal
description: "Program with Python's decimal module: Decimal fixed-point and floating-point arithmetic."
version: 1.0.0
tags: [decimal, programming, python, stdlib]
---

# Python: `decimal`

## Overview

Decimal fixed-point and floating-point arithmetic.

This is an implementation of decimal floating-point arithmetic based on
the General Decimal Arithmetic Specification:

    http://speleotrove.com/decimal/decarith.html

and IEEE standard 854-1987:

    http://en.wikipedia.org/wiki/IEEE_854-1987

Decimal floating point has finite precision with arbitrarily large bounds.

The purpose of this module is to support arithmetic using familiar
"schoolhouse" rules and to avoid some of the tricky representation
issues associated with binary floating point.  The package is especially
useful for financial applications or for contexts where users have
expectations that are at odds with binary floating point (for instance,
in binary floating point, 1.00 % 0.1 gives 0.09999999999999995 instead
of 0.0; Decimal('1.00') % Decimal('0.1') returns the expected
Decimal('0.00')).

Here are some examples of using the decimal module:

>>> from decimal import *
>>> setcontext(ExtendedContext)
>>> Decimal(0)
Decimal('0')
>>> Decimal('1')
Decimal('1')
>>> Decimal('-.0123')
Decimal('-0.0123')
>>> Decimal(123456)
Decimal('123456')
>>> Decimal('123.45e12345678')
Decimal('1.2345E+12345680')
>>> Decimal('1.33') + Decimal('1.27')
Decimal('2.60')
>>> Decimal('12.34') + Decimal('3.87') - Decimal('18.41')
Decimal('-2.20')
>>> dig = Decimal(1)
>>> print(dig / Decimal(3))
0.333333333
>>> getcontext().prec = 18
>>> print(dig / Decimal(3))
0.333333333333333333
>>> print(dig.sqrt())
1
>>> print(Decimal(3).sqrt())
1.73205080756887729
>>> print(Decimal(3) ** 123)
4.85192780976896427E+58
>>> inf = Decimal(1) / Decimal(0)
>>> print(inf)
Infinity
>>> neginf = Decimal(-1) / Decimal(0)
>>> print(neginf)
-Infinity
>>> print(neginf + inf)
NaN
>>> print(neginf * inf)
-Infinity
>>> print(dig / 0)
Infinity
>>> getcontext().traps[DivisionByZero] = 1
>>> print(dig / 0)
Traceback (most recent call last):
  ...
  ...
  ...
decimal.DivisionByZero: x / 0
>>> c = Context()
>>> c.traps[InvalidOperation] = 0
>>> print(c.flags[InvalidOperation])
0
>>> c.divide(Decimal(0), Decimal(0))
Decimal('NaN')
>>> c.traps[InvalidOperation] = 1
>>> print(c.flags[InvalidOperation])
1
>>> c.flags[InvalidOperation] = 0
>>> print(c.flags[InvalidOperation])
0
>>> print(c.divide(Decimal(0), Decimal(0)))
Traceback (most recent call last):
  ...
  ...
  ...
decimal.InvalidOperation: 0 / 0
>>> print(c.flags[InvalidOperation])
1
>>> c.flags[InvalidOperation] = 0
>>> c.traps[InvalidOperation] = 0
>>> print(c.divide(Decimal(0), Decimal(0)))
NaN
>>> print(c.flags[InvalidOperation])
1
>>>

## When to use

Reach for `decimal` when your task calls for Decimal fixed-point and floating-point arithmetic. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import decimal
```

## Key functions

- `decimal.IEEEContext(bits, /)`
- `decimal.getcontext()`
- `decimal.localcontext(ctx=None, **kwargs)`
- `decimal.setcontext(context, /)`

## Key classes

`Clamped`, `Context`, `ConversionSyntax`, `Decimal`, `DecimalException`, `DecimalTuple`, `DivisionByZero`, `DivisionImpossible`, `DivisionUndefined`, `FloatOperation`, `Inexact`, `InvalidContext`, `InvalidOperation`, `Overflow`, `Rounded`, `Subnormal`, `Underflow`

## Constants / attributes

`BasicContext`, `DefaultContext`, `ExtendedContext`, `HAVE_CONTEXTVAR`, `HAVE_THREADS`, `IEEE_CONTEXT_MAX_BITS`, `MAX_EMAX`, `MAX_PREC`, `MIN_EMIN`, `MIN_ETINY`, `ROUND_05UP`, `ROUND_CEILING`, `ROUND_DOWN`, `ROUND_FLOOR`, `ROUND_HALF_DOWN`, `ROUND_HALF_EVEN`, `ROUND_HALF_UP`, `ROUND_UP`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import decimal

def do_work(...):
    """Use decimal to accomplish one well-defined task."""
    result = decimal.IEEEContext(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `decimal` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module decimal

NAME
    decimal - Decimal fixed-point and floating-point arithmetic.

MODULE REFERENCE
    https://docs.python.org/3.14/library/decimal.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This is an implementation of decimal floating-point arithmetic based on
    the General Decimal Arithmetic Specification:

        http://speleotrove.com/decimal/decarith.html

    and IEEE standard 854-1987:

        http://en.wikipedia.org/wiki/IEEE_854-1987

    Decimal floating point has finite precision with arbitrarily large bounds.

    The purpose of this module is to support arithmetic using familiar
    "schoolhouse" rules and to avoid some of the tricky representation
    issues associated with binary floating point.  The package is especially
    useful for financial applications or for contexts where users have
    expectations that are at odds with binary floating point (for instance,
    in binary floating point, 1.00 % 0.1 gives 0.09999999999999995 instead
    of 0.0; Decimal('1.00') % Decimal('0.1') returns the expected
    Decimal('0.00')).

    Here are some examples of using the decimal module:

    >>> from decimal import *
    >>> setcontext(ExtendedContext)
    >>> Decimal(0)
    Decimal('0')
    >>> Decimal('1')
    Decimal('1')
    >>> Decimal('-.0123')
    Decimal('-0.0123')
    >>> Decimal(123456)
    Decimal('123456')
    >>> Decimal('123.45e12345678')
    Decimal('1.2345E+12345680')
    >>> Decimal('1.33') + Decimal('1.27')
    Decimal('2.60')
    >>> Decimal('12.34') + Decimal('3.87') - Decimal('18.41')
    Decimal('-2.20')
    >>> dig = Decimal(1)
    >>> print(dig / Decimal(3))
    0.333333333
    >>> getcontext().prec = 18
    >>> print(dig / Decimal(3))
    0.333333333333333333
    >>> print(dig.sqrt())
    1
    >>> print(Decimal(3).sqrt())
    1.73205080756887729
    >>> print(Decimal(3) ** 123)
    4.85192780976896427E+58
    >>> inf = Decimal(1) / Decimal(0)
    >>> print(inf)
    Infinity
    >>> neginf = Decimal(-1) / Decimal(0)
    >>> print(neginf)
    -Infinity
    >>> print(neginf + inf)
    NaN
    >>> print(neginf * inf)
    -Infinity
    >>> print(dig / 0)
    Infinity
    >>> getcontext().traps[DivisionByZero] = 1
    >>> print(dig / 0)
    Traceback (most recent call last):
      ...
      ...
      ...
    decimal.DivisionByZero: x / 0
    >>> c = Context()
    >>> c.traps[InvalidOperation] = 0
    >>> print(c.flags[InvalidOperation])
    0
    >>> c.divide(Decimal(0), Decimal(0))
    Decimal('NaN')
    >>> c.traps[InvalidOperation] = 1
    >>> print(c.flags[InvalidOperation])
    1
    >>> c.flags[InvalidOperation] = 0
    >>> print(c.flags[InvalidOperation])
    0
    >>> print(c.divide(Decimal(0), Decimal(0)))
    Traceback (most recent call last):
      ...
      ...
      ...
    decimal.InvalidOperation: 0 / 0
    >>> print(c.flags[InvalidOperation])
    1
    >>> c.flags[InvalidOperation] = 0
    >>> c.traps[InvalidOperation] = 0
    >>> print(c.divide(Decimal(0), Decimal(0)))
    NaN
    >>> print(c.flags[InvalidOperation])
    1
    >>>

CLASSES
    builtins.ArithmeticError(builtins.Exception)
        DecimalException
            Clamped
            DivisionByZero(DecimalException, builtins.ZeroDivisionError)
            FloatOperation(DecimalException, builtins.TypeError)
            Inexact
                Overflow(Inexact, Rounded)
                Underflow(Inexact, Rounded, Subnormal)
            InvalidOperation
                ConversionSyntax
                DivisionImpossible
                DivisionUndefined(InvalidOperation, builtins.ZeroDivisionError)
                InvalidContext
            Rounded
            Subnormal
    builtins.object
        Context
        Decimal
    builtins.tuple(builtins.object)
        DecimalTuple

    class Clamped(DecimalException)
     |  Method resolution order:
     |      Clamped
     |      DecimalException
     |      builtins.ArithmeticError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors inherited from DecimalException:
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.ArithmeticError:
     |
     |  __new__(*args, **kwargs) class method of builtins.ArithmeticError
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

    class Context(builtins.object)
     |  Context(
     |      prec=None,
     |      rounding=None,
     |      Emin=None,
     |      Emax=None,
     |      capitals=None,
     |      clamp=None,
     |    
```

## Related

Other standard-library modules pair well with `decimal`; explore the `python` domain of this catalog.
