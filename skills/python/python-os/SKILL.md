---
name: python-os
description: "Program with Python's os module: OS routines for NT or Posix depending on what system we're on."
version: 1.0.0
tags: [os, programming, python, stdlib]
---

# Python: `os`

## Overview

OS routines for NT or Posix depending on what system we're on.

This exports:
  - all functions from posix or nt, e.g. unlink, stat, etc.
  - os.path is either posixpath or ntpath
  - os.name is either 'posix' or 'nt'
  - os.curdir is a string representing the current directory (always '.')
  - os.pardir is a string representing the parent directory (always '..')
  - os.sep is the (or a most common) pathname separator ('/' or '\\')
  - os.extsep is the extension separator (always '.')
  - os.altsep is the alternate pathname separator (None or '/')
  - os.pathsep is the component separator used in $PATH etc
  - os.linesep is the line separator in text files ('\n' or '\r\n')
  - os.defpath is the default search path for executables
  - os.devnull is the file path of the null device ('/dev/null', etc.)

Programs that import and use 'os' stand a better chance of being
portable between different platforms.  Of course, they must then
only use functions that are defined by all platforms (e.g., unlink
and opendir), and leave all pathname manipulation to os.path
(e.g., split and join).

## When to use

Reach for `os` when your task calls for OS routines for NT or Posix depending on what system we're on. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import os
```

## Key functions

- `os.abort()`
- `os.access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True)`
- `os.add_dll_directory(path)`
- `os.chdir(path)`
- `os.chmod(...)`
- `os.close(fd)`
- `os.closerange(fd_low, fd_high, /)`
- `os.cpu_count()`
- `os.device_encoding(fd)`
- `os.dup(fd, /)`
- `os.dup2(fd, fd2, inheritable=True)`
- `os.execl(file, *args)`
- `os.execle(file, *args)`
- `os.execlp(file, *args)`
- `os.execlpe(file, *args)`
- `os.execv(path, argv, /)`
- `os.execve(path, argv, env)`
- `os.execvp(file, args)`
- `os.execvpe(file, args, env)`
- `os.fchmod(fd, mode)`
- `os.fdopen(fd, mode='r', buffering=-1, encoding=None, *args, **kwargs)`
- `os.fsdecode(filename)`
- `os.fsencode(filename)`
- `os.fspath(path)`
- `os.fstat(fd)`
- `os.fsync(fd)`
- `os.ftruncate(fd, length, /)`
- `os.get_blocking(fd, /)`
- `os.get_exec_path(env=None)`
- `os.get_handle_inheritable(handle, /)`

## Key classes

`DirEntry`, `GenericAlias`, `Mapping`, `MutableMapping`, `PathLike`, `error`, `stat_result`, `statvfs_result`, `terminal_size`, `times_result`, `uname_result`

## Constants / attributes

`EX_OK`, `F_OK`, `O_APPEND`, `O_BINARY`, `O_CREAT`, `O_EXCL`, `O_NOINHERIT`, `O_RANDOM`, `O_RDONLY`, `O_RDWR`, `O_SEQUENTIAL`, `O_SHORT_LIVED`, `O_TEMPORARY`, `O_TEXT`, `O_TRUNC`, `O_WRONLY`, `P_DETACH`, `P_NOWAIT`, `P_NOWAITO`, `P_OVERLAY`, `P_WAIT`, `R_OK`, `SEEK_CUR`, `SEEK_END`, `SEEK_SET`, `TMP_MAX`, `W_OK`, `X_OK`, `altsep`, `curdir`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import os

def do_work(...):
    """Use os to accomplish one well-defined task."""
    result = os.abort(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `os` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module os

NAME
    os - OS routines for NT or Posix depending on what system we're on.

MODULE REFERENCE
    https://docs.python.org/3.14/library/os.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This exports:
      - all functions from posix or nt, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix' or 'nt'
      - os.curdir is a string representing the current directory (always '.')
      - os.pardir is a string representing the parent directory (always '..')
      - os.sep is the (or a most common) pathname separator ('/' or '\\')
      - os.extsep is the extension separator (always '.')
      - os.altsep is the alternate pathname separator (None or '/')
      - os.pathsep is the component separator used in $PATH etc
      - os.linesep is the line separator in text files ('\n' or '\r\n')
      - os.defpath is the default search path for executables
      - os.devnull is the file path of the null device ('/dev/null', etc.)

    Programs that import and use 'os' stand a better chance of being
    portable between different platforms.  Of course, they must then
    only use functions that are defined by all platforms (e.g., unlink
    and opendir), and leave all pathname manipulation to os.path
    (e.g., split and join).

CLASSES
    builtins.Exception(builtins.BaseException)
        builtins.OSError
    builtins.object
        nt.DirEntry
    builtins.tuple(builtins.object)
        nt.times_result
        nt.uname_result
        stat_result
        statvfs_result
        terminal_size

    class DirEntry(builtins.object)
     |  Methods defined here:
     |
     |  __fspath__(self, /)
     |      Returns the path for the entry.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  inode(self, /)
     |      Return inode of the entry; cached per entry.
     |
     |  is_dir(self, /, *, follow_symlinks=True)
     |      Return True if the entry is a directory; cached per entry.
     |
     |  is_file(self, /, *, follow_symlinks=True)
     |      Return True if the entry is a file; cached per entry.
     |
     |  is_junction(self, /)
     |      Return True if the entry is a junction; cached per entry.
     |
     |  is_symlink(self, /)
     |      Return True if the entry is a symbolic link; cached per entry.
     |
     |  stat(self, /, *, follow_symlinks=True)
     |      Return stat_result object for the entry; cached per entry.
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  __class_getitem__(object, /)
     |      See PEP 585
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  name
     |      the entry's base filename, relative to scandir() "path" argument
     |
     |  path
     |      the entry's full path name; equivalent to os.path.join(scandir_path, entry.name)

    error = class OSError(Exception)
     |  Base class for I/O related errors.
     |
     |  Method resolution order:
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |
     |  Built-in subclasses:
     |      BlockingIOError
     |      ChildProcessError
     |      ConnectionError
     |      FileExistsError
     |      ... and 7 other subclasses
     |
     |  Methods defined here:
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
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs)
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
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
     |  Methods inherited from BaseException:
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
     |  Data descriptors inherited from BaseException:
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

    class stat_result(builtins.tuple)
     |  stat_result(iterable=(), /)
     |
     |  stat_result: Result from stat, fstat, or lstat.
     |
     |  This object may be accessed either as a tuple of
     |    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
     |  or via the attributes st_mode, st_ino, st_dev, st_nlink, st_uid, and so on.
     |
     |  Posix/windows: If your platform supports st_blksize, st_blocks, st_rdev,
     |  or st_flags, they are available as attributes only.
     |
     |  See os.stat for more information.
     |
     |  Method resolution order:
   
```

## Related

Other standard-library modules pair well with `os`; explore the `python` domain of this catalog.
