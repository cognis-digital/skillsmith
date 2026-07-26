---
name: python-shlex
description: "Program with Python's shlex module: A lexical analyzer class for simple shell-like syntaxes."
version: 1.0.0
tags: [programming, python, shlex, stdlib]
---

# Python: `shlex`

## Overview

A lexical analyzer class for simple shell-like syntaxes.

## When to use

Reach for `shlex` when your task calls for A lexical analyzer class for simple shell-like syntaxes. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import shlex
```

## Key functions

- `shlex.join(split_command)`
- `shlex.quote(s)`
- `shlex.split(s, comments=False, posix=True)`

## Key classes

`StringIO`, `shlex`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import shlex

def do_work(...):
    """Use shlex to accomplish one well-defined task."""
    result = shlex.join(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `shlex` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module shlex

NAME
    shlex - A lexical analyzer class for simple shell-like syntaxes.

MODULE REFERENCE
    https://docs.python.org/3.14/library/shlex.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.object
        shlex

    class shlex(builtins.object)
     |  shlex(instream=None, infile=None, posix=False, punctuation_chars=False)
     |
     |  A lexical analyzer class for simple shell-like syntaxes.
     |
     |  Methods defined here:
     |
     |  __init__(self, instream=None, infile=None, posix=False, punctuation_chars=False)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __iter__(self)
     |
     |  __next__(self)
     |
     |  error_leader(self, infile=None, lineno=None)
     |      Emit a C-compiler-like, Emacs-friendly error-message leader.
     |
     |  get_token(self)
     |      Get a token from the input stream (or from stack if it's nonempty)
     |
     |  pop_source(self)
     |      Pop the input source stack.
     |
     |  push_source(self, newstream, newfile=None)
     |      Push an input source onto the lexer's input source stack.
     |
     |  push_token(self, tok)
     |      Push a token onto the stack popped by the get_token method
     |
     |  read_token(self)
     |
     |  sourcehook(self, newfile)
     |      Hook called on a filename to be sourced.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  punctuation_chars
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
    join(split_command)
        Return a shell-escaped string from *split_command*.

    quote(s)
        Return a shell-escaped version of the string *s*.

    split(s, comments=False, posix=True)
        Split the string *s* using shell-like syntax.

DATA
    __all__ = ['shlex', 'split', 'quote', 'join']

FILE
    c:\python314\lib\shlex.py


```

## Related

Other standard-library modules pair well with `shlex`; explore the `python` domain of this catalog.
