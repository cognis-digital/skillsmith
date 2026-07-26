---
name: python-unicodedata
description: "Program with Python's unicodedata module: This module provides access to the Unicode Character Database which defines character properties for all Unicode characters."
version: 1.0.0
tags: [programming, python, stdlib, unicodedata]
---

# Python: `unicodedata`

## Overview

This module provides access to the Unicode Character Database which
defines character properties for all Unicode characters. The data in
this database is based on the UnicodeData.txt file version
16.0.0 which is publicly available from ftp://ftp.unicode.org/.

The module uses the same names and symbols as defined by the
UnicodeData File Format 16.0.0.

## When to use

Reach for `unicodedata` when your task calls for This module provides access to the Unicode Character Database which defines character properties for all Unicode charact. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import unicodedata
```

## Key functions

- `unicodedata.bidirectional(chr, /)`
- `unicodedata.category(chr, /)`
- `unicodedata.combining(chr, /)`
- `unicodedata.decimal(...)`
- `unicodedata.decomposition(chr, /)`
- `unicodedata.digit(...)`
- `unicodedata.east_asian_width(chr, /)`
- `unicodedata.is_normalized(form, unistr, /)`
- `unicodedata.lookup(name, /)`
- `unicodedata.mirrored(chr, /)`
- `unicodedata.name(...)`
- `unicodedata.normalize(form, unistr, /)`
- `unicodedata.numeric(...)`

## Key classes

`UCD`

## Constants / attributes

`ucd_3_2_0`, `unidata_version`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import unicodedata

def do_work(...):
    """Use unicodedata to accomplish one well-defined task."""
    result = unicodedata.bidirectional(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `unicodedata` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module unicodedata

NAME
    unicodedata

DESCRIPTION
    This module provides access to the Unicode Character Database which
    defines character properties for all Unicode characters. The data in
    this database is based on the UnicodeData.txt file version
    16.0.0 which is publicly available from ftp://ftp.unicode.org/.

    The module uses the same names and symbols as defined by the
    UnicodeData File Format 16.0.0.

CLASSES
    builtins.object
        UCD

    class UCD(builtins.object)
     |  Methods defined here:
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  bidirectional(self, chr, /)
     |      Returns the bidirectional class assigned to the character chr as string.
     |
     |      If no such value is defined, an empty string is returned.
     |
     |  category(self, chr, /)
     |      Returns the general category assigned to the character chr as string.
     |
     |  combining(self, chr, /)
     |      Returns the canonical combining class assigned to the character chr as integer.
     |
     |      Returns 0 if no combining class is defined.
     |
     |  decimal(self, chr, default=<unrepresentable>, /)
     |      Converts a Unicode character into its equivalent decimal value.
     |
     |      Returns the decimal value assigned to the character chr as integer.
     |      If no such value is defined, default is returned, or, if not given,
     |      ValueError is raised.
     |
     |  decomposition(self, chr, /)
     |      Returns the character decomposition mapping assigned to the character chr as string.
     |
     |      An empty string is returned in case no such mapping is defined.
     |
     |  digit(self, chr, default=<unrepresentable>, /)
     |      Converts a Unicode character into its equivalent digit value.
     |
     |      Returns the digit value assigned to the character chr as integer.
     |      If no such value is defined, default is returned, or, if not given,
     |      ValueError is raised.
     |
     |  east_asian_width(self, chr, /)
     |      Returns the east asian width assigned to the character chr as string.
     |
     |  is_normalized(self, form, unistr, /)
     |      Return whether the Unicode string unistr is in the normal form 'form'.
     |
     |      Valid values for form are 'NFC', 'NFKC', 'NFD', and 'NFKD'.
     |
     |  lookup(self, name, /)
     |      Look up character by name.
     |
     |      If a character with the given name is found, return the
     |      corresponding character.  If not found, KeyError is raised.
     |
     |  mirrored(self, chr, /)
     |      Returns the mirrored property assigned to the character chr as integer.
     |
     |      Returns 1 if the character has been identified as a "mirrored"
     |      character in bidirectional text, 0 otherwise.
     |
     |  name(self, chr, default=<unrepresentable>, /)
     |      Returns the name assigned to the character chr as a string.
     |
     |      If no name is defined, default is returned, or, if not given,
     |      ValueError is raised.
     |
     |  normalize(self, form, unistr, /)
     |      Return the normal form 'form' for the Unicode string unistr.
     |
     |      Valid values for form are 'NFC', 'NFKC', 'NFD', and 'NFKD'.
     |
     |  numeric(self, chr, default=<unrepresentable>, /)
     |      Converts a Unicode character into its equivalent numeric value.
     |
     |      Returns the numeric value assigned to the character chr as float.
     |      If no such value is defined, default is returned, or, if not given,
     |      ValueError is raised.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  unidata_version

FUNCTIONS
    bidirectional(chr, /)
        Returns the bidirectional class assigned to the character chr as string.

        If no such value is defined, an empty string is returned.

    category(chr, /)
        Returns the general category assigned to the character chr as string.

    combining(chr, /)
        Returns the canonical combining class assigned to the character chr as integer.

        Returns 0 if no combining class is defined.

    decimal(chr, default=<unrepresentable>, /)
        Converts a Unicode character into its equivalent decimal value.

        Returns the decimal value assigned to the character chr as integer.
        If no such value is defined, default is returned, or, if not given,
        ValueError is raised.

    decomposition(chr, /)
        Returns the character decomposition mapping assigned to the character chr as string.

        An empty string is returned in case no such mapping is defined.

    digit(chr, default=<unrepresentable>, /)
        Converts a Unicode character into its equivalent digit value.

        Returns the digit value assigned to the character chr as integer.
        If no such value is defined, default is returned, or, if not given,
        ValueError is raised.

    east_asian_width(chr, /)
        Returns the east asian width assigned to the character chr as string.

    is_normalized(form, unistr, /)
        Return whether the Unicode string unistr is in the normal form 'form'.

        Valid values for form are 'NFC', 'NFKC', 'NFD', and 'NFKD'.

    lookup(name, /)
        Look up character by name.

        If a character with the given name is found, return the
        corresponding character.  If not found, KeyError is raised.

    mirrored(chr, /)
        Returns the mirrored property assigned to the character chr as integer.

        Returns 1 if the character has been identified as a "mirrored"
        character in bidirectional text, 0 otherwise.

    name(chr, default=<unrepresentable>, /)
        Returns the name assigned to the character chr as a string.

        If no name is defined, default is returned, or, if not given,
        ValueError is rai
```

## Related

Other standard-library modules pair well with `unicodedata`; explore the `python` domain of this catalog.
