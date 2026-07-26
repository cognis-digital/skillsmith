---
name: python-signal
description: "Program with Python's signal module: The Python standard-library module `signal`."
version: 1.0.0
tags: [programming, python, signal, stdlib]
---

# Python: `signal`

## Overview

`signal` is part of the Python standard library.

## When to use

Reach for `signal` when your task calls for The Python standard-library module `signal`. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import signal
```

## Key functions

- `signal.default_int_handler(signalnum, frame, /)`
- `signal.getsignal(signalnum)`
- `signal.raise_signal(signalnum, /)`
- `signal.set_wakeup_fd(fd, /, *, warn_on_full_buffer=True)`
- `signal.signal(signalnum, handler)`
- `signal.strsignal(signalnum, /)`
- `signal.valid_signals()`

## Key classes

`Handlers`, `Signals`

## Constants / attributes

`CTRL_BREAK_EVENT`, `CTRL_C_EVENT`, `NSIG`, `SIGABRT`, `SIGBREAK`, `SIGFPE`, `SIGILL`, `SIGINT`, `SIGSEGV`, `SIGTERM`, `SIG_DFL`, `SIG_IGN`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import signal

def do_work(...):
    """Use signal to accomplish one well-defined task."""
    result = signal.default_int_handler(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `signal` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module signal

NAME
    signal

MODULE REFERENCE
    https://docs.python.org/3.14/library/signal.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    enum.IntEnum(builtins.int, enum.ReprEnum)
        Handlers
        Signals

    class Handlers(enum.IntEnum)
     |  Handlers(*values)
     |
     |  An enumeration.
     |
     |  Method resolution order:
     |      Handlers
     |      enum.IntEnum
     |      builtins.int
     |      enum.ReprEnum
     |      enum.Enum
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __format__(self, format_spec, /) from builtins.int
     |      Convert to a string according to format_spec.
     |
     |  __new__(cls, value) from enum.Enum
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  SIG_DFL = <Handlers.SIG_DFL: 0>
     |
     |  SIG_IGN = <Handlers.SIG_IGN: 1>
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from enum.IntEnum:
     |
     |  __repr__(self) from enum.Enum
     |      Return repr(self).
     |
     |  __str__ = __repr__(self, /) from builtins.int
     |      Return repr(self).
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.int:
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
     |  __ceil__(self, /)
     |      Ceiling of an Integral returns itself.
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
     |  __floor__(self, /)
     |      Flooring an Integral returns itself.
     |
     |  __floordiv__(self, value, /)
     |      Return self//value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getnewargs__(self, /)
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
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
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __lshift__(self, value, /)
     |      Return self<<value.
     |
     |  __lt__(self, value, /)
     |      Return self<value.
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
     |  __rfloordiv__(self, value, /)
     |      Return value//self.
     |
     |  __rlshift__(self, value, /)
     |      Return value<<self.
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
     |  __round__(self, ndigits=None, /)
     |      Rounding an Integral returns itself.
     |
     |      Rounding with an ndigits argument also returns an integer.
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
     |  __sizeof__(self, /)
     |      Returns size in memory, in bytes.
     |
     |  __sub__(self, value, /)
     |      Return self-value.
     |
     |  __truediv__(self, value, /)
     |      Return self/value.
     |
     |  __trunc__(self, /)
     |      Truncating an Integral returns itself.
     |
     |  __xor__(self, value, /)
     |      Return self^value.
     |
     |  as_integer_ratio(self, /)
     |      Return a pair of integers, whose ratio is equal to the original int.
     |
     |      The ratio is in lowest terms and has a positive denominator.
     |
     |      >>> (10).as_integer_ratio()
     |      (10, 1)
     |      >>> (-10).as_integer_ratio()
     |      (-10, 1)
     |      >>> (0).as_integer_ratio()
     |      (0, 1)
     |
     |  bit_count(self, /)
     |      Number of ones in the binary representation of the absolute value of self.
     |
     |      Also known as the population count.
     |
     |      >>> bin(13)
     |      '0b1101'
     |      >>> (13).bit_count()
     |      3
     |
     |  bit_length(self, /)
     |      Number of bits necessary to rep
```

## Related

Other standard-library modules pair well with `signal`; explore the `python` domain of this catalog.
