---
name: python-copyreg
description: "Program with Python's copyreg module: Helper to provide extensibility for pickle."
version: 1.0.0
tags: [copyreg, programming, python, stdlib]
---

# Python: `copyreg`

## Overview

Helper to provide extensibility for pickle.

This is only useful to add pickle support for extension types defined in
C, not for instances of user-defined classes.

## When to use

Reach for `copyreg` when your task calls for Helper to provide extensibility for pickle. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import copyreg
```

## Key functions

- `copyreg.add_extension(module, name, code)`
- `copyreg.clear_extension_cache()`
- `copyreg.constructor(object)`
- `copyreg.pickle(ob_type, pickle_function, constructor_ob=None)`
- `copyreg.pickle_complex(c)`
- `copyreg.pickle_super(obj)`
- `copyreg.pickle_union(obj)`
- `copyreg.remove_extension(module, name, code)`

## Constants / attributes

`dispatch_table`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import copyreg

def do_work(...):
    """Use copyreg to accomplish one well-defined task."""
    result = copyreg.add_extension(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `copyreg` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module copyreg

NAME
    copyreg - Helper to provide extensibility for pickle.

MODULE REFERENCE
    https://docs.python.org/3.14/library/copyreg.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This is only useful to add pickle support for extension types defined in
    C, not for instances of user-defined classes.

FUNCTIONS
    __newobj__(cls, *args)

    __newobj_ex__(cls, args, kwargs)
        Used by pickle protocol 4, instead of __newobj__ to allow classes with
        keyword-only arguments to be pickled correctly.

    add_extension(module, name, code)
        Register an extension code.

    clear_extension_cache()

    constructor(object)

    pickle(ob_type, pickle_function, constructor_ob=None)

    remove_extension(module, name, code)
        Unregister an extension code.  For testing only.

DATA
    __all__ = ['pickle', 'constructor', 'add_extension', 'remove_extension...

FILE
    c:\python314\lib\copyreg.py


```

## Related

Other standard-library modules pair well with `copyreg`; explore the `python` domain of this catalog.
