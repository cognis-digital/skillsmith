---
name: python-ensurepip
description: "Program with Python's ensurepip module: The Python standard-library module `ensurepip`."
version: 1.0.0
tags: [ensurepip, programming, python, stdlib]
---

# Python: `ensurepip`

## Overview

`ensurepip` is part of the Python standard library.

## When to use

Reach for `ensurepip` when your task calls for The Python standard-library module `ensurepip`. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import ensurepip
```

## Key functions

- `ensurepip.bootstrap(*, root=None, upgrade=False, user=False, altinstall=False, default_pip=False, verbosity=0)`
- `ensurepip.copy2(src, dst, *, follow_symlinks=True)`
- `ensurepip.version()`

## Key classes

`Path`, `nullcontext`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import ensurepip

def do_work(...):
    """Use ensurepip to accomplish one well-defined task."""
    result = ensurepip.bootstrap(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `ensurepip` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: package ensurepip

NAME
    ensurepip

MODULE REFERENCE
    https://docs.python.org/3.14/library/ensurepip.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

PACKAGE CONTENTS
    __main__
    _uninstall

FUNCTIONS
    bootstrap(
        *,
        root=None,
        upgrade=False,
        user=False,
        altinstall=False,
        default_pip=False,
        verbosity=0
    )
        Bootstrap pip into the current Python installation (or the given root
        directory).

        Note that calling this function will alter both sys.path and os.environ.

    version()
        Returns a string specifying the bundled version of pip.

DATA
    __all__ = ['version', 'bootstrap']

FILE
    c:\python314\lib\ensurepip\__init__.py


```

## Related

Other standard-library modules pair well with `ensurepip`; explore the `python` domain of this catalog.
