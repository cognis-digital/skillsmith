---
name: python-queue
description: "Program with Python's queue module: A multi-producer, multi-consumer queue."
version: 1.0.0
tags: [programming, python, queue, stdlib]
---

# Python: `queue`

## Overview

A multi-producer, multi-consumer queue.

## When to use

Reach for `queue` when your task calls for A multi-producer, multi-consumer queue. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import queue
```

## Key functions

- `queue.heappop(heap, /)`
- `queue.heappush(heap, item, /)`
- `queue.time()`

## Key classes

`Empty`, `Full`, `LifoQueue`, `PriorityQueue`, `Queue`, `ShutDown`, `SimpleQueue`, `deque`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import queue

def do_work(...):
    """Use queue to accomplish one well-defined task."""
    result = queue.heappop(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `queue` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module queue

NAME
    queue - A multi-producer, multi-consumer queue.

MODULE REFERENCE
    https://docs.python.org/3.14/library/queue.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.Exception(builtins.BaseException)
        _queue.Empty
        Full
        ShutDown
    builtins.object
        _queue.SimpleQueue
        Queue
            LifoQueue
            PriorityQueue

    class Empty(builtins.Exception)
     |  Exception raised by Queue.get(block=0)/get_nowait().
     |
     |  Method resolution order:
     |      Empty
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

    class Full(builtins.Exception)
     |  Exception raised by Queue.put(block=0)/put_nowait().
     |
     |  Method resolution order:
     |      Full
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

    class LifoQueue(Queue)
     |  LifoQueue(maxsize=0)
     |
     |  Variant of Queue that retrieves most recently added entries first.
     |
     |  Method resolution order:
     |      LifoQueue
     |      Queue
     |      builtins.object
     |
     |  Methods inherited from Queue:
     |
     |  __init__(self, maxsize=0)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  empty(self)
     |      Return True if the queue is empty, False otherwise (not reliable!).
     |
     |      This method is likely to be removed at some point.  Use qsize() == 0
     |      as a direct substitute, but be aware that either approach risks a race
     |      condition where a queue can grow before the result of empty() or
     |      qsize() can be used.
     |
     |      To create code that needs to wait for all queued tasks to be
     |      completed, the preferred technique is to use the join() method.
     |
     |  full(self)
     |      Return True if the queue is full, False otherwise (not reliable!).
     |
     |      This method is likely to be removed at some point.  Use qsize() >= n
     |      as a direct substitute, but be aware that either approach risks a race
     |      condition where a queue can shrink before the result of full() or
     |      qsize() can be used.
     |
     |  get(self, block=True, timeout=None)
     |      Remove and return an item from the queue.
     |
     |      If optional args 'block' is true and 'timeout' is None (the default),
     |      block if necessary until an item is available. If 'timeout' is
     |      a non-negative number, it blocks at most 'timeout' seconds and raises
     |      the Empty exception if no item was available within that time.
     |      Otherwise ('block' is false), return an item if one is immediately
     |      available, else raise the Empty exception ('timeout' is ignored
     |      in that case).
     |
  
```

## Related

Other standard-library modules pair well with `queue`; explore the `python` domain of this catalog.
