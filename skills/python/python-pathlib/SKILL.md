---
name: python-pathlib
description: "Program with Python's pathlib module: Object-oriented filesystem paths."
version: 1.0.0
tags: [pathlib, programming, python, stdlib]
---

# Python: `pathlib`

## Overview

Object-oriented filesystem paths.

This module provides classes to represent abstract paths and concrete
paths with operations that have semantics appropriate for different
operating systems.

## When to use

Reach for `pathlib` when your task calls for Object-oriented filesystem paths. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import pathlib
```

## Key functions

- `pathlib.S_ISBLK(object, /)`
- `pathlib.S_ISCHR(object, /)`
- `pathlib.S_ISDIR(object, /)`
- `pathlib.S_ISFIFO(object, /)`
- `pathlib.S_ISREG(object, /)`
- `pathlib.S_ISSOCK(object, /)`
- `pathlib.copy_info(info, target, follow_symlinks=True)`
- `pathlib.copyfile2(source, target)`
- `pathlib.copyfileobj(source_f, target_f)`
- `pathlib.ensure_different_files(source, target)`
- `pathlib.ensure_distinct_paths(source, target)`
- `pathlib.magic_open(path, mode='r', buffering=-1, encoding=None, errors=None, newline=None)`

## Key classes

`DirEntryInfo`, `Path`, `PathInfo`, `PosixPath`, `PurePath`, `PurePosixPath`, `PureWindowsPath`, `Sequence`, `UnsupportedOperation`, `WindowsPath`, `chain`

## Constants / attributes

`E2BIG`, `EACCES`, `EADDRINUSE`, `EADDRNOTAVAIL`, `EAFNOSUPPORT`, `EAGAIN`, `EALREADY`, `EBADF`, `EBADMSG`, `EBUSY`, `ECANCELED`, `ECHILD`, `ECONNABORTED`, `ECONNREFUSED`, `ECONNRESET`, `EDEADLK`, `EDEADLOCK`, `EDESTADDRREQ`, `EDOM`, `EDQUOT`, `EEXIST`, `EFAULT`, `EFBIG`, `EHOSTDOWN`, `EHOSTUNREACH`, `EIDRM`, `EILSEQ`, `EINPROGRESS`, `EINTR`, `EINVAL`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import pathlib

def do_work(...):
    """Use pathlib to accomplish one well-defined task."""
    result = pathlib.S_ISBLK(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `pathlib` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: package pathlib

NAME
    pathlib - Object-oriented filesystem paths.

MODULE REFERENCE
    https://docs.python.org/3.14/library/pathlib.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides classes to represent abstract paths and concrete
    paths with operations that have semantics appropriate for different
    operating systems.

PACKAGE CONTENTS
    _os
    types

CLASSES
    builtins.NotImplementedError(builtins.RuntimeError)
        UnsupportedOperation
    builtins.object
        PurePath
            Path
                PosixPath(Path, PurePosixPath)
                WindowsPath(Path, PureWindowsPath)
            PurePosixPath
            PureWindowsPath

    class Path(PurePath)
     |  Path(*args, **kwargs)
     |
     |  PurePath subclass that can make system calls.
     |
     |  Path represents a filesystem path but unlike PurePath, also offers
     |  methods to do system calls on path objects. Depending on your system,
     |  instantiating a Path will return either a PosixPath or a WindowsPath
     |  object. You can also instantiate a PosixPath or WindowsPath directly,
     |  but cannot instantiate a WindowsPath on a POSIX system or vice versa.
     |
     |  Method resolution order:
     |      Path
     |      PurePath
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  absolute(self)
     |      Return an absolute version of this path
     |      No normalization or symlink resolution is performed.
     |
     |      Use resolve() to resolve symlinks and remove '..' segments.
     |
     |  as_uri(self)
     |      Return the path as a URI.
     |
     |  chmod(self, mode, *, follow_symlinks=True)
     |      Change the permissions of the path, like os.chmod().
     |
     |  copy(self, target, **kwargs)
     |      Recursively copy this file or directory tree to the given destination.
     |
     |  copy_into(self, target_dir, **kwargs)
     |      Copy this file or directory tree into the given existing directory.
     |
     |  exists(self, *, follow_symlinks=True)
     |      Whether this path exists.
     |
     |      This method normally follows symlinks; to check whether a symlink exists,
     |      add the argument follow_symlinks=False.
     |
     |  expanduser(self)
     |      Return a new path with expanded ~ and ~user constructs
     |      (as returned by os.path.expanduser)
     |
     |  glob(self, pattern, *, case_sensitive=None, recurse_symlinks=False)
     |      Iterate over this subtree and yield all existing files (of any
     |      kind, including directories) matching the given relative pattern.
     |
     |  group(self, *, follow_symlinks=True)
     |      Return the group name of the file gid.
     |
     |  hardlink_to(self, target)
     |      Make this path a hard link pointing to the same file as *target*.
     |
     |      Note the order of arguments (self, target) is the reverse of os.link's.
     |
     |  is_block_device(self)
     |      Whether this path is a block device.
     |
     |  is_char_device(self)
     |      Whether this path is a character device.
     |
     |  is_dir(self, *, follow_symlinks=True)
     |      Whether this path is a directory.
     |
     |  is_fifo(self)
     |      Whether this path is a FIFO.
     |
     |  is_file(self, *, follow_symlinks=True)
     |      Whether this path is a regular file (also True for symlinks pointing
     |      to regular files).
     |
     |  is_junction(self)
     |      Whether this path is a junction.
     |
     |  is_mount(self)
     |      Check if this path is a mount point
     |
     |  is_socket(self)
     |      Whether this path is a socket.
     |
     |  is_symlink(self)
     |      Whether this path is a symbolic link.
     |
     |  iterdir(self)
     |      Yield path objects of the directory contents.
     |
     |      The children are yielded in arbitrary order, and the
     |      special entries '.' and '..' are not included.
     |
     |  lchmod(self, mode)
     |      Like chmod(), except if the path points to a symlink, the symlink's
     |      permissions are changed, rather than its target's.
     |
     |  lstat(self)
     |      Like stat(), except if the path points to a symlink, the symlink's
     |      status information is returned, rather than its target's.
     |
     |  mkdir(self, mode=511, parents=False, exist_ok=False)
     |      Create a new directory at this given path.
     |
     |  move(self, target)
     |      Recursively move this file or directory tree to the given destination.
     |
     |  move_into(self, target_dir)
     |      Move this file or directory tree into the given existing directory.
     |
     |  open(self, mode='r', buffering=-1, encoding=None, errors=None, newline=None)
     |      Open the file pointed to by this path and return a file object, as
     |      the built-in open() function does.
     |
     |  owner(self, *, follow_symlinks=True)
     |      Return the login name of the file owner.
     |
     |  read_bytes(self)
     |      Open the file in bytes mode, read it, and close the file.
     |
     |  read_text(self, encoding=None, errors=None, newline=None)
     |      Open the file in text mode, read it, and close the file.
     |
     |  readlink(self)
     |      Return the path to which the symbolic link points.
     |
     |  rename(self, target)
     |      Rename this path to the target path.
     |
     |      The target path may be absolute or relative. Relative paths are
     |      interpreted relative to the current working directory, *not* the
     |      directory of the Path object.
     |
     |      Returns
```

## Related

Other standard-library modules pair well with `pathlib`; explore the `python` domain of this catalog.
