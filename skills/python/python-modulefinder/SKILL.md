---
name: python-modulefinder
description: "Program with Python's modulefinder module: Find modules used by a script, using introspection."
version: 1.0.0
tags: [modulefinder, programming, python, stdlib]
---

# Python: `modulefinder`

## Overview

Find modules used by a script, using introspection.

## When to use

Reach for `modulefinder` when your task calls for Find modules used by a script, using introspection. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import modulefinder
```

## Key functions

- `modulefinder.AddPackagePath(packagename, path)`
- `modulefinder.ReplacePackage(oldname, newname)`
- `modulefinder.test()`

## Key classes

`Module`, `ModuleFinder`

## Constants / attributes

`packagePathMap`, `replacePackageMap`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import modulefinder

def do_work(...):
    """Use modulefinder to accomplish one well-defined task."""
    result = modulefinder.AddPackagePath(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `modulefinder` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module modulefinder

NAME
    modulefinder - Find modules used by a script, using introspection.

MODULE REFERENCE
    https://docs.python.org/3.14/library/modulefinder.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.object
        Module
        ModuleFinder

    class Module(builtins.object)
     |  Module(name, file=None, path=None)
     |
     |  Methods defined here:
     |
     |  __init__(self, name, file=None, path=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
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

    class ModuleFinder(builtins.object)
     |  ModuleFinder(path=None, debug=0, excludes=None, replace_paths=None)
     |
     |  Methods defined here:
     |
     |  __init__(self, path=None, debug=0, excludes=None, replace_paths=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  add_module(self, fqname)
     |
     |  any_missing(self)
     |      Return a list of modules that appear to be missing. Use
     |      any_missing_maybe() if you want to know which modules are
     |      certain to be missing, and which *may* be missing.
     |
     |  any_missing_maybe(self)
     |      Return two lists, one with modules that are certainly missing
     |      and one with modules that *may* be missing. The latter names could
     |      either be submodules *or* just global names in the package.
     |
     |      The reason it can't always be determined is that it's impossible to
     |      tell which names are imported when "from module import *" is done
     |      with an extension module, short of actually importing it.
     |
     |  determine_parent(self, caller, level=-1)
     |
     |  ensure_fromlist(self, m, fromlist, recursive=0)
     |
     |  find_all_submodules(self, m)
     |
     |  find_head_package(self, parent, name)
     |
     |  find_module(self, name, path, parent=None)
     |
     |  import_hook(self, name, caller=None, fromlist=None, level=-1)
     |
     |  import_module(self, partname, fqname, parent)
     |
     |  load_file(self, pathname)
     |
     |  load_module(self, fqname, fp, pathname, file_info)
     |
     |  load_package(self, fqname, pathname)
     |
     |  load_tail(self, q, tail)
     |
     |  msg(self, level, str, *args)
     |
     |  msgin(self, *args)
     |
     |  msgout(self, *args)
     |
     |  replace_paths_in_code(self, co)
     |
     |  report(self)
     |      Print a report to stdout, listing the found modules with their
     |      paths, as well as modules that are missing, or seem to be missing.
     |
     |  run_script(self, pathname)
     |
     |  scan_code(self, co, m)
     |
     |  scan_opcodes(self, co)
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
    AddPackagePath(packagename, path)
        # A Public interface

    ReplacePackage(oldname, newname)

    test()

DATA
    packagePathMap = {}
    replacePackageMap = {}

FILE
    c:\python314\lib\modulefinder.py


```

## Related

Other standard-library modules pair well with `modulefinder`; explore the `python` domain of this catalog.
