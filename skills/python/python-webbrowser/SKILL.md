---
name: python-webbrowser
description: "Program with Python's webbrowser module: Interfaces for launching and remotely controlling web browsers."
version: 1.0.0
tags: [programming, python, stdlib, webbrowser]
---

# Python: `webbrowser`

## Overview

Interfaces for launching and remotely controlling web browsers.

## When to use

Reach for `webbrowser` when your task calls for Interfaces for launching and remotely controlling web browsers. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import webbrowser
```

## Key functions

- `webbrowser.get(using=None)`
- `webbrowser.main(arg_list: list[str] | None = None)`
- `webbrowser.open(url, new=0, autoraise=True)`
- `webbrowser.open_new(url)`
- `webbrowser.open_new_tab(url)`
- `webbrowser.parse_args(arg_list: list[str] | None)`
- `webbrowser.register(name, klass, instance=None, *, preferred=False)`
- `webbrowser.register_X_browsers()`
- `webbrowser.register_standard_browsers()`

## Key classes

`BackgroundBrowser`, `BaseBrowser`, `Chrome`, `Chromium`, `Edge`, `Elinks`, `Epiphany`, `Error`, `GenericBrowser`, `Konqueror`, `Mozilla`, `Opera`, `UnixBrowser`, `WindowsDefault`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import webbrowser

def do_work(...):
    """Use webbrowser to accomplish one well-defined task."""
    result = webbrowser.get(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `webbrowser` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module webbrowser

NAME
    webbrowser - Interfaces for launching and remotely controlling web browsers.

MODULE REFERENCE
    https://docs.python.org/3.14/library/webbrowser.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.Exception(builtins.BaseException)
        Error

    class Error(builtins.Exception)
     |  Method resolution order:
     |      Error
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

FUNCTIONS
    get(using=None)
        Return a browser launcher instance appropriate for the environment.

    open(url, new=0, autoraise=True)
        Display url using the default browser.

        If possible, open url in a location determined by new.
        - 0: the same browser window (the default).
        - 1: a new browser window.
        - 2: a new browser page ("tab").
        If possible, autoraise raises the window (the default) or not.

        If opening the browser succeeds, return True.
        If there is a problem, return False.

    open_new(url)
        Open url in a new window of the default browser.

        If not possible, then open url in the only browser window.

    open_new_tab(url)
        Open url in a new page ("tab") of the default browser.

        If not possible, then the behavior becomes equivalent to open_new().

    register(name, klass, instance=None, *, preferred=False)
        Register a browser connector.

DATA
    __all__ = ['Error', 'open', 'open_new', 'open_new_tab', 'get', 'regist...

FILE
    c:\python314\lib\webbrowser.py


```

## Related

Other standard-library modules pair well with `webbrowser`; explore the `python` domain of this catalog.
