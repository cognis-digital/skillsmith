---
name: python-getopt
description: "Program with Python's getopt module: Parser for command line options."
version: 1.0.0
tags: [getopt, programming, python, stdlib]
---

# Python: `getopt`

## Overview

Parser for command line options.

This module helps scripts to parse the command line arguments in
sys.argv.  It supports the same conventions as the Unix getopt()
function (including the special meanings of arguments of the form '-'
and '--').  Long options similar to those supported by GNU software
may be used as well via an optional third argument.  This module
provides two functions and an exception:

getopt() -- Parse command line options
gnu_getopt() -- Like getopt(), but allow option and non-option arguments
to be intermixed.
GetoptError -- exception (class) raised with 'opt' attribute, which is the
option involved with the exception.

## When to use

Reach for `getopt` when your task calls for Parser for command line options. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import getopt
```

## Key functions

- `getopt.do_longs(opts, opt, longopts, args)`
- `getopt.do_shorts(opts, optstring, shortopts, args)`
- `getopt.getopt(args, shortopts, longopts=[])`
- `getopt.gnu_getopt(args, shortopts, longopts=[])`
- `getopt.long_has_args(opt, longopts)`
- `getopt.short_has_arg(opt, shortopts)`

## Key classes

`GetoptError`, `error`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import getopt

def do_work(...):
    """Use getopt to accomplish one well-defined task."""
    result = getopt.do_longs(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `getopt` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module getopt

NAME
    getopt - Parser for command line options.

MODULE REFERENCE
    https://docs.python.org/3.14/library/getopt.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module helps scripts to parse the command line arguments in
    sys.argv.  It supports the same conventions as the Unix getopt()
    function (including the special meanings of arguments of the form '-'
    and '--').  Long options similar to those supported by GNU software
    may be used as well via an optional third argument.  This module
    provides two functions and an exception:

    getopt() -- Parse command line options
    gnu_getopt() -- Like getopt(), but allow option and non-option arguments
    to be intermixed.
    GetoptError -- exception (class) raised with 'opt' attribute, which is the
    option involved with the exception.

CLASSES
    builtins.Exception(builtins.BaseException)
        GetoptError

    class GetoptError(builtins.Exception)
     |  GetoptError(msg, opt='')
     |
     |  Method resolution order:
     |      GetoptError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, msg, opt='')
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __str__(self)
     |      Return str(self).
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  msg = ''
     |
     |  opt = ''
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
     |  __reduce__(self, /)
     |      Helper for pickle.
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

    error = class GetoptError(builtins.Exception)
     |  error(msg, opt='')
     |
     |  Method resolution order:
     |      GetoptError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, msg, opt='')
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __str__(self)
     |      Return str(self).
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  msg = ''
     |
     |  opt = ''
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
     |  __reduce__(self, /)
     |      Helper for pickle.
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
    getopt(args, shortopts, longopts=[])
        getopt(args, options[, long_options]) -> opts, args

        Parses command line options and parameter list.  args is the
        argument list to be parsed, without the leading reference to the
        running program.  Typically, this means "sys.argv[1:]".  shortopts
        is the string of option letters that the script wants to
        recognize, with options that require an argument followed by a
        colon and options that accept an optional argument followed by
        two colons (i.e., the same format that Unix getopt() uses).  If
        specified, longopts is a list of strings with the names of the
        long options which should be supported.  The leading '--'
        characters should not be included in the option name.  Options
        which require an argument should be followed by an equ
```

## Related

Other standard-library modules pair well with `getopt`; explore the `python` domain of this catalog.
