---
name: python-zipfile
description: "Program with Python's zipfile module: Read and write ZIP files."
version: 1.0.0
tags: [programming, python, stdlib, zipfile]
---

# Python: `zipfile`

## Overview

Read and write ZIP files.

XXX references to utf-8 need further investigation.

## When to use

Reach for `zipfile` when your task calls for Read and write ZIP files. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import zipfile
```

## Key functions

- `zipfile.crc32(data, value=0, /)`
- `zipfile.is_zipfile(filename)`
- `zipfile.main(args=None)`

## Key classes

`BadZipFile`, `BadZipfile`, `CompleteDirs`, `LZMACompressor`, `LZMADecompressor`, `LargeZipFile`, `Path`, `PyZipFile`, `ZipExtFile`, `ZipFile`, `ZipInfo`, `error`

## Constants / attributes

`BZIP2_VERSION`, `DEFAULT_VERSION`, `LZMA_VERSION`, `MAX_EXTRACT_VERSION`, `ZIP64_LIMIT`, `ZIP64_VERSION`, `ZIP_BZIP2`, `ZIP_DEFLATED`, `ZIP_FILECOUNT_LIMIT`, `ZIP_LZMA`, `ZIP_MAX_COMMENT`, `ZIP_STORED`, `ZIP_ZSTANDARD`, `ZSTANDARD_VERSION`, `compressor_names`, `sizeCentralDir`, `sizeEndCentDir`, `sizeEndCentDir64`, `sizeEndCentDir64Locator`, `sizeFileHeader`, `stringCentralDir`, `stringEndArchive`, `stringEndArchive64`, `stringEndArchive64Locator`, `stringFileHeader`, `structCentralDir`, `structEndArchive`, `structEndArchive64`, `structEndArchive64Locator`, `structFileHeader`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import zipfile

def do_work(...):
    """Use zipfile to accomplish one well-defined task."""
    result = zipfile.crc32(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `zipfile` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: package zipfile

NAME
    zipfile - Read and write ZIP files.

MODULE REFERENCE
    https://docs.python.org/3.14/library/zipfile.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    XXX references to utf-8 need further investigation.

PACKAGE CONTENTS
    __main__
    _path (package)

CLASSES
    builtins.Exception(builtins.BaseException)
        BadZipFile
        LargeZipFile
    builtins.object
        ZipFile
            PyZipFile
        ZipInfo
        zipfile._path.Path

    class BadZipFile(builtins.Exception)
     |  Method resolution order:
     |      BadZipFile
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors defined here:
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |
     |  __new__(*args, **kwargs) class method of builtins.Exception
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__(self, /)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setstate__(self, state, /)
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  add_note(self, note, /)
     |      Add a note to the exception
     |
     |  with_traceback(self, tb, /)
     |      Set self.__traceback__ to tb and return self.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |
     |  __cause__
     |
     |  __context__
     |
     |  __dict__
     |
     |  __suppress_context__
     |
     |  __traceback__
     |
     |  args

    BadZipfile = class BadZipFile(builtins.Exception)
     |  Method resolution order:
     |      BadZipFile
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors defined here:
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |
     |  __new__(*args, **kwargs) class method of builtins.Exception
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__(self, /)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setstate__(self, state, /)
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  add_note(self, note, /)
     |      Add a note to the exception
     |
     |  with_traceback(self, tb, /)
     |      Set self.__traceback__ to tb and return self.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |
     |  __cause__
     |
     |  __context__
     |
     |  __dict__
     |
     |  __suppress_context__
     |
     |  __traceback__
     |
     |  args

    class LargeZipFile(builtins.Exception)
     |  Raised when writing a zipfile, the zipfile requires ZIP64 extensions
     |  and those extensions are disabled.
     |
     |  Method resolution order:
     |      LargeZipFile
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors defined here:
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |
     |  __new__(*args, **kwargs) class method of builtins.Exception
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__(self, /)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setstate__(self, state, /)
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  add_note(self, note, /)
     |      Add a note to the exception
     |
     |  with_traceback(self, tb, /)
     |      Set self.__traceback__ to tb and return self.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |
     |  __cause__
     |
     |  __context__
     |
     |  __dict__
     |
     |  __suppress_context__
     |
     |  __traceback__
     |
     |  args

    class Path(builtins.object)
     |  Path(root, at='')
     |
     |  A :class:`importlib.resources.abc.Traversable` interface for zip files.
     |
     |  Implements many of the features users enjoy from
     |  :cl
```

## Related

Other standard-library modules pair well with `zipfile`; explore the `python` domain of this catalog.
