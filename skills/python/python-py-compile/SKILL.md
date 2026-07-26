---
name: python-py-compile
description: "Program with Python's py_compile module: Routine to 'compile' a .py file to a .pyc file."
version: 1.0.0
tags: [programming, py-compile, python, stdlib]
---

# Python: `py_compile`

## Overview

Routine to "compile" a .py file to a .pyc file.

This module has intimate knowledge of the format of .pyc files.

## When to use

Reach for `py_compile` when your task calls for Routine to "compile" a .py file to a .pyc file. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import py_compile
```

## Key functions

- `py_compile.compile(file, cfile=None, dfile=None, doraise=False, optimize=-1, invalidation_mode=None, quiet=0)`
- `py_compile.main()`

## Key classes

`PyCompileError`, `PycInvalidationMode`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import py_compile

def do_work(...):
    """Use py_compile to accomplish one well-defined task."""
    result = py_compile.compile(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `py_compile` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module py_compile

NAME
    py_compile - Routine to "compile" a .py file to a .pyc file.

MODULE REFERENCE
    https://docs.python.org/3.14/library/py_compile.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module has intimate knowledge of the format of .pyc files.

CLASSES
    builtins.Exception(builtins.BaseException)
        PyCompileError
    enum.Enum(builtins.object)
        PycInvalidationMode

    class PyCompileError(builtins.Exception)
     |  PyCompileError(exc_type, exc_value, file, msg='')
     |
     |  Exception raised when an error occurs while attempting to
     |  compile the file.
     |
     |  To raise this exception, use
     |
     |      raise PyCompileError(exc_type,exc_value,file[,msg])
     |
     |  where
     |
     |      exc_type:   exception type to be used in error message
     |                  type name can be accesses as class variable
     |                  'exc_type_name'
     |
     |      exc_value:  exception value to be used in error message
     |                  can be accesses as class variable 'exc_value'
     |
     |      file:       name of file being compiled to be used in error message
     |                  can be accesses as class variable 'file'
     |
     |      msg:        string message to be written as error message
     |                  If no value is given, a default exception message will be
     |                  given, consistent with 'standard' py_compile output.
     |                  message (or default) can be accesses as class variable
     |                  'msg'
     |
     |  Method resolution order:
     |      PyCompileError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, exc_type, exc_value, file, msg='')
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

    class PycInvalidationMode(enum.Enum)
     |  PycInvalidationMode(*values)
     |
     |  Method resolution order:
     |      PycInvalidationMode
     |      enum.Enum
     |      builtins.object
     |
     |  Data and other attributes defined here:
     |
     |  CHECKED_HASH = <PycInvalidationMode.CHECKED_HASH: 2>
     |
     |  TIMESTAMP = <PycInvalidationMode.TIMESTAMP: 1>
     |
     |  UNCHECKED_HASH = <PycInvalidationMode.UNCHECKED_HASH: 3>
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from enum.Enum:
     |
     |  name
     |      The name of the Enum member.
     |
     |  value
     |      The value of the Enum member.
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from enum.EnumType:
     |
     |  __contains__(value)
     |      Return True if `value` is in `cls`.
     |
     |      `value` is in `cls` if:
     |      1) `value` is a member of `cls`, or
     |      2) `value` is the value of one of the `cls`'s members.
     |      3) `value` is a pseudo-member (flags)
     |
     |  __getitem__(name)
     |      Return the member matching `name`.
     |
     |  __iter__()
     |      Return members in definition order.
     |
     |  __len__()
     |      Return the number of members (no aliases)
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties inherited from enum.EnumType:
     |
     |  __members__
     |      Returns a mapping of member name->value.
     |
     |      This mapping lists all enum members, including aliases. Note that this
     |      is a read-only view of the internal mapping.

FUNCTIONS
    compile(
        file,
        cfile=None,
        dfile=None,
        doraise=False,
        optimize=-1,
        invalidation_mode=None,
        quiet=0
    )
        Byte-compile one Python source file to Python bytecode.

        :param file: The source file name.
        :param cfile: The target byte compiled file name.  When not given, this
            defaults to the PEP 3147/PEP 488 location.
        :param dfile: Purported file name, i.e. the file name that shows up in
            error messages.  Defaults to the source file name.
        :param doraise: Flag indicating whether or not an exception should be
   
```

## Related

Other standard-library modules pair well with `py_compile`; explore the `python` domain of this catalog.
