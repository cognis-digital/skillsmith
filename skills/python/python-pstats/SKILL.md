---
name: python-pstats
description: "Program with Python's pstats module: Class for printing reports on profiled python code."
version: 1.0.0
tags: [programming, pstats, python, stdlib]
---

# Python: `pstats`

## Overview

Class for printing reports on profiled python code.

## When to use

Reach for `pstats` when your task calls for Class for printing reports on profiled python code. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import pstats
```

## Key functions

- `pstats.add_callers(target, source)`
- `pstats.add_func_stats(target, source)`
- `pstats.cmp_to_key(mycmp)`
- `pstats.count_calls(callers)`
- `pstats.dataclass(cls=None, /, *, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=False, weakref_slot=False)`
- `pstats.f8(x)`
- `pstats.func_get_function_name(func)`
- `pstats.func_std_string(func_name)`
- `pstats.func_strip_path(func_name)`

## Key classes

`FunctionProfile`, `SortKey`, `Stats`, `StatsProfile`, `StrEnum`, `TupleComp`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import pstats

def do_work(...):
    """Use pstats to accomplish one well-defined task."""
    result = pstats.add_callers(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `pstats` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module pstats

NAME
    pstats - Class for printing reports on profiled python code.

MODULE REFERENCE
    https://docs.python.org/3.14/library/pstats.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.object
        FunctionProfile
        Stats
        StatsProfile
    enum.StrEnum(builtins.str, enum.ReprEnum)
        SortKey

    class FunctionProfile(builtins.object)
     |  FunctionProfile(
     |      ncalls: __dataclass_type_ncalls__,
     |      tottime: __dataclass_type_tottime__,
     |      percall_tottime: __dataclass_type_percall_tottime__,
     |      cumtime: __dataclass_type_cumtime__,
     |      percall_cumtime: __dataclass_type_percall_cumtime__,
     |      file_name: __dataclass_type_file_name__,
     |      line_number: __dataclass_type_line_number__
     |  ) -> __dataclass___init___return_type__
     |
     |  FunctionProfile(ncalls: str, tottime: float, percall_tottime: float, cumtime: float, percall_cumtime: float, file_name: str, line_number: int)
     |
     |  Methods defined here:
     |
     |  __eq__(self, other)
     |      Return self==value.
     |
     |  __hash__(self)
     |      Return hash(self).
     |
     |  __init__(
     |      self,
     |      ncalls: __dataclass_type_ncalls__,
     |      tottime: __dataclass_type_tottime__,
     |      percall_tottime: __dataclass_type_percall_tottime__,
     |      cumtime: __dataclass_type_cumtime__,
     |      percall_cumtime: __dataclass_type_percall_cumtime__,
     |      file_name: __dataclass_type_file_name__,
     |      line_number: __dataclass_type_line_number__
     |  ) -> __dataclass___init___return_type__
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __replace__ = _replace(self, /, **changes) from dataclasses
     |
     |  __repr__(self)
     |      Return repr(self).
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
     |  Data and other attributes defined here:
     |
     |  __dataclass_fields__ = {'cumtime': Field(name='cumtime',type=<class 'f...
     |
     |  __dataclass_params__ = _DataclassParams(init=True,repr=True,eq=True,or...
     |
     |  __match_args__ = ('ncalls', 'tottime', 'percall_tottime', 'cumtime', '...

    class SortKey(enum.StrEnum)
     |  SortKey(*values)
     |
     |  An enumeration.
     |
     |  Method resolution order:
     |      SortKey
     |      enum.StrEnum
     |      builtins.str
     |      enum.ReprEnum
     |      enum.Enum
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __format__(self, format_spec, /) from builtins.str
     |      Return a formatted version of the string as described by format_spec.
     |
     |  __new__(cls, value) from enum.Enum
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  __str__(self, /) from builtins.str
     |      Return str(self).
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  CALLS = <SortKey.CALLS: 'calls'>
     |
     |  CUMULATIVE = <SortKey.CUMULATIVE: 'cumulative'>
     |
     |  FILENAME = <SortKey.FILENAME: 'filename'>
     |
     |  LINE = <SortKey.LINE: 'line'>
     |
     |  NAME = <SortKey.NAME: 'name'>
     |
     |  NFL = <SortKey.NFL: 'nfl'>
     |
     |  PCALLS = <SortKey.PCALLS: 'pcalls'>
     |
     |  STDNAME = <SortKey.STDNAME: 'stdname'>
     |
     |  TIME = <SortKey.TIME: 'time'>
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from enum.StrEnum:
     |
     |  __repr__(self) from enum.Enum
     |      Return repr(self).
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.str:
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __contains__(self, key, /)
     |      Return bool(key in self).
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getitem__(self, key, /)
     |      Return self[key].
     |
     |  __getnewargs__(self, /)
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __len__(self, /)
     |      Return len(self).
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __mod__(self, value, /)
     |      Return self%value.
     |
     |  __mul__(self, value, /)
     |      Return self*value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __rmod__(self, value, /)
     |      Return value%self.
     |
     |  __rmul__(self, value, /)
     |      Return value*self.
     |
     |  __sizeof__(self, /)
     |      Return the size of the string in memory, in bytes.
     |
     |  capitalize(self, /)
     |      Return a capitalized version of the string.
     |
     |      More specifically, make the first character have upper case and the rest lower
     |      case.
     |
     |  casefold(self, /)
     |      Return a version of the string suitable for caseless comparis
```

## Related

Other standard-library modules pair well with `pstats`; explore the `python` domain of this catalog.
