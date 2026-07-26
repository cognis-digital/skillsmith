---
name: python-nt
description: "Program with Python's nt module: This module provides access to operating system functionality that is standardized by the C Standard and the POSIX standard (a thinly disguised Unix interface)."
version: 1.0.0
tags: [nt, programming, python, stdlib]
---

# Python: `nt`

## Overview

This module provides access to operating system functionality that is
standardized by the C Standard and the POSIX standard (a thinly
disguised Unix interface).  Refer to the library manual and
corresponding Unix manual entries for more information on calls.

## When to use

Reach for `nt` when your task calls for This module provides access to operating system functionality that is standardized by the C Standard and the POSIX stand. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import nt
```

## Key functions

- `nt.abort()`
- `nt.access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True)`
- `nt.chdir(path)`
- `nt.chmod(...)`
- `nt.close(fd)`
- `nt.closerange(fd_low, fd_high, /)`
- `nt.cpu_count()`
- `nt.device_encoding(fd)`
- `nt.dup(fd, /)`
- `nt.dup2(fd, fd2, inheritable=True)`
- `nt.execv(path, argv, /)`
- `nt.execve(path, argv, env)`
- `nt.fchmod(fd, mode)`
- `nt.fspath(path)`
- `nt.fstat(fd)`
- `nt.fsync(fd)`
- `nt.ftruncate(fd, length, /)`
- `nt.get_blocking(fd, /)`
- `nt.get_handle_inheritable(handle, /)`
- `nt.get_inheritable(fd, /)`
- `nt.get_terminal_size(...)`
- `nt.getcwd()`
- `nt.getcwdb()`
- `nt.getlogin()`
- `nt.getpid()`
- `nt.getppid()`
- `nt.isatty(fd, /)`
- `nt.kill(pid, signal, /)`
- `nt.lchmod(path, mode)`
- `nt.link(...)`

## Key classes

`DirEntry`, `error`, `stat_result`, `statvfs_result`, `terminal_size`, `times_result`, `uname_result`

## Constants / attributes

`EX_OK`, `F_OK`, `O_APPEND`, `O_BINARY`, `O_CREAT`, `O_EXCL`, `O_NOINHERIT`, `O_RANDOM`, `O_RDONLY`, `O_RDWR`, `O_SEQUENTIAL`, `O_SHORT_LIVED`, `O_TEMPORARY`, `O_TEXT`, `O_TRUNC`, `O_WRONLY`, `P_DETACH`, `P_NOWAIT`, `P_NOWAITO`, `P_OVERLAY`, `P_WAIT`, `R_OK`, `TMP_MAX`, `W_OK`, `X_OK`, `environ`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import nt

def do_work(...):
    """Use nt to accomplish one well-defined task."""
    result = nt.abort(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `nt` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: built-in module nt

NAME
    nt

DESCRIPTION
    This module provides access to operating system functionality that is
    standardized by the C Standard and the POSIX standard (a thinly
    disguised Unix interface).  Refer to the library manual and
    corresponding Unix manual entries for more information on calls.

CLASSES
    builtins.object
        DirEntry
    builtins.tuple(builtins.object)
        times_result
        uname_result

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

    class times_result(builtins.tuple)
     |  times_result(iterable=(), /)
     |
     |  times_result: Result from os.times().
     |
     |  This object may be accessed either as a tuple of
     |    (user, system, children_user, children_system, elapsed),
     |  or via the attributes user, system, children_user, children_system,
     |  and elapsed.
     |
     |  See os.times for more information.
     |
     |  Method resolution order:
     |      times_result
     |      builtins.tuple
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __reduce__(self, /)
     |      Helper for pickle.
     |
     |  __replace__(self, /, **changes)
     |      Return a copy of the structure with new values for the specified fields.
     |
     |  __repr__(self, /)
     |      Return repr(self).
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
     |  children_system
     |      system time of children
     |
     |  children_user
     |      user time of children
     |
     |  elapsed
     |      elapsed time since an arbitrary point in the past
     |
     |  system
     |      system time
     |
     |  user
     |      user time
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __match_args__ = ('user', 'system', 'children_user', 'children_system'...
     |
     |  n_fields = 5
     |
     |  n_sequence_fields = 5
     |
     |  n_unnamed_fields = 0
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
     |  __getnewargs__(self, /)
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

    class uname_result(builtins.tuple)
     |  uname_result(iterable=(), /)
     |
     |  uname_result: Result from os.uname().
     |
     |  This object may be accessed either as a tuple of
     |    (sysname, nodename, release, version, machine),
     |  or via the attributes sysname, nodename, release, version, and machine.
     |
     |  See os.uname for more information.
     |
     |  Method resolution order:
     |      uname_result
     |      builtins.tuple
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __reduce__(self, /)
     |      Helper for pickle.
     |
     |  __replace__(self, /, **changes)
     |      Retu
```

## Related

Other standard-library modules pair well with `nt`; explore the `python` domain of this catalog.
