---
name: python-fnmatch
description: "Program with Python's fnmatch module: Filename matching with shell patterns."
version: 1.0.0
tags: [fnmatch, programming, python, stdlib]
---

# Python: `fnmatch`

## Overview

Filename matching with shell patterns.

fnmatch(FILENAME, PATTERN) matches according to the local convention.
fnmatchcase(FILENAME, PATTERN) always takes case in account.

The functions operate by translating the pattern into a regular
expression.  They cache the compiled regular expressions for speed.

The function translate(PATTERN) returns a regular expression
corresponding to PATTERN.  (It does not compile it.)

## When to use

Reach for `fnmatch` when your task calls for Filename matching with shell patterns. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import fnmatch
```

## Key functions

- `fnmatch.filter(names, pat)`
- `fnmatch.filterfalse(names, pat)`
- `fnmatch.fnmatch(name, pat)`
- `fnmatch.fnmatchcase(name, pat)`
- `fnmatch.translate(pat)`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import fnmatch

def do_work(...):
    """Use fnmatch to accomplish one well-defined task."""
    result = fnmatch.filter(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `fnmatch` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module fnmatch

NAME
    fnmatch - Filename matching with shell patterns.

MODULE REFERENCE
    https://docs.python.org/3.14/library/fnmatch.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    fnmatch(FILENAME, PATTERN) matches according to the local convention.
    fnmatchcase(FILENAME, PATTERN) always takes case in account.

    The functions operate by translating the pattern into a regular
    expression.  They cache the compiled regular expressions for speed.

    The function translate(PATTERN) returns a regular expression
    corresponding to PATTERN.  (It does not compile it.)

FUNCTIONS
    filter(names, pat)
        Construct a list from those elements of the iterable NAMES that match PAT.

    filterfalse(names, pat)
        Construct a list from those elements of the iterable NAMES that do not match PAT.

    fnmatch(name, pat)
        Test whether FILENAME matches PATTERN.

        Patterns are Unix shell style:

        *       matches everything
        ?       matches any single character
        [seq]   matches any character in seq
        [!seq]  matches any char not in seq

        An initial period in FILENAME is not special.
        Both FILENAME and PATTERN are first case-normalized
        if the operating system requires it.
        If you don't want this, use fnmatchcase(FILENAME, PATTERN).

    fnmatchcase(name, pat)
        Test whether FILENAME matches PATTERN, including case.

        This is a version of fnmatch() which doesn't case-normalize
        its arguments.

    translate(pat)
        Translate a shell PATTERN to a regular expression.

        There is no way to quote meta-characters.

DATA
    __all__ = ['filter', 'filterfalse', 'fnmatch', 'fnmatchcase', 'transla...

FILE
    c:\python314\lib\fnmatch.py


```

## Related

Other standard-library modules pair well with `fnmatch`; explore the `python` domain of this catalog.
