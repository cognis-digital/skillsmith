---
name: python-plistlib
description: "Program with Python's plistlib module: plistlib.py -- a tool to generate and parse MacOSX .plist files."
version: 1.0.0
tags: [plistlib, programming, python, stdlib]
---

# Python: `plistlib`

## Overview

plistlib.py -- a tool to generate and parse MacOSX .plist files.

The property list (.plist) file format is a simple XML pickle supporting
basic object types, like dictionaries, lists, numbers and strings.
Usually the top level object is a dictionary.

To write out a plist file, use the dump(value, file)
function. 'value' is the top level object, 'file' is
a (writable) file object.

To parse a plist from a file, use the load(file) function,
with a (readable) file object as the only argument. It
returns the top level object (again, usually a dictionary).

To work with plist data in bytes objects, you can use loads()
and dumps().

Values can be strings, integers, floats, booleans, tuples, lists,
dictionaries (but only with string keys), Data, bytes, bytearray, or
datetime.datetime objects.

Generate Plist example:

    import datetime
    import plistlib

    pl = dict(
        aString = "Doodah",
        aList = ["A", "B", 12, 32.1, [1, 2, 3]],
        aFloat = 0.1,
        anInt = 728,
        aDict = dict(
            anotherString = "<hello & hi there!>",
            aThirdString = "M\xe4ssig, Ma\xdf",
            aTrueValue = True,
            aFalseValue = False,
        ),
        someData = b"<binary gunk>",
        someMoreData = b"<lots of binary gunk>" * 10,
        aDate = datetime.datetime.now()
    )
    print(plistlib.dumps(pl).decode())

Parse Plist example:

    import plistlib

    plist = b'''<plist version="1.0">
    <dict>
        <key>foo</key>
        <string>bar</string>
    </dict>
    </plist>'''
    pl = plistlib.loads(plist)
    print(pl["foo"])

## When to use

Reach for `plistlib` when your task calls for plistlib.py -- a tool to generate and parse MacOSX .plist files. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import plistlib
```

## Key functions

- `plistlib.ParserCreate(...)`
- `plistlib.dump(value, fp, *, fmt=<PlistFormat.FMT_XML: 1>, sort_keys=True, skipkeys=False, aware_datetime=False)`
- `plistlib.dumps(value, *, fmt=<PlistFormat.FMT_XML: 1>, skipkeys=False, sort_keys=True, aware_datetime=False)`
- `plistlib.load(fp, *, fmt=None, dict_type=<class 'dict'>, aware_datetime=False)`
- `plistlib.loads(value, *, fmt=None, dict_type=<class 'dict'>, aware_datetime=False)`

## Key classes

`BytesIO`, `InvalidFileException`, `PlistFormat`, `UID`

## Constants / attributes

`FMT_BINARY`, `FMT_XML`, `PLISTHEADER`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import plistlib

def do_work(...):
    """Use plistlib to accomplish one well-defined task."""
    result = plistlib.ParserCreate(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `plistlib` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module plistlib

NAME
    plistlib - plistlib.py -- a tool to generate and parse MacOSX .plist files.

MODULE REFERENCE
    https://docs.python.org/3.14/library/plistlib.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    The property list (.plist) file format is a simple XML pickle supporting
    basic object types, like dictionaries, lists, numbers and strings.
    Usually the top level object is a dictionary.

    To write out a plist file, use the dump(value, file)
    function. 'value' is the top level object, 'file' is
    a (writable) file object.

    To parse a plist from a file, use the load(file) function,
    with a (readable) file object as the only argument. It
    returns the top level object (again, usually a dictionary).

    To work with plist data in bytes objects, you can use loads()
    and dumps().

    Values can be strings, integers, floats, booleans, tuples, lists,
    dictionaries (but only with string keys), Data, bytes, bytearray, or
    datetime.datetime objects.

    Generate Plist example:

        import datetime
        import plistlib

        pl = dict(
            aString = "Doodah",
            aList = ["A", "B", 12, 32.1, [1, 2, 3]],
            aFloat = 0.1,
            anInt = 728,
            aDict = dict(
                anotherString = "<hello & hi there!>",
                aThirdString = "M\xe4ssig, Ma\xdf",
                aTrueValue = True,
                aFalseValue = False,
            ),
            someData = b"<binary gunk>",
            someMoreData = b"<lots of binary gunk>" * 10,
            aDate = datetime.datetime.now()
        )
        print(plistlib.dumps(pl).decode())

    Parse Plist example:

        import plistlib

        plist = b'''<plist version="1.0">
        <dict>
            <key>foo</key>
            <string>bar</string>
        </dict>
        </plist>'''
        pl = plistlib.loads(plist)
        print(pl["foo"])

CLASSES
    builtins.ValueError(builtins.Exception)
        InvalidFileException
    builtins.object
        UID

    class InvalidFileException(builtins.ValueError)
     |  InvalidFileException(message='Invalid file')
     |
     |  Method resolution order:
     |      InvalidFileException
     |      builtins.ValueError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, message='Invalid file')
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.ValueError:
     |
     |  __new__(*args, **kwargs) class method of builtins.ValueError
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
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

    class UID(builtins.object)
     |  UID(data)
     |
     |  Methods defined here:
     |
     |  __eq__(self, other)
     |      Return self==value.
     |
     |  __hash__(self)
     |      Return hash(self).
     |
     |  __index__(self)
     |
     |  __init__(self, data)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__(self)
     |      Helper for pickle.
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

FUNCTIONS
    dump(
        value,
        fp,
        *,
        fmt=<PlistFormat.FMT_XML: 1>,
        sort_keys=True,
        skipkeys=False,
        aware_datetime=False
    )
        Write 'value' to a .plist file. 'fp' should be a writable,
        binary file object.

    dumps(
        value,
        *,
        fmt=<PlistFormat.FMT_XML: 1>,
        skipkeys=False,
        sort_keys=True,
        aware_datetime=False
    )
        Return a bytes object with the contents for a .plist file.

    load(fp, *, fmt=None, dict_type=<class 'dict'>, aware_datetime=False)
        Read a .plist file. 'fp' should be a readable and binary file object.
        Return the unpacked root object (which usually is a dictionary).

    loads(value, *, fmt=None, dict_type=<class 'dict'>, aware_datetime=False)
        Read a .plist file from a bytes object.
        Return the unpacked root object (which usually is a dictionary).

DATA
    FMT_BINARY = <PlistFormat.FMT_BINARY: 2>
    FMT_XML = <PlistFormat.FMT_XML: 1>
    __all__ = ['InvalidFile
```

## Related

Other standard-library modules pair well with `plistlib`; explore the `python` domain of this catalog.
