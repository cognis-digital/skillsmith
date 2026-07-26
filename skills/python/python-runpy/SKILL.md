---
name: python-runpy
description: "Program with Python's runpy module: runpy.py - locating and running Python code using the module namespace Provides support for locating and running Python scripts using the Python module namespace instead of the native filesystem."
version: 1.0.0
tags: [programming, python, runpy, stdlib]
---

# Python: `runpy`

## Overview

runpy.py - locating and running Python code using the module namespace

Provides support for locating and running Python scripts using the Python
module namespace instead of the native filesystem.

This allows Python code to play nicely with non-filesystem based PEP 302
importers when locating support scripts as well as when importing modules.

## When to use

Reach for `runpy` when your task calls for runpy.py - locating and running Python code using the module namespace Provides support for locating and running Python . It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import runpy
```

## Key functions

- `runpy.run_module(mod_name, init_globals=None, run_name=None, alter_sys=False)`
- `runpy.run_path(path_name, init_globals=None, run_name=None)`

## Key classes

`ModuleType`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import runpy

def do_work(...):
    """Use runpy to accomplish one well-defined task."""
    result = runpy.run_module(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `runpy` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module runpy

NAME
    runpy - runpy.py - locating and running Python code using the module namespace

MODULE REFERENCE
    https://docs.python.org/3.14/library/runpy.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Provides support for locating and running Python scripts using the Python
    module namespace instead of the native filesystem.

    This allows Python code to play nicely with non-filesystem based PEP 302
    importers when locating support scripts as well as when importing modules.

FUNCTIONS
    run_module(mod_name, init_globals=None, run_name=None, alter_sys=False)
        Execute a module's code without importing it.

        mod_name -- an absolute module name or package name.

        Optional arguments:
        init_globals -- dictionary used to pre-populate the module’s
        globals dictionary before the code is executed.

        run_name -- if not None, this will be used for setting __name__;
        otherwise, __name__ will be set to mod_name + '__main__' if the
        named module is a package and to just mod_name otherwise.

        alter_sys -- if True, sys.argv[0] is updated with the value of
        __file__ and sys.modules[__name__] is updated with a temporary
        module object for the module being executed. Both are
        restored to their original values before the function returns.

        Returns the resulting module globals dictionary.

    run_path(path_name, init_globals=None, run_name=None)
        Execute code located at the specified filesystem location.

        path_name -- filesystem location of a Python script, zipfile,
        or directory containing a top level __main__.py script.

        Optional arguments:
        init_globals -- dictionary used to pre-populate the module’s
        globals dictionary before the code is executed.

        run_name -- if not None, this will be used to set __name__;
        otherwise, '<run_path>' will be used for __name__.

        Returns the resulting module globals dictionary.

DATA
    __all__ = ['run_module', 'run_path']

FILE
    c:\python314\lib\runpy.py


```

## Related

Other standard-library modules pair well with `runpy`; explore the `python` domain of this catalog.
