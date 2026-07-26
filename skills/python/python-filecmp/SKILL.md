---
name: python-filecmp
description: "Program with Python's filecmp module: Utilities for comparing files and directories."
version: 1.0.0
tags: [filecmp, programming, python, stdlib]
---

# Python: `filecmp`

## Overview

Utilities for comparing files and directories.

Classes:
    dircmp

Functions:
    cmp(f1, f2, shallow=True) -> int
    cmpfiles(a, b, common) -> ([], [], [])
    clear_cache()

## When to use

Reach for `filecmp` when your task calls for Utilities for comparing files and directories. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import filecmp
```

## Key functions

- `filecmp.clear_cache()`
- `filecmp.cmp(f1, f2, shallow=True)`
- `filecmp.cmpfiles(a, b, common, shallow=True)`
- `filecmp.demo()`

## Key classes

`GenericAlias`, `dircmp`, `filterfalse`

## Constants / attributes

`BUFSIZE`, `DEFAULT_IGNORES`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import filecmp

def do_work(...):
    """Use filecmp to accomplish one well-defined task."""
    result = filecmp.clear_cache(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `filecmp` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module filecmp

NAME
    filecmp - Utilities for comparing files and directories.

MODULE REFERENCE
    https://docs.python.org/3.14/library/filecmp.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Classes:
        dircmp

    Functions:
        cmp(f1, f2, shallow=True) -> int
        cmpfiles(a, b, common) -> ([], [], [])
        clear_cache()

CLASSES
    builtins.object
        dircmp

    class dircmp(builtins.object)
     |  dircmp(a, b, ignore=None, hide=None, *, shallow=True)
     |
     |  A class that manages the comparison of 2 directories.
     |
     |  dircmp(a, b, ignore=None, hide=None, *, shallow=True)
     |    A and B are directories.
     |    IGNORE is a list of names to ignore,
     |      defaults to DEFAULT_IGNORES.
     |    HIDE is a list of names to hide,
     |      defaults to [os.curdir, os.pardir].
     |    SHALLOW specifies whether to just check the stat signature (do not read
     |      the files).
     |      defaults to True.
     |
     |  High level usage:
     |    x = dircmp(dir1, dir2)
     |    x.report() -> prints a report on the differences between dir1 and dir2
     |     or
     |    x.report_partial_closure() -> prints report on differences between dir1
     |          and dir2, and reports on common immediate subdirectories.
     |    x.report_full_closure() -> like report_partial_closure,
     |          but fully recursive.
     |
     |  Attributes:
     |   left_list, right_list: The files in dir1 and dir2,
     |      filtered by hide and ignore.
     |   common: a list of names in both dir1 and dir2.
     |   left_only, right_only: names only in dir1, dir2.
     |   common_dirs: subdirectories in both dir1 and dir2.
     |   common_files: files in both dir1 and dir2.
     |   common_funny: names in both dir1 and dir2 where the type differs between
     |      dir1 and dir2, or the name is not stat-able.
     |   same_files: list of identical files.
     |   diff_files: list of filenames which differ.
     |   funny_files: list of files which could not be compared.
     |   subdirs: a dictionary of dircmp instances (or MyDirCmp instances if this
     |     object is of type MyDirCmp, a subclass of dircmp), keyed by names
     |     in common_dirs.
     |
     |  Methods defined here:
     |
     |  __getattr__(self, attr)
     |
     |  __init__(self, a, b, ignore=None, hide=None, *, shallow=True)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  phase0(self)
     |
     |  phase1(self)
     |
     |  phase2(self)
     |
     |  phase3(self)
     |
     |  phase4(self)
     |
     |  phase4_closure(self)
     |
     |  report(self)
     |
     |  report_full_closure(self)
     |
     |  report_partial_closure(self)
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  __class_getitem__ = GenericAlias(args, /)
     |      Represent a PEP 585 generic type
     |
     |      E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).
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
     |  methodmap = {'common': <function dircmp.phase1>, 'common_dirs': <funct...

FUNCTIONS
    clear_cache()
        Clear the filecmp cache.

    cmp(f1, f2, shallow=True)
        Compare two files.

        Arguments:

        f1 -- First file name

        f2 -- Second file name

        shallow -- treat files as identical if their stat signatures (type, size,
                   mtime) are identical. Otherwise, files are considered different
                   if their sizes or contents differ.  [default: True]

        Return value:

        True if the files are the same, False otherwise.

        This function uses a cache for past comparisons and the results,
        with cache entries invalidated if their stat information
        changes.  The cache may be cleared by calling clear_cache().

    cmpfiles(a, b, common, shallow=True)
        Compare common files in two directories.

        a, b -- directory names
        common -- list of file names found in both directories
        shallow -- if true, do comparison based solely on stat() information

        Returns a tuple of three lists:
          files that compare equal
          files that are different
          filenames that aren't regular files.

DATA
    DEFAULT_IGNORES = ['RCS', 'CVS', 'tags', '.git', '.hg', '.bzr', '_darc...
    __all__ = ['clear_cache', 'cmp', 'dircmp', 'cmpfiles', 'DEFAULT_IGNORE...

FILE
    c:\python314\lib\filecmp.py


```

## Related

Other standard-library modules pair well with `filecmp`; explore the `python` domain of this catalog.
