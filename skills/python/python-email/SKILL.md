---
name: python-email
description: "Program with Python's email module: A package for parsing, handling, and generating email messages."
version: 1.0.0
tags: [email, programming, python, stdlib]
---

# Python: `email`

## Overview

A package for parsing, handling, and generating email messages.

## When to use

Reach for `email` when your task calls for A package for parsing, handling, and generating email messages. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import email
```

## Key functions

- `email.message_from_binary_file(fp, *args, **kws)`
- `email.message_from_bytes(s, *args, **kws)`
- `email.message_from_file(fp, *args, **kws)`
- `email.message_from_string(s, *args, **kws)`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import email

def do_work(...):
    """Use email to accomplish one well-defined task."""
    result = email.message_from_binary_file(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `email` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: package email

NAME
    email - A package for parsing, handling, and generating email messages.

MODULE REFERENCE
    https://docs.python.org/3.14/library/email.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

PACKAGE CONTENTS
    _encoded_words
    _header_value_parser
    _parseaddr
    _policybase
    base64mime
    charset
    contentmanager
    encoders
    errors
    feedparser
    generator
    header
    headerregistry
    iterators
    message
    mime (package)
    parser
    policy
    quoprimime
    utils

FUNCTIONS
    message_from_binary_file(fp, *args, **kws)
        Read a binary file and parse its contents into a Message object model.

        Optional _class and strict are passed to the Parser constructor.

    message_from_bytes(s, *args, **kws)
        Parse a bytes string into a Message object model.

        Optional _class and strict are passed to the Parser constructor.

    message_from_file(fp, *args, **kws)
        Read a file and parse its contents into a Message object model.

        Optional _class and strict are passed to the Parser constructor.

    message_from_string(s, *args, **kws)
        Parse a string into a Message object model.

        Optional _class and strict are passed to the Parser constructor.

DATA
    __all__ = ['base64mime', 'charset', 'encoders', 'errors', 'feedparser'...

FILE
    c:\python314\lib\email\__init__.py


```

## Related

Other standard-library modules pair well with `email`; explore the `python` domain of this catalog.
