---
name: python-gzip
description: "Program with Python's gzip module: Functions that read and write gzipped files."
version: 1.0.0
tags: [gzip, programming, python, stdlib]
---

# Python: `gzip`

## Overview

Functions that read and write gzipped files.

The user of the file doesn't have to worry about the compression,
but random access is not allowed.

## When to use

Reach for `gzip` when your task calls for Functions that read and write gzipped files. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import gzip
```

## Key functions

- `gzip.compress(data, compresslevel=9, *, mtime=0)`
- `gzip.decompress(data)`
- `gzip.main()`
- `gzip.open(filename, mode='rb', compresslevel=9, encoding=None, errors=None, newline=None)`
- `gzip.write32u(output, value)`

## Key classes

`BadGzipFile`, `GzipFile`

## Constants / attributes

`FCOMMENT`, `FEXTRA`, `FHCRC`, `FNAME`, `FTEXT`, `READ`, `READ_BUFFER_SIZE`, `WRITE`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import gzip

def do_work(...):
    """Use gzip to accomplish one well-defined task."""
    result = gzip.compress(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `gzip` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module gzip

NAME
    gzip - Functions that read and write gzipped files.

MODULE REFERENCE
    https://docs.python.org/3.14/library/gzip.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    The user of the file doesn't have to worry about the compression,
    but random access is not allowed.

CLASSES
    builtins.OSError(builtins.Exception)
        BadGzipFile
    compression._common._streams.BaseStream(io.BufferedIOBase)
        GzipFile

    class BadGzipFile(builtins.OSError)
     |  Exception raised in some cases for invalid gzip files.
     |
     |  Method resolution order:
     |      BadGzipFile
     |      builtins.OSError
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
     |  Methods inherited from builtins.OSError:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__(self, /)
     |      Helper for pickle.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.OSError:
     |
     |  __new__(*args, **kwargs) class method of builtins.OSError
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.OSError:
     |
     |  characters_written
     |
     |  errno
     |      POSIX exception code
     |
     |  filename
     |      exception filename
     |
     |  filename2
     |      second exception filename
     |
     |  strerror
     |      exception strerror
     |
     |  winerror
     |      Win32 exception code
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setstate__(self, state, /)
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

    class GzipFile(compression._common._streams.BaseStream)
     |  GzipFile(filename=None, mode=None, compresslevel=9, fileobj=None, mtime=None)
     |
     |  The GzipFile class simulates most of the methods of a file object with
     |  the exception of the truncate() method.
     |
     |  This class only supports opening files in binary mode. If you need to open a
     |  compressed file in text mode, use the gzip.open() function.
     |
     |  Method resolution order:
     |      GzipFile
     |      compression._common._streams.BaseStream
     |      io.BufferedIOBase
     |      _io._BufferedIOBase
     |      io.IOBase
     |      _io._IOBase
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __del__(self)
     |      Called when the instance is about to be destroyed.
     |
     |  __init__(
     |      self,
     |      filename=None,
     |      mode=None,
     |      compresslevel=9,
     |      fileobj=None,
     |      mtime=None
     |  )
     |      Constructor for the GzipFile class.
     |
     |      At least one of fileobj and filename must be given a
     |      non-trivial value.
     |
     |      The new class instance is based on fileobj, which can be a regular
     |      file, an io.BytesIO object, or any other object which simulates a file.
     |      It defaults to None, in which case filename is opened to provide
     |      a file object.
     |
     |      When fileobj is not None, the filename argument is only used to be
     |      included in the gzip file header, which may include the original
     |      filename of the uncompressed file.  It defaults to the filename of
     |      fileobj, if discernible; otherwise, it defaults to the empty string,
     |      and in this case the original filename is not included in the header.
     |
     |      The mode argument can be any of 'r', 'rb', 'a', 'ab', 'w', 'wb', 'x', or
     |      'xb' depending on whether the file will be read or written.  The default
     |      is the mode of fileobj if discernible; otherwise, the default is 'rb'.
     |      A mode of 'r' is equivalent to one of 'rb', and similarly for 'w' and
     |      'wb', 'a' and 'ab', and 'x' and 'xb'.
     |
     |      The compresslevel argument is an integer from 0 to 9 controlling the
     |      level of compression; 1 is fastest and produces the least compression,
     |      and 9 is slowest and produces the most compression. 0 is no compression
     |      at all. The default is 9.
     |
     |      The optional mtime argument is the timestamp requested by gzip. The time
     |      is in Unix format, i.e., seconds since 00:00:00 UTC, January 1, 1970.
     |      If mtime is omitted or None, the current time is used. Use mtime = 0
     |      to generate a compressed stream that does not depend on creation time.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  clo
```

## Related

Other standard-library modules pair well with `gzip`; explore the `python` domain of this catalog.
