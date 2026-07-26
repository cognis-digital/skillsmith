---
name: python-select
description: "Program with Python's select module: This module supports asynchronous I/O on multiple file descriptors."
version: 1.0.0
tags: [programming, python, select, stdlib]
---

# Python: `select`

## Overview

This module supports asynchronous I/O on multiple file descriptors.

*** IMPORTANT NOTICE ***
On Windows, only sockets are supported; on Unix, all file descriptors.

## When to use

Reach for `select` when your task calls for This module supports asynchronous I/O on multiple file descriptors. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import select
```

## Key functions

- `select.select(rlist, wlist, xlist, timeout=None, /)`

## Key classes

`error`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import select

def do_work(...):
    """Use select to accomplish one well-defined task."""
    result = select.select(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `select` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module select

NAME
    select - This module supports asynchronous I/O on multiple file descriptors.

DESCRIPTION
    *** IMPORTANT NOTICE ***
    On Windows, only sockets are supported; on Unix, all file descriptors.

FUNCTIONS
    select(rlist, wlist, xlist, timeout=None, /)
        Wait until one or more file descriptors are ready for some kind of I/O.

        The first three arguments are iterables of file descriptors to be waited for:
        rlist -- wait until ready for reading
        wlist -- wait until ready for writing
        xlist -- wait for an "exceptional condition"
        If only one kind of condition is required, pass [] for the other lists.

        A file descriptor is either a socket or file object, or a small integer
        gotten from a fileno() method call on one of those.

        The optional 4th argument specifies a timeout in seconds; it may be
        a floating-point number to specify fractions of seconds.  If it is absent
        or None, the call will never time out.

        The return value is a tuple of three lists corresponding to the first three
        arguments; each contains the subset of the corresponding file descriptors
        that are ready.

        *** IMPORTANT NOTICE ***
        On Windows, only sockets are supported; on Unix, all file
        descriptors can be used.

FILE
    c:\python314\dlls\select.pyd


```

## Related

Other standard-library modules pair well with `select`; explore the `python` domain of this catalog.
