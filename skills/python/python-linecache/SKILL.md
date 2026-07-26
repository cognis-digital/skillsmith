---
name: python-linecache
description: "Program with Python's linecache module: Cache lines from Python source files."
version: 1.0.0
tags: [linecache, programming, python, stdlib]
---

# Python: `linecache`

## Overview

Cache lines from Python source files.

This is intended to read lines from modules imported -- hence if a filename
is not found, it will look down the module search path for a file by
that name.

## When to use

Reach for `linecache` when your task calls for Cache lines from Python source files. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import linecache
```

## Key functions

- `linecache.checkcache(filename=None)`
- `linecache.clearcache()`
- `linecache.getline(filename, lineno, module_globals=None)`
- `linecache.getlines(filename, module_globals=None)`
- `linecache.lazycache(filename, module_globals)`
- `linecache.updatecache(filename, module_globals=None)`

## Constants / attributes

`cache`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import linecache

def do_work(...):
    """Use linecache to accomplish one well-defined task."""
    result = linecache.checkcache(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `linecache` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module linecache

NAME
    linecache - Cache lines from Python source files.

MODULE REFERENCE
    https://docs.python.org/3.14/library/linecache.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This is intended to read lines from modules imported -- hence if a filename
    is not found, it will look down the module search path for a file by
    that name.

FUNCTIONS
    checkcache(filename=None)
        Discard cache entries that are out of date.
        (This is not checked upon each call!)

    clearcache()
        Clear the cache entirely.

    getline(filename, lineno, module_globals=None)
        Get a line for a Python source file from the cache.
        Update the cache if it doesn't contain an entry for this file already.

    lazycache(filename, module_globals)
        Seed the cache for filename with module_globals.

        The module loader will be asked for the source only when getlines is
        called, not immediately.

        If there is an entry in the cache already, it is not altered.

        :return: True if a lazy load is registered in the cache,
            otherwise False. To register such a load a module loader with a
            get_source method must be found, the filename must be a cacheable
            filename, and the filename must not be already cached.

DATA
    __all__ = ['getline', 'clearcache', 'checkcache', 'lazycache']

FILE
    c:\python314\lib\linecache.py


```

## Related

Other standard-library modules pair well with `linecache`; explore the `python` domain of this catalog.
