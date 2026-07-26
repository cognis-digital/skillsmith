---
name: python-contextlib
description: "Program with Python's contextlib module: Utilities for with-statement contexts."
version: 1.0.0
tags: [contextlib, programming, python, stdlib]
---

# Python: `contextlib`

## Overview

Utilities for with-statement contexts.  See PEP 343.

## When to use

Reach for `contextlib` when your task calls for Utilities for with-statement contexts. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import contextlib
```

## Key functions

- `contextlib.asynccontextmanager(func)`
- `contextlib.contextmanager(func)`
- `contextlib.wraps(wrapped, assigned=('__module__', '__name__', '__qualname__', '__doc__', '__annotate__', '__type_params__'), updated=('__dict__',))`

## Key classes

`AbstractAsyncContextManager`, `AbstractContextManager`, `AsyncContextDecorator`, `AsyncExitStack`, `ContextDecorator`, `ExitStack`, `GenericAlias`, `MethodType`, `aclosing`, `chdir`, `closing`, `deque`, `nullcontext`, `redirect_stderr`, `redirect_stdout`, `suppress`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import contextlib

def do_work(...):
    """Use contextlib to accomplish one well-defined task."""
    result = contextlib.asynccontextmanager(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `contextlib` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module contextlib

NAME
    contextlib - Utilities for with-statement contexts.  See PEP 343.

MODULE REFERENCE
    https://docs.python.org/3.14/library/contextlib.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    abc.ABC(builtins.object)
        AbstractAsyncContextManager
            AsyncExitStack(_BaseExitStack, AbstractAsyncContextManager)
            aclosing
        AbstractContextManager
            ExitStack(_BaseExitStack, AbstractContextManager)
            chdir
            closing
            nullcontext(AbstractContextManager, AbstractAsyncContextManager)
            suppress
    builtins.object
        ContextDecorator
    _BaseExitStack(builtins.object)
        AsyncExitStack(_BaseExitStack, AbstractAsyncContextManager)
        ExitStack(_BaseExitStack, AbstractContextManager)
    _RedirectStream(AbstractContextManager)
        redirect_stderr
        redirect_stdout

    class AbstractAsyncContextManager(abc.ABC)
     |  An abstract base class for asynchronous context managers.
     |
     |  Method resolution order:
     |      AbstractAsyncContextManager
     |      abc.ABC
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  async __aenter__(self)
     |      Return `self` upon entering the runtime context.
     |
     |  async __aexit__(self, exc_type, exc_value, traceback)
     |      Raise any exception triggered within the runtime context.
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  __class_getitem__ = GenericAlias(args, /)
     |      Represent a PEP 585 generic type
     |
     |      E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).
     |
     |  __subclasshook__(C)
     |      Abstract classes can override this to customize issubclass().
     |
     |      This is invoked early on by abc.ABCMeta.__subclasscheck__().
     |      It should return True, False or NotImplemented.  If it returns
     |      NotImplemented, the normal algorithm is used.  Otherwise, it
     |      overrides the normal algorithm (and the outcome is cached).
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __abstractmethods__ = frozenset({'__aexit__'})

    class AbstractContextManager(abc.ABC)
     |  An abstract base class for context managers.
     |
     |  Method resolution order:
     |      AbstractContextManager
     |      abc.ABC
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __enter__(self)
     |      Return `self` upon entering the runtime context.
     |
     |  __exit__(self, exc_type, exc_value, traceback)
     |      Raise any exception triggered within the runtime context.
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  __class_getitem__ = GenericAlias(args, /)
     |      Represent a PEP 585 generic type
     |
     |      E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).
     |
     |  __subclasshook__(C)
     |      Abstract classes can override this to customize issubclass().
     |
     |      This is invoked early on by abc.ABCMeta.__subclasscheck__().
     |      It should return True, False or NotImplemented.  If it returns
     |      NotImplemented, the normal algorithm is used.  Otherwise, it
     |      overrides the normal algorithm (and the outcome is cached).
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __abstractmethods__ = frozenset({'__exit__'})

    class AsyncExitStack(_BaseExitStack, AbstractAsyncContextManager)
     |  Async context manager for dynamic management of a stack of exit
     |  callbacks.
     |
     |  For example:
     |      async with AsyncExitStack() as stack:
     |          connections = [await stack.enter_async_context(get_connection())
     |              for i in range(5)]
     |          # All opened connections will automatically be released at the
     |          # end of the async with statement, even if attempts to open a
     |          # connection later in the list raise an exception.
     |
     |  Method resolution order:
     |      AsyncExitStack
     |      _BaseExitStack
     |      AbstractAsyncContextManager
     |      abc.ABC
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  async __aenter__(self)
     |      Return `self` upon entering the runtime context.
     |
     |  async __aexit__(self, *exc_details)
     |      Raise any exception triggered within the runtime context.
     |
     |  async aclose(self)
     |      Immediately unwind the context stack.
     |
     |  async enter_async_context(self, cm)
     |      Enters the supplied async context manager.
     |
     |      If successful, also pushes its __aexit__ method as a callback and
     |      returns the result of the __aenter__ method.
     |
     |  push_async_callback(self, callback, /, *args, **kwds)
     |      Registers an arbitrary coroutine function and arguments.
     |
     |      Cannot suppress exceptions.
     |
     |  push_async_exit(self, exit)
     |      Registers a coroutine function with the standard __aexit__ method
     |      signature.
     |
     |      Can suppress exceptions the same way __aexit__ method can.
     |      Also accepts any object with an __aexit__ method (registering a call
     |      to the method instead of the object itself).
     |
     |  ------------------------------------
```

## Related

Other standard-library modules pair well with `contextlib`; explore the `python` domain of this catalog.
