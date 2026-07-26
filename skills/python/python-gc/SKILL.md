---
name: python-gc
description: "Program with Python's gc module: This module provides access to the garbage collector for reference cycles."
version: 1.0.0
tags: [gc, programming, python, stdlib]
---

# Python: `gc`

## Overview

This module provides access to the garbage collector for reference cycles.

enable() -- Enable automatic garbage collection.
disable() -- Disable automatic garbage collection.
isenabled() -- Returns true if automatic collection is enabled.
collect() -- Do a full collection right now.
get_count() -- Return the current collection counts.
get_stats() -- Return list of dictionaries containing per-generation stats.
set_debug() -- Set debugging flags.
get_debug() -- Get debugging flags.
set_threshold() -- Set the collection thresholds.
get_threshold() -- Return the current collection thresholds.
get_objects() -- Return a list of all objects tracked by the collector.
is_tracked() -- Returns true if a given object is tracked.
is_finalized() -- Returns true if a given object has been already finalized.
get_referrers() -- Return the list of objects that refer to an object.
get_referents() -- Return the list of objects that an object refers to.
freeze() -- Freeze all tracked objects and ignore them for future collections.
unfreeze() -- Unfreeze all objects in the permanent generation.
get_freeze_count() -- Return the number of objects in the permanent generation.

## When to use

Reach for `gc` when your task calls for This module provides access to the garbage collector for reference cycles. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import gc
```

## Key functions

- `gc.collect(generation=2)`
- `gc.disable()`
- `gc.enable()`
- `gc.freeze()`
- `gc.get_count()`
- `gc.get_debug()`
- `gc.get_freeze_count()`
- `gc.get_objects(generation=None)`
- `gc.get_referents(*objs)`
- `gc.get_referrers(*objs)`
- `gc.get_stats()`
- `gc.get_threshold()`
- `gc.is_finalized(obj, /)`
- `gc.is_tracked(obj, /)`
- `gc.isenabled()`
- `gc.set_debug(flags, /)`
- `gc.set_threshold(...)`
- `gc.unfreeze()`

## Constants / attributes

`DEBUG_COLLECTABLE`, `DEBUG_LEAK`, `DEBUG_SAVEALL`, `DEBUG_STATS`, `DEBUG_UNCOLLECTABLE`, `callbacks`, `garbage`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import gc

def do_work(...):
    """Use gc to accomplish one well-defined task."""
    result = gc.collect(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `gc` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: built-in module gc

NAME
    gc - This module provides access to the garbage collector for reference cycles.

MODULE REFERENCE
    https://docs.python.org/3.14/library/gc.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    enable() -- Enable automatic garbage collection.
    disable() -- Disable automatic garbage collection.
    isenabled() -- Returns true if automatic collection is enabled.
    collect() -- Do a full collection right now.
    get_count() -- Return the current collection counts.
    get_stats() -- Return list of dictionaries containing per-generation stats.
    set_debug() -- Set debugging flags.
    get_debug() -- Get debugging flags.
    set_threshold() -- Set the collection thresholds.
    get_threshold() -- Return the current collection thresholds.
    get_objects() -- Return a list of all objects tracked by the collector.
    is_tracked() -- Returns true if a given object is tracked.
    is_finalized() -- Returns true if a given object has been already finalized.
    get_referrers() -- Return the list of objects that refer to an object.
    get_referents() -- Return the list of objects that an object refers to.
    freeze() -- Freeze all tracked objects and ignore them for future collections.
    unfreeze() -- Unfreeze all objects in the permanent generation.
    get_freeze_count() -- Return the number of objects in the permanent generation.

FUNCTIONS
    collect(generation=2)
        Run the garbage collector.

        With no arguments, run a full collection.  The optional argument
        may be an integer specifying which generation to collect.  A ValueError
        is raised if the generation number is invalid.

        The number of unreachable objects is returned.

    disable()
        Disable automatic garbage collection.

    enable()
        Enable automatic garbage collection.

    freeze()
        Freeze all current tracked objects and ignore them for future collections.

        This can be used before a POSIX fork() call to make the gc copy-on-write friendly.
        Note: collection before a POSIX fork() call may free pages for future allocation
        which can cause copy-on-write.

    get_count()
        Return a three-tuple of the current collection counts.

    get_debug()
        Get the garbage collection debugging flags.

    get_freeze_count()
        Return the number of objects in the permanent generation.

    get_objects(generation=None)
        Return a list of objects tracked by the collector (excluding the list returned).

          generation
            Generation to extract the objects from.

        If generation is not None, return only the objects tracked by the collector
        that are in that generation.

    get_referents(*objs)
        Return the list of objects that are directly referred to by 'objs'.

    get_referrers(*objs)
        Return the list of objects that directly refer to any of 'objs'.

    get_stats()
        Return a list of dictionaries containing per-generation statistics.

    get_threshold()
        Return the current collection thresholds.

    is_finalized(obj, /)
        Returns true if the object has been already finalized by the GC.

    is_tracked(obj, /)
        Returns true if the object is tracked by the garbage collector.

        Simple atomic objects will return false.

    isenabled()
        Returns true if automatic garbage collection is enabled.

    set_debug(flags, /)
        Set the garbage collection debugging flags.

          flags
            An integer that can have the following bits turned on:
              DEBUG_STATS - Print statistics during collection.
              DEBUG_COLLECTABLE - Print collectable objects found.
              DEBUG_UNCOLLECTABLE - Print unreachable but uncollectable objects
                found.
              DEBUG_SAVEALL - Save objects to gc.garbage rather than freeing them.
              DEBUG_LEAK - Debug leaking programs (everything but STATS).

        Debugging information is written to sys.stderr.

    set_threshold(...)
        set_threshold(threshold0, [threshold1, [threshold2]])
        Set the collection thresholds (the collection frequency).

        Setting 'threshold0' to zero disables collection.

    unfreeze()
        Unfreeze all objects in the permanent generation.

        Put all objects in the permanent generation back into oldest generation.

DATA
    DEBUG_COLLECTABLE = 2
    DEBUG_LEAK = 38
    DEBUG_SAVEALL = 32
    DEBUG_STATS = 1
    DEBUG_UNCOLLECTABLE = 4
    callbacks = []
    garbage = []

FILE
    (built-in)


```

## Related

Other standard-library modules pair well with `gc`; explore the `python` domain of this catalog.
