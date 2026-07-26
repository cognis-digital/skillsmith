---
name: python-tarfile
description: "Program with Python's tarfile module: Read from and write to tar format archives."
version: 1.0.0
tags: [programming, python, stdlib, tarfile]
---

# Python: `tarfile`

## Overview

Read from and write to tar format archives.

## When to use

Reach for `tarfile` when your task calls for Read from and write to tar format archives. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import tarfile
```

## Key functions

- `tarfile.bltn_open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`
- `tarfile.calc_chksums(buf)`
- `tarfile.copyfileobj(src, dst, length=None, exception=<class 'OSError'>, bufsize=None)`
- `tarfile.data_filter(member, dest_path)`
- `tarfile.fully_trusted_filter(member, dest_path)`
- `tarfile.is_tarfile(name)`
- `tarfile.itn(n, digits=8, format=2)`
- `tarfile.main()`
- `tarfile.nti(s)`
- `tarfile.nts(s, encoding, errors)`
- `tarfile.open(name=None, mode='r', fileobj=None, bufsize=10240, **kwargs)`
- `tarfile.stn(s, length, encoding, errors)`
- `tarfile.tar_filter(member, dest_path)`

## Key classes

`AbsoluteLinkError`, `AbsolutePathError`, `CompressionError`, `EOFHeaderError`, `EmptyHeaderError`, `ExFileObject`, `ExtractError`, `FilterError`, `HeaderError`, `InvalidHeaderError`, `LinkFallbackError`, `LinkOutsideDestinationError`, `OutsideDestinationError`, `ReadError`, `SpecialFileError`, `StreamError`, `SubsequentHeaderError`, `TarError`, `TarFile`, `TarInfo`, `TruncatedHeaderError`

## Constants / attributes

`AREGTYPE`, `BLKTYPE`, `BLOCKSIZE`, `CHRTYPE`, `CONTTYPE`, `DEFAULT_FORMAT`, `DIRTYPE`, `ENCODING`, `FIFOTYPE`, `GNUTYPE_LONGLINK`, `GNUTYPE_LONGNAME`, `GNUTYPE_SPARSE`, `GNU_FORMAT`, `GNU_MAGIC`, `GNU_TYPES`, `LENGTH_LINK`, `LENGTH_NAME`, `LENGTH_PREFIX`, `LNKTYPE`, `NUL`, `PAX_FIELDS`, `PAX_FORMAT`, `PAX_NAME_FIELDS`, `PAX_NUMBER_FIELDS`, `POSIX_MAGIC`, `RECORDSIZE`, `REGTYPE`, `REGULAR_TYPES`, `SOLARIS_XHDTYPE`, `SUPPORTED_TYPES`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import tarfile

def do_work(...):
    """Use tarfile to accomplish one well-defined task."""
    result = tarfile.bltn_open(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `tarfile` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module tarfile

NAME
    tarfile - Read from and write to tar format archives.

MODULE REFERENCE
    https://docs.python.org/3.14/library/tarfile.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.Exception(builtins.BaseException)
        TarError
            CompressionError
            ExtractError
            FilterError
                AbsoluteLinkError
                AbsolutePathError
                LinkFallbackError
                LinkOutsideDestinationError
                OutsideDestinationError
                SpecialFileError
            HeaderError
            ReadError
            StreamError
    builtins.object
        TarFile
        TarInfo

    class AbsoluteLinkError(FilterError)
     |  AbsoluteLinkError(tarinfo)
     |
     |  Method resolution order:
     |      AbsoluteLinkError
     |      FilterError
     |      TarError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, tarinfo)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from TarError:
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

    class AbsolutePathError(FilterError)
     |  AbsolutePathError(tarinfo)
     |
     |  Method resolution order:
     |      AbsolutePathError
     |      FilterError
     |      TarError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, tarinfo)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from TarError:
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

    class CompressionError(TarError)
     |  Exception for unavailable compression methods.
     |
     |  Method resolution order:
     |      CompressionError
     |      TarError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors inherited from TarError:
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
     |      Set self.__tra
```

## Related

Other standard-library modules pair well with `tarfile`; explore the `python` domain of this catalog.
