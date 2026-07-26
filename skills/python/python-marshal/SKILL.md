---
name: python-marshal
description: "Program with Python's marshal module: This module contains functions that can read and write Python values in a binary format."
version: 1.0.0
tags: [marshal, programming, python, stdlib]
---

# Python: `marshal`

## Overview

This module contains functions that can read and write Python values in
a binary format. The format is specific to Python, but independent of
machine architecture issues.

Not all Python object types are supported; in general, only objects
whose value is independent from a particular invocation of Python can be
written and read by this module. The following types are supported:
None, integers, floating-point numbers, strings, bytes, bytearrays,
tuples, lists, sets, dictionaries, and code objects, where it
should be understood that tuples, lists and dictionaries are only
supported as long as the values contained therein are themselves
supported; and recursive lists and dictionaries should not be written
(they will cause infinite loops).

Variables:

version -- indicates the format that the module uses. Version 0 is the
    historical format, version 1 shares interned strings and version 2
    uses a binary format for floating-point numbers.
    Version 3 shares common object references (New in version 3.4).

Functions:

dump() -- write value to a file
load() -- read value from a file
dumps() -- marshal value as a bytes object
loads() -- read value from a bytes-like object

## When to use

Reach for `marshal` when your task calls for This module contains functions that can read and write Python values in a binary format. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import marshal
```

## Key functions

- `marshal.dump(value, file, version=5, /, *, allow_code=True)`
- `marshal.dumps(value, version=5, /, *, allow_code=True)`
- `marshal.load(file, /, *, allow_code=True)`
- `marshal.loads(bytes, /, *, allow_code=True)`

## Constants / attributes

`version`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import marshal

def do_work(...):
    """Use marshal to accomplish one well-defined task."""
    result = marshal.dump(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `marshal` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: built-in module marshal

NAME
    marshal

MODULE REFERENCE
    https://docs.python.org/3.14/library/marshal.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module contains functions that can read and write Python values in
    a binary format. The format is specific to Python, but independent of
    machine architecture issues.

    Not all Python object types are supported; in general, only objects
    whose value is independent from a particular invocation of Python can be
    written and read by this module. The following types are supported:
    None, integers, floating-point numbers, strings, bytes, bytearrays,
    tuples, lists, sets, dictionaries, and code objects, where it
    should be understood that tuples, lists and dictionaries are only
    supported as long as the values contained therein are themselves
    supported; and recursive lists and dictionaries should not be written
    (they will cause infinite loops).

    Variables:

    version -- indicates the format that the module uses. Version 0 is the
        historical format, version 1 shares interned strings and version 2
        uses a binary format for floating-point numbers.
        Version 3 shares common object references (New in version 3.4).

    Functions:

    dump() -- write value to a file
    load() -- read value from a file
    dumps() -- marshal value as a bytes object
    loads() -- read value from a bytes-like object

FUNCTIONS
    dump(value, file, version=5, /, *, allow_code=True)
        Write the value on the open file.

          value
            Must be a supported type.
          file
            Must be a writeable binary file.
          version
            Indicates the data format that dump should use.
          allow_code
            Allow to write code objects.

        If the value has (or contains an object that has) an unsupported type, a
        ValueError exception is raised - but garbage data will also be written
        to the file. The object will not be properly read back by load().

    dumps(value, version=5, /, *, allow_code=True)
        Return the bytes object that would be written to a file by dump(value, file).

          value
            Must be a supported type.
          version
            Indicates the data format that dumps should use.
          allow_code
            Allow to write code objects.

        Raise a ValueError exception if value has (or contains an object that has) an
        unsupported type.

    load(file, /, *, allow_code=True)
        Read one value from the open file and return it.

          file
            Must be readable binary file.
          allow_code
            Allow to load code objects.

        If no valid value is read (e.g. because the data has a different Python
        version's incompatible marshal format), raise EOFError, ValueError or
        TypeError.

        Note: If an object containing an unsupported type was marshalled with
        dump(), load() will substitute None for the unmarshallable type.

    loads(bytes, /, *, allow_code=True)
        Convert the bytes-like object to a value.

          allow_code
            Allow to load code objects.

        If no valid value is found, raise EOFError, ValueError or TypeError.  Extra
        bytes in the input are ignored.

DATA
    version = 5

FILE
    (built-in)


```

## Related

Other standard-library modules pair well with `marshal`; explore the `python` domain of this catalog.
