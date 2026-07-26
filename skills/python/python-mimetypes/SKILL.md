---
name: python-mimetypes
description: "Program with Python's mimetypes module: Guess the MIME type of a file."
version: 1.0.0
tags: [mimetypes, programming, python, stdlib]
---

# Python: `mimetypes`

## Overview

Guess the MIME type of a file.

This module defines two useful functions:

guess_type(url, strict=True) -- guess the MIME type and encoding of a URL.

guess_extension(type, strict=True) -- guess the extension for a given MIME type.

It also contains the following, for tuning the behavior:

Data:

knownfiles -- list of files to parse
inited -- flag set when init() has been called
suffix_map -- dictionary mapping suffixes to suffixes
encodings_map -- dictionary mapping suffixes to encodings
types_map -- dictionary mapping suffixes to types

Functions:

init([files]) -- parse a list of files, default knownfiles (on Windows, the
  default values are taken from the registry)
read_mime_types(file) -- parse one file, return a dictionary or None

## When to use

Reach for `mimetypes` when your task calls for Guess the MIME type of a file. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import mimetypes
```

## Key functions

- `mimetypes.add_type(type, ext, strict=True)`
- `mimetypes.guess_all_extensions(type, strict=True)`
- `mimetypes.guess_extension(type, strict=True)`
- `mimetypes.guess_file_type(path, *, strict=True)`
- `mimetypes.guess_type(url, strict=True)`
- `mimetypes.init(files=None)`
- `mimetypes.read_mime_types(file)`

## Key classes

`MimeTypes`

## Constants / attributes

`common_types`, `encodings_map`, `inited`, `knownfiles`, `suffix_map`, `types_map`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import mimetypes

def do_work(...):
    """Use mimetypes to accomplish one well-defined task."""
    result = mimetypes.add_type(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `mimetypes` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module mimetypes

NAME
    mimetypes - Guess the MIME type of a file.

MODULE REFERENCE
    https://docs.python.org/3.14/library/mimetypes.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module defines two useful functions:

    guess_type(url, strict=True) -- guess the MIME type and encoding of a URL.

    guess_extension(type, strict=True) -- guess the extension for a given MIME type.

    It also contains the following, for tuning the behavior:

    Data:

    knownfiles -- list of files to parse
    inited -- flag set when init() has been called
    suffix_map -- dictionary mapping suffixes to suffixes
    encodings_map -- dictionary mapping suffixes to encodings
    types_map -- dictionary mapping suffixes to types

    Functions:

    init([files]) -- parse a list of files, default knownfiles (on Windows, the
      default values are taken from the registry)
    read_mime_types(file) -- parse one file, return a dictionary or None

CLASSES
    builtins.object
        MimeTypes

    class MimeTypes(builtins.object)
     |  MimeTypes(filenames=(), strict=True)
     |
     |  MIME-types datastore.
     |
     |  This datastore can handle information from mime.types-style files
     |  and supports basic determination of MIME type from a filename or
     |  URL, and can guess a reasonable extension given a MIME type.
     |
     |  Methods defined here:
     |
     |  __init__(self, filenames=(), strict=True)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  add_type(self, type, ext, strict=True)
     |      Add a mapping between a type and an extension.
     |
     |      When the extension is already known, the new
     |      type will replace the old one. When the type
     |      is already known the extension will be added
     |      to the list of known extensions.
     |
     |      If strict is true, information will be added to
     |      list of standard types, else to the list of non-standard
     |      types.
     |
     |      Valid extensions are empty or start with a '.'.
     |
     |  guess_all_extensions(self, type, strict=True)
     |      Guess the extensions for a file based on its MIME type.
     |
     |      Return value is a list of strings giving the possible filename
     |      extensions, including the leading dot ('.').  The extension is not
     |      guaranteed to have been associated with any particular data stream,
     |      but would be mapped to the MIME type 'type' by guess_type().
     |
     |      Optional 'strict' argument when false adds a bunch of commonly found,
     |      but non-standard types.
     |
     |  guess_extension(self, type, strict=True)
     |      Guess the extension for a file based on its MIME type.
     |
     |      Return value is a string giving a filename extension,
     |      including the leading dot ('.').  The extension is not
     |      guaranteed to have been associated with any particular data
     |      stream, but would be mapped to the MIME type 'type' by
     |      guess_type().  If no extension can be guessed for 'type', None
     |      is returned.
     |
     |      Optional 'strict' argument when false adds a bunch of commonly found,
     |      but non-standard types.
     |
     |  guess_file_type(self, path, *, strict=True)
     |      Guess the type of a file based on its path.
     |
     |      Similar to guess_type(), but takes file path instead of URL.
     |
     |  guess_type(self, url, strict=True)
     |      Guess the type of a file which is either a URL or a path-like object.
     |
     |      Return value is a tuple (type, encoding) where type is None if
     |      the type can't be guessed (no or unknown suffix) or a string
     |      of the form type/subtype, usable for a MIME Content-type
     |      header; and encoding is None for no encoding or the name of
     |      the program used to encode (e.g. compress or gzip).  The
     |      mappings are table driven.  Encoding suffixes are case
     |      sensitive; type suffixes are first tried case sensitive, then
     |      case insensitive.
     |
     |      The suffixes .tgz, .taz and .tz (case sensitive!) are all
     |      mapped to '.tar.gz'.  (This is table-driven too, using the
     |      dictionary suffix_map.)
     |
     |      Optional 'strict' argument when False adds a bunch of commonly found,
     |      but non-standard types.
     |
     |  read(self, filename, strict=True)
     |      Read a single mime.types-format file, specified by pathname.
     |
     |      If strict is true, information will be added to
     |      list of standard types, else to the list of non-standard
     |      types.
     |
     |  read_windows_registry(self, strict=True)
     |      Load the MIME types database from Windows registry.
     |
     |      If strict is true, information will be added to
     |      list of standard types, else to the list of non-standard
     |      types.
     |
     |  readfp(self, fp, strict=True)
     |      Read a single mime.types-format file.
     |
     |      If strict is true, information will be added to
     |      list of standard types, else to the list of non-standard
     |      types.
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
    add_type(type, ext, strict=True)
        Add a mapping between a type and an extension.

        When the extension is already known, the new
     
```

## Related

Other standard-library modules pair well with `mimetypes`; explore the `python` domain of this catalog.
