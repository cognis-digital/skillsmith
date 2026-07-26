---
name: python-hashlib
description: "Program with Python's hashlib module: hashlib module - A common interface to many hash functions."
version: 1.0.0
tags: [hashlib, programming, python, stdlib]
---

# Python: `hashlib`

## Overview

hashlib module - A common interface to many hash functions.

new(name, data=b'', **kwargs) - returns a new hash object implementing the
                                given hash function; initializing the hash
                                using the given binary data.

Named constructor functions are also available, these are faster
than using new(name):

md5(), sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), blake2s(),
sha3_224, sha3_256, sha3_384, sha3_512, shake_128, and shake_256.

More algorithms may be available on your platform but the above are guaranteed
to exist.  See the algorithms_guaranteed and algorithms_available attributes
to find out what algorithm names can be passed to new().

NOTE: If you want the adler32 or crc32 hash functions they are available in
the zlib module.

Choose your hash function wisely.  Some have known collision weaknesses.
sha384 and sha512 will be slow on 32 bit platforms.

Hash objects have these methods:
 - update(data): Update the hash object with the bytes in data. Repeated calls
                 are equivalent to a single call with the concatenation of all
                 the arguments.
 - digest():     Return the digest of the bytes passed to the update() method
                 so far as a bytes object.
 - hexdigest():  Like digest() except the digest is returned as a string
                 of double length, containing only hexadecimal digits.
 - copy():       Return a copy (clone) of the hash object. This can be used to
                 efficiently compute the digests of data that share a common
                 initial substring.

For example, to obtain the digest of the byte string 'Nobody inspects the
spammish repetition':

    >>> import hashlib
    >>> m = hashlib.md5()
    >>> m.update(b"Nobody inspects")
    >>> m.update(b" the spammish repetition")
    >>> m.digest()
    b'\xbbd\x9c\x83\xdd\x1e\xa5\xc9\xd9\xde\xc9\xa1\x8d\xf0\xff\xe9'

More condensed:

    >>> hashlib.sha224(b"Nobody inspects the spammish repetition").hexdigest()
    'a4337bc45a8fc544c03f52dc550cd6e1e87021bc896588bd79e901e2'

## When to use

Reach for `hashlib` when your task calls for hashlib module - A common interface to many hash functions. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import hashlib
```

## Key functions

- `hashlib.file_digest(fileobj, digest, /, *, _bufsize=262144)`
- `hashlib.md5(data=b'', *, usedforsecurity=True, string=None)`
- `hashlib.new(name, *args, **kwargs)`
- `hashlib.pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None)`
- `hashlib.scrypt(password, *, salt, n, r, p, maxmem=0, dklen=64)`
- `hashlib.sha1(data=b'', *, usedforsecurity=True, string=None)`
- `hashlib.sha224(data=b'', *, usedforsecurity=True, string=None)`
- `hashlib.sha256(data=b'', *, usedforsecurity=True, string=None)`
- `hashlib.sha384(data=b'', *, usedforsecurity=True, string=None)`
- `hashlib.sha3_224(data=b'', *, usedforsecurity=True, string=None)`
- `hashlib.sha3_256(data=b'', *, usedforsecurity=True, string=None)`
- `hashlib.sha3_384(data=b'', *, usedforsecurity=True, string=None)`
- `hashlib.sha3_512(data=b'', *, usedforsecurity=True, string=None)`
- `hashlib.sha512(data=b'', *, usedforsecurity=True, string=None)`
- `hashlib.shake_128(data=b'', *, usedforsecurity=True, string=None)`
- `hashlib.shake_256(data=b'', *, usedforsecurity=True, string=None)`

## Key classes

`blake2b`, `blake2s`

## Constants / attributes

`algorithms_available`, `algorithms_guaranteed`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import hashlib

def do_work(...):
    """Use hashlib to accomplish one well-defined task."""
    result = hashlib.file_digest(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `hashlib` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module hashlib

NAME
    hashlib - hashlib module - A common interface to many hash functions.

MODULE REFERENCE
    https://docs.python.org/3.14/library/hashlib.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    new(name, data=b'', **kwargs) - returns a new hash object implementing the
                                    given hash function; initializing the hash
                                    using the given binary data.

    Named constructor functions are also available, these are faster
    than using new(name):

    md5(), sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), blake2s(),
    sha3_224, sha3_256, sha3_384, sha3_512, shake_128, and shake_256.

    More algorithms may be available on your platform but the above are guaranteed
    to exist.  See the algorithms_guaranteed and algorithms_available attributes
    to find out what algorithm names can be passed to new().

    NOTE: If you want the adler32 or crc32 hash functions they are available in
    the zlib module.

    Choose your hash function wisely.  Some have known collision weaknesses.
    sha384 and sha512 will be slow on 32 bit platforms.

    Hash objects have these methods:
     - update(data): Update the hash object with the bytes in data. Repeated calls
                     are equivalent to a single call with the concatenation of all
                     the arguments.
     - digest():     Return the digest of the bytes passed to the update() method
                     so far as a bytes object.
     - hexdigest():  Like digest() except the digest is returned as a string
                     of double length, containing only hexadecimal digits.
     - copy():       Return a copy (clone) of the hash object. This can be used to
                     efficiently compute the digests of data that share a common
                     initial substring.

    For example, to obtain the digest of the byte string 'Nobody inspects the
    spammish repetition':

        >>> import hashlib
        >>> m = hashlib.md5()
        >>> m.update(b"Nobody inspects")
        >>> m.update(b" the spammish repetition")
        >>> m.digest()
        b'\xbbd\x9c\x83\xdd\x1e\xa5\xc9\xd9\xde\xc9\xa1\x8d\xf0\xff\xe9'

    More condensed:

        >>> hashlib.sha224(b"Nobody inspects the spammish repetition").hexdigest()
        'a4337bc45a8fc544c03f52dc550cd6e1e87021bc896588bd79e901e2'

CLASSES
    builtins.object
        _blake2.blake2b
        _blake2.blake2s

    class blake2b(builtins.object)
     |  blake2b(
     |      data=b'',
     |      *,
     |      digest_size=64,
     |      key=b'',
     |      salt=b'',
     |      person=b'',
     |      fanout=1,
     |      depth=1,
     |      leaf_size=0,
     |      node_offset=0,
     |      node_depth=0,
     |      inner_size=0,
     |      last_node=False,
     |      usedforsecurity=True,
     |      string=None
     |  )
     |
     |  Return a new BLAKE2b hash object.
     |
     |  Methods defined here:
     |
     |  copy(self, /)
     |      Return a copy of the hash object.
     |
     |  digest(self, /)
     |      Return the digest value as a bytes object.
     |
     |  hexdigest(self, /)
     |      Return the digest value as a string of hexadecimal digits.
     |
     |  update(self, data, /)
     |      Update this hash object's state with the provided bytes-like object.
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
     |  block_size
     |
     |  digest_size
     |
     |  name
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  MAX_DIGEST_SIZE = 64
     |
     |  MAX_KEY_SIZE = 64
     |
     |  PERSON_SIZE = 16
     |
     |  SALT_SIZE = 16

    class blake2s(builtins.object)
     |  blake2s(
     |      data=b'',
     |      *,
     |      digest_size=32,
     |      key=b'',
     |      salt=b'',
     |      person=b'',
     |      fanout=1,
     |      depth=1,
     |      leaf_size=0,
     |      node_offset=0,
     |      node_depth=0,
     |      inner_size=0,
     |      last_node=False,
     |      usedforsecurity=True,
     |      string=None
     |  )
     |
     |  Return a new BLAKE2s hash object.
     |
     |  Methods defined here:
     |
     |  copy(self, /)
     |      Return a copy of the hash object.
     |
     |  digest(self, /)
     |      Return the digest value as a bytes object.
     |
     |  hexdigest(self, /)
     |      Return the digest value as a string of hexadecimal digits.
     |
     |  update(self, data, /)
     |      Update this hash object's state with the provided bytes-like object.
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
     |  block_size
     |
     |  digest_size
     |
     |  name
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  MAX_DIGEST_SIZE = 32
     |
     |  MAX_KEY_SIZE = 32
     |
     |  PERSON_SIZE = 8
     |
     |  SALT_SIZE 
```

## Related

Other standard-library modules pair well with `hashlib`; explore the `python` domain of this catalog.
