---
name: python-glob
description: "Program with Python's glob module: Filename globbing utility."
version: 1.0.0
tags: [glob, programming, python, stdlib]
---

# Python: `glob`

## Overview

Filename globbing utility.

## When to use

Reach for `glob` when your task calls for Filename globbing utility. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import glob
```

## Key functions

- `glob.escape(pathname)`
- `glob.glob(pathname, *, root_dir=None, dir_fd=None, recursive=False, include_hidden=False)`
- `glob.glob0(dirname, pattern)`
- `glob.glob1(dirname, pattern)`
- `glob.has_magic(s)`
- `glob.iglob(pathname, *, root_dir=None, dir_fd=None, recursive=False, include_hidden=False)`
- `glob.translate(pat, *, recursive=False, include_hidden=False, seps=None)`

## Constants / attributes

`magic_check`, `magic_check_bytes`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import glob

def do_work(...):
    """Use glob to accomplish one well-defined task."""
    result = glob.escape(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `glob` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module glob

NAME
    glob - Filename globbing utility.

MODULE REFERENCE
    https://docs.python.org/3.14/library/glob.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

FUNCTIONS
    escape(pathname)
        Escape all special characters.

    glob(
        pathname,
        *,
        root_dir=None,
        dir_fd=None,
        recursive=False,
        include_hidden=False
    )
        Return a list of paths matching a pathname pattern.

        The pattern may contain simple shell-style wildcards a la
        fnmatch. Unlike fnmatch, filenames starting with a
        dot are special cases that are not matched by '*' and '?'
        patterns by default.

        If `include_hidden` is true, the patterns '*', '?', '**'  will match hidden
        directories.

        If `recursive` is true, the pattern '**' will match any files and
        zero or more directories and subdirectories.

    iglob(
        pathname,
        *,
        root_dir=None,
        dir_fd=None,
        recursive=False,
        include_hidden=False
    )
        Return an iterator which yields the paths matching a pathname pattern.

        The pattern may contain simple shell-style wildcards a la
        fnmatch. However, unlike fnmatch, filenames starting with a
        dot are special cases that are not matched by '*' and '?'
        patterns.

        If recursive is true, the pattern '**' will match any files and
        zero or more directories and subdirectories.

    translate(pat, *, recursive=False, include_hidden=False, seps=None)
        Translate a pathname with shell wildcards to a regular expression.

        If `recursive` is true, the pattern segment '**' will match any number of
        path segments.

        If `include_hidden` is true, wildcards can match path segments beginning
        with a dot ('.').

        If a sequence of separator characters is given to `seps`, they will be
        used to split the pattern into segments and match path separators. If not
        given, os.path.sep and os.path.altsep (where available) are used.

DATA
    __all__ = ['glob', 'iglob', 'escape', 'translate']

FILE
    c:\python314\lib\glob.py


```

## Related

Other standard-library modules pair well with `glob`; explore the `python` domain of this catalog.
