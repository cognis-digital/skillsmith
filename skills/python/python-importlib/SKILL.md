---
name: python-importlib
description: "Program with Python's importlib module: A pure Python implementation of import."
version: 1.0.0
tags: [importlib, programming, python, stdlib]
---

# Python: `importlib`

## Overview

A pure Python implementation of import.

## When to use

Reach for `importlib` when your task calls for A pure Python implementation of import. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import importlib
```

## Key functions

- `importlib.import_module(name, package=None)`
- `importlib.invalidate_caches()`
- `importlib.reload(module)`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import importlib

def do_work(...):
    """Use importlib to accomplish one well-defined task."""
    result = importlib.import_module(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `importlib` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: package importlib

NAME
    importlib - A pure Python implementation of import.

MODULE REFERENCE
    https://docs.python.org/3.14/library/importlib.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

PACKAGE CONTENTS
    _abc
    _bootstrap
    _bootstrap_external
    abc
    machinery
    metadata (package)
    readers
    resources (package)
    simple
    util

FUNCTIONS
    __import__(name, globals=None, locals=None, fromlist=(), level=0)
        Import a module.

        The 'globals' argument is used to infer where the import is occurring from
        to handle relative imports. The 'locals' argument is ignored. The
        'fromlist' argument specifies what should exist as attributes on the module
        being imported (e.g. ``from module import <fromlist>``).  The 'level'
        argument represents the package location to import from in a relative
        import (e.g. ``from ..pkg import mod`` would have a 'level' of 2).

    import_module(name, package=None)
        Import a module.

        The 'package' argument is required when performing a relative import. It
        specifies the package to use as the anchor point from which to resolve the
        relative import to an absolute import.

    invalidate_caches()
        Call the invalidate_caches() method on all meta path finders stored in
        sys.meta_path (where implemented).

    reload(module)
        Reload the module and return it.

        The module must have been successfully imported before.

DATA
    __all__ = ['__import__', 'import_module', 'invalidate_caches', 'reload...

FILE
    c:\python314\lib\importlib\__init__.py


```

## Related

Other standard-library modules pair well with `importlib`; explore the `python` domain of this catalog.
