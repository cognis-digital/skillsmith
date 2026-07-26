---
name: python-cprofile
description: "Program with Python's cProfile module: Python interface for the 'lsprof' profiler."
version: 1.0.0
tags: [cprofile, programming, python, stdlib]
---

# Python: `cProfile`

## Overview

Python interface for the 'lsprof' profiler.
Compatible with the 'profile' module.

## When to use

Reach for `cProfile` when your task calls for Python interface for the 'lsprof' profiler. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import cProfile
```

## Key functions

- `cProfile.label(code)`
- `cProfile.main()`
- `cProfile.run(statement, filename=None, sort=-1)`
- `cProfile.runctx(statement, globals, locals, filename=None, sort=-1)`

## Key classes

`Profile`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import cProfile

def do_work(...):
    """Use cProfile to accomplish one well-defined task."""
    result = cProfile.label(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `cProfile` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module cProfile

NAME
    cProfile

MODULE REFERENCE
    https://docs.python.org/3.14/library/cprofile.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Python interface for the 'lsprof' profiler.
    Compatible with the 'profile' module.

CLASSES
    _lsprof.Profiler(builtins.object)
        Profile

    class Profile(_lsprof.Profiler)
     |  Profile(timer=None, timeunit=0.0, subcalls=True, builtins=True)
     |
     |  Profile(timer=None, timeunit=None, subcalls=True, builtins=True)
     |
     |  Builds a profiler object using the specified timer function.
     |  The default timer is a fast built-in one based on real time.
     |  For custom timer functions returning integers, timeunit can
     |  be a float specifying a scale (i.e. how long each integer unit
     |  is, in seconds).
     |
     |  Method resolution order:
     |      Profile
     |      _lsprof.Profiler
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __enter__(self)
     |
     |  __exit__(self, *exc_info)
     |
     |  create_stats(self)
     |
     |  dump_stats(self, file)
     |
     |  print_stats(self, sort=-1)
     |
     |  run(self, cmd)
     |
     |  runcall(self, func, /, *args, **kw)
     |      # This method is more useful to profile a single function call.
     |
     |  runctx(self, cmd, globals, locals)
     |
     |  snapshot_stats(self)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from _lsprof.Profiler:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  clear(self, /)
     |      Clear all profiling information collected so far.
     |
     |  disable(self, /)
     |      Stop collecting profiling information.
     |
     |  enable(self, /, subcalls=True, builtins=True)
     |      Start collecting profiling information.
     |
     |      subcalls
     |        If True, also records for each function
     |        statistics separated according to its current caller.
     |      builtins
     |        If True, records the time spent in
     |        built-in functions separately from their caller.
     |
     |  getstats(self, /)
     |      list of profiler_entry objects.
     |
     |      getstats() -> list of profiler_entry objects
     |
     |      Return all information collected by the profiler.
     |      Each profiler_entry is a tuple-like object with the
     |      following attributes:
     |
     |          code          code object
     |          callcount     how many times this was called
     |          reccallcount  how many times called recursively
     |          totaltime     total time in this entry
     |          inlinetime    inline time in this entry (not in subcalls)
     |          calls         details of the calls
     |
     |      The calls attribute is either None or a list of
     |      profiler_subentry objects:
     |
     |          code          called code object
     |          callcount     how many times this is called
     |          reccallcount  how many times this is called recursively
     |          totaltime     total time spent in this call
     |          inlinetime    inline time (not in further subcalls)

FUNCTIONS
    run(statement, filename=None, sort=-1)
        Run statement under profiler optionally saving results in filename

        This function takes a single argument that can be passed to the
        "exec" statement, and an optional file name.  In all cases this
        routine attempts to "exec" its first argument and gather profiling
        statistics from the execution. If no file name is present, then this
        function automatically prints a simple profiling report, sorted by the
        standard name string (file/line/function-name) that is presented in
        each line.

    runctx(statement, globals, locals, filename=None, sort=-1)
        Run statement under profiler, supplying your own globals and locals,
        optionally saving results in filename.

        statement and filename have the same semantics as profile.run

DATA
    __all__ = ['run', 'runctx', 'Profile']

FILE
    c:\python314\lib\cprofile.py


```

## Related

Other standard-library modules pair well with `cProfile`; explore the `python` domain of this catalog.
