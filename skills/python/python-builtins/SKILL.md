---
name: python-builtins
description: "Program with Python's builtins module: Built-in functions, types, exceptions, and other objects."
version: 1.0.0
tags: [builtins, programming, python, stdlib]
---

# Python: `builtins`

## Overview

Built-in functions, types, exceptions, and other objects.

This module provides direct access to all 'built-in'
identifiers of Python; for example, builtins.len is
the full name for the built-in function len().

This module is not normally accessed explicitly by most
applications, but can be useful in modules that provide
objects with the same name as a built-in value, but in
which the built-in of that name is also needed.

## When to use

Reach for `builtins` when your task calls for Built-in functions, types, exceptions, and other objects. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import builtins
```

## Key functions

- `builtins.abs(x, /)`
- `builtins.aiter(async_iterable, /)`
- `builtins.all(iterable, /)`
- `builtins.anext(...)`
- `builtins.any(iterable, /)`
- `builtins.ascii(obj, /)`
- `builtins.bin(number, /)`
- `builtins.breakpoint(*args, **kws)`
- `builtins.callable(obj, /)`
- `builtins.chr(i, /)`
- `builtins.compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1, *, _feature_version=-1)`
- `builtins.copyright()`
- `builtins.credits()`
- `builtins.delattr(obj, name, /)`
- `builtins.dir(...)`
- `builtins.divmod(x, y, /)`
- `builtins.eval(source, /, globals=None, locals=None)`
- `builtins.exec(source, /, globals=None, locals=None, *, closure=None)`
- `builtins.exit(code=None)`
- `builtins.format(value, format_spec='', /)`
- `builtins.getattr(...)`
- `builtins.globals()`
- `builtins.hasattr(obj, name, /)`
- `builtins.hash(obj, /)`
- `builtins.help(*args, **kwds)`
- `builtins.hex(number, /)`
- `builtins.id(obj, /)`
- `builtins.input(prompt='', /)`
- `builtins.isinstance(obj, class_or_tuple, /)`
- `builtins.issubclass(cls, class_or_tuple, /)`

## Key classes

`ArithmeticError`, `AssertionError`, `AttributeError`, `BaseException`, `BaseExceptionGroup`, `BlockingIOError`, `BrokenPipeError`, `BufferError`, `BytesWarning`, `ChildProcessError`, `ConnectionAbortedError`, `ConnectionError`, `ConnectionRefusedError`, `ConnectionResetError`, `DeprecationWarning`, `EOFError`, `EncodingWarning`, `EnvironmentError`, `Exception`, `ExceptionGroup`, `FileExistsError`, `FileNotFoundError`, `FloatingPointError`, `FutureWarning`, `GeneratorExit`, `IOError`, `ImportError`, `ImportWarning`, `IndentationError`, `IndexError`

## Constants / attributes

`Ellipsis`, `False`, `None`, `NotImplemented`, `True`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import builtins

def do_work(...):
    """Use builtins to accomplish one well-defined task."""
    result = builtins.abs(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `builtins` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: built-in module builtins

NAME
    builtins - Built-in functions, types, exceptions, and other objects.

DESCRIPTION
    This module provides direct access to all 'built-in'
    identifiers of Python; for example, builtins.len is
    the full name for the built-in function len().

    This module is not normally accessed explicitly by most
    applications, but can be useful in modules that provide
    objects with the same name as a built-in value, but in
    which the built-in of that name is also needed.

CLASSES
    object
        BaseException
            BaseExceptionGroup
                ExceptionGroup(BaseExceptionGroup, Exception)
            Exception
                ArithmeticError
                    FloatingPointError
                    OverflowError
                    ZeroDivisionError
                AssertionError
                AttributeError
                BufferError
                EOFError
                ImportError
                    ModuleNotFoundError
                LookupError
                    IndexError
                    KeyError
                MemoryError
                NameError
                    UnboundLocalError
                OSError
                    BlockingIOError
                    ChildProcessError
                    ConnectionError
                        BrokenPipeError
                        ConnectionAbortedError
                        ConnectionRefusedError
                        ConnectionResetError
                    FileExistsError
                    FileNotFoundError
                    InterruptedError
                    IsADirectoryError
                    NotADirectoryError
                    PermissionError
                    ProcessLookupError
                    TimeoutError
                ReferenceError
                RuntimeError
                    NotImplementedError
                    PythonFinalizationError
                    RecursionError
                StopAsyncIteration
                StopIteration
                SyntaxError
                    IndentationError
                        TabError
                SystemError
                TypeError
                ValueError
                    UnicodeError
                        UnicodeDecodeError
                        UnicodeEncodeError
                        UnicodeTranslateError
                Warning
                    BytesWarning
                    DeprecationWarning
                    EncodingWarning
                    FutureWarning
                    ImportWarning
                    PendingDeprecationWarning
                    ResourceWarning
                    RuntimeWarning
                    SyntaxWarning
                    UnicodeWarning
                    UserWarning
            GeneratorExit
            KeyboardInterrupt
            SystemExit
        bytearray
        bytes
        classmethod
        complex
        dict
        enumerate
        filter
        float
        frozenset
        int
            bool
        list
        map
        memoryview
        property
        range
        reversed
        set
        slice
        staticmethod
        str
        super
        tuple
        type
        zip

    class ArithmeticError(Exception)
     |  Base class for arithmetic errors.
     |
     |  Method resolution order:
     |      ArithmeticError
     |      Exception
     |      BaseException
     |      object
     |
     |  Built-in subclasses:
     |      FloatingPointError
     |      OverflowError
     |      ZeroDivisionError
     |
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs)
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
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
     |  Data descriptors inherited from BaseException:
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

    class AssertionError(Exception)
     |  Assertion failed.
     |
     |  Method resolution order:
     |      AssertionError
     |      Exception
     |      BaseException
     |      object
     |
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs)
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
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
     |  Data descriptors inherited from BaseException:
     |
     |  __cause__
     |
     |  __context__
     |
  
```

## Related

Other standard-library modules pair well with `builtins`; explore the `python` domain of this catalog.
