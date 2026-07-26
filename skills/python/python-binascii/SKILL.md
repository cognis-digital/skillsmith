---
name: python-binascii
description: "Program with Python's binascii module: Conversion between binary data and ASCII"
version: 1.0.0
tags: [binascii, programming, python, stdlib]
---

# Python: `binascii`

## Overview

Conversion between binary data and ASCII

## When to use

Reach for `binascii` when your task calls for Conversion between binary data and ASCII. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import binascii
```

## Key functions

- `binascii.a2b_base64(data, /, *, strict_mode=False)`
- `binascii.a2b_hex(hexstr, /)`
- `binascii.a2b_qp(data, header=False)`
- `binascii.a2b_uu(data, /)`
- `binascii.b2a_base64(data, /, *, newline=True)`
- `binascii.b2a_hex(...)`
- `binascii.b2a_qp(data, quotetabs=False, istext=True, header=False)`
- `binascii.b2a_uu(data, /, *, backtick=False)`
- `binascii.crc32(data, crc=0, /)`
- `binascii.crc_hqx(data, crc, /)`
- `binascii.hexlify(...)`
- `binascii.unhexlify(hexstr, /)`

## Key classes

`Error`, `Incomplete`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import binascii

def do_work(...):
    """Use binascii to accomplish one well-defined task."""
    result = binascii.a2b_base64(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `binascii` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: built-in module binascii

NAME
    binascii - Conversion between binary data and ASCII

CLASSES
    builtins.Exception(builtins.BaseException)
        Incomplete
    builtins.ValueError(builtins.Exception)
        Error

    class Error(builtins.ValueError)
     |  Method resolution order:
     |      Error
     |      builtins.ValueError
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
     |  Static methods inherited from builtins.ValueError:
     |
     |  __new__(*args, **kwargs) class method of builtins.ValueError
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

    class Incomplete(builtins.Exception)
     |  Method resolution order:
     |      Incomplete
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
    a2b_base64(data, /, *, strict_mode=False)
        Decode a line of base64 data.

        strict_mode
          When set to True, bytes that are not part of the base64 standard are not allowed.
          The same applies to excess data after padding (= / ==).

    a2b_hex(hexstr, /)
        Binary data of hexadecimal representation.

        hexstr must contain an even number of hex digits (upper or lower case).
        This function is also available as "unhexlify()".

    a2b_qp(data, header=False)
        Decode a string of qp-encoded data.

    a2b_uu(data, /)
        Decode a line of uuencoded data.

    b2a_base64(data, /, *, newline=True)
        Base64-code line of data.

    b2a_hex(data, sep=<unrepresentable>, bytes_per_sep=1)
        Hexadecimal representation of binary data.

          sep
            An optional single character or byte to separate hex bytes.
          bytes_per_sep
            How many bytes between separators.  Positive values count from the
            right, negative values count from the left.

        The return value is a bytes object.  This function is also
        available as "hexlify()".

        Example:
        >>> binascii.b2a_hex(b'\xb9\x01\xef')
        b'b901ef'
        >>> binascii.hexlify(b'\xb9\x01\xef', ':')
        b'b9:01:ef'
        >>> binascii.b2a_hex(b'\xb9\x01\xef', b'_', 2)
        b'b9_01ef'

    b2a_qp(data, quotetabs=False, istext=True, header=False)
        Encode a string using quoted-printable encoding.

        On encoding, when istext is set, newlines are not encoded, and white
        space at end of lines is.  When istext is not set, \r and \n (CR/LF)
        are both encoded.  When quotetabs is set, space and tabs are encoded.

    b2a_uu(data, /, *, backtick=False)
        Uuencode line of data.

    crc32(data, crc=0, /)
        Compute CRC-32 incrementally.

    crc_hqx(data, crc, /)
        Compute CRC-CCITT incrementally.

    hexlify(data, sep=<unrepresentable>, bytes_per_sep=1)
        Hexadecimal representation of binary data.

          sep
            An optional single character or byte to separate hex bytes.
          bytes_per_sep
            How many bytes between separators.  Positive values count from the
            right, negative values count from the left.

        The return value is a bytes object.  This function is also
        available as "b2a_hex()".

    unhexlify(hexstr, /)
        Binary data of hexadecimal representation.

        hexstr must cont
```

## Related

Other standard-library modules pair well with `binascii`; explore the `python` domain of this catalog.
