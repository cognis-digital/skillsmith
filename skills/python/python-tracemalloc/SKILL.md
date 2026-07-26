---
name: python-tracemalloc
description: "Program with Python's tracemalloc module: The Python standard-library module `tracemalloc`."
version: 1.0.0
tags: [programming, python, stdlib, tracemalloc]
---

# Python: `tracemalloc`

## Overview

`tracemalloc` is part of the Python standard library.

## When to use

Reach for `tracemalloc` when your task calls for The Python standard-library module `tracemalloc`. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import tracemalloc
```

## Key functions

- `tracemalloc.clear_traces()`
- `tracemalloc.get_object_traceback(obj)`
- `tracemalloc.get_traceback_limit()`
- `tracemalloc.get_traced_memory()`
- `tracemalloc.get_tracemalloc_memory()`
- `tracemalloc.is_tracing()`
- `tracemalloc.reset_peak()`
- `tracemalloc.start(nframe=1, /)`
- `tracemalloc.stop()`
- `tracemalloc.take_snapshot()`
- `tracemalloc.total_ordering(cls)`

## Key classes

`BaseFilter`, `DomainFilter`, `Filter`, `Frame`, `Iterable`, `Sequence`, `Snapshot`, `Statistic`, `StatisticDiff`, `Trace`, `Traceback`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import tracemalloc

def do_work(...):
    """Use tracemalloc to accomplish one well-defined task."""
    result = tracemalloc.clear_traces(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `tracemalloc` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module tracemalloc

NAME
    tracemalloc

MODULE REFERENCE
    https://docs.python.org/3.14/library/tracemalloc.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.object
        BaseFilter
            DomainFilter
            Filter
        Frame
        Snapshot
        Statistic
        StatisticDiff
        Trace
    collections.abc.Sequence(collections.abc.Reversible, collections.abc.Collection)
        Traceback

    class BaseFilter(builtins.object)
     |  BaseFilter(inclusive)
     |
     |  Methods defined here:
     |
     |  __init__(self, inclusive)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class DomainFilter(BaseFilter)
     |  DomainFilter(inclusive, domain)
     |
     |  Method resolution order:
     |      DomainFilter
     |      BaseFilter
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, inclusive, domain)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  domain
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseFilter:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class Filter(BaseFilter)
     |  Filter(inclusive, filename_pattern, lineno=None, all_frames=False, domain=None)
     |
     |  Method resolution order:
     |      Filter
     |      BaseFilter
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(
     |      self,
     |      inclusive,
     |      filename_pattern,
     |      lineno=None,
     |      all_frames=False,
     |      domain=None
     |  )
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  filename_pattern
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseFilter:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class Frame(builtins.object)
     |  Frame(frame)
     |
     |  Frame of a traceback.
     |
     |  Methods defined here:
     |
     |  __eq__(self, other)
     |      Return self==value.
     |
     |  __ge__(self, other) from functools
     |      Return a >= b.  Computed by @total_ordering from (not a < b).
     |
     |  __gt__(self, other) from functools
     |      Return a > b.  Computed by @total_ordering from (not a < b) and (a != b).
     |
     |  __hash__(self)
     |      Return hash(self).
     |
     |  __init__(self, frame)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __le__(self, other) from functools
     |      Return a <= b.  Computed by @total_ordering from (a < b) or (a == b).
     |
     |  __lt__(self, other)
     |      Return self<value.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __str__(self)
     |      Return str(self).
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  filename
     |
     |  lineno

    class Snapshot(builtins.object)
     |  Snapshot(traces, traceback_limit)
     |
     |  Snapshot of traces of memory blocks allocated by Python.
     |
     |  Methods defined here:
     |
     |  __init__(self, traces, traceback_limit)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  compare_to(self, old_snapshot, key_type, cumulative=False)
     |      Compute the differences with an old snapshot old_snapshot. Get
     |      statistics as a sorted list of StatisticDiff instances, grouped by
     |      group_by.
     |
     |  dump(self, filename)
     |      Write the snapshot into a file.
     |
     |  filter_traces(self, filters)
     |      Create a new Snapshot instance with a filtered traces sequence, filters
     |      is a list of Filter or DomainFilter instances.  If filters is an empty
     |      list, return a new Snapshot instance with a copy of the traces.
     |
     |  statistics(self, key_type, cumulative=False)
     |      Group statistics by key_type. Return a sorted list of Statistic
     |      instances.
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  load(filename)
     |      Load a snapshot from a file.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class Statistic(builtins.object)
     |  Statistic(traceback, size, count)
     |
     |  Statistic difference on memory allocations between two Snapshot instance.
     |
     |  Methods defined here:
     |
     |  __eq__(self, other)
     |      Return self==value.
     |
     |  __hash__(self)
     |      Retu
```

## Related

Other standard-library modules pair well with `tracemalloc`; explore the `python` domain of this catalog.
