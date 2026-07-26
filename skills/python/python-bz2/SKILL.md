---
name: python-bz2
description: "Program with Python's bz2 module: Interface to the libbzip2 compression library."
version: 1.0.0
tags: [bz2, programming, python, stdlib]
---

# Python: `bz2`

## Overview

Interface to the libbzip2 compression library.

This module provides a file interface, classes for incremental
(de)compression, and functions for one-shot (de)compression.

## When to use

Reach for `bz2` when your task calls for Interface to the libbzip2 compression library. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import bz2
```

## Key functions

- `bz2.compress(data, compresslevel=9)`
- `bz2.decompress(data)`
- `bz2.open(filename, mode='rb', compresslevel=9, encoding=None, errors=None, newline=None)`

## Key classes

`BZ2Compressor`, `BZ2Decompressor`, `BZ2File`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import bz2

def do_work(...):
    """Use bz2 to accomplish one well-defined task."""
    result = bz2.compress(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `bz2` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module bz2

NAME
    bz2 - Interface to the libbzip2 compression library.

MODULE REFERENCE
    https://docs.python.org/3.14/library/bz2.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides a file interface, classes for incremental
    (de)compression, and functions for one-shot (de)compression.

CLASSES
    builtins.object
        _bz2.BZ2Compressor
        _bz2.BZ2Decompressor
    compression._common._streams.BaseStream(io.BufferedIOBase)
        BZ2File

    class BZ2Compressor(builtins.object)
     |  BZ2Compressor(compresslevel=9, /)
     |
     |  Create a compressor object for compressing data incrementally.
     |
     |    compresslevel
     |      Compression level, as a number between 1 and 9.
     |
     |  For one-shot compression, use the compress() function instead.
     |
     |  Methods defined here:
     |
     |  compress(self, data, /)
     |      Provide data to the compressor object.
     |
     |      Returns a chunk of compressed data if possible, or b'' otherwise.
     |
     |      When you have finished providing data to the compressor, call the
     |      flush() method to finish the compression process.
     |
     |  flush(self, /)
     |      Finish the compression process.
     |
     |      Returns the compressed data left in internal buffers.
     |
     |      The compressor object may not be used after this method is called.
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs)
     |      Create and return a new object.  See help(type) for accurate signature.

    class BZ2Decompressor(builtins.object)
     |  Create a decompressor object for decompressing data incrementally.
     |
     |  For one-shot decompression, use the decompress() function instead.
     |
     |  Methods defined here:
     |
     |  decompress(self, /, data, max_length=-1)
     |      Decompress *data*, returning uncompressed data as bytes.
     |
     |      If *max_length* is nonnegative, returns at most *max_length* bytes of
     |      decompressed data. If this limit is reached and further output can be
     |      produced, *self.needs_input* will be set to ``False``. In this case, the next
     |      call to *decompress()* may provide *data* as b'' to obtain more of the output.
     |
     |      If all of the input data was decompressed and returned (either because this
     |      was less than *max_length* bytes, or because *max_length* was negative),
     |      *self.needs_input* will be set to True.
     |
     |      Attempting to decompress data after the end of stream is reached raises an
     |      EOFError.  Any data found after the end of the stream is ignored and saved in
     |      the unused_data attribute.
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs)
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  eof
     |      True if the end-of-stream marker has been reached.
     |
     |  needs_input
     |      True if more input is needed before more decompressed data can be produced.
     |
     |  unused_data
     |      Data found after the end of the compressed stream.

    class BZ2File(compression._common._streams.BaseStream)
     |  BZ2File(filename, mode='r', *, compresslevel=9)
     |
     |  A file object providing transparent bzip2 (de)compression.
     |
     |  A BZ2File can act as a wrapper for an existing file object, or refer
     |  directly to a named file on disk.
     |
     |  Note that BZ2File provides a *binary* file interface - data read is
     |  returned as bytes, and data to be written should be given as bytes.
     |
     |  Method resolution order:
     |      BZ2File
     |      compression._common._streams.BaseStream
     |      io.BufferedIOBase
     |      _io._BufferedIOBase
     |      io.IOBase
     |      _io._IOBase
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, filename, mode='r', *, compresslevel=9)
     |      Open a bzip2-compressed file.
     |
     |      If filename is a str, bytes, or PathLike object, it gives the
     |      name of the file to be opened. Otherwise, it should be a file
     |      object, which will be used to read or write the compressed data.
     |
     |      mode can be 'r' for reading (default), 'w' for (over)writing,
     |      'x' for creating exclusively, or 'a' for appending. These can
     |      equivalently be given as 'rb', 'wb', 'xb', and 'ab'.
     |
     |      If mode is 'w', 'x' or 'a', compresslevel can be a number between 1
     |      and 9 specifying the level of compression: 1 produces the least
     |      compression, and 9 (default) produces the most compression.
     |
     |      If mode is 'r', the input file may be the concatenation of
     |      multiple compressed streams.
     |
     |  close(self)
     |      Flush and close the file.
     |
     |      May be called more than once without error. Once the file is
     |      closed, any other operation on it will raise a ValueError.
     |
     |  fileno(self)
     |      Return the file descriptor for the underlying file.
     |
     |  peek(self, n=0)
     |      Return buffered data without advancing the file position.
     |
     |      Always returns at least one byte of data, unless at EOF.
     |      The exact number of byte
```

## Related

Other standard-library modules pair well with `bz2`; explore the `python` domain of this catalog.
