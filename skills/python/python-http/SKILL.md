---
name: python-http
description: "Program with Python's http module: The Python standard-library module `http`."
version: 1.0.0
tags: [http, programming, python, stdlib]
---

# Python: `http`

## Overview

`http` is part of the Python standard library.

## When to use

Reach for `http` when your task calls for The Python standard-library module `http`. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import http
```

## Key classes

`HTTPMethod`, `HTTPStatus`, `IntEnum`, `StrEnum`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import http

def do_work(...):
    """Use http to accomplish one well-defined task."""
    result = http.HTTPMethod(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `http` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: package http

NAME
    http

MODULE REFERENCE
    https://docs.python.org/3.14/library/http.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

PACKAGE CONTENTS
    client
    cookiejar
    cookies
    server

CLASSES
    enum.IntEnum(builtins.int, enum.ReprEnum)
        HTTPStatus
    enum.StrEnum(builtins.str, enum.ReprEnum)
        HTTPMethod

    class HTTPMethod(enum.StrEnum)
     |  HTTPMethod(*values)
     |
     |  HTTP methods and descriptions
     |
     |  Methods from the following RFCs are all observed:
     |
     |      * RFC 9110: HTTP Semantics, obsoletes 7231, which obsoleted 2616
     |      * RFC 5789: PATCH Method for HTTP
     |
     |  Method resolution order:
     |      HTTPMethod
     |      enum.StrEnum
     |      builtins.str
     |      enum.ReprEnum
     |      enum.Enum
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __format__(self, format_spec, /) from builtins.str
     |      Return a formatted version of the string as described by format_spec.
     |
     |  __new__(cls, value) from enum.Enum
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __str__(self, /) from builtins.str
     |      Return str(self).
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  CONNECT = <HTTPMethod.CONNECT>
     |
     |  DELETE = <HTTPMethod.DELETE>
     |
     |  GET = <HTTPMethod.GET>
     |
     |  HEAD = <HTTPMethod.HEAD>
     |
     |  OPTIONS = <HTTPMethod.OPTIONS>
     |
     |  PATCH = <HTTPMethod.PATCH>
     |
     |  POST = <HTTPMethod.POST>
     |
     |  PUT = <HTTPMethod.PUT>
     |
     |  TRACE = <HTTPMethod.TRACE>
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.str:
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __contains__(self, key, /)
     |      Return bool(key in self).
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getitem__(self, key, /)
     |      Return self[key].
     |
     |  __getnewargs__(self, /)
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __len__(self, /)
     |      Return len(self).
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __mod__(self, value, /)
     |      Return self%value.
     |
     |  __mul__(self, value, /)
     |      Return self*value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __rmod__(self, value, /)
     |      Return value%self.
     |
     |  __rmul__(self, value, /)
     |      Return value*self.
     |
     |  __sizeof__(self, /)
     |      Return the size of the string in memory, in bytes.
     |
     |  capitalize(self, /)
     |      Return a capitalized version of the string.
     |
     |      More specifically, make the first character have upper case and the rest lower
     |      case.
     |
     |  casefold(self, /)
     |      Return a version of the string suitable for caseless comparisons.
     |
     |  center(self, width, fillchar=' ', /)
     |      Return a centered string of length width.
     |
     |      Padding is done using the specified fill character (default is a space).
     |
     |  count(self, sub[, start[, end]], /)
     |      Return the number of non-overlapping occurrences of substring sub in string S[start:end].
     |
     |      Optional arguments start and end are interpreted as in slice notation.
     |
     |  encode(self, /, encoding='utf-8', errors='strict')
     |      Encode the string using the codec registered for encoding.
     |
     |      encoding
     |        The encoding in which to encode the string.
     |      errors
     |        The error handling scheme to use for encoding errors.
     |        The default is 'strict' meaning that encoding errors raise a
     |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
     |        'xmlcharrefreplace' as well as any other name registered with
     |        codecs.register_error that can handle UnicodeEncodeErrors.
     |
     |  endswith(self, suffix[, start[, end]], /)
     |      Return True if the string ends with the specified suffix, False otherwise.
     |
     |      suffix
     |        A string or a tuple of strings to try.
     |      start
     |        Optional start position. Default: start of the string.
     |      end
     |        Optional stop position. Default: end of the string.
     |
     |  expandtabs(self, /, tabsize=8)
     |      Return a copy where all tab characters are expanded using spaces.
     |
     |      If tabsize is not given, a tab size of 8 characters is assumed.
     |
     |  find(self, sub[, start[, end]], /)
     |      Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].
     |
     |      Optional arguments start and end are interpreted as in slice notation.
     |      Return -1 on failure.
     |
     |  format(self, /, *args, **kwargs)
     |      Return a formatted version of the string, using substitutions from args and kwargs.
     |      The substitutions are identified by braces ('{' and '}').
     |
     |  for
```

## Related

Other standard-library modules pair well with `http`; explore the `python` domain of this catalog.
