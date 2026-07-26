---
name: python-gettext
description: "Program with Python's gettext module: Internationalization and localization support."
version: 1.0.0
tags: [gettext, programming, python, stdlib]
---

# Python: `gettext`

## Overview

Internationalization and localization support.

This module provides internationalization (I18N) and localization (L10N)
support for your Python programs by providing an interface to the GNU gettext
message catalog library.

I18N refers to the operation by which a program is made aware of multiple
languages.  L10N refers to the adaptation of your program, once
internationalized, to the local language and cultural habits.

## When to use

Reach for `gettext` when your task calls for Internationalization and localization support. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import gettext
```

## Key functions

- `gettext.Catalog(domain, localedir=None, languages=None, class_=None, fallback=False)`
- `gettext.bindtextdomain(domain, localedir=None)`
- `gettext.c2py(plural)`
- `gettext.dgettext(domain, message)`
- `gettext.dngettext(domain, msgid1, msgid2, n)`
- `gettext.dnpgettext(domain, context, msgid1, msgid2, n)`
- `gettext.dpgettext(domain, context, message)`
- `gettext.find(domain, localedir=None, languages=None, all=False)`
- `gettext.gettext(message)`
- `gettext.install(domain, localedir=None, *, names=None)`
- `gettext.ngettext(msgid1, msgid2, n)`
- `gettext.npgettext(context, msgid1, msgid2, n)`
- `gettext.pgettext(context, message)`
- `gettext.textdomain(domain=None)`
- `gettext.translation(domain, localedir=None, languages=None, class_=None, fallback=False)`

## Key classes

`GNUTranslations`, `NullTranslations`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import gettext

def do_work(...):
    """Use gettext to accomplish one well-defined task."""
    result = gettext.Catalog(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `gettext` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module gettext

NAME
    gettext - Internationalization and localization support.

MODULE REFERENCE
    https://docs.python.org/3.14/library/gettext.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides internationalization (I18N) and localization (L10N)
    support for your Python programs by providing an interface to the GNU gettext
    message catalog library.

    I18N refers to the operation by which a program is made aware of multiple
    languages.  L10N refers to the adaptation of your program, once
    internationalized, to the local language and cultural habits.

CLASSES
    builtins.object
        NullTranslations
            GNUTranslations

    class GNUTranslations(NullTranslations)
     |  GNUTranslations(fp=None)
     |
     |  Method resolution order:
     |      GNUTranslations
     |      NullTranslations
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  gettext(self, message)
     |
     |  ngettext(self, msgid1, msgid2, n)
     |
     |  npgettext(self, context, msgid1, msgid2, n)
     |
     |  pgettext(self, context, message)
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  BE_MAGIC = 3725722773
     |
     |  CONTEXT = '%s\x04%s'
     |
     |  LE_MAGIC = 2500072158
     |
     |  VERSIONS = (0, 1)
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from NullTranslations:
     |
     |  __init__(self, fp=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  add_fallback(self, fallback)
     |
     |  charset(self)
     |
     |  info(self)
     |
     |  install(self, names=None)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from NullTranslations:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class NullTranslations(builtins.object)
     |  NullTranslations(fp=None)
     |
     |  Methods defined here:
     |
     |  __init__(self, fp=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  add_fallback(self, fallback)
     |
     |  charset(self)
     |
     |  gettext(self, message)
     |
     |  info(self)
     |
     |  install(self, names=None)
     |
     |  ngettext(self, msgid1, msgid2, n)
     |
     |  npgettext(self, context, msgid1, msgid2, n)
     |
     |  pgettext(self, context, message)
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
    Catalog = translation(domain, localedir=None, languages=None, class_=None, fallback=False)

    bindtextdomain(domain, localedir=None)

    dgettext(domain, message)

    dngettext(domain, msgid1, msgid2, n)

    dnpgettext(domain, context, msgid1, msgid2, n)

    dpgettext(domain, context, message)

    find(domain, localedir=None, languages=None, all=False)
        # Locate a .mo file using the gettext strategy

    gettext(message)

    install(domain, localedir=None, *, names=None)

    ngettext(msgid1, msgid2, n)

    npgettext(context, msgid1, msgid2, n)

    pgettext(context, message)

    textdomain(domain=None)

    translation(domain, localedir=None, languages=None, class_=None, fallback=False)

DATA
    __all__ = ['NullTranslations', 'GNUTranslations', 'Catalog', 'bindtext...

FILE
    c:\python314\lib\gettext.py


```

## Related

Other standard-library modules pair well with `gettext`; explore the `python` domain of this catalog.
