---
name: python-multiprocessing
description: "Program with Python's multiprocessing module: The Python standard-library module `multiprocessing`."
version: 1.0.0
tags: [multiprocessing, programming, python, stdlib]
---

# Python: `multiprocessing`

## Overview

`multiprocessing` is part of the Python standard library.

## When to use

Reach for `multiprocessing` when your task calls for The Python standard-library module `multiprocessing`. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import multiprocessing
```

## Key functions

- `multiprocessing.Array(typecode_or_type, size_or_initializer, *, lock=True)`
- `multiprocessing.Barrier(parties, action=None, timeout=None)`
- `multiprocessing.BoundedSemaphore(value=1)`
- `multiprocessing.Condition(lock=None)`
- `multiprocessing.Event()`
- `multiprocessing.JoinableQueue(maxsize=0)`
- `multiprocessing.Lock()`
- `multiprocessing.Manager()`
- `multiprocessing.Pipe(duplex=True)`
- `multiprocessing.Pool(processes=None, initializer=None, initargs=(), maxtasksperchild=None)`
- `multiprocessing.Queue(maxsize=0)`
- `multiprocessing.RLock()`
- `multiprocessing.RawArray(typecode_or_type, size_or_initializer)`
- `multiprocessing.RawValue(typecode_or_type, *args)`
- `multiprocessing.Semaphore(value=1)`
- `multiprocessing.SimpleQueue()`
- `multiprocessing.Value(typecode_or_type, *args, lock=True)`
- `multiprocessing.active_children()`
- `multiprocessing.allow_connection_pickling()`
- `multiprocessing.cpu_count()`
- `multiprocessing.current_process()`
- `multiprocessing.freeze_support()`
- `multiprocessing.get_all_start_methods()`
- `multiprocessing.get_context(method=None)`
- `multiprocessing.get_logger()`
- `multiprocessing.get_start_method(allow_none=False)`
- `multiprocessing.log_to_stderr(level=None)`
- `multiprocessing.parent_process()`
- `multiprocessing.set_executable(executable)`
- `multiprocessing.set_forkserver_preload(module_names)`

## Key classes

`AuthenticationError`, `BufferTooShort`, `Process`, `ProcessError`, `TimeoutError`

## Constants / attributes

`SUBDEBUG`, `SUBWARNING`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import multiprocessing

def do_work(...):
    """Use multiprocessing to accomplish one well-defined task."""
    result = multiprocessing.Array(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `multiprocessing` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: package multiprocessing

NAME
    multiprocessing

MODULE REFERENCE
    https://docs.python.org/3.14/library/multiprocessing.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    # Package analogous to 'threading.py' but using processes
    #
    # multiprocessing/__init__.py
    #
    # This package is intended to duplicate the functionality (and much of
    # the API) of threading.py but uses processes instead of threads.  A
    # subpackage 'multiprocessing.dummy' has the same API but is a simple
    # wrapper for 'threading'.
    #
    # Copyright (c) 2006-2008, R Oudkerk
    # Licensed to PSF under a Contributor Agreement.
    #

PACKAGE CONTENTS
    connection
    context
    dummy (package)
    forkserver
    heap
    managers
    pool
    popen_fork
    popen_forkserver
    popen_spawn_posix
    popen_spawn_win32
    process
    queues
    reduction
    resource_sharer
    resource_tracker
    shared_memory
    sharedctypes
    spawn
    synchronize
    util

SUBMODULES
    reducer

CLASSES
    builtins.Exception(builtins.BaseException)
        multiprocessing.context.ProcessError
            multiprocessing.context.AuthenticationError
            multiprocessing.context.BufferTooShort
            multiprocessing.context.TimeoutError
    multiprocessing.process.BaseProcess(builtins.object)
        multiprocessing.context.Process

    class AuthenticationError(ProcessError)
     |  Method resolution order:
     |      AuthenticationError
     |      ProcessError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors inherited from ProcessError:
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

    class BufferTooShort(ProcessError)
     |  Method resolution order:
     |      BufferTooShort
     |      ProcessError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors inherited from ProcessError:
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

    class Process(multiprocessing.process.BaseProcess)
     |  Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
     |
     |  Method resolution order:
     |      Process
     |      multiprocessing.process.BaseProcess
     |      builtins.object
     |
     |  Methods inherited from multiprocessing.process.BaseProcess:
     |
     |  __init__(
     |      self,
     |      group=None,
     |      target=None,
     |      name=None,
     |      args=(),
     |      kwargs={},
     |      *,
     |      daemon=None
     |  )
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  close(self)
     |      Close the Process object.
     |
     |      This method releases resources held by the Process object.  It is
     |      an error to call this method if the child process is still running.
     |
     |  interrupt(self)
     |      Terminate process; sends SIGINT si
```

## Related

Other standard-library modules pair well with `multiprocessing`; explore the `python` domain of this catalog.
