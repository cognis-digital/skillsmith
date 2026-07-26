---
name: python-calendar
description: "Program with Python's calendar module: Calendar printing functions Note when comparing these calendars to the ones printed by cal(1): By default, these calendars have Monday as the first day of the week, and Sunday as the last (the European convention)."
version: 1.0.0
tags: [calendar, programming, python, stdlib]
---

# Python: `calendar`

## Overview

Calendar printing functions

Note when comparing these calendars to the ones printed by cal(1): By
default, these calendars have Monday as the first day of the week, and
Sunday as the last (the European convention). Use setfirstweekday() to
set the first day of the week (0=Monday, 6=Sunday).

## When to use

Reach for `calendar` when your task calls for Calendar printing functions Note when comparing these calendars to the ones printed by cal(1): By default, these calenda. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import calendar
```

## Key functions

- `calendar.calendar(theyear, w=2, l=1, c=6, m=3)`
- `calendar.firstweekday()`
- `calendar.format(cols, colwidth=20, spacing=6)`
- `calendar.formatstring(cols, colwidth=20, spacing=6)`
- `calendar.global_enum(cls, update_str=False)`
- `calendar.isleap(year)`
- `calendar.leapdays(y1, y2)`
- `calendar.main(args=None)`
- `calendar.month(theyear, themonth, w=0, l=0)`
- `calendar.monthcalendar(year, month)`
- `calendar.monthrange(year, month)`
- `calendar.prcal(theyear, w=0, l=0, c=6, m=3)`
- `calendar.prmonth(theyear, themonth, w=0, l=0)`
- `calendar.prweek(theweek, width)`
- `calendar.setfirstweekday(firstweekday)`
- `calendar.timegm(tuple)`
- `calendar.week(theweek, width)`
- `calendar.weekday(year, month, day)`
- `calendar.weekheader(width)`

## Key classes

`Calendar`, `Day`, `HTMLCalendar`, `IllegalMonthError`, `IllegalWeekdayError`, `IntEnum`, `LocaleHTMLCalendar`, `LocaleTextCalendar`, `Month`, `TextCalendar`, `different_locale`, `error`, `repeat`

## Constants / attributes

`APRIL`, `AUGUST`, `DECEMBER`, `EPOCH`, `FEBRUARY`, `FRIDAY`, `JANUARY`, `JULY`, `JUNE`, `MARCH`, `MAY`, `MONDAY`, `NOVEMBER`, `OCTOBER`, `SATURDAY`, `SEPTEMBER`, `SUNDAY`, `THURSDAY`, `TUESDAY`, `WEDNESDAY`, `c`, `day_abbr`, `day_name`, `mdays`, `month_abbr`, `month_name`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import calendar

def do_work(...):
    """Use calendar to accomplish one well-defined task."""
    result = calendar.calendar(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `calendar` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module calendar

NAME
    calendar - Calendar printing functions

MODULE REFERENCE
    https://docs.python.org/3.14/library/calendar.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Note when comparing these calendars to the ones printed by cal(1): By
    default, these calendars have Monday as the first day of the week, and
    Sunday as the last (the European convention). Use setfirstweekday() to
    set the first day of the week (0=Monday, 6=Sunday).

CLASSES
    builtins.IndexError(builtins.LookupError)
        IllegalMonthError(builtins.ValueError, builtins.IndexError)
    builtins.ValueError(builtins.Exception)
        IllegalMonthError(builtins.ValueError, builtins.IndexError)
        IllegalWeekdayError
    builtins.object
        Calendar
            HTMLCalendar
                LocaleHTMLCalendar
            TextCalendar
                LocaleTextCalendar
    enum.IntEnum(builtins.int, enum.ReprEnum)
        Day
        Month

    class Calendar(builtins.object)
     |  Calendar(firstweekday=0)
     |
     |  Base calendar class. This class doesn't do any formatting. It simply
     |  provides data to subclasses.
     |
     |  Methods defined here:
     |
     |  __init__(self, firstweekday=0)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  getfirstweekday(self)
     |
     |  itermonthdates(self, year, month)
     |      Return an iterator for one month. The iterator will yield datetime.date
     |      values and will always iterate through complete weeks, so it will yield
     |      dates outside the specified month.
     |
     |  itermonthdays(self, year, month)
     |      Like itermonthdates(), but will yield day numbers. For days outside
     |      the specified month the day number is 0.
     |
     |  itermonthdays2(self, year, month)
     |      Like itermonthdates(), but will yield (day number, weekday number)
     |      tuples. For days outside the specified month the day number is 0.
     |
     |  itermonthdays3(self, year, month)
     |      Like itermonthdates(), but will yield (year, month, day) tuples.  Can be
     |      used for dates outside of datetime.date range.
     |
     |  itermonthdays4(self, year, month)
     |      Like itermonthdates(), but will yield (year, month, day, day_of_week) tuples.
     |      Can be used for dates outside of datetime.date range.
     |
     |  iterweekdays(self)
     |      Return an iterator for one week of weekday numbers starting with the
     |      configured first one.
     |
     |  monthdatescalendar(self, year, month)
     |      Return a matrix (list of lists) representing a month's calendar.
     |      Each row represents a week; week entries are datetime.date values.
     |
     |  monthdays2calendar(self, year, month)
     |      Return a matrix representing a month's calendar.
     |      Each row represents a week; week entries are
     |      (day number, weekday number) tuples. Day numbers outside this month
     |      are zero.
     |
     |  monthdayscalendar(self, year, month)
     |      Return a matrix representing a month's calendar.
     |      Each row represents a week; days outside this month are zero.
     |
     |  setfirstweekday(self, firstweekday)
     |
     |  yeardatescalendar(self, year, width=3)
     |      Return the data for the specified year ready for formatting. The return
     |      value is a list of month rows. Each month row contains up to width months.
     |      Each month contains between 4 and 6 weeks and each week contains 1-7
     |      days. Days are datetime.date objects.
     |
     |  yeardays2calendar(self, year, width=3)
     |      Return the data for the specified year ready for formatting (similar to
     |      yeardatescalendar()). Entries in the week lists are
     |      (day number, weekday number) tuples. Day numbers outside this month are
     |      zero.
     |
     |  yeardayscalendar(self, year, width=3)
     |      Return the data for the specified year ready for formatting (similar to
     |      yeardatescalendar()). Entries in the week lists are day numbers.
     |      Day numbers outside this month are zero.
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
     |  firstweekday

    class Day(enum.IntEnum)
     |  Day(*values)
     |
     |  # Constants for days
     |
     |  Method resolution order:
     |      Day
     |      enum.IntEnum
     |      builtins.int
     |      enum.ReprEnum
     |      enum.Enum
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __format__(self, format_spec, /) from builtins.int
     |      Convert to a string according to format_spec.
     |
     |  __new__(cls, value) from enum.Enum
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  __repr__ = global_enum_repr(self) from enum
     |      use module.enum_name instead of class.enum_name
     |
     |      the module is the last module in case of a multi-module name
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  FRIDAY = calendar.FRIDAY
     |
     |  MONDAY = calendar.MONDAY
     |
     |  SATURDAY = calendar.SATURDAY
     |
     |  SUNDAY = calendar.SUNDAY
     |
     |  THURSDAY = calendar.THURSDAY
     |
     |  TUESDAY = calendar.TUESDAY
     |
     |  WEDNESDAY = calendar.WEDNESDAY
   
```

## Related

Other standard-library modules pair well with `calendar`; explore the `python` domain of this catalog.
