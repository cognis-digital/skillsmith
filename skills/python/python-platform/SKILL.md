---
name: python-platform
description: "Program with Python's platform module: This module tries to retrieve as much platform-identifying data as possible."
version: 1.0.0
tags: [platform, programming, python, stdlib]
---

# Python: `platform`

## Overview

This module tries to retrieve as much platform-identifying data as
possible. It makes this information available via function APIs.

If called from the command line, it prints the platform
information concatenated as single string to stdout. The output
format is usable as part of a filename.

## When to use

Reach for `platform` when your task calls for This module tries to retrieve as much platform-identifying data as possible. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import platform
```

## Key functions

- `platform.android_ver(release='', api_level=0, manufacturer='', model='', device='', is_emulator=False)`
- `platform.architecture(executable='C:\\Python314\\python.exe', bits='', linkage='')`
- `platform.freedesktop_os_release()`
- `platform.invalidate_caches()`
- `platform.ios_ver(system='', release='', model='', is_simulator=False)`
- `platform.java_ver(release='', vendor='', vminfo=('', '', ''), osinfo=('', '', ''))`
- `platform.libc_ver(executable=None, lib='', version='', chunksize=16384)`
- `platform.mac_ver(release='', versioninfo=('', '', ''), machine='')`
- `platform.machine()`
- `platform.node()`
- `platform.platform(aliased=False, terse=False)`
- `platform.processor()`
- `platform.python_branch()`
- `platform.python_build()`
- `platform.python_compiler()`
- `platform.python_implementation()`
- `platform.python_revision()`
- `platform.python_version()`
- `platform.python_version_tuple()`
- `platform.release()`
- `platform.system()`
- `platform.system_alias(system, release, version)`
- `platform.uname()`
- `platform.version()`
- `platform.win32_edition()`
- `platform.win32_is_iot()`
- `platform.win32_ver(release='', version='', csd='', ptype='')`

## Key classes

`AndroidVer`, `IOSVersionInfo`, `uname_result`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import platform

def do_work(...):
    """Use platform to accomplish one well-defined task."""
    result = platform.android_ver(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `platform` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module platform

NAME
    platform

MODULE REFERENCE
    https://docs.python.org/3.14/library/platform.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module tries to retrieve as much platform-identifying data as
    possible. It makes this information available via function APIs.

    If called from the command line, it prints the platform
    information concatenated as single string to stdout. The output
    format is usable as part of a filename.

CLASSES
    builtins.tuple(builtins.object)
        AndroidVer
        IOSVersionInfo
    uname_result_base(builtins.tuple)
        uname_result

    class AndroidVer(builtins.tuple)
     |  AndroidVer(release, api_level, manufacturer, model, device, is_emulator)
     |
     |  AndroidVer(release, api_level, manufacturer, model, device, is_emulator)
     |
     |  Method resolution order:
     |      AndroidVer
     |      builtins.tuple
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __getnewargs__(self) from collections.AndroidVer
     |      Return self as a plain tuple.  Used by copy and pickle.
     |
     |  __replace__ = _replace(self, /, **kwds)
     |
     |  __repr__(self) from collections.AndroidVer
     |      Return a nicely formatted representation string
     |
     |  _asdict(self) from collections.AndroidVer
     |      Return a new dict which maps field names to their values.
     |
     |  _replace(self, /, **kwds) from collections.AndroidVer
     |      Return a new AndroidVer object replacing specified fields with new values
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  _make(iterable) from collections.AndroidVer
     |      Make a new AndroidVer object from a sequence or iterable
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(_cls, release, api_level, manufacturer, model, device, is_emulator) from namedtuple_AndroidVer.AndroidVer
     |      Create new instance of AndroidVer(release, api_level, manufacturer, model, device, is_emulator)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  release
     |      Alias for field number 0
     |
     |  api_level
     |      Alias for field number 1
     |
     |  manufacturer
     |      Alias for field number 2
     |
     |  model
     |      Alias for field number 3
     |
     |  device
     |      Alias for field number 4
     |
     |  is_emulator
     |      Alias for field number 5
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __match_args__ = ('release', 'api_level', 'manufacturer', 'model', 'de...
     |
     |  _field_defaults = {}
     |
     |  _fields = ('release', 'api_level', 'manufacturer', 'model', 'device', ...
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

    class IOSVersionInfo(builtins.tuple)
     |  IOSVersionInfo(system, release, model, is_simulator)
     |
     |  IOSVersionInfo(system, release, model, is_simulator)
     |
     |  Method resolution order:
     |      IOSVersionInfo
     |      builtins.tuple
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __getnewargs__(self) from collections.IOSVersionInfo
     |      Return self as a plain tuple.  Used by copy and pickle.
     |
     |  __replace__ = _replace(self, /, **kwds)
     |
     |  __repr__(self) from collections.IOSVersionInfo
     |      Return a nicely formatted representation string
     |
     |  _asdict(self) from collections.IOSVersionInfo
     |      Return a new dict which maps field names to their values.
     |
     |  _replace(self, /, **kwds) from collections.IOSVersionInfo
     |      Return a new IOSVersionInfo object replacing specified fields with new values
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  _make(iterable)
```

## Related

Other standard-library modules pair well with `platform`; explore the `python` domain of this catalog.
