---
name: python-selectors
description: "Program with Python's selectors module: Selectors module."
version: 1.0.0
tags: [programming, python, selectors, stdlib]
---

# Python: `selectors`

## Overview

Selectors module.

This module allows high-level and efficient I/O multiplexing, built upon the
`select` module primitives.

## When to use

Reach for `selectors` when your task calls for Selectors module. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import selectors
```

## Key functions

- `selectors.abstractmethod(funcobj)`
- `selectors.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)`

## Key classes

`ABCMeta`, `BaseSelector`, `DefaultSelector`, `Mapping`, `SelectSelector`, `SelectorKey`

## Constants / attributes

`EVENT_READ`, `EVENT_WRITE`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import selectors

def do_work(...):
    """Use selectors to accomplish one well-defined task."""
    result = selectors.abstractmethod(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `selectors` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module selectors

NAME
    selectors - Selectors module.

MODULE REFERENCE
    https://docs.python.org/3.14/library/selectors.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module allows high-level and efficient I/O multiplexing, built upon the
    `select` module primitives.

CLASSES
    builtins.object
        BaseSelector
    builtins.tuple(builtins.object)
        SelectorKey
    _BaseSelectorImpl(BaseSelector)
        SelectSelector

    class BaseSelector(builtins.object)
     |  Selector abstract base class.
     |
     |  A selector supports registering file objects to be monitored for specific
     |  I/O events.
     |
     |  A file object is a file descriptor or any object with a `fileno()` method.
     |  An arbitrary object can be attached to the file object, which can be used
     |  for example to store context information, a callback, etc.
     |
     |  A selector can use various implementations (select(), poll(), epoll()...)
     |  depending on the platform. The default `Selector` class uses the most
     |  efficient implementation on the current platform.
     |
     |  Methods defined here:
     |
     |  __enter__(self)
     |
     |  __exit__(self, *args)
     |
     |  close(self)
     |      Close the selector.
     |
     |      This must be called to make sure that any underlying resource is freed.
     |
     |  get_key(self, fileobj)
     |      Return the key associated to a registered file object.
     |
     |      Returns:
     |      SelectorKey for this file object
     |
     |  get_map(self)
     |      Return a mapping of file objects to selector keys.
     |
     |  modify(self, fileobj, events, data=None)
     |      Change a registered file object monitored events or attached data.
     |
     |      Parameters:
     |      fileobj -- file object or file descriptor
     |      events  -- events to monitor (bitwise mask of EVENT_READ|EVENT_WRITE)
     |      data    -- attached data
     |
     |      Returns:
     |      SelectorKey instance
     |
     |      Raises:
     |      Anything that unregister() or register() raises
     |
     |  register(self, fileobj, events, data=None)
     |      Register a file object.
     |
     |      Parameters:
     |      fileobj -- file object or file descriptor
     |      events  -- events to monitor (bitwise mask of EVENT_READ|EVENT_WRITE)
     |      data    -- attached data
     |
     |      Returns:
     |      SelectorKey instance
     |
     |      Raises:
     |      ValueError if events is invalid
     |      KeyError if fileobj is already registered
     |      OSError if fileobj is closed or otherwise is unacceptable to
     |              the underlying system call (if a system call is made)
     |
     |      Note:
     |      OSError may or may not be raised
     |
     |  select(self, timeout=None)
     |      Perform the actual selection, until some monitored file objects are
     |      ready or a timeout expires.
     |
     |      Parameters:
     |      timeout -- if timeout > 0, this specifies the maximum wait time, in
     |                 seconds
     |                 if timeout <= 0, the select() call won't block, and will
     |                 report the currently ready file objects
     |                 if timeout is None, select() will block until a monitored
     |                 file object becomes ready
     |
     |      Returns:
     |      list of (key, events) for ready file objects
     |      `events` is a bitwise mask of EVENT_READ|EVENT_WRITE
     |
     |  unregister(self, fileobj)
     |      Unregister a file object.
     |
     |      Parameters:
     |      fileobj -- file object or file descriptor
     |
     |      Returns:
     |      SelectorKey instance
     |
     |      Raises:
     |      KeyError if fileobj is not registered
     |
     |      Note:
     |      If fileobj is registered but has since been closed this does
     |      *not* raise OSError (even if the wrapped syscall does)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __abstractmethods__ = frozenset({'get_map', 'register', 'select', 'unr...

    DefaultSelector = class SelectSelector(_BaseSelectorImpl)
     |  Select-based selector.
     |
     |  Method resolution order:
     |      SelectSelector
     |      _BaseSelectorImpl
     |      BaseSelector
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  register(self, fileobj, events, data=None)
     |      Register a file object.
     |
     |      Parameters:
     |      fileobj -- file object or file descriptor
     |      events  -- events to monitor (bitwise mask of EVENT_READ|EVENT_WRITE)
     |      data    -- attached data
     |
     |      Returns:
     |      SelectorKey instance
     |
     |      Raises:
     |      ValueError if events is invalid
     |      KeyError if fileobj is already registered
     |      OSError if fileobj is closed or otherwise is unacceptable to
     |              the underlying system call (if a system call is made)
     |
     |      Note:
     |      OSError may or may not be raised
     |
     |  select(self, timeout=None)
     |      Perform the actual selection, un
```

## Related

Other standard-library modules pair well with `selectors`; explore the `python` domain of this catalog.
