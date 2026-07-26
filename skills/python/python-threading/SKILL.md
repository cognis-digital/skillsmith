---
name: python-threading
description: "Program with Python's threading module: Thread module emulating a subset of Java's threading model."
version: 1.0.0
tags: [programming, python, stdlib, threading]
---

# Python: `threading`

## Overview

Thread module emulating a subset of Java's threading model.

## When to use

Reach for `threading` when your task calls for Thread module emulating a subset of Java's threading model. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import threading
```

## Key functions

- `threading.RLock(*args, **kwargs)`
- `threading.activeCount()`
- `threading.active_count()`
- `threading.currentThread()`
- `threading.current_thread()`
- `threading.enumerate()`
- `threading.excepthook(args, /)`
- `threading.get_ident()`
- `threading.get_native_id()`
- `threading.getprofile()`
- `threading.gettrace()`
- `threading.main_thread()`
- `threading.setprofile(func)`
- `threading.setprofile_all_threads(func)`
- `threading.settrace(func)`
- `threading.settrace_all_threads(func)`
- `threading.stack_size(size=0, /)`

## Key classes

`Barrier`, `BoundedSemaphore`, `BrokenBarrierError`, `Condition`, `Event`, `ExceptHookArgs`, `Lock`, `Semaphore`, `Thread`, `ThreadError`, `Timer`, `WeakSet`, `local`

## Constants / attributes

`TIMEOUT_MAX`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import threading

def do_work(...):
    """Use threading to accomplish one well-defined task."""
    result = threading.RLock(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `threading` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module threading

NAME
    threading - Thread module emulating a subset of Java's threading model.

MODULE REFERENCE
    https://docs.python.org/3.14/library/threading.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.Exception(builtins.BaseException)
        builtins.RuntimeError
            BrokenBarrierError
    builtins.object
        _thread._local
        _thread.lock
        Barrier
        Condition
        Event
        Semaphore
            BoundedSemaphore
        Thread
            Timer
    builtins.tuple(builtins.object)
        _thread._ExceptHookArgs

    class Barrier(builtins.object)
     |  Barrier(parties, action=None, timeout=None)
     |
     |  Implements a Barrier.
     |
     |  Useful for synchronizing a fixed number of threads at known synchronization
     |  points.  Threads block on 'wait()' and are simultaneously awoken once they
     |  have all made that call.
     |
     |  Methods defined here:
     |
     |  __init__(self, parties, action=None, timeout=None)
     |      Create a barrier, initialised to 'parties' threads.
     |
     |      'action' is a callable which, when supplied, will be called by one of
     |      the threads after they have all entered the barrier and just prior to
     |      releasing them all. If a 'timeout' is provided, it is used as the
     |      default for all subsequent 'wait()' calls.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  abort(self)
     |      Place the barrier into a 'broken' state.
     |
     |      Useful in case of error.  Any currently waiting threads and threads
     |      attempting to 'wait()' will have BrokenBarrierError raised.
     |
     |  reset(self)
     |      Reset the barrier to the initial state.
     |
     |      Any threads currently waiting will get the BrokenBarrier exception
     |      raised.
     |
     |  wait(self, timeout=None)
     |      Wait for the barrier.
     |
     |      When the specified number of threads have started waiting, they are all
     |      simultaneously awoken. If an 'action' was provided for the barrier, one
     |      of the threads will have executed that callback prior to returning.
     |      Returns an individual index number from 0 to 'parties-1'.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  broken
     |      Return True if the barrier is in a broken state.
     |
     |  n_waiting
     |      Return the number of threads currently waiting at the barrier.
     |
     |  parties
     |      Return the number of threads required to trip the barrier.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class BoundedSemaphore(Semaphore)
     |  BoundedSemaphore(value=1)
     |
     |  Implements a bounded semaphore.
     |
     |  A bounded semaphore checks to make sure its current value doesn't exceed its
     |  initial value. If it does, ValueError is raised. In most situations
     |  semaphores are used to guard resources with limited capacity.
     |
     |  If the semaphore is released too many times it's a sign of a bug. If not
     |  given, value defaults to 1.
     |
     |  Like regular semaphores, bounded semaphores manage a counter representing
     |  the number of release() calls minus the number of acquire() calls, plus an
     |  initial value. The acquire() method blocks if necessary until it can return
     |  without making the counter negative. If not given, value defaults to 1.
     |
     |  Method resolution order:
     |      BoundedSemaphore
     |      Semaphore
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, value=1)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  release(self, n=1)
     |      Release a semaphore, incrementing the internal counter by one or more.
     |
     |      When the counter is zero on entry and another thread is waiting for it
     |      to become larger than zero again, wake up that thread.
     |
     |      If the number of releases exceeds the number of acquires,
     |      raise a ValueError.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Semaphore:
     |
     |  __enter__ = acquire(self, blocking=True, timeout=None)
     |
     |  __exit__(self, t, v, tb)
     |
     |  acquire(self, blocking=True, timeout=None)
     |      Acquire a semaphore, decrementing the internal counter by one.
     |
     |      When invoked without arguments: if the internal counter is larger than
     |      zero on entry, decrement it by one and return immediately. If it is zero
     |      on entry, block, waiting until some other thread has called release() to
     |      make it larger than zero. This is done with proper interlocking so that
     |      if multiple acquire() calls are blocked, release() will wake exactly one
     |      of them up. The implementation may pick one at random, so the order in
     |      which blocked threads are awakened should not be relied on. There is no
     |      return value in this case.
     |
     |      When invoked with blocking set to true, do the same thing as when called
     |      without arguments, and return true.
     |
     |      When invoked with blocking set to fals
```

## Related

Other standard-library modules pair well with `threading`; explore the `python` domain of this catalog.
