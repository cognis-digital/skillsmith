---
name: python-colorsys
description: "Program with Python's colorsys module: Conversion functions between RGB and other color systems."
version: 1.0.0
tags: [colorsys, programming, python, stdlib]
---

# Python: `colorsys`

## Overview

Conversion functions between RGB and other color systems.

This modules provides two functions for each color system ABC:

  rgb_to_abc(r, g, b) --> a, b, c
  abc_to_rgb(a, b, c) --> r, g, b

All inputs and outputs are triples of floats in the range [0.0...1.0]
(with the exception of I and Q, which covers a slightly larger range).
Inputs outside the valid range may cause exceptions or invalid outputs.

Supported color systems:
RGB: Red, Green, Blue components
YIQ: Luminance, Chrominance (used by composite video signals)
HLS: Hue, Luminance, Saturation
HSV: Hue, Saturation, Value

## When to use

Reach for `colorsys` when your task calls for Conversion functions between RGB and other color systems. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import colorsys
```

## Key functions

- `colorsys.hls_to_rgb(h, l, s)`
- `colorsys.hsv_to_rgb(h, s, v)`
- `colorsys.rgb_to_hls(r, g, b)`
- `colorsys.rgb_to_hsv(r, g, b)`
- `colorsys.rgb_to_yiq(r, g, b)`
- `colorsys.yiq_to_rgb(y, i, q)`

## Constants / attributes

`ONE_SIXTH`, `ONE_THIRD`, `TWO_THIRD`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import colorsys

def do_work(...):
    """Use colorsys to accomplish one well-defined task."""
    result = colorsys.hls_to_rgb(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `colorsys` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module colorsys

NAME
    colorsys - Conversion functions between RGB and other color systems.

MODULE REFERENCE
    https://docs.python.org/3.14/library/colorsys.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This modules provides two functions for each color system ABC:

      rgb_to_abc(r, g, b) --> a, b, c
      abc_to_rgb(a, b, c) --> r, g, b

    All inputs and outputs are triples of floats in the range [0.0...1.0]
    (with the exception of I and Q, which covers a slightly larger range).
    Inputs outside the valid range may cause exceptions or invalid outputs.

    Supported color systems:
    RGB: Red, Green, Blue components
    YIQ: Luminance, Chrominance (used by composite video signals)
    HLS: Hue, Luminance, Saturation
    HSV: Hue, Saturation, Value

FUNCTIONS
    hls_to_rgb(h, l, s)

    hsv_to_rgb(h, s, v)

    rgb_to_hls(r, g, b)

    rgb_to_hsv(r, g, b)

    rgb_to_yiq(r, g, b)

    yiq_to_rgb(y, i, q)

DATA
    __all__ = ['rgb_to_yiq', 'yiq_to_rgb', 'rgb_to_hls', 'hls_to_rgb', 'rg...

FILE
    c:\python314\lib\colorsys.py


```

## Related

Other standard-library modules pair well with `colorsys`; explore the `python` domain of this catalog.
