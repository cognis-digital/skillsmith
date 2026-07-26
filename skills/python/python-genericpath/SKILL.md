---
name: python-genericpath
description: "Program with Python's genericpath module: Path operations common to more than one OS Do not use directly."
version: 1.0.0
tags: [genericpath, programming, python, stdlib]
---

# Python: `genericpath`

## Overview

Path operations common to more than one OS
Do not use directly.  The OS specific modules import the appropriate
functions from this module themselves.

## When to use

Reach for `genericpath` when your task calls for Path operations common to more than one OS Do not use directly. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import genericpath
```

## Key functions

- `genericpath.commonprefix(m)`
- `genericpath.exists(path)`
- `genericpath.getatime(filename)`
- `genericpath.getctime(filename)`
- `genericpath.getmtime(filename)`
- `genericpath.getsize(filename)`
- `genericpath.isdevdrive(path)`
- `genericpath.isdir(s)`
- `genericpath.isfile(path)`
- `genericpath.isjunction(path)`
- `genericpath.islink(path)`
- `genericpath.lexists(path)`
- `genericpath.samefile(f1, f2)`
- `genericpath.sameopenfile(fp1, fp2)`
- `genericpath.samestat(s1, s2)`

## Constants / attributes

`ALLOW_MISSING`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import genericpath

def do_work(...):
    """Use genericpath to accomplish one well-defined task."""
    result = genericpath.commonprefix(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `genericpath` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module genericpath

NAME
    genericpath

MODULE REFERENCE
    https://docs.python.org/3.14/library/genericpath.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Path operations common to more than one OS
    Do not use directly.  The OS specific modules import the appropriate
    functions from this module themselves.

FUNCTIONS
    commonprefix(m)
        Given a list of pathnames, returns the longest common leading component

    exists(path)
        Test whether a path exists.  Returns False for broken symbolic links

    getatime(filename)
        Return the last access time of a file, reported by os.stat().

    getctime(filename)
        Return the metadata change time of a file, reported by os.stat().

    getmtime(filename)
        Return the last modification time of a file, reported by os.stat().

    getsize(filename)
        Return the size of a file, reported by os.stat().

    isdevdrive(path)
        Determines whether the specified path is on a Windows Dev Drive.
        Dev Drives are not supported on the current platform

    isdir(s)
        Return true if the pathname refers to an existing directory.

    isfile(path)
        Test whether a path is a regular file

    isjunction(path)
        Test whether a path is a junction
        Junctions are not supported on the current platform

    islink(path)
        Test whether a path is a symbolic link

    lexists(path)
        Test whether a path exists.  Returns True for broken symbolic links

    samefile(f1, f2)
        Test whether two pathnames reference the same actual file or directory

        This is determined by the device number and i-node number and
        raises an exception if an os.stat() call on either pathname fails.

    sameopenfile(fp1, fp2)
        Test whether two open file objects reference the same file

    samestat(s1, s2)
        Test whether two stat buffers reference the same file

DATA
    ALLOW_MISSING = os.path.ALLOW_MISSING
    __all__ = ['commonprefix', 'exists', 'getatime', 'getctime', 'getmtime...

FILE
    c:\python314\lib\genericpath.py


```

## Related

Other standard-library modules pair well with `genericpath`; explore the `python` domain of this catalog.
