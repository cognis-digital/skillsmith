---
name: python-atexit
description: "Program with Python's atexit module: allow programmer to define multiple exit functions to be executed upon normal program termination."
version: 1.0.0
tags: [atexit, programming, python, stdlib]
---

# Python: `atexit`

## Overview

allow programmer to define multiple exit functions to be executed
upon normal program termination.

Two public functions, register and unregister, are defined.

## When to use

Reach for `atexit` when your task calls for allow programmer to define multiple exit functions to be executed upon normal program termination. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import atexit
```

## Key functions

- `atexit.register(func, /, *args, **kwargs)`
- `atexit.unregister(func, /)`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import atexit

def do_work(...):
    """Use atexit to accomplish one well-defined task."""
    result = atexit.register(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `atexit` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: built-in module atexit

NAME
    atexit

DESCRIPTION
    allow programmer to define multiple exit functions to be executed
    upon normal program termination.

    Two public functions, register and unregister, are defined.

FUNCTIONS
    register(func, /, *args, **kwargs)
        Register a function to be executed upon normal program termination

        func - function to be called at exit
        args - optional arguments to pass to func
        kwargs - optional keyword arguments to pass to func

        func is returned to facilitate usage as a decorator.

    unregister(func, /)
        Unregister an exit function which was previously registered using
        atexit.register

            func - function to be unregistered

FILE
    (built-in)


```

## Related

Other standard-library modules pair well with `atexit`; explore the `python` domain of this catalog.
