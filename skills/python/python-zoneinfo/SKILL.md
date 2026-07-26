---
name: python-zoneinfo
description: "Program with Python's zoneinfo module: The Python standard-library module `zoneinfo`."
version: 1.0.0
tags: [programming, python, stdlib, zoneinfo]
---

# Python: `zoneinfo`

## Overview

`zoneinfo` is part of the Python standard library.

## When to use

Reach for `zoneinfo` when your task calls for The Python standard-library module `zoneinfo`. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import zoneinfo
```

## Key functions

- `zoneinfo.available_timezones()`
- `zoneinfo.reset_tzpath(to=None)`

## Key classes

`InvalidTZPathWarning`, `ZoneInfo`, `ZoneInfoNotFoundError`

## Constants / attributes

`TZPATH`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import zoneinfo

def do_work(...):
    """Use zoneinfo to accomplish one well-defined task."""
    result = zoneinfo.available_timezones(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `zoneinfo` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: package zoneinfo

NAME
    zoneinfo

MODULE REFERENCE
    https://docs.python.org/3.14/library/zoneinfo.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

PACKAGE CONTENTS
    _common
    _tzpath
    _zoneinfo

CLASSES
    builtins.KeyError(builtins.LookupError)
        zoneinfo._common.ZoneInfoNotFoundError
    builtins.RuntimeWarning(builtins.Warning)
        zoneinfo._tzpath.InvalidTZPathWarning
    datetime.tzinfo(builtins.object)
        ZoneInfo

    class InvalidTZPathWarning(builtins.RuntimeWarning)
     |  Warning raised if an invalid path is specified in PYTHONTZPATH.
     |
     |  Method resolution order:
     |      InvalidTZPathWarning
     |      builtins.RuntimeWarning
     |      builtins.Warning
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors defined here:
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.RuntimeWarning:
     |
     |  __new__(*args, **kwargs) class method of builtins.RuntimeWarning
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__(self, /)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setstate__(self, state, /)
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  add_note(self, note, /)
     |      Add a note to the exception
     |
     |  with_traceback(self, tb, /)
     |      Set self.__traceback__ to tb and return self.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |
     |  __cause__
     |
     |  __context__
     |
     |  __dict__
     |
     |  __suppress_context__
     |
     |  __traceback__
     |
     |  args

    class ZoneInfo(datetime.tzinfo)
     |  Method resolution order:
     |      ZoneInfo
     |      datetime.tzinfo
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __reduce__(self, /)
     |      Function for serialization with the pickle protocol.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  dst(self, dt, /)
     |      Retrieve a timedelta representing the amount of DST applied in a zone at the given datetime.
     |
     |  fromutc(self, object, /)
     |      Given a datetime with local time in UTC, retrieve an adjusted datetime in local time.
     |
     |  tzname(self, dt, /)
     |      Retrieve a string containing the abbreviation for the time zone that applies in a zone at a given datetime.
     |
     |  utcoffset(self, dt, /)
     |      Retrieve a timedelta representing the UTC offset in a zone at the given datetime.
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  __init_subclass__(...)
     |      Function to initialize subclasses.
     |
     |  clear_cache(*, only_keys=None)
     |
     |  from_file(file_obj, /, key=None)
     |
     |  no_cache(key)
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs)
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  key

    class ZoneInfoNotFoundError(builtins.KeyError)
     |  Exception raised when a ZoneInfo key is not found.
     |
     |  Method resolution order:
     |      ZoneInfoNotFoundError
     |      builtins.KeyError
     |      builtins.LookupError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors defined here:
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.KeyError:
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.LookupError:
     |
     |  __new__(*args, **kwargs) class method of builtins.LookupError
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__(self, /)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setstate__(self, state, /)
     |
     |  add_note(self, note, /)
     |      Add a note to the exception
     |
     |  with_traceback(self, tb, /)
     |      Set self.__traceback__ to tb and return self.
     |
     |  ---------------------------------------------------------------
```

## Related

Other standard-library modules pair well with `zoneinfo`; explore the `python` domain of this catalog.
