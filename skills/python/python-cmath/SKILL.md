---
name: python-cmath
description: "Program with Python's cmath module: This module provides access to mathematical functions for complex numbers."
version: 1.0.0
tags: [cmath, programming, python, stdlib]
---

# Python: `cmath`

## Overview

This module provides access to mathematical functions for complex
numbers.

## When to use

Reach for `cmath` when your task calls for This module provides access to mathematical functions for complex numbers. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import cmath
```

## Key functions

- `cmath.acos(z, /)`
- `cmath.acosh(z, /)`
- `cmath.asin(z, /)`
- `cmath.asinh(z, /)`
- `cmath.atan(z, /)`
- `cmath.atanh(z, /)`
- `cmath.cos(z, /)`
- `cmath.cosh(z, /)`
- `cmath.exp(z, /)`
- `cmath.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)`
- `cmath.isfinite(z, /)`
- `cmath.isinf(z, /)`
- `cmath.isnan(z, /)`
- `cmath.log(...)`
- `cmath.log10(z, /)`
- `cmath.phase(z, /)`
- `cmath.polar(z, /)`
- `cmath.rect(r, phi, /)`
- `cmath.sin(z, /)`
- `cmath.sinh(z, /)`
- `cmath.sqrt(z, /)`
- `cmath.tan(z, /)`
- `cmath.tanh(z, /)`

## Constants / attributes

`e`, `inf`, `infj`, `nan`, `nanj`, `pi`, `tau`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import cmath

def do_work(...):
    """Use cmath to accomplish one well-defined task."""
    result = cmath.acos(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `cmath` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: built-in module cmath

NAME
    cmath

DESCRIPTION
    This module provides access to mathematical functions for complex
    numbers.

FUNCTIONS
    acos(z, /)
        Return the arc cosine of z.

    acosh(z, /)
        Return the inverse hyperbolic cosine of z.

    asin(z, /)
        Return the arc sine of z.

    asinh(z, /)
        Return the inverse hyperbolic sine of z.

    atan(z, /)
        Return the arc tangent of z.

    atanh(z, /)
        Return the inverse hyperbolic tangent of z.

    cos(z, /)
        Return the cosine of z.

    cosh(z, /)
        Return the hyperbolic cosine of z.

    exp(z, /)
        Return the exponential value e**z.

    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two complex numbers are close in value.

          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values

        Return True if a is close in value to b, and False otherwise.

        For the values to be considered close, the difference between them must be
        smaller than at least one of the tolerances.

        -inf, inf and NaN behave similarly to the IEEE 754 Standard. That is, NaN is
        not close to anything, even itself. inf and -inf are only close to themselves.

    isfinite(z, /)
        Return True if both the real and imaginary parts of z are finite, else False.

    isinf(z, /)
        Checks if the real or imaginary part of z is infinite.

    isnan(z, /)
        Checks if the real or imaginary part of z not a number (NaN).

    log(z, base=<unrepresentable>, /)
        log(z[, base]) -> the logarithm of z to the given base.

        If the base is not specified, returns the natural logarithm (base e) of z.

    log10(z, /)
        Return the base-10 logarithm of z.

    phase(z, /)
        Return argument, also known as the phase angle, of a complex.

    polar(z, /)
        Convert a complex from rectangular coordinates to polar coordinates.

        r is the distance from 0 and phi the phase angle.

    rect(r, phi, /)
        Convert from polar coordinates to rectangular coordinates.

    sin(z, /)
        Return the sine of z.

    sinh(z, /)
        Return the hyperbolic sine of z.

    sqrt(z, /)
        Return the square root of z.

    tan(z, /)
        Return the tangent of z.

    tanh(z, /)
        Return the hyperbolic tangent of z.

DATA
    e = 2.718281828459045
    inf = inf
    infj = infj
    nan = nan
    nanj = nanj
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)


```

## Related

Other standard-library modules pair well with `cmath`; explore the `python` domain of this catalog.
