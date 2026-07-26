---
name: python-stringprep
description: "Program with Python's stringprep module: Library that exposes various tables found in the StringPrep RFC 3454."
version: 1.0.0
tags: [programming, python, stdlib, stringprep]
---

# Python: `stringprep`

## Overview

Library that exposes various tables found in the StringPrep RFC 3454.

There are two kinds of tables: sets, for which a member test is provided,
and mappings, for which a mapping function is provided.

## When to use

Reach for `stringprep` when your task calls for Library that exposes various tables found in the StringPrep RFC 3454. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import stringprep
```

## Key functions

- `stringprep.in_table_a1(code)`
- `stringprep.in_table_b1(code)`
- `stringprep.in_table_c11(code)`
- `stringprep.in_table_c11_c12(code)`
- `stringprep.in_table_c12(code)`
- `stringprep.in_table_c21(code)`
- `stringprep.in_table_c21_c22(code)`
- `stringprep.in_table_c22(code)`
- `stringprep.in_table_c3(code)`
- `stringprep.in_table_c4(code)`
- `stringprep.in_table_c5(code)`
- `stringprep.in_table_c6(code)`
- `stringprep.in_table_c7(code)`
- `stringprep.in_table_c8(code)`
- `stringprep.in_table_c9(code)`
- `stringprep.in_table_d1(code)`
- `stringprep.in_table_d2(code)`
- `stringprep.map_table_b2(a)`
- `stringprep.map_table_b3(code)`

## Constants / attributes

`b1_set`, `b3_exceptions`, `c22_specials`, `c6_set`, `c7_set`, `c8_set`, `c9_set`, `unicodedata`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import stringprep

def do_work(...):
    """Use stringprep to accomplish one well-defined task."""
    result = stringprep.in_table_a1(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `stringprep` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module stringprep

NAME
    stringprep - Library that exposes various tables found in the StringPrep RFC 3454.

MODULE REFERENCE
    https://docs.python.org/3.14/library/stringprep.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    There are two kinds of tables: sets, for which a member test is provided,
    and mappings, for which a mapping function is provided.

FUNCTIONS
    in_table_a1(code)

    in_table_b1(code)

    in_table_c11(code)

    in_table_c11_c12(code)

    in_table_c12(code)

    in_table_c21(code)

    in_table_c21_c22(code)

    in_table_c22(code)

    in_table_c3(code)

    in_table_c4(code)

    in_table_c5(code)

    in_table_c6(code)

    in_table_c7(code)

    in_table_c8(code)

    in_table_c9(code)

    in_table_d1(code)

    in_table_d2(code)

    map_table_b2(a)

    map_table_b3(code)

DATA
    b1_set = {173, 847, 6150, 6155, 6156, 6157, ...}
    b3_exceptions = {181: 'μ', 223: 'ss', 304: 'i̇', 329: 'ʼn', 383: 's', ...
    c22_specials = {1757, 1807, 6158, 8204, 8205, 8232, ...}
    c6_set = {65529, 65530, 65531, 65532, 65533}
    c7_set = {12272, 12273, 12274, 12275, 12276, 12277, ...}
    c8_set = {832, 833, 8206, 8207, 8234, 8235, ...}
    c9_set = {917505, 917536, 917537, 917538, 917539, 917540, ...}
    unicodedata = <unicodedata.UCD object>

FILE
    c:\python314\lib\stringprep.py


```

## Related

Other standard-library modules pair well with `stringprep`; explore the `python` domain of this catalog.
