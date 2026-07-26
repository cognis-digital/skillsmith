---
name: python-posixpath
description: "Program with Python's posixpath module: Common operations on Posix pathnames."
version: 1.0.0
tags: [posixpath, programming, python, stdlib]
---

# Python: `posixpath`

## Overview

Common operations on Posix pathnames.

Instead of importing this module directly, import os and refer to
this module as os.path.  The "os.path" name is an alias for this
module on Posix systems; on other systems (e.g. Windows),
os.path provides the same operations in a manner specific to that
platform, and is an alias to another module (e.g. ntpath).

Some of this can actually be useful on non-Posix systems too, e.g.
for manipulation of the pathname component of URLs.

## When to use

Reach for `posixpath` when your task calls for Common operations on Posix pathnames. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import posixpath
```

## Key functions

- `posixpath.abspath(path)`
- `posixpath.basename(p)`
- `posixpath.commonpath(paths)`
- `posixpath.commonprefix(m)`
- `posixpath.dirname(p)`
- `posixpath.exists(path)`
- `posixpath.expanduser(path)`
- `posixpath.expandvars(path)`
- `posixpath.getatime(filename)`
- `posixpath.getctime(filename)`
- `posixpath.getmtime(filename)`
- `posixpath.getsize(filename)`
- `posixpath.isabs(s)`
- `posixpath.isdevdrive(path)`
- `posixpath.isdir(s)`
- `posixpath.isfile(path)`
- `posixpath.isjunction(path)`
- `posixpath.islink(path)`
- `posixpath.ismount(path)`
- `posixpath.join(a, *p)`
- `posixpath.lexists(path)`
- `posixpath.normcase(s)`
- `posixpath.normpath(path)`
- `posixpath.realpath(filename, *, strict=False)`
- `posixpath.relpath(path, start=None)`
- `posixpath.samefile(f1, f2)`
- `posixpath.sameopenfile(fp1, fp2)`
- `posixpath.samestat(s1, s2)`
- `posixpath.split(p)`
- `posixpath.splitdrive(p)`

## Constants / attributes

`ALLOW_MISSING`, `altsep`, `curdir`, `defpath`, `devnull`, `extsep`, `pardir`, `pathsep`, `sep`, `supports_unicode_filenames`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import posixpath

def do_work(...):
    """Use posixpath to accomplish one well-defined task."""
    result = posixpath.abspath(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `posixpath` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module posixpath

NAME
    posixpath - Common operations on Posix pathnames.

MODULE REFERENCE
    https://docs.python.org/3.14/library/posixpath.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Instead of importing this module directly, import os and refer to
    this module as os.path.  The "os.path" name is an alias for this
    module on Posix systems; on other systems (e.g. Windows),
    os.path provides the same operations in a manner specific to that
    platform, and is an alias to another module (e.g. ntpath).

    Some of this can actually be useful on non-Posix systems too, e.g.
    for manipulation of the pathname component of URLs.

FUNCTIONS
    abspath(path)
        Return an absolute path.

    basename(p)
        Returns the final component of a pathname

    commonpath(paths)
        Given a sequence of path names, returns the longest common sub-path.

    commonprefix(m)
        Given a list of pathnames, returns the longest common leading component

    dirname(p)
        Returns the directory component of a pathname

    exists(path)
        Test whether a path exists.  Returns False for broken symbolic links

    expanduser(path)
        Expand ~ and ~user constructions.  If user or $HOME is unknown,
        do nothing.

    expandvars(path)
        Expand shell variables of form $var and ${var}.  Unknown variables
        are left unchanged.

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

    ismount(path)
        Test whether a path is a mount point

    join(a, *p)
        Join two or more pathname components, inserting '/' as needed.
        If any component is an absolute path, all previous path components
        will be discarded.  An empty last part will result in a path that
        ends with a separator.

    lexists(path)
        Test whether a path exists.  Returns True for broken symbolic links

    normcase(s)
        Normalize case of pathname.  Has no effect under Posix

    normpath(path)
        Normalize path, eliminating double slashes, etc.

    realpath(filename, *, strict=False)
        Return the canonical path of the specified filename, eliminating any
        symbolic links encountered in the path.

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
        Split a pathname.  Returns tuple "(head, tail)" where "tail" is
        everything after the final slash.  Either part may be empty.

    splitdrive(p)
        Split a pathname into drive and path. On Posix, drive is always
        empty.

    splitext(p)
        Split the extension from a pathname.

        Extension is everything from the last dot to the end, ignoring
        leading dots.  Returns "(root, ext)"; ext may be empty.

    splitroot(p)
        Split a pathname into drive, root and tail.

        The tail contains anything after the root.

DATA
    ALLOW_MISSING = os.path.ALLOW_MISSING
    __all__ = ['normcase', 'isabs', 'join', 'splitdrive', 'splitroot', 'sp...
    altsep = None
    curdir = '.'
    defpath = '/bin:/usr/bin'
    devnull = '/dev/null'
    extsep = '.'
    pardir = '..'
    pathsep = ':'
    sep = '/'
    supports_unicode_filenames = False

FILE
    c:\python314\lib\posixpath.py


```

## Related

Other standard-library modules pair well with `posixpath`; explore the `python` domain of this catalog.
