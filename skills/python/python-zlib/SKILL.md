---
name: python-zlib
description: "Program with Python's zlib module: The functions in this module allow compression and decompression using the zlib library, which is based on GNU zip."
version: 1.0.0
tags: [programming, python, stdlib, zlib]
---

# Python: `zlib`

## Overview

The functions in this module allow compression and decompression using the
zlib library, which is based on GNU zip.

adler32(string[, start]) -- Compute an Adler-32 checksum.
compress(data[, level]) -- Compress data, with compression level 0-9 or -1.
compressobj([level[, ...]]) -- Return a compressor object.
crc32(string[, start]) -- Compute a CRC-32 checksum.
decompress(string,[wbits],[bufsize]) -- Decompresses a compressed string.
decompressobj([wbits[, zdict]]) -- Return a decompressor object.

'wbits' is window buffer size and container format.
Compressor objects support compress() and flush() methods; decompressor
objects support decompress() and flush().

## When to use

Reach for `zlib` when your task calls for The functions in this module allow compression and decompression using the zlib library, which is based on GNU zip. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import zlib
```

## Key functions

- `zlib.adler32(data, value=1, /)`
- `zlib.compress(data, /, level=-1, wbits=15)`
- `zlib.compressobj(level=-1, method=8, wbits=15, memLevel=8, strategy=0, zdict=None)`
- `zlib.crc32(data, value=0, /)`
- `zlib.decompress(data, /, wbits=15, bufsize=16384)`
- `zlib.decompressobj(wbits=15, zdict=b'')`

## Key classes

`error`

## Constants / attributes

`DEFLATED`, `DEF_BUF_SIZE`, `DEF_MEM_LEVEL`, `MAX_WBITS`, `ZLIBNG_VERSION`, `ZLIB_RUNTIME_VERSION`, `ZLIB_VERSION`, `Z_BEST_COMPRESSION`, `Z_BEST_SPEED`, `Z_BLOCK`, `Z_DEFAULT_COMPRESSION`, `Z_DEFAULT_STRATEGY`, `Z_FILTERED`, `Z_FINISH`, `Z_FIXED`, `Z_FULL_FLUSH`, `Z_HUFFMAN_ONLY`, `Z_NO_COMPRESSION`, `Z_NO_FLUSH`, `Z_PARTIAL_FLUSH`, `Z_RLE`, `Z_SYNC_FLUSH`, `Z_TREES`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import zlib

def do_work(...):
    """Use zlib to accomplish one well-defined task."""
    result = zlib.adler32(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `zlib` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: built-in module zlib

NAME
    zlib

DESCRIPTION
    The functions in this module allow compression and decompression using the
    zlib library, which is based on GNU zip.

    adler32(string[, start]) -- Compute an Adler-32 checksum.
    compress(data[, level]) -- Compress data, with compression level 0-9 or -1.
    compressobj([level[, ...]]) -- Return a compressor object.
    crc32(string[, start]) -- Compute a CRC-32 checksum.
    decompress(string,[wbits],[bufsize]) -- Decompresses a compressed string.
    decompressobj([wbits[, zdict]]) -- Return a decompressor object.

    'wbits' is window buffer size and container format.
    Compressor objects support compress() and flush() methods; decompressor
    objects support decompress() and flush().

CLASSES
    builtins.Exception(builtins.BaseException)
        error

    class error(builtins.Exception)
     |  Method resolution order:
     |      error
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

FUNCTIONS
    adler32(data, value=1, /)
        Compute an Adler-32 checksum of data.

          value
            Starting value of the checksum.

        The returned checksum is an integer.

    compress(data, /, level=-1, wbits=15)
        Returns a bytes object containing compressed data.

        data
          Binary data to be compressed.
        level
          Compression level, in 0-9 or -1.
        wbits
          The window buffer size and container format.

    compressobj(level=-1, method=8, wbits=15, memLevel=8, strategy=0, zdict=None)
        Return a compressor object.

        level
          The compression level (an integer in the range 0-9 or -1; default is
          currently equivalent to 6).  Higher compression levels are slower,
          but produce smaller results.
        method
          The compression algorithm.  If given, this must be DEFLATED.
        wbits
          +9 to +15: The base-two logarithm of the window size.  Include a zlib
              container.
          -9 to -15: Generate a raw stream.
          +25 to +31: Include a gzip container.
        memLevel
          Controls the amount of memory used for internal compression state.
          Valid values range from 1 to 9.  Higher values result in higher memory
          usage, faster compression, and smaller output.
        strategy
          Used to tune the compression algorithm.  Possible values are
          Z_DEFAULT_STRATEGY, Z_FILTERED, and Z_HUFFMAN_ONLY.
        zdict
          The predefined compression dictionary - a sequence of bytes
          containing subsequences that are likely to occur in the input data.

    crc32(data, value=0, /)
        Compute a CRC-32 checksum of data.

          value
            Starting value of the checksum.

        The returned checksum is an integer.

    decompress(data, /, wbits=15, bufsize=16384)
        Returns a bytes object containing the uncompressed data.

        data
          Compressed data.
        wbits
          The window buffer size and container format.
        bufsize
          The initial output buffer size.

    decompressobj(wbits=15, zdict=b'')
        Return a decompressor object.

        wbits
          The window buffer size and container format.
        zdict
          The predefined compression dictionary.  This must be the same
          dictionary as used by the compressor that produced the input data.

DATA
    DEFLATED = 8
    DEF_BUF_SIZE = 16384
    DEF_MEM_LEVEL = 8
    MAX_WBITS = 15
    ZLIBNG_VERSION = '2.2.4'
    ZLIB_RUNTIME_VERSION = '1.3.1.zlib-ng'
    ZLIB_VERSION = '1.3.1.zlib-ng'
    Z_BEST_COMPRESSION = 9
    Z_BEST_SPEED = 1
    Z_BLOCK = 5
    Z_DEFAULT_COMPRESSION = -1
    Z_DEFAULT_STRATEGY = 0
    Z_FILTERED = 1
    Z_FINISH = 4
    Z_FIXED = 4
    Z_FULL_FLUSH = 3
    Z_HUFFMAN_ONLY = 2
    Z_NO_COMPRESSION = 0
    Z_NO_FLUSH = 0
    Z_PARTIAL_FLUSH = 1
    Z_RLE = 3
    Z_SYNC_FLUSH = 2
    Z_TREES = 6

VERSION
    1.0

FILE
    (built-in)


```

## Related

Other standard-library modules pair well with `zlib`; explore the `python` domain of this catalog.
