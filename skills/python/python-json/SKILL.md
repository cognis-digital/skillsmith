---
name: python-json
description: "Program with Python's json module: JSON (JavaScript Object Notation) <https://json.org> is a subset of JavaScript syntax (ECMA-262 3rd edition) used as a lightweight data interchange format."
version: 1.0.0
tags: [json, programming, python, stdlib]
---

# Python: `json`

## Overview

JSON (JavaScript Object Notation) <https://json.org> is a subset of
JavaScript syntax (ECMA-262 3rd edition) used as a lightweight data
interchange format.

:mod:`json` exposes an API familiar to users of the standard library
:mod:`marshal` and :mod:`pickle` modules.  It is derived from a
version of the externally maintained simplejson library.

Encoding basic Python object hierarchies::

    >>> import json
    >>> json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    '["foo", {"bar": ["baz", null, 1.0, 2]}]'
    >>> print(json.dumps("\"foo\bar"))
    "\"foo\bar"
    >>> print(json.dumps('\u1234'))
    "\u1234"
    >>> print(json.dumps('\\'))
    "\\"
    >>> print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
    {"a": 0, "b": 0, "c": 0}
    >>> from io import StringIO
    >>> io = StringIO()
    >>> json.dump(['streaming API'], io)
    >>> io.getvalue()
    '["streaming API"]'

Compact encoding::

    >>> import json
    >>> mydict = {'4': 5, '6': 7}
    >>> json.dumps([1,2,3,mydict], separators=(',', ':'))
    '[1,2,3,{"4":5,"6":7}]'

Pretty printing::

    >>> import json
    >>> print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
    {
        "4": 5,
        "6": 7
    }

Decoding JSON::

    >>> import json
    >>> obj = ['foo', {'bar': ['baz', None, 1.0, 2]}]
    >>> json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]') == obj
    True
    >>> json.loads('"\\"foo\\bar"') == '"foo\x08ar'
    True
    >>> from io import StringIO
    >>> io = StringIO('["streaming API"]')
    >>> json.load(io)[0] == 'streaming API'
    True

Specializing JSON object decoding::

    >>> import json
    >>> def as_complex(dct):
    ...     if '__complex__' in dct:
    ...         return complex(dct['real'], dct['imag'])
    ...     return dct
    ...
    >>> json.loads('{"__complex__": true, "real": 1, "imag": 2}',
    ...     object_hook=as_complex)
    (1+2j)
    >>> from decimal import Decimal
    >>> json.loads('1.1', parse_float=Decimal) == Decimal('1.1')
    True

Specializing JSON object encoding::

    >>> import json
    >>> def encode_complex(obj):
    ...     if isinstance(obj, complex):
    ...         return [obj.real, obj.imag]
    ...     raise TypeError(f'Object of type {obj.__class__.__name__} '
    ...                     f'is not JSON serializable')
    ...
    >>> json.dumps(2 + 1j, default=encode_complex)
    '[2.0, 1.0]'
    >>> json.JSONEncoder(default=encode_complex).encode(2 + 1j)
    '[2.0, 1.0]'
    >>> ''.join(json.JSONEncoder(default=encode_complex).iterencode(2 + 1j))
    '[2.0, 1.0]'


Using json from the shell to validate and pretty-print::

    $ echo '{"json":"obj"}' | python -m json
    {
        "json": "obj"
    }
    $ echo '{ 1.2:3.4}' | python -m json
    Expecting property name enclosed in double quotes: line 1 column 3 (char 2)

## When to use

Reach for `json` when your task calls for JSON (JavaScript Object Notation) <https://json.org> is a subset of JavaScript syntax (ECMA-262 3rd edition) used as a l. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import json
```

## Key functions

- `json.detect_encoding(b)`
- `json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)`
- `json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)`
- `json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)`
- `json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)`

## Key classes

`JSONDecodeError`, `JSONDecoder`, `JSONEncoder`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import json

def do_work(...):
    """Use json to accomplish one well-defined task."""
    result = json.detect_encoding(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `json` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: package json

NAME
    json

MODULE REFERENCE
    https://docs.python.org/3.14/library/json.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    JSON (JavaScript Object Notation) <https://json.org> is a subset of
    JavaScript syntax (ECMA-262 3rd edition) used as a lightweight data
    interchange format.

    :mod:`json` exposes an API familiar to users of the standard library
    :mod:`marshal` and :mod:`pickle` modules.  It is derived from a
    version of the externally maintained simplejson library.

    Encoding basic Python object hierarchies::

        >>> import json
        >>> json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
        '["foo", {"bar": ["baz", null, 1.0, 2]}]'
        >>> print(json.dumps("\"foo\bar"))
        "\"foo\bar"
        >>> print(json.dumps('\u1234'))
        "\u1234"
        >>> print(json.dumps('\\'))
        "\\"
        >>> print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
        {"a": 0, "b": 0, "c": 0}
        >>> from io import StringIO
        >>> io = StringIO()
        >>> json.dump(['streaming API'], io)
        >>> io.getvalue()
        '["streaming API"]'

    Compact encoding::

        >>> import json
        >>> mydict = {'4': 5, '6': 7}
        >>> json.dumps([1,2,3,mydict], separators=(',', ':'))
        '[1,2,3,{"4":5,"6":7}]'

    Pretty printing::

        >>> import json
        >>> print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
        {
            "4": 5,
            "6": 7
        }

    Decoding JSON::

        >>> import json
        >>> obj = ['foo', {'bar': ['baz', None, 1.0, 2]}]
        >>> json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]') == obj
        True
        >>> json.loads('"\\"foo\\bar"') == '"foo\x08ar'
        True
        >>> from io import StringIO
        >>> io = StringIO('["streaming API"]')
        >>> json.load(io)[0] == 'streaming API'
        True

    Specializing JSON object decoding::

        >>> import json
        >>> def as_complex(dct):
        ...     if '__complex__' in dct:
        ...         return complex(dct['real'], dct['imag'])
        ...     return dct
        ...
        >>> json.loads('{"__complex__": true, "real": 1, "imag": 2}',
        ...     object_hook=as_complex)
        (1+2j)
        >>> from decimal import Decimal
        >>> json.loads('1.1', parse_float=Decimal) == Decimal('1.1')
        True

    Specializing JSON object encoding::

        >>> import json
        >>> def encode_complex(obj):
        ...     if isinstance(obj, complex):
        ...         return [obj.real, obj.imag]
        ...     raise TypeError(f'Object of type {obj.__class__.__name__} '
        ...                     f'is not JSON serializable')
        ...
        >>> json.dumps(2 + 1j, default=encode_complex)
        '[2.0, 1.0]'
        >>> json.JSONEncoder(default=encode_complex).encode(2 + 1j)
        '[2.0, 1.0]'
        >>> ''.join(json.JSONEncoder(default=encode_complex).iterencode(2 + 1j))
        '[2.0, 1.0]'


    Using json from the shell to validate and pretty-print::

        $ echo '{"json":"obj"}' | python -m json
        {
            "json": "obj"
        }
        $ echo '{ 1.2:3.4}' | python -m json
        Expecting property name enclosed in double quotes: line 1 column 3 (char 2)

PACKAGE CONTENTS
    __main__
    decoder
    encoder
    scanner
    tool

CLASSES
    builtins.ValueError(builtins.Exception)
        json.decoder.JSONDecodeError
    builtins.object
        json.decoder.JSONDecoder
        json.encoder.JSONEncoder

    class JSONDecodeError(builtins.ValueError)
     |  JSONDecodeError(msg, doc, pos)
     |
     |  Subclass of ValueError with the following additional properties:
     |
     |  msg: The unformatted error message
     |  doc: The JSON document being parsed
     |  pos: The start index of doc where parsing failed
     |  lineno: The line corresponding to pos
     |  colno: The column corresponding to pos
     |
     |  Method resolution order:
     |      JSONDecodeError
     |      builtins.ValueError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, msg, doc, pos)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__(self)
     |      Helper for pickle.
     |
     |  ----------------------------------------------------------------------
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

    cl
```

## Related

Other standard-library modules pair well with `json`; explore the `python` domain of this catalog.
