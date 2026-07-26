---
name: python-sysconfig
description: "Program with Python's sysconfig module: Access to Python's configuration information."
version: 1.0.0
tags: [programming, python, stdlib, sysconfig]
---

# Python: `sysconfig`

## Overview

Access to Python's configuration information.

## When to use

Reach for `sysconfig` when your task calls for Access to Python's configuration information. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import sysconfig
```

## Key functions

- `sysconfig.expand_makefile_vars(s, vars)`
- `sysconfig.get_config_h_filename()`
- `sysconfig.get_config_var(name)`
- `sysconfig.get_config_vars(*args)`
- `sysconfig.get_default_scheme()`
- `sysconfig.get_makefile_filename()`
- `sysconfig.get_path(name, scheme='nt', vars=None, expand=True)`
- `sysconfig.get_path_names()`
- `sysconfig.get_paths(scheme='nt', vars=None, expand=True)`
- `sysconfig.get_platform()`
- `sysconfig.get_preferred_scheme(key)`
- `sysconfig.get_python_version()`
- `sysconfig.get_scheme_names()`
- `sysconfig.is_python_build(check_home=None)`
- `sysconfig.parse_config_h(fp, vars=None)`
- `sysconfig.realpath(path, *, strict=False)`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import sysconfig

def do_work(...):
    """Use sysconfig to accomplish one well-defined task."""
    result = sysconfig.expand_makefile_vars(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `sysconfig` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: package sysconfig

NAME
    sysconfig - Access to Python's configuration information.

MODULE REFERENCE
    https://docs.python.org/3.14/library/sysconfig.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

PACKAGE CONTENTS
    __main__

FUNCTIONS
    get_config_h_filename()
        Return the path of pyconfig.h.

    get_config_var(name)
        Return the value of a single variable using the dictionary returned by
        'get_config_vars()'.

        Equivalent to get_config_vars().get(name)

    get_config_vars(*args)
        With no arguments, return a dictionary of all configuration
        variables relevant for the current platform.

        On Unix, this means every variable defined in Python's installed Makefile;
        On Windows it's a much smaller set.

        With arguments, return a list of values that result from looking up
        each argument in the configuration variable dictionary.

    get_makefile_filename()
        Return the path of the Makefile.

    get_path(name, scheme='nt', vars=None, expand=True)
        Return a path corresponding to the scheme.

        ``scheme`` is the install scheme name.

    get_path_names()
        Return a tuple containing the paths names.

    get_paths(scheme='nt', vars=None, expand=True)
        Return a mapping containing an install scheme.

        ``scheme`` is the install scheme name. If not provided, it will
        return the default scheme for the current platform.

    get_platform()
        Return a string that identifies the current platform.

        This is used mainly to distinguish platform-specific build directories and
        platform-specific built distributions.  Typically includes the OS name and
        version and the architecture (as supplied by 'os.uname()'), although the
        exact information included depends on the OS; on Linux, the kernel version
        isn't particularly important.

        Examples of returned values:


        Windows:

        - win-amd64 (64-bit Windows on AMD64, aka x86_64, Intel64, and EM64T)
        - win-arm64 (64-bit Windows on ARM64, aka AArch64)
        - win32 (all others - specifically, sys.platform is returned)

        POSIX based OS:

        - linux-x86_64
        - macosx-15.5-arm64
        - macosx-26.0-universal2 (macOS on Apple Silicon or Intel)
        - android-24-arm64_v8a

        For other non-POSIX platforms, currently just returns :data:`sys.platform`.

    get_python_version()

    get_scheme_names()
        Return a tuple containing the schemes names.

    parse_config_h(fp, vars=None)
        Parse a config.h-style file.

        A dictionary containing name/value pairs is returned.  If an
        optional dictionary is passed in as the second argument, it is
        used instead of a new dictionary.

DATA
    __all__ = ['get_config_h_filename', 'get_config_var', 'get_config_vars...

FILE
    c:\python314\lib\sysconfig\__init__.py


```

## Related

Other standard-library modules pair well with `sysconfig`; explore the `python` domain of this catalog.
