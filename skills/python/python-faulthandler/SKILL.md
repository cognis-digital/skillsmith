---
name: python-faulthandler
description: "Program with Python's faulthandler module: faulthandler module."
version: 1.0.0
tags: [faulthandler, programming, python, stdlib]
---

# Python: `faulthandler`

## Overview

faulthandler module.

## When to use

Reach for `faulthandler` when your task calls for faulthandler module. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import faulthandler
```

## Key functions

- `faulthandler.cancel_dump_traceback_later()`
- `faulthandler.disable()`
- `faulthandler.dump_c_stack(...)`
- `faulthandler.dump_traceback(...)`
- `faulthandler.dump_traceback_later(...)`
- `faulthandler.enable(...)`
- `faulthandler.is_enabled()`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import faulthandler

def do_work(...):
    """Use faulthandler to accomplish one well-defined task."""
    result = faulthandler.cancel_dump_traceback_later(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `faulthandler` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: built-in module faulthandler

NAME
    faulthandler - faulthandler module.

FUNCTIONS
    cancel_dump_traceback_later()
        Cancel the previous call to dump_traceback_later().

    disable()
        Disable the fault handler.

    dump_c_stack(file=sys.stderr)
        Dump the C stack of the current thread.

    dump_traceback(file=sys.stderr, all_threads=True)
        Dump the traceback of the current thread, or of all threads if all_threads is True, into file.

    dump_traceback_later(timeout, repeat=False, file=sys.stderr, exit=False)
        Dump the traceback of all threads in timeout seconds,
        or each timeout seconds if repeat is True. If exit is True, call _exit(1) which is not safe.

    enable(file=sys.stderr, all_threads=True)
        Enable the fault handler.

    is_enabled()
        Check if the handler is enabled.

FILE
    (built-in)


```

## Related

Other standard-library modules pair well with `faulthandler`; explore the `python` domain of this catalog.
