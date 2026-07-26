---
name: python-quopri
description: "Program with Python's quopri module: Conversions to/from quoted-printable transport encoding as per RFC 1521."
version: 1.0.0
tags: [programming, python, quopri, stdlib]
---

# Python: `quopri`

## Overview

Conversions to/from quoted-printable transport encoding as per RFC 1521.

## When to use

Reach for `quopri` when your task calls for Conversions to/from quoted-printable transport encoding as per RFC 1521. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import quopri
```

## Key functions

- `quopri.a2b_qp(data, header=False)`
- `quopri.b2a_qp(data, quotetabs=False, istext=True, header=False)`
- `quopri.decode(input, output, header=False)`
- `quopri.decodestring(s, header=False)`
- `quopri.encode(input, output, quotetabs, header=False)`
- `quopri.encodestring(s, quotetabs=False, header=False)`
- `quopri.ishex(c)`
- `quopri.main()`
- `quopri.needsquoting(c, quotetabs, header)`
- `quopri.quote(c)`
- `quopri.unhex(s)`

## Constants / attributes

`EMPTYSTRING`, `ESCAPE`, `HEX`, `MAXLINESIZE`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import quopri

def do_work(...):
    """Use quopri to accomplish one well-defined task."""
    result = quopri.a2b_qp(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `quopri` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module quopri

NAME
    quopri - Conversions to/from quoted-printable transport encoding as per RFC 1521.

MODULE REFERENCE
    https://docs.python.org/3.14/library/quopri.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

FUNCTIONS
    decode(input, output, header=False)
        Read 'input', apply quoted-printable decoding, and write to 'output'.
        'input' and 'output' are binary file objects.
        If 'header' is true, decode underscore as space (per RFC 1522).

    decodestring(s, header=False)

    encode(input, output, quotetabs, header=False)
        Read 'input', apply quoted-printable encoding, and write to 'output'.

        'input' and 'output' are binary file objects. The 'quotetabs' flag
        indicates whether embedded tabs and spaces should be quoted. Note that
        line-ending tabs and spaces are always encoded, as per RFC 1521.
        The 'header' flag indicates whether we are encoding spaces as _ as per RFC
        1522.

    encodestring(s, quotetabs=False, header=False)

DATA
    __all__ = ['encode', 'decode', 'encodestring', 'decodestring']

FILE
    c:\python314\lib\quopri.py


```

## Related

Other standard-library modules pair well with `quopri`; explore the `python` domain of this catalog.
