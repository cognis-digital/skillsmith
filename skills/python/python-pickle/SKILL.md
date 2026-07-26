---
name: python-pickle
description: "Program with Python's pickle module: Create portable serialized representations of Python objects."
version: 1.0.0
tags: [pickle, programming, python, stdlib]
---

# Python: `pickle`

## Overview

Create portable serialized representations of Python objects.

See module copyreg for a mechanism for registering custom picklers.
See module pickletools source for extensive comments.

Classes:

    Pickler
    Unpickler

Functions:

    dump(object, file)
    dumps(object) -> string
    load(file) -> object
    loads(bytes) -> object

Misc variables:

    __version__
    format_version
    compatible_formats

## When to use

Reach for `pickle` when your task calls for Create portable serialized representations of Python objects. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import pickle
```

## Key functions

- `pickle.decode_long(data)`
- `pickle.dump(obj, file, protocol=None, *, fix_imports=True, buffer_callback=None)`
- `pickle.dumps(obj, protocol=None, *, fix_imports=True, buffer_callback=None)`
- `pickle.encode_long(x)`
- `pickle.load(file, *, fix_imports=True, encoding='ASCII', errors='strict', buffers=())`
- `pickle.loads(data, /, *, fix_imports=True, encoding='ASCII', errors='strict', buffers=())`
- `pickle.pack(...)`
- `pickle.unpack(format, buffer, /)`
- `pickle.whichmodule(obj, name)`

## Key classes

`FunctionType`, `PickleBuffer`, `PickleError`, `Pickler`, `PicklingError`, `Unpickler`, `UnpicklingError`, `batched`, `partial`

## Constants / attributes

`ADDITEMS`, `APPEND`, `APPENDS`, `BINBYTES`, `BINBYTES8`, `BINFLOAT`, `BINGET`, `BININT`, `BININT1`, `BININT2`, `BINPERSID`, `BINPUT`, `BINSTRING`, `BINUNICODE`, `BINUNICODE8`, `BUILD`, `BYTEARRAY8`, `DEFAULT_PROTOCOL`, `DICT`, `DUP`, `EMPTY_DICT`, `EMPTY_LIST`, `EMPTY_SET`, `EMPTY_TUPLE`, `EXT1`, `EXT2`, `EXT4`, `FALSE`, `FLOAT`, `FRAME`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import pickle

def do_work(...):
    """Use pickle to accomplish one well-defined task."""
    result = pickle.decode_long(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `pickle` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module pickle

NAME
    pickle - Create portable serialized representations of Python objects.

MODULE REFERENCE
    https://docs.python.org/3.14/library/pickle.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    See module copyreg for a mechanism for registering custom picklers.
    See module pickletools source for extensive comments.

    Classes:

        Pickler
        Unpickler

    Functions:

        dump(object, file)
        dumps(object) -> string
        load(file) -> object
        loads(bytes) -> object

    Misc variables:

        __version__
        format_version
        compatible_formats

CLASSES
    builtins.Exception(builtins.BaseException)
        _pickle.PickleError
            _pickle.PicklingError
            _pickle.UnpicklingError
    builtins.object
        _pickle.Pickler
        _pickle.Unpickler
        PickleBuffer

    class PickleBuffer(builtins.object)
     |  Wrapper for potentially out-of-band buffers
     |
     |  Methods defined here:
     |
     |  __buffer__(self, flags, /)
     |      Return a buffer object that exposes the underlying memory of the object.
     |
     |  __release_buffer__(self, buffer, /)
     |      Release the buffer object that exposes the underlying memory of the object.
     |
     |  raw(self, /)
     |      Return a memoryview of the raw memory underlying this buffer.
     |      Will raise BufferError is the buffer isn't contiguous.
     |
     |  release(self, /)
     |      Release the underlying buffer exposed by the PickleBuffer object.
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs)
     |      Create and return a new object.  See help(type) for accurate signature.

    class PickleError(builtins.Exception)
     |  Method resolution order:
     |      PickleError
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

    class Pickler(builtins.object)
     |  Pickler(file, protocol=None, fix_imports=True, buffer_callback=None)
     |
     |  This takes a binary file for writing a pickle data stream.
     |
     |  The optional *protocol* argument tells the pickler to use the given
     |  protocol; supported protocols are 0, 1, 2, 3, 4 and 5.  The default
     |  protocol is 5. It was introduced in Python 3.8, and is incompatible
     |  with previous versions.
     |
     |  Specifying a negative protocol version selects the highest protocol
     |  version supported.  The higher the protocol used, the more recent the
     |  version of Python needed to read the pickle produced.
     |
     |  The *file* argument must have a write() method that accepts a single
     |  bytes argument. It can thus be a file object opened for binary
     |  writing, an io.BytesIO instance, or any other custom object that meets
     |  this interface.
     |
     |  If *fix_imports* is True and protocol is less than 3, pickle will try
     |  to map the new Python 3 names to the old module names used in Python
     |  2, so that the pickle data stream is readable with Python 2.
     |
     |  If *buffer_callback* is None (the default), buffer views are
     |  serialized into *file* as part of the pickle stream.
     |
     |  If *buffer_callback* is not None, then it can be called any number
     |  of times with a buffer view.  If the callback returns a false value
     |  (such as None), the given buffer is out-of-band; otherwise the
     |  buffer is serialized in-band, i.e. inside the pickle stream.
     |
     |  It is an error if *buffer_callback* is not None and *protocol*
     |  is None or smaller than 5.
     |
     |  Methods defined here:
     |
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __sizeof__(self, /)
     |      Returns size in memory, in bytes.
     |
     |  clear_memo(self, /)
     |      Clears t
```

## Related

Other standard-library modules pair well with `pickle`; explore the `python` domain of this catalog.
