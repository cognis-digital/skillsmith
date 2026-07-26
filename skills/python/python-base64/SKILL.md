---
name: python-base64
description: "Program with Python's base64 module: Base16, Base32, Base64 (RFC 3548), Base85 and Ascii85 data encodings"
version: 1.0.0
tags: [base64, programming, python, stdlib]
---

# Python: `base64`

## Overview

Base16, Base32, Base64 (RFC 3548), Base85 and Ascii85 data encodings

## When to use

Reach for `base64` when your task calls for Base16, Base32, Base64 (RFC 3548), Base85 and Ascii85 data encodings. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import base64
```

## Key functions

- `base64.a85decode(b, *, foldspaces=False, adobe=False, ignorechars=b' \t\n\r\x0b')`
- `base64.a85encode(b, *, foldspaces=False, wrapcol=0, pad=False, adobe=False)`
- `base64.b16decode(s, casefold=False)`
- `base64.b16encode(s)`
- `base64.b32decode(s, casefold=False, map01=None)`
- `base64.b32encode(s)`
- `base64.b32hexdecode(s, casefold=False)`
- `base64.b32hexencode(s)`
- `base64.b64decode(s, altchars=None, validate=False)`
- `base64.b64encode(s, altchars=None)`
- `base64.b85decode(b)`
- `base64.b85encode(b, pad=False)`
- `base64.decode(input, output)`
- `base64.decodebytes(s)`
- `base64.encode(input, output)`
- `base64.encodebytes(s)`
- `base64.main()`
- `base64.standard_b64decode(s)`
- `base64.standard_b64encode(s)`
- `base64.urlsafe_b64decode(s)`
- `base64.urlsafe_b64encode(s)`
- `base64.z85decode(s)`
- `base64.z85encode(s)`

## Constants / attributes

`MAXBINSIZE`, `MAXLINESIZE`, `bytes_types`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import base64

def do_work(...):
    """Use base64 to accomplish one well-defined task."""
    result = base64.a85decode(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `base64` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module base64

NAME
    base64 - Base16, Base32, Base64 (RFC 3548), Base85 and Ascii85 data encodings

MODULE REFERENCE
    https://docs.python.org/3.14/library/base64.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

FUNCTIONS
    a85decode(b, *, foldspaces=False, adobe=False, ignorechars=b' \t\n\r\x0b')
        Decode the Ascii85 encoded bytes-like object or ASCII string b.

        foldspaces is a flag that specifies whether the 'y' short sequence should be
        accepted as shorthand for 4 consecutive spaces (ASCII 0x20). This feature is
        not supported by the "standard" Adobe encoding.

        adobe controls whether the input sequence is in Adobe Ascii85 format (i.e.
        is framed with <~ and ~>).

        ignorechars should be a byte string containing characters to ignore from the
        input. This should only contain whitespace characters, and by default
        contains all whitespace characters in ASCII.

        The result is returned as a bytes object.

    a85encode(b, *, foldspaces=False, wrapcol=0, pad=False, adobe=False)
        Encode bytes-like object b using Ascii85 and return a bytes object.

        foldspaces is an optional flag that uses the special short sequence 'y'
        instead of 4 consecutive spaces (ASCII 0x20) as supported by 'btoa'. This
        feature is not supported by the "standard" Adobe encoding.

        wrapcol controls whether the output should have newline (b'\n') characters
        added to it. If this is non-zero, each output line will be at most this
        many characters long, excluding the trailing newline.

        pad controls whether the input is padded to a multiple of 4 before
        encoding. Note that the btoa implementation always pads.

        adobe controls whether the encoded byte sequence is framed with <~ and ~>,
        which is used by the Adobe implementation.

    b16decode(s, casefold=False)
        Decode the Base16 encoded bytes-like object or ASCII string s.

        Optional casefold is a flag specifying whether a lowercase alphabet is
        acceptable as input.  For security purposes, the default is False.

        The result is returned as a bytes object.  A binascii.Error is raised if
        s is incorrectly padded or if there are non-alphabet characters present
        in the input.

    b16encode(s)
        Encode the bytes-like object s using Base16 and return a bytes object.

    b32decode(s, casefold=False, map01=None)
        Decode the base32 encoded bytes-like object or ASCII string s.

        Optional casefold is a flag specifying whether a lowercase alphabet is
        acceptable as input.  For security purposes, the default is False.

        RFC 3548 allows for optional mapping of the digit 0 (zero) to the
        letter O (oh), and for optional mapping of the digit 1 (one) to
        either the letter I (eye) or letter L (el).  The optional argument
        map01 when not None, specifies which letter the digit 1 should be
        mapped to (when map01 is not None, the digit 0 is always mapped to
        the letter O).  For security purposes the default is None, so that
        0 and 1 are not allowed in the input.

        The result is returned as a bytes object.  A binascii.Error is raised if
        the input is incorrectly padded or if there are non-alphabet
        characters present in the input.

    b32encode(s)
        Encode the bytes-like objects using base32 and return a bytes object.

    b32hexdecode(s, casefold=False)
        Decode the base32hex encoded bytes-like object or ASCII string s.

        Optional casefold is a flag specifying whether a lowercase alphabet is
        acceptable as input.  For security purposes, the default is False.

        The result is returned as a bytes object.  A binascii.Error is raised if
        the input is incorrectly padded or if there are non-alphabet
        characters present in the input.

    b32hexencode(s)
        Encode the bytes-like objects using base32hex and return a bytes object.

    b64decode(s, altchars=None, validate=False)
        Decode the Base64 encoded bytes-like object or ASCII string s.

        Optional altchars must be a bytes-like object or ASCII string of length 2
        which specifies the alternative alphabet used instead of the '+' and '/'
        characters.

        The result is returned as a bytes object.  A binascii.Error is raised if
        s is incorrectly padded.

        If validate is False (the default), characters that are neither in the
        normal base-64 alphabet nor the alternative alphabet are discarded prior
        to the padding check.  If validate is True, these non-alphabet characters
        in the input result in a binascii.Error.
        For more information about the strict base64 check, see:

        https://docs.python.org/3.11/library/binascii.html#binascii.a2b_base64

    b64encode(s, altchars=None)
        Encode the bytes-like object s using Base64 and return a bytes object.

        Optional altchars should be a byte string of length 2 which specifies an
        alternative alphabet for the '+' and '/' characters.  This allows an
        application to e.g. generate url or filesystem safe Base64 strings.

    b85decode(b)
        Decode the base85-encoded bytes-like object or ASCII string b

        The result is returned as a bytes object.

    b85encode(b, pad=False)
        Encode bytes-like object b in base85 format and return a bytes object.

        If pad is true, the input is padded with b'\0' so its length is a multiple of
        4 bytes before encoding.

    decode(input, output)
        Decode a file; input and output are binary files.

    decod
```

## Related

Other standard-library modules pair well with `base64`; explore the `python` domain of this catalog.
