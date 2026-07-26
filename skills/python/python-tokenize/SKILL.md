---
name: python-tokenize
description: "Program with Python's tokenize module: Tokenization help for Python programs."
version: 1.0.0
tags: [programming, python, stdlib, tokenize]
---

# Python: `tokenize`

## Overview

Tokenization help for Python programs.

tokenize(readline) is a generator that breaks a stream of bytes into
Python tokens.  It decodes the bytes according to PEP-0263 for
determining source file encoding.

It accepts a readline-like method which is called repeatedly to get the
next line of input (or b"" for EOF).  It generates 5-tuples with these
members:

    the token type (see token.py)
    the token (a string)
    the starting (row, column) indices of the token (a 2-tuple of ints)
    the ending (row, column) indices of the token (a 2-tuple of ints)
    the original line (string)

It is designed to match the working of the Python tokenizer exactly, except
that it produces COMMENT tokens for comments and gives type OP for all
operators.  Additionally, all token lists start with an ENCODING token
which tells you which encoding was used to decode the bytes stream.

## When to use

Reach for `tokenize` when your task calls for Tokenization help for Python programs. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import tokenize
```

## Key functions

- `tokenize.ISEOF(x: int) -> bool`
- `tokenize.ISNONTERMINAL(x: int) -> bool`
- `tokenize.ISTERMINAL(x: int) -> bool`
- `tokenize.any(*choices)`
- `tokenize.detect_encoding(readline)`
- `tokenize.generate_tokens(readline)`
- `tokenize.group(*choices)`
- `tokenize.lookup(encoding, /)`
- `tokenize.maybe(*choices)`
- `tokenize.open(filename)`
- `tokenize.tokenize(readline)`
- `tokenize.untokenize(iterable)`

## Key classes

`TextIOWrapper`, `TokenError`, `TokenInfo`, `Untokenizer`

## Constants / attributes

`AMPER`, `AMPEREQUAL`, `AT`, `ATEQUAL`, `BOM_UTF8`, `Binnumber`, `CIRCUMFLEX`, `CIRCUMFLEXEQUAL`, `COLON`, `COLONEQUAL`, `COMMA`, `COMMENT`, `Comment`, `ContStr`, `DEDENT`, `DOT`, `DOUBLESLASH`, `DOUBLESLASHEQUAL`, `DOUBLESTAR`, `DOUBLESTAREQUAL`, `Decnumber`, `Double`, `Double3`, `ELLIPSIS`, `ENCODING`, `ENDMARKER`, `EQEQUAL`, `EQUAL`, `ERRORTOKEN`, `EXACT_TOKEN_TYPES`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import tokenize

def do_work(...):
    """Use tokenize to accomplish one well-defined task."""
    result = tokenize.ISEOF(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `tokenize` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module tokenize

NAME
    tokenize - Tokenization help for Python programs.

MODULE REFERENCE
    https://docs.python.org/3.14/library/tokenize.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    tokenize(readline) is a generator that breaks a stream of bytes into
    Python tokens.  It decodes the bytes according to PEP-0263 for
    determining source file encoding.

    It accepts a readline-like method which is called repeatedly to get the
    next line of input (or b"" for EOF).  It generates 5-tuples with these
    members:

        the token type (see token.py)
        the token (a string)
        the starting (row, column) indices of the token (a 2-tuple of ints)
        the ending (row, column) indices of the token (a 2-tuple of ints)
        the original line (string)

    It is designed to match the working of the Python tokenizer exactly, except
    that it produces COMMENT tokens for comments and gives type OP for all
    operators.  Additionally, all token lists start with an ENCODING token
    which tells you which encoding was used to decode the bytes stream.

CLASSES
    builtins.Exception(builtins.BaseException)
        TokenError
    TokenInfo(builtins.tuple)
        TokenInfo

    class TokenError(builtins.Exception)
     |  Method resolution order:
     |      TokenError
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

    class TokenInfo(TokenInfo)
     |  TokenInfo(type, string, start, end, line)
     |
     |  Method resolution order:
     |      TokenInfo
     |      TokenInfo
     |      builtins.tuple
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __repr__(self)
     |      Return a nicely formatted representation string
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  exact_type
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from TokenInfo:
     |
     |  __getnewargs__(self) from collections.TokenInfo
     |      Return self as a plain tuple.  Used by copy and pickle.
     |
     |  __replace__ = _replace(self, /, **kwds)
     |
     |  _asdict(self) from collections.TokenInfo
     |      Return a new dict which maps field names to their values.
     |
     |  _replace(self, /, **kwds) from collections.TokenInfo
     |      Return a new TokenInfo object replacing specified fields with new values
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from TokenInfo:
     |
     |  _make(iterable) from collections.TokenInfo
     |      Make a new TokenInfo object from a sequence or iterable
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from TokenInfo:
     |
     |  __new__(_cls, type, string, start, end, line) from namedtuple_TokenInfo.TokenInfo
     |      Create new instance of TokenInfo(type, string, start, end, line)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from TokenInfo:
     |
     |  type
     |      Alias for field number 0
     |
     |  string
     |      Alias for field number 1
     |
     |  start
     |      Alias for field number 2
     |
     |  end
     |      Alias for field number 3
     |
     |  line
     |      Alias for field number 4
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from TokenInfo:
     |
     |  __match_args__ = ('type', 'string', 'start', 'end', 'line')
     |
     |  _field_defaults = {}
     |
     |  _fields = ('type', 'string', 'start', 'end', 'line')
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __contains__(self, key, /)
 
```

## Related

Other standard-library modules pair well with `tokenize`; explore the `python` domain of this catalog.
