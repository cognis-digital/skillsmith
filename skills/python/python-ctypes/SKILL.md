---
name: python-ctypes
description: "Program with Python's ctypes module: create and manipulate C data types in Python"
version: 1.0.0
tags: [ctypes, programming, python, stdlib]
---

# Python: `ctypes`

## Overview

create and manipulate C data types in Python

## When to use

Reach for `ctypes` when your task calls for create and manipulate C data types in Python. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import ctypes
```

## Key functions

- `ctypes.ARRAY(typ, len)`
- `ctypes.CFUNCTYPE(restype, *argtypes, **kw)`
- `ctypes.CopyComPointer(...)`
- `ctypes.DllCanUnloadNow()`
- `ctypes.DllGetClassObject(rclsid, riid, ppv)`
- `ctypes.FormatError(...)`
- `ctypes.GetLastError(*args, **kwargs)`
- `ctypes.POINTER(cls)`
- `ctypes.PYFUNCTYPE(restype, *argtypes)`
- `ctypes.SetPointerType(pointer, cls)`
- `ctypes.WINFUNCTYPE(restype, *argtypes, **kw)`
- `ctypes.WinError(code=None, descr=None)`
- `ctypes.addressof(obj, /)`
- `ctypes.alignment(object, /)`
- `ctypes.byref(obj, offset=0, /)`
- `ctypes.c_buffer(init, size=None)`
- `ctypes.cast(obj, typ)`
- `ctypes.create_string_buffer(init, size=None)`
- `ctypes.create_unicode_buffer(init, size=None)`
- `ctypes.get_errno()`
- `ctypes.get_last_error()`
- `ctypes.memmove(*args, **kwargs)`
- `ctypes.memoryview_at(ptr, size, readonly=False)`
- `ctypes.memset(*args, **kwargs)`
- `ctypes.pointer(obj)`
- `ctypes.resize(obj, size, /)`
- `ctypes.set_errno(...)`
- `ctypes.set_last_error(...)`
- `ctypes.sizeof(obj, /)`
- `ctypes.string_at(ptr, size=-1)`

## Key classes

`ArgumentError`, `Array`, `BigEndianStructure`, `BigEndianUnion`, `CDLL`, `CField`, `COMError`, `HRESULT`, `LibraryLoader`, `LittleEndianStructure`, `LittleEndianUnion`, `OleDLL`, `PyDLL`, `Structure`, `Union`, `WinDLL`, `c_bool`, `c_byte`, `c_char`, `c_char_p`, `c_double`, `c_float`, `c_int`, `c_int16`, `c_int32`, `c_int64`, `c_int8`, `c_long`, `c_longdouble`, `c_longlong`

## Constants / attributes

`DEFAULT_MODE`, `RTLD_GLOBAL`, `RTLD_LOCAL`, `SIZEOF_TIME_T`, `cdll`, `oledll`, `pydll`, `pythonapi`, `windll`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import ctypes

def do_work(...):
    """Use ctypes to accomplish one well-defined task."""
    result = ctypes.ARRAY(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `ctypes` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: package ctypes

NAME
    ctypes - create and manipulate C data types in Python

MODULE REFERENCE
    https://docs.python.org/3.14/library/ctypes.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

PACKAGE CONTENTS
    _aix
    _endian
    _layout
    macholib (package)
    util
    wintypes

CLASSES
    _ctypes._SimpleCData(_ctypes._CData)
        HRESULT
        c_bool
        c_byte
        c_char
        c_char_p
        c_double
        c_float
        c_long
        c_longlong
        c_short
        c_ubyte
        c_ulong
        c_ulonglong
        c_ushort
        c_void_p
        c_wchar
        c_wchar_p
        py_object
    builtins.Exception(builtins.BaseException)
        ArgumentError
    builtins.object
        CDLL
            OleDLL
            PyDLL
            WinDLL
        CField
        LibraryLoader

    class ArgumentError(builtins.Exception)
     |  Method resolution order:
     |      ArgumentError
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

    class CDLL(builtins.object)
     |  CDLL(
     |      name,
     |      mode=0,
     |      handle=None,
     |      use_errno=False,
     |      use_last_error=False,
     |      winmode=None
     |  )
     |
     |  An instance of this class represents a loaded dll/shared
     |  library, exporting functions using the standard C calling
     |  convention (named 'cdecl' on Windows).
     |
     |  The exported functions can be accessed as attributes, or by
     |  indexing with the function name.  Examples:
     |
     |  <obj>.qsort -> callable object
     |  <obj>['qsort'] -> callable object
     |
     |  Calling the functions releases the Python GIL during the call and
     |  reacquires it afterwards.
     |
     |  Methods defined here:
     |
     |  __getattr__(self, name)
     |
     |  __getitem__(self, name_or_ordinal)
     |
     |  __init__(
     |      self,
     |      name,
     |      mode=0,
     |      handle=None,
     |      use_errno=False,
     |      use_last_error=False,
     |      winmode=None
     |  )
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class CField(builtins.object)
     |  Structure/Union member
     |
     |  Methods defined here:
     |
     |  __delete__(self, instance, /)
     |      Delete an attribute of instance.
     |
     |  __get__(self, instance, owner=None, /)
     |      Return an attribute of instance, which is of type owner.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __set__(self, instance, value, /)
     |      Set an attribute of instance to value.
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
     |  bit_offset
     |      additional offset in bits (relative to byte_offset); zero for non-bitfields
     |
     |  bit_size
     |      size of this field in bits
     |
     |  byte_offset
     |      offset in bytes of this field. For bitfields: excludes bit_offset.
     |
     |  byte_size
     |      size of this field in bytes
     |
     |  is_anonymous
     |      true if this field is anonymous
     |
     |  is_bitfield
     |      true if this is a bitfield
     |
     |  name
     |      name of this field
     |
     |  offset
     |      offset in bytes of this field (same as byte_offset)
     |
     |  size
     |      size in bytes of this field. For bitfields, this is a legacy packed value; use byte_size instead
     |
     |  type
     |      type of this field

    class HRESULT(_ctypes._SimpleCData)
     |  Method resolution order:
     |      HRESULT
     |      _ctypes._SimpleCData
```

## Related

Other standard-library modules pair well with `ctypes`; explore the `python` domain of this catalog.
