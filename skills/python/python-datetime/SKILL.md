---
name: python-datetime
description: "Program with Python's datetime module: Specific date/time and related types."
version: 1.0.0
tags: [datetime, programming, python, stdlib]
---

# Python: `datetime`

## Overview

Specific date/time and related types.

See https://data.iana.org/time-zones/tz-link.html for
time zone and DST data sources.

## When to use

Reach for `datetime` when your task calls for Specific date/time and related types. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import datetime
```

## Key classes

`date`, `datetime`, `time`, `timedelta`, `timezone`, `tzinfo`

## Constants / attributes

`MAXYEAR`, `MINYEAR`, `UTC`, `datetime_CAPI`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import datetime

def do_work(...):
    """Use datetime to accomplish one well-defined task."""
    result = datetime.date(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `datetime` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module datetime

NAME
    datetime - Specific date/time and related types.

MODULE REFERENCE
    https://docs.python.org/3.14/library/datetime.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    See https://data.iana.org/time-zones/tz-link.html for
    time zone and DST data sources.

CLASSES
    builtins.object
        date
            datetime
        time
        timedelta
        tzinfo
            timezone

    class date(builtins.object)
     |  date(year, month, day) --> date object
     |
     |  Methods defined here:
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __format__(...)
     |      Formats self with strftime.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __radd__(self, value, /)
     |      Return value+self.
     |
     |  __reduce__(self, /)
     |      __reduce__() -> (cls, state)
     |
     |  __replace__(self, /, **changes)
     |      The same as replace().
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __rsub__(self, value, /)
     |      Return value-self.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  __sub__(self, value, /)
     |      Return self-value.
     |
     |  ctime(self, /)
     |      Return ctime() style string.
     |
     |  isocalendar(self, /)
     |      Return a named tuple containing ISO year, week number, and weekday.
     |
     |  isoformat(self, /)
     |      Return string in ISO 8601 format, YYYY-MM-DD.
     |
     |  isoweekday(self, /)
     |      Return the day of the week represented by the date.
     |      Monday == 1 ... Sunday == 7
     |
     |  replace(self, /, year=unchanged, month=unchanged, day=unchanged)
     |      Return date with new specified fields.
     |
     |  strftime(...)
     |      format -> strftime() style string.
     |
     |  timetuple(self, /)
     |      Return time tuple, compatible with time.localtime().
     |
     |  toordinal(self, /)
     |      Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.
     |
     |  weekday(self, /)
     |      Return the day of the week represented by the date.
     |      Monday == 0 ... Sunday == 6
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  fromisocalendar(...)
     |      int, int, int -> Construct a date from the ISO year, week number and weekday.
     |
     |      This is the inverse of the date.isocalendar() function
     |
     |  fromisoformat(object, /)
     |      str -> Construct a date from a string in ISO 8601 format.
     |
     |  fromordinal(...)
     |      int -> date corresponding to a proleptic Gregorian ordinal.
     |
     |  fromtimestamp(timestamp, /)
     |      Create a date from a POSIX timestamp.
     |
     |      The timestamp is a number, e.g. created via time.time(), that is interpreted
     |      as local time.
     |
     |  strptime(...)
     |      string, format -> new date parsed from a string (like time.strptime()).
     |
     |  today()
     |      Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).
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
     |  day
     |
     |  month
     |
     |  year
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  max = datetime.date(9999, 12, 31)
     |
     |  min = datetime.date(1, 1, 1)
     |
     |  resolution = datetime.timedelta(days=1)

    class datetime(date)
     |  datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
     |
     |  The year, month and day arguments are required. tzinfo may be None, or an
     |  instance of a tzinfo subclass. The remaining arguments may be ints.
     |
     |  Method resolution order:
     |      datetime
     |      date
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __radd__(self, value, /)
     |      Return value+self.
     |
     |  __reduce__(self, /)
     |      __reduce__() -> (cls, state)
     |
     |  __reduce_ex__(...)
     |      __reduce_ex__(proto) -> (cls, state)
     |
     |  __replace__(self, /, **changes)
     |      The same as replace().
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     | 
```

## Related

Other standard-library modules pair well with `datetime`; explore the `python` domain of this catalog.
