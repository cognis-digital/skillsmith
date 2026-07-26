---
name: python-shutil
description: "Program with Python's shutil module: Utility functions for copying and archiving files and directory trees."
version: 1.0.0
tags: [programming, python, shutil, stdlib]
---

# Python: `shutil`

## Overview

Utility functions for copying and archiving files and directory trees.

XXX The functions here don't copy the resource fork or other metadata on Mac.

## When to use

Reach for `shutil` when your task calls for Utility functions for copying and archiving files and directory trees. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import shutil
```

## Key functions

- `shutil.chown(path, user=None, group=None, *, dir_fd=None, follow_symlinks=True)`
- `shutil.copy(src, dst, *, follow_symlinks=True)`
- `shutil.copy2(src, dst, *, follow_symlinks=True)`
- `shutil.copyfile(src, dst, *, follow_symlinks=True)`
- `shutil.copyfileobj(fsrc, fdst, length=0)`
- `shutil.copymode(src, dst, *, follow_symlinks=True)`
- `shutil.copystat(src, dst, *, follow_symlinks=True)`
- `shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=<function copy2 at 0x000001B05FAA2E50>, ignore_dangling_symlinks=False, dirs_exist_ok=False)`
- `shutil.disk_usage(path)`
- `shutil.get_archive_formats()`
- `shutil.get_terminal_size(fallback=(80, 24))`
- `shutil.get_unpack_formats()`
- `shutil.ignore_patterns(*patterns)`
- `shutil.make_archive(base_name, format, root_dir=None, base_dir=None, verbose=0, dry_run=0, owner=None, group=None, logger=None)`
- `shutil.move(src, dst, copy_function=<function copy2 at 0x000001B05FAA2E50>)`
- `shutil.register_archive_format(name, function, extra_args=None, description='')`
- `shutil.register_unpack_format(name, extensions, function, extra_args=None, description='')`
- `shutil.rmtree(path, ignore_errors=False, onerror=None, *, onexc=None, dir_fd=None)`
- `shutil.unpack_archive(filename, extract_dir=None, format=None, *, filter=None)`
- `shutil.unregister_archive_format(name)`
- `shutil.unregister_unpack_format(name)`
- `shutil.which(cmd, mode=1, path=None)`

## Key classes

`Error`, `ReadError`, `RegistryError`, `SameFileError`, `SpecialFileError`

## Constants / attributes

`COPY_BUFSIZE`, `posix`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import shutil

def do_work(...):
    """Use shutil to accomplish one well-defined task."""
    result = shutil.chown(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `shutil` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module shutil

NAME
    shutil - Utility functions for copying and archiving files and directory trees.

MODULE REFERENCE
    https://docs.python.org/3.14/library/shutil.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    XXX The functions here don't copy the resource fork or other metadata on Mac.

CLASSES
    builtins.OSError(builtins.Exception)
        Error
            SameFileError
        SpecialFileError

    class Error(builtins.OSError)
     |  Method resolution order:
     |      Error
     |      builtins.OSError
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
     |  Methods inherited from builtins.OSError:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__(self, /)
     |      Helper for pickle.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.OSError:
     |
     |  __new__(*args, **kwargs) class method of builtins.OSError
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.OSError:
     |
     |  characters_written
     |
     |  errno
     |      POSIX exception code
     |
     |  filename
     |      exception filename
     |
     |  filename2
     |      second exception filename
     |
     |  strerror
     |      exception strerror
     |
     |  winerror
     |      Win32 exception code
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setstate__(self, state, /)
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

    class SameFileError(Error)
     |  Raised when source and destination are the same file.
     |
     |  Method resolution order:
     |      SameFileError
     |      Error
     |      builtins.OSError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors inherited from Error:
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.OSError:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__(self, /)
     |      Helper for pickle.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.OSError:
     |
     |  __new__(*args, **kwargs) class method of builtins.OSError
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.OSError:
     |
     |  characters_written
     |
     |  errno
     |      POSIX exception code
     |
     |  filename
     |      exception filename
     |
     |  filename2
     |      second exception filename
     |
     |  strerror
     |      exception strerror
     |
     |  winerror
     |      Win32 exception code
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setstate__(self, state, /)
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

    class SpecialFileError(builtins.OSError)
     |  Raised when trying to do a kind of operation (e.g. copying) which is
     |  not supported on a special file (e.g. a named pipe)
     |
     |  Method resolution order:
     |      SpecialFileError
     |      builtins.OSError
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
     |  Methods inherited from builtins.OSError:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(
```

## Related

Other standard-library modules pair well with `shutil`; explore the `python` domain of this catalog.
