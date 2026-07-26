---
name: python-xml
description: "Program with Python's xml module: Core XML support for Python."
version: 1.0.0
tags: [programming, python, stdlib, xml]
---

# Python: `xml`

## Overview

Core XML support for Python.

This package contains four sub-packages:

dom -- The W3C Document Object Model.  This supports DOM Level 1 +
       Namespaces.

parsers -- Python wrappers for XML parsers (currently only supports Expat).

sax -- The Simple API for XML, developed by XML-Dev, led by David
       Megginson and ported to Python by Lars Marius Garshol.  This
       supports the SAX 2 API.

etree -- The ElementTree XML library.  This is a subset of the full
       ElementTree XML release.

## When to use

Reach for `xml` when your task calls for Core XML support for Python. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import xml
```

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import xml

def do_work(...):
    """Use xml to accomplish one well-defined task."""
    result = xml. ...
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `xml` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: package xml

NAME
    xml - Core XML support for Python.

MODULE REFERENCE
    https://docs.python.org/3.14/library/xml.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This package contains four sub-packages:

    dom -- The W3C Document Object Model.  This supports DOM Level 1 +
           Namespaces.

    parsers -- Python wrappers for XML parsers (currently only supports Expat).

    sax -- The Simple API for XML, developed by XML-Dev, led by David
           Megginson and ported to Python by Lars Marius Garshol.  This
           supports the SAX 2 API.

    etree -- The ElementTree XML library.  This is a subset of the full
           ElementTree XML release.

PACKAGE CONTENTS
    dom (package)
    etree (package)
    parsers (package)
    sax (package)

DATA
    __all__ = ['dom', 'parsers', 'sax', 'etree']

FILE
    c:\python314\lib\xml\__init__.py


```

## Related

Other standard-library modules pair well with `xml`; explore the `python` domain of this catalog.
