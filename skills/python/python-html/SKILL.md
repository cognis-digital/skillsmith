---
name: python-html
description: "Program with Python's html module: General functions for HTML manipulation."
version: 1.0.0
tags: [html, programming, python, stdlib]
---

# Python: `html`

## Overview

General functions for HTML manipulation.

## When to use

Reach for `html` when your task calls for General functions for HTML manipulation. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import html
```

## Key functions

- `html.escape(s, quote=True)`
- `html.unescape(s)`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import html

def do_work(...):
    """Use html to accomplish one well-defined task."""
    result = html.escape(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `html` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: package html

NAME
    html - General functions for HTML manipulation.

MODULE REFERENCE
    https://docs.python.org/3.14/library/html.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

PACKAGE CONTENTS
    entities
    parser

FUNCTIONS
    escape(s, quote=True)
        Replace special characters "&", "<" and ">" to HTML-safe sequences.
        If the optional flag quote is true (the default), the quotation mark
        characters, both double quote (") and single quote (') characters are also
        translated.

    unescape(s)
        Convert all named and numeric character references (e.g. &gt;, &#62;,
        &x3e;) in the string s to the corresponding unicode characters.
        This function uses the rules defined by the HTML 5 standard
        for both valid and invalid character references, and the list of
        HTML 5 named character references defined in html.entities.html5.

DATA
    __all__ = ['escape', 'unescape']

FILE
    c:\python314\lib\html\__init__.py


```

## Related

Other standard-library modules pair well with `html`; explore the `python` domain of this catalog.
