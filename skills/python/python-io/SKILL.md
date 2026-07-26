---
name: python-io
description: "Program with Python's io module: The io module provides the Python interfaces to stream handling."
version: 1.0.0
tags: [io, programming, python, stdlib]
---

# Python: `io`

## Overview

The io module provides the Python interfaces to stream handling. The
builtin open function is defined in this module.

At the top of the I/O hierarchy is the abstract base class IOBase. It
defines the basic interface to a stream. Note, however, that there is no
separation between reading and writing to streams; implementations are
allowed to raise an OSError if they do not support a given operation.

Extending IOBase is RawIOBase which deals simply with the reading and
writing of raw bytes to a stream. FileIO subclasses RawIOBase to provide
an interface to OS files.

BufferedIOBase deals with buffering on a raw byte stream (RawIOBase). Its
subclasses, BufferedWriter, BufferedReader, and BufferedRWPair buffer
streams that are readable, writable, and both respectively.
BufferedRandom provides a buffered interface to random access
streams. BytesIO is a simple stream of in-memory bytes.

Another IOBase subclass, TextIOBase, deals with the encoding and decoding
of streams into text. TextIOWrapper, which extends it, is a buffered text
interface to a buffered raw stream (`BufferedIOBase`). Finally, StringIO
is an in-memory stream for text.

Argument names are not part of the specification, and only the arguments
of open() are intended to be used as keyword arguments.

data:

DEFAULT_BUFFER_SIZE

   An int containing the default buffer size used by the module's buffered
   I/O classes. open() uses the file's blksize (as obtained by os.stat) if
   possible.

## When to use

Reach for `io` when your task calls for The io module provides the Python interfaces to stream handling. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import io
```

## Key functions

- `io.open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`
- `io.open_code(path)`
- `io.text_encoding(encoding, stacklevel=2, /)`

## Key classes

`BlockingIOError`, `BufferedIOBase`, `BufferedRWPair`, `BufferedRandom`, `BufferedReader`, `BufferedWriter`, `BytesIO`, `FileIO`, `GenericAlias`, `IOBase`, `IncrementalNewlineDecoder`, `RawIOBase`, `Reader`, `StringIO`, `TextIOBase`, `TextIOWrapper`, `UnsupportedOperation`, `Writer`

## Constants / attributes

`DEFAULT_BUFFER_SIZE`, `SEEK_CUR`, `SEEK_END`, `SEEK_SET`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import io

def do_work(...):
    """Use io to accomplish one well-defined task."""
    result = io.open(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `io` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module io

NAME
    io

MODULE REFERENCE
    https://docs.python.org/3.14/library/io.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    The io module provides the Python interfaces to stream handling. The
    builtin open function is defined in this module.

    At the top of the I/O hierarchy is the abstract base class IOBase. It
    defines the basic interface to a stream. Note, however, that there is no
    separation between reading and writing to streams; implementations are
    allowed to raise an OSError if they do not support a given operation.

    Extending IOBase is RawIOBase which deals simply with the reading and
    writing of raw bytes to a stream. FileIO subclasses RawIOBase to provide
    an interface to OS files.

    BufferedIOBase deals with buffering on a raw byte stream (RawIOBase). Its
    subclasses, BufferedWriter, BufferedReader, and BufferedRWPair buffer
    streams that are readable, writable, and both respectively.
    BufferedRandom provides a buffered interface to random access
    streams. BytesIO is a simple stream of in-memory bytes.

    Another IOBase subclass, TextIOBase, deals with the encoding and decoding
    of streams into text. TextIOWrapper, which extends it, is a buffered text
    interface to a buffered raw stream (`BufferedIOBase`). Finally, StringIO
    is an in-memory stream for text.

    Argument names are not part of the specification, and only the arguments
    of open() are intended to be used as keyword arguments.

    data:

    DEFAULT_BUFFER_SIZE

       An int containing the default buffer size used by the module's buffered
       I/O classes. open() uses the file's blksize (as obtained by os.stat) if
       possible.

CLASSES
    _io._BufferedIOBase(_io._IOBase)
        _io.BufferedRWPair
        _io.BufferedRandom
        _io.BufferedReader
        _io.BufferedWriter
        _io.BytesIO
        BufferedIOBase(_io._BufferedIOBase, IOBase)
    _io._IOBase(builtins.object)
        IOBase
            BufferedIOBase(_io._BufferedIOBase, IOBase)
            RawIOBase(_io._RawIOBase, IOBase)
            TextIOBase(_io._TextIOBase, IOBase)
    _io._RawIOBase(_io._IOBase)
        _io.FileIO
        RawIOBase(_io._RawIOBase, IOBase)
    _io._TextIOBase(_io._IOBase)
        _io.StringIO
        _io.TextIOWrapper
        TextIOBase(_io._TextIOBase, IOBase)
    builtins.OSError(builtins.Exception)
        builtins.BlockingIOError
        UnsupportedOperation(builtins.OSError, builtins.ValueError)
    builtins.ValueError(builtins.Exception)
        UnsupportedOperation(builtins.OSError, builtins.ValueError)
    builtins.object
        _io.IncrementalNewlineDecoder
        Reader
        Writer

    class BlockingIOError(OSError)
     |  I/O operation would block.
     |
     |  Method resolution order:
     |      BlockingIOError
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |
     |  Methods inherited from OSError:
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
     |  Static methods inherited from OSError:
     |
     |  __new__(*args, **kwargs) class method of builtins.OSError
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from OSError:
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
     |  Methods inherited from BaseException:
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
     |  Data descriptors inherited from BaseException:
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

    class BufferedIOBase(_io._BufferedIOBase, IOBase)
     |  Base class for buffered IO objects.
     |
     |  The main difference with RawIOBase is that the read() method
     |  supports omitting the size argument, and does not have a default
     |  implementation that defers to readinto().
     |
     |  In addition, read(), readinto() and write() may raise
     |  BlockingIOError if the underlying raw stream is in non-blocking
     |  mode and not ready; unlike their raw counterparts, they will never
     |  return None.
     |
     |  A typical implementation should not inherit from a RawIOBase
     |  implementation, but wrap one.
     |
     |  Method resolution order:
     |      BufferedIOBase
     |      _io._BufferedIOBase
     |      IOBase
     |      _io._IOBase
     |      builtins.object
     |
     |  Data and other attributes defined here:
     |
     |  __abstractmethods__ = frozenset()
     |
     |  -------------------------------------------------------------
```

## Related

Other standard-library modules pair well with `io`; explore the `python` domain of this catalog.
