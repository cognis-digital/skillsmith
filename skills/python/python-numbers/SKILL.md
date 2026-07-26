---
name: python-numbers
description: "Program with Python's numbers module: Abstract Base Classes (ABCs) for numbers, according to PEP 3141."
version: 1.0.0
tags: [numbers, programming, python, stdlib]
---

# Python: `numbers`

## Overview

Abstract Base Classes (ABCs) for numbers, according to PEP 3141.

TODO: Fill out more detailed documentation on the operators.

## When to use

Reach for `numbers` when your task calls for Abstract Base Classes (ABCs) for numbers, according to PEP 3141. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import numbers
```

## Key functions

- `numbers.abstractmethod(funcobj)`

## Key classes

`ABCMeta`, `Complex`, `Integral`, `Number`, `Rational`, `Real`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import numbers

def do_work(...):
    """Use numbers to accomplish one well-defined task."""
    result = numbers.abstractmethod(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `numbers` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module numbers

NAME
    numbers - Abstract Base Classes (ABCs) for numbers, according to PEP 3141.

MODULE REFERENCE
    https://docs.python.org/3.14/library/numbers.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    TODO: Fill out more detailed documentation on the operators.

CLASSES
    builtins.object
        Number
            Complex
                Real
                    Rational
                        Integral

    class Complex(Number)
     |  Complex defines the operations that work on the builtin complex type.
     |
     |  In short, those are: a conversion to complex, .real, .imag, +, -,
     |  *, /, **, abs(), .conjugate, ==, and !=.
     |
     |  If it is given heterogeneous arguments, and doesn't have special
     |  knowledge about them, it should fall back to the builtin complex
     |  type as described below.
     |
     |  Method resolution order:
     |      Complex
     |      Number
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __abs__(self)
     |      Returns the Real distance from 0. Called for abs(self).
     |
     |  __add__(self, other)
     |      self + other
     |
     |  __bool__(self)
     |      True if self != 0. Called for bool(self).
     |
     |  __complex__(self)
     |      Return a builtin complex instance. Called for complex(self).
     |
     |  __eq__(self, other)
     |      self == other
     |
     |  __mul__(self, other)
     |      self * other
     |
     |  __neg__(self)
     |      -self
     |
     |  __pos__(self)
     |      +self
     |
     |  __pow__(self, exponent)
     |      self ** exponent; should promote to float or complex when necessary.
     |
     |  __radd__(self, other)
     |      other + self
     |
     |  __rmul__(self, other)
     |      other * self
     |
     |  __rpow__(self, base)
     |      base ** self
     |
     |  __rsub__(self, other)
     |      other - self
     |
     |  __rtruediv__(self, other)
     |      other / self
     |
     |  __sub__(self, other)
     |      self - other
     |
     |  __truediv__(self, other)
     |      self / other: Should promote to float when necessary.
     |
     |  conjugate(self)
     |      (x+y*i).conjugate() returns (x-y*i).
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  imag
     |      Retrieve the imaginary component of this number.
     |
     |      This should subclass Real.
     |
     |  real
     |      Retrieve the real component of this number.
     |
     |      This should subclass Real.
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __abstractmethods__ = frozenset({'__abs__', '__add__', '__complex__', ...
     |
     |  __hash__ = None

    class Integral(Rational)
     |  Integral adds methods that work on integral numbers.
     |
     |  In short, these are conversion to int, pow with modulus, and the
     |  bit-string operations.
     |
     |  Method resolution order:
     |      Integral
     |      Rational
     |      Real
     |      Complex
     |      Number
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __and__(self, other)
     |      self & other
     |
     |  __float__(self)
     |      float(self) == float(int(self))
     |
     |  __index__(self)
     |      Called whenever an index is needed, such as in slicing
     |
     |  __int__(self)
     |      int(self)
     |
     |  __invert__(self)
     |      ~self
     |
     |  __lshift__(self, other)
     |      self << other
     |
     |  __or__(self, other)
     |      self | other
     |
     |  __pow__(self, exponent, modulus=None)
     |      self ** exponent % modulus, but maybe faster.
     |
     |      Accept the modulus argument if you want to support the
     |      3-argument version of pow(). Raise a TypeError if exponent < 0
     |      or any argument isn't Integral. Otherwise, just implement the
     |      2-argument version described in Complex.
     |
     |  __rand__(self, other)
     |      other & self
     |
     |  __rlshift__(self, other)
     |      other << self
     |
     |  __ror__(self, other)
     |      other | self
     |
     |  __rrshift__(self, other)
     |      other >> self
     |
     |  __rshift__(self, other)
     |      self >> other
     |
     |  __rxor__(self, other)
     |      other ^ self
     |
     |  __xor__(self, other)
     |      self ^ other
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  denominator
     |      Integers have a denominator of 1.
     |
     |  numerator
     |      Integers are their own numerators.
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __abstractmethods__ = frozenset({'__abs__', '__add__', '__and__', '__c...
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Real:
     |
     |  __ceil__(self)
     |      Finds the least Integral >= self.
     |
     |  __complex__(self)
     |      complex(self) == complex(float(self), 0)
     |
     |  __divmod__(self, other)
     |      divmod(self, other): The pair (self // other, self % other).
     |
     |      Sometimes this can be computed faster than the pair of
     |      operations.
     |
     |  __floor__(self)
     |      Finds the greatest Integral <= self.
     |
     |  __floordiv__(self, other)
     
```

## Related

Other standard-library modules pair well with `numbers`; explore the `python` domain of this catalog.
