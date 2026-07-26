---
name: python-pkgutil
description: "Program with Python's pkgutil module: Utilities to support packages."
version: 1.0.0
tags: [pkgutil, programming, python, stdlib]
---

# Python: `pkgutil`

## Overview

Utilities to support packages.

## When to use

Reach for `pkgutil` when your task calls for Utilities to support packages. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import pkgutil
```

## Key functions

- `pkgutil.extend_path(path, name)`
- `pkgutil.get_data(package, resource)`
- `pkgutil.get_importer(path_item)`
- `pkgutil.iter_importer_modules(importer, prefix='')`
- `pkgutil.iter_importers(fullname='')`
- `pkgutil.iter_modules(path=None, prefix='')`
- `pkgutil.iter_zipimport_modules(importer, prefix='')`
- `pkgutil.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)`
- `pkgutil.read_code(stream)`
- `pkgutil.resolve_name(name)`
- `pkgutil.simplegeneric(func)`
- `pkgutil.walk_packages(path=None, prefix='', onerror=None)`

## Key classes

`ModuleInfo`, `zipimporter`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import pkgutil

def do_work(...):
    """Use pkgutil to accomplish one well-defined task."""
    result = pkgutil.extend_path(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `pkgutil` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module pkgutil

NAME
    pkgutil - Utilities to support packages.

MODULE REFERENCE
    https://docs.python.org/3.14/library/pkgutil.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.tuple(builtins.object)
        ModuleInfo

    class ModuleInfo(builtins.tuple)
     |  ModuleInfo(module_finder, name, ispkg)
     |
     |  A namedtuple with minimal info about a module.
     |
     |  Method resolution order:
     |      ModuleInfo
     |      builtins.tuple
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __getnewargs__(self) from collections.ModuleInfo
     |      Return self as a plain tuple.  Used by copy and pickle.
     |
     |  __replace__ = _replace(self, /, **kwds)
     |
     |  __repr__(self) from collections.ModuleInfo
     |      Return a nicely formatted representation string
     |
     |  _asdict(self) from collections.ModuleInfo
     |      Return a new dict which maps field names to their values.
     |
     |  _replace(self, /, **kwds) from collections.ModuleInfo
     |      Return a new ModuleInfo object replacing specified fields with new values
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  _make(iterable) from collections.ModuleInfo
     |      Make a new ModuleInfo object from a sequence or iterable
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(_cls, module_finder, name, ispkg) from namedtuple_ModuleInfo.ModuleInfo
     |      Create new instance of ModuleInfo(module_finder, name, ispkg)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  module_finder
     |      Alias for field number 0
     |
     |  name
     |      Alias for field number 1
     |
     |  ispkg
     |      Alias for field number 2
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __match_args__ = ('module_finder', 'name', 'ispkg')
     |
     |  _field_defaults = {}
     |
     |  _fields = ('module_finder', 'name', 'ispkg')
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __contains__(self, key, /)
     |      Return bool(key in self).
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getitem__(self, key, /)
     |      Return self[key].
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __len__(self, /)
     |      Return len(self).
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __mul__(self, value, /)
     |      Return self*value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __rmul__(self, value, /)
     |      Return value*self.
     |
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |
     |      Raises ValueError if the value is not present.
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from builtins.tuple:
     |
     |  __class_getitem__(object, /)
     |      See PEP 585

FUNCTIONS
    extend_path(path, name)
        Extend a package's path.

        Intended use is to place the following code in a package's __init__.py:

            from pkgutil import extend_path
            __path__ = extend_path(__path__, __name__)

        For each directory on sys.path that has a subdirectory that
        matches the package name, add the subdirectory to the package's
        __path__.  This is useful if one wants to distribute different
        parts of a single logical package as multiple directories.

        It also looks for *.pkg files beginning where * matches the name
        argument.  This feature is similar to *.pth files (see site.py),
        except that it doesn't special-case lines starting with 'import'.
        A *.pkg file is trusted at face value: apart from checking for
        duplicates, all entries found in a *.pkg file are added to the
        path, regardless of whether they are exist the filesystem.  (This
        is a feature.)

        If the input path is not a list (as is the case for frozen
        packages) it is returned unchanged.  The input path is not
        modified; an extended copy is returned.  Items are only appended
        to the copy at the end.

        It is assumed that sys.path is a sequence.  Items of sys.path that
        are not (unicode or 8-bit) strings referring to existing
        directories are ignored.  Unicode items of sys.path that cause
        errors when used as filenames may cause this function to raise an
        exception (in line with os.path.isdir() behavior).

    get_data(package, resource)
        Get a resource from a package.

        This is a wrapper round the PEP 302 loader get_data API. The package
        argument should be the name of a package, in standard module format
        (foo.bar). The resourc
```

## Related

Other standard-library modules pair well with `pkgutil`; explore the `python` domain of this catalog.
