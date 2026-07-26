---
name: python-pprint
description: "Program with Python's pprint module: Support to pretty-print lists, tuples, & dictionaries recursively."
version: 1.0.0
tags: [pprint, programming, python, stdlib]
---

# Python: `pprint`

## Overview

Support to pretty-print lists, tuples, & dictionaries recursively.

Very simple, but useful, especially in debugging data structures.

Classes
-------

PrettyPrinter()
    Handle pretty-printing operations onto a stream using a configured
    set of formatting parameters.

Functions
---------

pformat()
    Format a Python object into a pretty-printed representation.

pprint()
    Pretty-print a Python object to a stream [default is sys.stdout].

saferepr()
    Generate a 'standard' repr()-like value, but protect against recursive
    data structures.

## When to use

Reach for `pprint` when your task calls for Support to pretty-print lists, tuples, & dictionaries recursively. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import pprint
```

## Key functions

- `pprint.isreadable(object)`
- `pprint.isrecursive(object)`
- `pprint.pformat(object, indent=1, width=80, depth=None, *, compact=False, sort_dicts=True, underscore_numbers=False)`
- `pprint.pp(object, *args, sort_dicts=False, **kwargs)`
- `pprint.pprint(object, stream=None, indent=1, width=80, depth=None, *, compact=False, sort_dicts=True, underscore_numbers=False)`
- `pprint.saferepr(object)`

## Key classes

`PrettyPrinter`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import pprint

def do_work(...):
    """Use pprint to accomplish one well-defined task."""
    result = pprint.isreadable(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `pprint` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module pprint

NAME
    pprint - Support to pretty-print lists, tuples, & dictionaries recursively.

MODULE REFERENCE
    https://docs.python.org/3.14/library/pprint.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Very simple, but useful, especially in debugging data structures.

    Classes
    -------

    PrettyPrinter()
        Handle pretty-printing operations onto a stream using a configured
        set of formatting parameters.

    Functions
    ---------

    pformat()
        Format a Python object into a pretty-printed representation.

    pprint()
        Pretty-print a Python object to a stream [default is sys.stdout].

    saferepr()
        Generate a 'standard' repr()-like value, but protect against recursive
        data structures.

CLASSES
    builtins.object
        PrettyPrinter

    class PrettyPrinter(builtins.object)
     |  PrettyPrinter(
     |      indent=1,
     |      width=80,
     |      depth=None,
     |      stream=None,
     |      *,
     |      compact=False,
     |      sort_dicts=True,
     |      underscore_numbers=False
     |  )
     |
     |  Methods defined here:
     |
     |  __init__(
     |      self,
     |      indent=1,
     |      width=80,
     |      depth=None,
     |      stream=None,
     |      *,
     |      compact=False,
     |      sort_dicts=True,
     |      underscore_numbers=False
     |  )
     |      Handle pretty printing operations onto a stream using a set of
     |      configured parameters.
     |
     |      indent
     |          Number of spaces to indent for each level of nesting.
     |
     |      width
     |          Attempted maximum number of columns in the output.
     |
     |      depth
     |          The maximum depth to print out nested structures.
     |
     |      stream
     |          The desired output stream.  If omitted (or false), the standard
     |          output stream available at construction will be used.
     |
     |      compact
     |          If true, several items will be combined in one line.
     |
     |      sort_dicts
     |          If true, dict keys are sorted.
     |
     |      underscore_numbers
     |          If true, digit groups are separated with underscores.
     |
     |  format(self, object, context, maxlevels, level)
     |      Format object for a specific context, returning a string
     |      and flags indicating whether the representation is 'readable'
     |      and whether the object represents a recursive construct.
     |
     |  isreadable(self, object)
     |
     |  isrecursive(self, object)
     |
     |  pformat(self, object)
     |
     |  pprint(self, object)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

FUNCTIONS
    isreadable(object)
        Determine if saferepr(object) is readable by eval().

    isrecursive(object)
        Determine if object requires a recursive representation.

    pformat(
        object,
        indent=1,
        width=80,
        depth=None,
        *,
        compact=False,
        sort_dicts=True,
        underscore_numbers=False
    )
        Format a Python object into a pretty-printed representation.

    pp(object, *args, sort_dicts=False, **kwargs)
        Pretty-print a Python object

    pprint(
        object,
        stream=None,
        indent=1,
        width=80,
        depth=None,
        *,
        compact=False,
        sort_dicts=True,
        underscore_numbers=False
    )
        Pretty-print a Python object to a stream [default is sys.stdout].

    saferepr(object)
        Version of repr() which can handle recursive data structures.

DATA
    __all__ = ['pprint', 'pformat', 'isreadable', 'isrecursive', 'saferepr...

FILE
    c:\python314\lib\pprint.py


```

## Related

Other standard-library modules pair well with `pprint`; explore the `python` domain of this catalog.
