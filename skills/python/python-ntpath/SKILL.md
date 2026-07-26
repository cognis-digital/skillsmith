---
name: python-ntpath
description: "Program with Python's ntpath module: Common pathname manipulations, WindowsNT/95 version."
version: 1.0.0
tags: [ntpath, programming, python, stdlib]
---

# Python: `ntpath`

## Overview

Common pathname manipulations, WindowsNT/95 version.

Instead of importing this module directly, import os and refer to this
module as os.path.

## When to use

Reach for `ntpath` when your task calls for Common pathname manipulations, WindowsNT/95 version. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import ntpath
```

## Key functions

- `ntpath.abspath(path)`
- `ntpath.basename(p)`
- `ntpath.commonpath(paths)`
- `ntpath.commonprefix(m)`
- `ntpath.dirname(p)`
- `ntpath.exists(path)`
- `ntpath.expanduser(path)`
- `ntpath.expandvars(path)`
- `ntpath.getatime(filename)`
- `ntpath.getctime(filename)`
- `ntpath.getmtime(filename)`
- `ntpath.getsize(filename)`
- `ntpath.isabs(s)`
- `ntpath.isdevdrive(path)`
- `ntpath.isdir(s)`
- `ntpath.isfile(path)`
- `ntpath.isjunction(path)`
- `ntpath.islink(path)`
- `ntpath.ismount(path)`
- `ntpath.isreserved(path)`
- `ntpath.join(path, *paths)`
- `ntpath.lexists(path)`
- `ntpath.normcase(s)`
- `ntpath.normpath(path)`
- `ntpath.realpath(path, *, strict=False)`
- `ntpath.relpath(path, start=None)`
- `ntpath.samefile(f1, f2)`
- `ntpath.sameopenfile(fp1, fp2)`
- `ntpath.samestat(s1, s2)`
- `ntpath.split(p)`

## Constants / attributes

`ALLOW_MISSING`, `altsep`, `curdir`, `defpath`, `devnull`, `extsep`, `pardir`, `pathsep`, `sep`, `supports_unicode_filenames`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import ntpath

def do_work(...):
    """Use ntpath to accomplish one well-defined task."""
    result = ntpath.abspath(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `ntpath` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module ntpath

NAME
    ntpath - Common pathname manipulations, WindowsNT/95 version.

MODULE REFERENCE
    https://docs.python.org/3.14/library/ntpath.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Instead of importing this module directly, import os and refer to this
    module as os.path.

FUNCTIONS
    abspath(path)
        Return the absolute version of a path.

    basename(p)
        Returns the final component of a pathname

    commonpath(paths)
        Given an iterable of path names, returns the longest common sub-path.

    commonprefix(m)
        Given a list of pathnames, returns the longest common leading component

    dirname(p)
        Returns the directory component of a pathname

    exists = _path_exists(path)
        Test whether a path exists.  Returns False for broken symbolic links.

    expanduser(path)
        Expand ~ and ~user constructs.

        If user or $HOME is unknown, do nothing.

    expandvars(path)
        Expand shell variables of the forms $var, ${var} and %var%.

        Unknown variables are left unchanged.

    getatime(filename)
        Return the last access time of a file, reported by os.stat().

    getctime(filename)
        Return the metadata change time of a file, reported by os.stat().

    getmtime(filename)
        Return the last modification time of a file, reported by os.stat().

    getsize(filename)
        Return the size of a file, reported by os.stat().

    isabs(s)
        Test whether a path is absolute

    isdevdrive(path)
        Determines whether the specified path is on a Windows Dev Drive.

    isdir = _path_isdir(s)
        Return true if the pathname refers to an existing directory.

    isfile = _path_isfile(path)
        Test whether a path is a regular file

    isjunction = _path_isjunction(path)
        Test whether a path is a junction

    islink = _path_islink(path)
        Test whether a path is a symbolic link

    ismount(path)
        Test whether a path is a mount point (a drive root, the root of a
        share, or a mounted volume)

    isreserved(path)
        Return true if the pathname is reserved by the system.

    join(path, *paths)
        # Join two (or more) paths.

    lexists = _path_lexists(path)
        Test whether a path exists.  Returns True for broken symbolic links.

    normcase(s)
        Normalize case of pathname.

        Makes all characters lowercase and all slashes into backslashes.

    normpath = _path_normpath(path)
        Normalize path, eliminating double slashes, etc.

    realpath(path, *, strict=False)

    relpath(path, start=None)
        Return a relative version of a path

    samefile(f1, f2)
        Test whether two pathnames reference the same actual file or directory

        This is determined by the device number and i-node number and
        raises an exception if an os.stat() call on either pathname fails.

    sameopenfile(fp1, fp2)
        Test whether two open file objects reference the same file

    samestat(s1, s2)
        Test whether two stat buffers reference the same file

    split(p)
        Split a pathname.

        Return tuple (head, tail) where tail is everything after the final slash.
        Either part may be empty.

    splitdrive(p)
        Split a pathname into drive/UNC sharepoint and relative path specifiers.
        Returns a 2-tuple (drive_or_unc, path); either part may be empty.

        If you assign
            result = splitdrive(p)
        It is always true that:
            result[0] + result[1] == p

        If the path contained a drive letter, drive_or_unc will contain everything
        up to and including the colon.  e.g. splitdrive("c:/dir") returns ("c:", "/dir")

        If the path contained a UNC path, the drive_or_unc will contain the host name
        and share up to but not including the fourth directory separator character.
        e.g. splitdrive("//host/computer/dir") returns ("//host/computer", "/dir")

        Paths cannot contain both a drive letter and a UNC path.

    splitext(p)
        Split the extension from a pathname.

        Extension is everything from the last dot to the end, ignoring
        leading dots.  Returns "(root, ext)"; ext may be empty.

    splitroot = _path_splitroot_ex(p)
        Split a pathname into drive, root and tail.

        The tail contains anything after the root.

DATA
    ALLOW_MISSING = os.path.ALLOW_MISSING
    __all__ = ['normcase', 'isabs', 'join', 'splitdrive', 'splitroot', 'sp...
    altsep = '/'
    curdir = '.'
    defpath = r'.;C:\bin'
    devnull = 'nul'
    extsep = '.'
    pardir = '..'
    pathsep = ';'
    sep = r'\'
    supports_unicode_filenames = True

FILE
    c:\python314\lib\ntpath.py


```

## Related

Other standard-library modules pair well with `ntpath`; explore the `python` domain of this catalog.
