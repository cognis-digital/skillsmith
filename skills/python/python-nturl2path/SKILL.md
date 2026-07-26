---
name: python-nturl2path
description: "Program with Python's nturl2path module: Convert a NT pathname to a file URL and vice versa."
version: 1.0.0
tags: [nturl2path, programming, python, stdlib]
---

# Python: `nturl2path`

## Overview

Convert a NT pathname to a file URL and vice versa.

This module only exists to provide OS-specific code
for urllib.requests, thus do not use directly.

## When to use

Reach for `nturl2path` when your task calls for Convert a NT pathname to a file URL and vice versa. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import nturl2path
```

## Key functions

- `nturl2path.pathname2url(p)`
- `nturl2path.url2pathname(url)`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import nturl2path

def do_work(...):
    """Use nturl2path to accomplish one well-defined task."""
    result = nturl2path.pathname2url(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `nturl2path` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module nturl2path

NAME
    nturl2path - Convert a NT pathname to a file URL and vice versa.

MODULE REFERENCE
    https://docs.python.org/3.14/library/nturl2path.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module only exists to provide OS-specific code
    for urllib.requests, thus do not use directly.

FUNCTIONS
    pathname2url(p)
        OS-specific conversion from a file system path to a relative URL
        of the 'file' scheme; not recommended for general use.

    url2pathname(url)
        OS-specific conversion from a relative URL of the 'file' scheme
        to a file system path; not recommended for general use.

FILE
    c:\python314\lib\nturl2path.py


```

## Related

Other standard-library modules pair well with `nturl2path`; explore the `python` domain of this catalog.
