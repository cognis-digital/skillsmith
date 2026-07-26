---
name: python-hmac
description: "Program with Python's hmac module: HMAC (Keyed-Hashing for Message Authentication) module."
version: 1.0.0
tags: [hmac, programming, python, stdlib]
---

# Python: `hmac`

## Overview

HMAC (Keyed-Hashing for Message Authentication) module.

Implements the HMAC algorithm as described by RFC 2104.

## When to use

Reach for `hmac` when your task calls for HMAC (Keyed-Hashing for Message Authentication) module. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import hmac
```

## Key functions

- `hmac.compare_digest(a, b, /)`
- `hmac.digest(key, msg, digest)`
- `hmac.new(key, msg=None, digestmod='')`

## Key classes

`HMAC`

## Constants / attributes

`digest_size`, `trans_36`, `trans_5C`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import hmac

def do_work(...):
    """Use hmac to accomplish one well-defined task."""
    result = hmac.compare_digest(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `hmac` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module hmac

NAME
    hmac - HMAC (Keyed-Hashing for Message Authentication) module.

MODULE REFERENCE
    https://docs.python.org/3.14/library/hmac.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Implements the HMAC algorithm as described by RFC 2104.

CLASSES
    builtins.object
        HMAC

    class HMAC(builtins.object)
     |  HMAC(key, msg=None, digestmod='')
     |
     |  RFC 2104 HMAC class.  Also complies with RFC 4231.
     |
     |  This supports the API for Cryptographic Hash Functions (PEP 247).
     |
     |  Methods defined here:
     |
     |  __init__(self, key, msg=None, digestmod='')
     |      Create a new HMAC object.
     |
     |      key: bytes or buffer, key for the keyed hash object.
     |      msg: bytes or buffer, Initial input for the hash or None.
     |      digestmod: A hash name suitable for hashlib.new(). *OR*
     |                 A hashlib constructor returning a new hash object. *OR*
     |                 A module supporting PEP 247.
     |
     |                 Required as of 3.8, despite its position after the optional
     |                 msg argument.  Passing it as a keyword argument is
     |                 recommended, though not required for legacy API reasons.
     |
     |  copy(self)
     |      Return a separate copy of this hashing object.
     |
     |      An update to this copy won't affect the original object.
     |
     |  digest(self)
     |      Return the hash value of this hashing object.
     |
     |      This returns the hmac value as bytes.  The object is
     |      not altered in any way by this function; you can continue
     |      updating the object after calling this function.
     |
     |  hexdigest(self)
     |      Like digest(), but returns a string of hexadecimal digits instead.
     |
     |  update(self, msg)
     |      Feed data from msg into this hashing object.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  name
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  block_size
     |
     |  digest_size
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  blocksize = 64

FUNCTIONS
    digest(key, msg, digest)
        Fast inline implementation of HMAC.

        key: bytes or buffer, The key for the keyed hash object.
        msg: bytes or buffer, Input message.
        digest: A hash name suitable for hashlib.new() for best performance. *OR*
                A hashlib constructor returning a new hash object. *OR*
                A module supporting PEP 247.

    new(key, msg=None, digestmod='')
        Create a new hashing object and return it.

        key: bytes or buffer, The starting key for the hash.
        msg: bytes or buffer, Initial input for the hash, or None.
        digestmod: A hash name suitable for hashlib.new(). *OR*
                   A hashlib constructor returning a new hash object. *OR*
                   A module supporting PEP 247.

                   Required as of 3.8, despite its position after the optional
                   msg argument.  Passing it as a keyword argument is
                   recommended, though not required for legacy API reasons.

        You can now feed arbitrary bytes into the object using its update()
        method, and can ask for the hash value at any time by calling its digest()
        or hexdigest() methods.

DATA
    digest_size = None
    trans_36 = b'67452301>?<=:;89&\'$%"# !./,-*+()\x16\x17\x14\...\xc2\xc3...
    trans_5C = b'\\]^_XYZ[TUVWPQRSLMNOHIJKDEFG@ABC|}~\x7fxyz{tu...\xa8\xa9...

FILE
    c:\python314\lib\hmac.py


```

## Related

Other standard-library modules pair well with `hmac`; explore the `python` domain of this catalog.
