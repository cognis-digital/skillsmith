---
name: builtin-complex
description: "Program with Python's built-in complex: Create a complex number from a string or numbers."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `complex`

    ## Overview

    `complex` is a Python built-in class — always available, no import required.

    Create a complex number from a string or numbers.

If a string is given, parse it as a complex number.
If a single number is given, convert it to a complex number.
If the 'real' or 'imag' arguments are given, create a complex number
with the specified real and imaginary components.

    ## Signature

    ```python
    complex(real=0, imag=0)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `complex` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = complex(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class complex in module builtins

class complex(object)
 |  complex(real=0, imag=0)
 |
 |  Create a complex number from a string or numbers.
 |
 |  If a string is given, parse it as a complex number.
 |  If a single number is given, convert it to a complex number.
 |  If the 'real' or 'imag' arguments are given, create a complex number
 |  with the specified real and imaginary components.
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
 |      abs(self)
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __bool__(self, /)
 |      True if self else False
 |
 |  __complex__(self, /)
 |      Convert this value to exact type complex.
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __format__(self, format_spec, /)
 |      Convert to a string according to format_spec.
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
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __lt__(self, value, /)
 |      Return self<value.
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
 |  __pos__(self, /)
 |      +self
 |
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |
 |  __radd__(self, value, /)
 |      Return value+self.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |
 |  __rsub__(self, value, /)
 |      Return value-self.
 |
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |
 |  __sub__(self, value, /)
 |      Return self-value.
 |
 |  __truediv__(self, value, /)
 |      Return self/value.
 |
 |  conjugate(self, /)
 |      Return the complex conjugate of its argument. (3-4j).conjugate() == 3+4j.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  from_number(number, /)
 |      Convert number to a complex floating-point number.
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
 |  imag
 |      the imaginary part of a complex number
 |
 |  real
 |      the real part of a complex number

    ```
