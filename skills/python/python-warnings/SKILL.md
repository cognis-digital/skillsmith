---
name: python-warnings
description: "Program with Python's warnings module: The Python standard-library module `warnings`."
version: 1.0.0
tags: [programming, python, stdlib, warnings]
---

# Python: `warnings`

## Overview

`warnings` is part of the Python standard library.

## When to use

Reach for `warnings` when your task calls for The Python standard-library module `warnings`. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import warnings
```

## Key functions

- `warnings.filterwarnings(action, message='', category=<class 'Warning'>, module='', lineno=0, append=False)`
- `warnings.formatwarning(message, category, filename, lineno, line=None)`
- `warnings.resetwarnings()`
- `warnings.showwarning(message, category, filename, lineno, file=None, line=None)`
- `warnings.simplefilter(action, category=<class 'Warning'>, lineno=0, append=False)`
- `warnings.warn(...)`
- `warnings.warn_explicit(...)`

## Key classes

`WarningMessage`, `catch_warnings`, `deprecated`

## Constants / attributes

`defaultaction`, `filters`, `onceregistry`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import warnings

def do_work(...):
    """Use warnings to accomplish one well-defined task."""
    result = warnings.filterwarnings(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `warnings` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module warnings

NAME
    warnings

MODULE REFERENCE
    https://docs.python.org/3.14/library/warnings.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.object
        _py_warnings.catch_warnings
        _py_warnings.deprecated

    class catch_warnings(builtins.object)
     |  catch_warnings(
     |      *,
     |      record=False,
     |      module=None,
     |      action=None,
     |      category=<class 'Warning'>,
     |      lineno=0,
     |      append=False
     |  )
     |
     |  A context manager that copies and restores the warnings filter upon
     |  exiting the context.
     |
     |  The 'record' argument specifies whether warnings should be captured by a
     |  custom implementation of warnings.showwarning() and be appended to a list
     |  returned by the context manager. Otherwise None is returned by the context
     |  manager. The objects appended to the list are arguments whose attributes
     |  mirror the arguments to showwarning().
     |
     |  The 'module' argument is to specify an alternative module to the module
     |  named 'warnings' and imported under that name. This argument is only useful
     |  when testing the warnings module itself.
     |
     |  If the 'action' argument is not None, the remaining arguments are passed
     |  to warnings.simplefilter() as if it were called immediately on entering the
     |  context.
     |
     |  Methods defined here:
     |
     |  __enter__(self)
     |
     |  __exit__(self, *exc_info)
     |
     |  __init__(
     |      self,
     |      *,
     |      record=False,
     |      module=None,
     |      action=None,
     |      category=<class 'Warning'>,
     |      lineno=0,
     |      append=False
     |  )
     |      Specify whether to record warnings and if an alternative module
     |      should be used other than sys.modules['warnings'].
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class deprecated(builtins.object)
     |  deprecated(
     |      message: str,
     |      /,
     |      *,
     |      category: type[Warning] | None = <class 'DeprecationWarning'>,
     |      stacklevel: int = 1
     |  ) -> None
     |
     |  Indicate that a class, function or overload is deprecated.
     |
     |  When this decorator is applied to an object, the type checker
     |  will generate a diagnostic on usage of the deprecated object.
     |
     |  Usage:
     |
     |      @deprecated("Use B instead")
     |      class A:
     |          pass
     |
     |      @deprecated("Use g instead")
     |      def f():
     |          pass
     |
     |      @overload
     |      @deprecated("int support is deprecated")
     |      def g(x: int) -> int: ...
     |      @overload
     |      def g(x: str) -> int: ...
     |
     |  The warning specified by *category* will be emitted at runtime
     |  on use of deprecated objects. For functions, that happens on calls;
     |  for classes, on instantiation and on creation of subclasses.
     |  If the *category* is ``None``, no warning is emitted at runtime.
     |  The *stacklevel* determines where the
     |  warning is emitted. If it is ``1`` (the default), the warning
     |  is emitted at the direct caller of the deprecated object; if it
     |  is higher, it is emitted further up the stack.
     |  Static type checker behavior is not affected by the *category*
     |  and *stacklevel* arguments.
     |
     |  The deprecation message passed to the decorator is saved in the
     |  ``__deprecated__`` attribute on the decorated object.
     |  If applied to an overload, the decorator
     |  must be after the ``@overload`` decorator for the attribute to
     |  exist on the overload as returned by ``get_overloads()``.
     |
     |  See PEP 702 for details.
     |
     |  Methods defined here:
     |
     |  __call__(self, arg, /)
     |      Call self as a function.
     |
     |  __init__(
     |      self,
     |      message: str,
     |      /,
     |      *,
     |      category: type[Warning] | None = <class 'DeprecationWarning'>,
     |      stacklevel: int = 1
     |  ) -> None
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

FUNCTIONS
    filterwarnings(
        action,
        message='',
        category=<class 'Warning'>,
        module='',
        lineno=0,
        append=False
    )
        Insert an entry into the list of warnings filters (at the front).

        'action' -- one of "error", "ignore", "always", "all", "default", "module",
                    or "once"
        'message' -- a regex that the warning message must match
        'category' -- a class that the warning must be a subclass of
        'module' -- a regex that the module name must match
        'lineno' -- an integer line number, 0 matches all warnings
        'append' -- if true, append to the list of filters

    formatwarning(message, category, filename, lineno, line=None)
        Function to format a warning the standard way.

    resetwarnings()
        Clear the list of warning filters, so that no filters are active.

    showwarning(message, category, filenam
```

## Related

Other standard-library modules pair well with `warnings`; explore the `python` domain of this catalog.
