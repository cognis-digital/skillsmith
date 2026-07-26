---
name: python-sched
description: "Program with Python's sched module: A generally useful event scheduler class."
version: 1.0.0
tags: [programming, python, sched, stdlib]
---

# Python: `sched`

## Overview

A generally useful event scheduler class.

Each instance of this class manages its own queue.
No multi-threading is implied; you are supposed to hack that
yourself, or use a single instance per application.

Each instance is parametrized with two functions, one that is
supposed to return the current time, one that is supposed to
implement a delay.  You can implement real-time scheduling by
substituting time and sleep from built-in module time, or you can
implement simulated time by writing your own functions.  This can
also be used to integrate scheduling with STDWIN events; the delay
function is allowed to modify the queue.  Time can be expressed as
integers or floating-point numbers, as long as it is consistent.

Events are specified by tuples (time, priority, action, argument, kwargs).
As in UNIX, lower priority numbers mean higher priority; in this
way the queue can be maintained as a priority queue.  Execution of the
event means calling the action function, passing it the argument
sequence in "argument" (remember that in Python, multiple function
arguments are be packed in a sequence) and keyword parameters in "kwargs".
The action function may be an instance method so it
has another way to reference private data (besides global variables).

## When to use

Reach for `sched` when your task calls for A generally useful event scheduler class. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import sched
```

## Key functions

- `sched.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)`

## Key classes

`Event`, `count`, `scheduler`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import sched

def do_work(...):
    """Use sched to accomplish one well-defined task."""
    result = sched.namedtuple(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `sched` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module sched

NAME
    sched - A generally useful event scheduler class.

MODULE REFERENCE
    https://docs.python.org/3.14/library/sched.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Each instance of this class manages its own queue.
    No multi-threading is implied; you are supposed to hack that
    yourself, or use a single instance per application.

    Each instance is parametrized with two functions, one that is
    supposed to return the current time, one that is supposed to
    implement a delay.  You can implement real-time scheduling by
    substituting time and sleep from built-in module time, or you can
    implement simulated time by writing your own functions.  This can
    also be used to integrate scheduling with STDWIN events; the delay
    function is allowed to modify the queue.  Time can be expressed as
    integers or floating-point numbers, as long as it is consistent.

    Events are specified by tuples (time, priority, action, argument, kwargs).
    As in UNIX, lower priority numbers mean higher priority; in this
    way the queue can be maintained as a priority queue.  Execution of the
    event means calling the action function, passing it the argument
    sequence in "argument" (remember that in Python, multiple function
    arguments are be packed in a sequence) and keyword parameters in "kwargs".
    The action function may be an instance method so it
    has another way to reference private data (besides global variables).

CLASSES
    builtins.object
        scheduler

    class scheduler(builtins.object)
     |  scheduler(
     |      timefunc=<built-in function monotonic>,
     |      delayfunc=<built-in function sleep>
     |  )
     |
     |  Methods defined here:
     |
     |  __init__(
     |      self,
     |      timefunc=<built-in function monotonic>,
     |      delayfunc=<built-in function sleep>
     |  )
     |      Initialize a new instance, passing the time and delay
     |      functions
     |
     |  cancel(self, event)
     |      Remove an event from the queue.
     |
     |      This must be presented the ID as returned by enter().
     |      If the event is not in the queue, this raises ValueError.
     |
     |  empty(self)
     |      Check whether the queue is empty.
     |
     |  enter(
     |      self,
     |      delay,
     |      priority,
     |      action,
     |      argument=(),
     |      kwargs=<object object at 0x000001B05F332750>
     |  )
     |      A variant that specifies the time as a relative time.
     |
     |      This is actually the more commonly used interface.
     |
     |  enterabs(
     |      self,
     |      time,
     |      priority,
     |      action,
     |      argument=(),
     |      kwargs=<object object at 0x000001B05F332750>
     |  )
     |      Enter a new event in the queue at an absolute time.
     |
     |      Returns an ID for the event which can be used to remove it,
     |      if necessary.
     |
     |  run(self, blocking=True)
     |      Execute events until the queue is empty.
     |      If blocking is False executes the scheduled events due to
     |      expire soonest (if any) and then return the deadline of the
     |      next scheduled call in the scheduler.
     |
     |      When there is a positive delay until the first event, the
     |      delay function is called and the event is left in the queue;
     |      otherwise, the event is removed from the queue and executed
     |      (its action function is called, passing it the argument).  If
     |      the delay function returns prematurely, it is simply
     |      restarted.
     |
     |      It is legal for both the delay function and the action
     |      function to modify the queue or to raise an exception;
     |      exceptions are not caught but the scheduler's state remains
     |      well-defined so run() may be called again.
     |
     |      A questionable hack is added to allow other threads to run:
     |      just after an event is executed, a delay of 0 is executed, to
     |      avoid monopolizing the CPU when other threads are also
     |      runnable.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  queue
     |      An ordered list of upcoming events.
     |
     |      Events are named tuples with fields for:
     |          time, priority, action, arguments, kwargs
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

DATA
    __all__ = ['scheduler']

FILE
    c:\python314\lib\sched.py


```

## Related

Other standard-library modules pair well with `sched`; explore the `python` domain of this catalog.
