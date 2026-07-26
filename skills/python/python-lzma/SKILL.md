---
name: python-lzma
description: "Program with Python's lzma module: Interface to the liblzma compression library."
version: 1.0.0
tags: [lzma, programming, python, stdlib]
---

# Python: `lzma`

## Overview

Interface to the liblzma compression library.

This module provides a class for reading and writing compressed files,
classes for incremental (de)compression, and convenience functions for
one-shot (de)compression.

These classes and functions support both the XZ and legacy LZMA
container formats, as well as raw compressed data streams.

## When to use

Reach for `lzma` when your task calls for Interface to the liblzma compression library. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import lzma
```

## Key functions

- `lzma.compress(data, format=1, check=-1, preset=None, filters=None)`
- `lzma.decompress(data, format=0, memlimit=None, filters=None)`
- `lzma.is_check_supported(check_id, /)`
- `lzma.open(filename, mode='rb', *, format=None, check=-1, preset=None, filters=None, encoding=None, errors=None, newline=None)`

## Key classes

`LZMACompressor`, `LZMADecompressor`, `LZMAError`, `LZMAFile`

## Constants / attributes

`CHECK_CRC32`, `CHECK_CRC64`, `CHECK_ID_MAX`, `CHECK_NONE`, `CHECK_SHA256`, `CHECK_UNKNOWN`, `FILTER_ARM`, `FILTER_ARMTHUMB`, `FILTER_DELTA`, `FILTER_IA64`, `FILTER_LZMA1`, `FILTER_LZMA2`, `FILTER_POWERPC`, `FILTER_SPARC`, `FILTER_X86`, `FORMAT_ALONE`, `FORMAT_AUTO`, `FORMAT_RAW`, `FORMAT_XZ`, `MF_BT2`, `MF_BT3`, `MF_BT4`, `MF_HC3`, `MF_HC4`, `MODE_FAST`, `MODE_NORMAL`, `PRESET_DEFAULT`, `PRESET_EXTREME`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import lzma

def do_work(...):
    """Use lzma to accomplish one well-defined task."""
    result = lzma.compress(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `lzma` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module lzma

NAME
    lzma - Interface to the liblzma compression library.

MODULE REFERENCE
    https://docs.python.org/3.14/library/lzma.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides a class for reading and writing compressed files,
    classes for incremental (de)compression, and convenience functions for
    one-shot (de)compression.

    These classes and functions support both the XZ and legacy LZMA
    container formats, as well as raw compressed data streams.

CLASSES
    builtins.Exception(builtins.BaseException)
        _lzma.LZMAError
    builtins.object
        _lzma.LZMACompressor
        _lzma.LZMADecompressor
    compression._common._streams.BaseStream(io.BufferedIOBase)
        LZMAFile

    class LZMACompressor(builtins.object)
     |  LZMACompressor(format=FORMAT_XZ, check=-1, preset=None, filters=None)
     |
     |  Create a compressor object for compressing data incrementally.
     |
     |  format specifies the container format to use for the output. This can
     |  be FORMAT_XZ (default), FORMAT_ALONE, or FORMAT_RAW.
     |
     |  check specifies the integrity check to use. For FORMAT_XZ, the default
     |  is CHECK_CRC64. FORMAT_ALONE and FORMAT_RAW do not support integrity
     |  checks; for these formats, check must be omitted, or be CHECK_NONE.
     |
     |  The settings used by the compressor can be specified either as a
     |  preset compression level (with the 'preset' argument), or in detail
     |  as a custom filter chain (with the 'filters' argument). For FORMAT_XZ
     |  and FORMAT_ALONE, the default is to use the PRESET_DEFAULT preset
     |  level. For FORMAT_RAW, the caller must always specify a filter chain;
     |  the raw compressor does not support preset compression levels.
     |
     |  preset (if provided) should be an integer in the range 0-9, optionally
     |  OR-ed with the constant PRESET_EXTREME.
     |
     |  filters (if provided) should be a sequence of dicts. Each dict should
     |  have an entry for "id" indicating the ID of the filter, plus
     |  additional entries for options to the filter.
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

    class LZMADecompressor(builtins.object)
     |  LZMADecompressor(format=0, memlimit=None, filters=None)
     |
     |  Create a decompressor object for decompressing data incrementally.
     |
     |    format
     |      Specifies the container format of the input stream.  If this is
     |      FORMAT_AUTO (the default), the decompressor will automatically detect
     |      whether the input is FORMAT_XZ or FORMAT_ALONE.  Streams created with
     |      FORMAT_RAW cannot be autodetected.
     |    memlimit
     |      Limit the amount of memory used by the decompressor.  This will cause
     |      decompression to fail if the input cannot be decompressed within the
     |      given limit.
     |    filters
     |      A custom filter chain.  This argument is required for FORMAT_RAW, and
     |      not accepted with any other format.  When provided, this should be a
     |      sequence of dicts, each indicating the ID and options for a single
     |      filter.
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
     |  check
     |      ID of the integrity check used by the input stream.
     |
     |  eof
     |      True if the end-of-stream marker has been reached.
     |
     |  needs_input
     |      True if more input is 
```

## Related

Other standard-library modules pair well with `lzma`; explore the `python` domain of this catalog.
