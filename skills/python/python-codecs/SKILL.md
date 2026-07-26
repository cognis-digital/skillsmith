---
name: python-codecs
description: "Program with Python's codecs module: codecs -- Python Codec Registry, API and helpers."
version: 1.0.0
tags: [codecs, programming, python, stdlib]
---

# Python: `codecs`

## Overview

codecs -- Python Codec Registry, API and helpers.


Written by Marc-Andre Lemburg (mal@lemburg.com).

(c) Copyright CNRI, All Rights Reserved. NO WARRANTY.

## When to use

Reach for `codecs` when your task calls for codecs -- Python Codec Registry, API and helpers. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import codecs
```

## Key functions

- `codecs.EncodedFile(file, data_encoding, file_encoding=None, errors='strict')`
- `codecs.ascii_decode(data, errors=None, /)`
- `codecs.ascii_encode(str, errors=None, /)`
- `codecs.backslashreplace_errors(self, object, /)`
- `codecs.charmap_build(map, /)`
- `codecs.charmap_decode(data, errors=None, mapping=None, /)`
- `codecs.charmap_encode(str, errors=None, mapping=None, /)`
- `codecs.code_page_decode(codepage, data, errors=None, final=False, /)`
- `codecs.code_page_encode(code_page, str, errors=None, /)`
- `codecs.decode(obj, encoding='utf-8', errors='strict')`
- `codecs.encode(obj, encoding='utf-8', errors='strict')`
- `codecs.escape_decode(data, errors=None, /)`
- `codecs.escape_encode(data, errors=None, /)`
- `codecs.getdecoder(encoding)`
- `codecs.getencoder(encoding)`
- `codecs.getincrementaldecoder(encoding)`
- `codecs.getincrementalencoder(encoding)`
- `codecs.getreader(encoding)`
- `codecs.getwriter(encoding)`
- `codecs.ignore_errors(self, object, /)`
- `codecs.iterdecode(iterator, encoding, errors='strict', **kwargs)`
- `codecs.iterencode(iterator, encoding, errors='strict', **kwargs)`
- `codecs.latin_1_decode(data, errors=None, /)`
- `codecs.latin_1_encode(str, errors=None, /)`
- `codecs.lookup(encoding, /)`
- `codecs.lookup_error(name, /)`
- `codecs.make_encoding_map(decoding_map)`
- `codecs.make_identity_dict(rng)`
- `codecs.mbcs_decode(data, errors=None, final=False, /)`
- `codecs.mbcs_encode(str, errors=None, /)`

## Key classes

`BufferedIncrementalDecoder`, `BufferedIncrementalEncoder`, `Codec`, `CodecInfo`, `IncrementalDecoder`, `IncrementalEncoder`, `StreamReader`, `StreamReaderWriter`, `StreamRecoder`, `StreamWriter`

## Constants / attributes

`BOM`, `BOM32_BE`, `BOM32_LE`, `BOM64_BE`, `BOM64_LE`, `BOM_BE`, `BOM_LE`, `BOM_UTF16`, `BOM_UTF16_BE`, `BOM_UTF16_LE`, `BOM_UTF32`, `BOM_UTF32_BE`, `BOM_UTF32_LE`, `BOM_UTF8`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import codecs

def do_work(...):
    """Use codecs to accomplish one well-defined task."""
    result = codecs.EncodedFile(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `codecs` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module codecs

NAME
    codecs - codecs -- Python Codec Registry, API and helpers.

MODULE REFERENCE
    https://docs.python.org/3.14/library/codecs.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION

    Written by Marc-Andre Lemburg (mal@lemburg.com).

    (c) Copyright CNRI, All Rights Reserved. NO WARRANTY.

CLASSES
    builtins.object
        Codec
            StreamReader
            StreamWriter
        IncrementalDecoder
        IncrementalEncoder
        StreamReaderWriter
        StreamRecoder
    builtins.tuple(builtins.object)
        CodecInfo

    class Codec(builtins.object)
     |  Defines the interface for stateless encoders/decoders.
     |
     |  The .encode()/.decode() methods may use different error
     |  handling schemes by providing the errors argument. These
     |  string values are predefined:
     |
     |   'strict' - raise a ValueError error (or a subclass)
     |   'ignore' - ignore the character and continue with the next
     |   'replace' - replace with a suitable replacement character;
     |              Python will use the official U+FFFD REPLACEMENT
     |              CHARACTER for the builtin Unicode codecs on
     |              decoding and '?' on encoding.
     |   'surrogateescape' - replace with private code points U+DCnn.
     |   'xmlcharrefreplace' - Replace with the appropriate XML
     |                         character reference (only for encoding).
     |   'backslashreplace'  - Replace with backslashed escape sequences.
     |   'namereplace'       - Replace with \N{...} escape sequences
     |                         (only for encoding).
     |
     |  The set of allowed values can be extended via register_error.
     |
     |  Methods defined here:
     |
     |  decode(self, input, errors='strict')
     |      Decodes the object input and returns a tuple (output
     |      object, length consumed).
     |
     |      input must be an object which provides the bf_getreadbuf
     |      buffer slot. Python strings, buffer objects and memory
     |      mapped files are examples of objects providing this slot.
     |
     |      errors defines the error handling to apply. It defaults to
     |      'strict' handling.
     |
     |      The method may not store state in the Codec instance. Use
     |      StreamReader for codecs which have to keep state in order to
     |      make decoding efficient.
     |
     |      The decoder must be able to handle zero length input and
     |      return an empty object of the output object type in this
     |      situation.
     |
     |  encode(self, input, errors='strict')
     |      Encodes the object input and returns a tuple (output
     |      object, length consumed).
     |
     |      errors defines the error handling to apply. It defaults to
     |      'strict' handling.
     |
     |      The method may not store state in the Codec instance. Use
     |      StreamWriter for codecs which have to keep state in order to
     |      make encoding efficient.
     |
     |      The encoder must be able to handle zero length input and
     |      return an empty object of the output object type in this
     |      situation.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class CodecInfo(builtins.tuple)
     |  CodecInfo(
     |      encode,
     |      decode,
     |      streamreader=None,
     |      streamwriter=None,
     |      incrementalencoder=None,
     |      incrementaldecoder=None,
     |      name=None,
     |      *,
     |      _is_text_encoding=None
     |  )
     |
     |  Codec details when looking up the codec registry
     |
     |  Method resolution order:
     |      CodecInfo
     |      builtins.tuple
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __getnewargs__(self)
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(
     |      cls,
     |      encode,
     |      decode,
     |      streamreader=None,
     |      streamwriter=None,
     |      incrementalencoder=None,
     |      incrementaldecoder=None,
     |      name=None,
     |      *,
     |      _is_text_encoding=None
     |  )
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __contains__(self, key, /)
     |      Return bool(key in self).
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getitem__(self, key, /)
     |      Return self[key].
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __len__(self, /)
     |      Return len(self).
     |
     |  __lt__(self, value, /)
     |      Return self<valu
```

## Related

Other standard-library modules pair well with `codecs`; explore the `python` domain of this catalog.
