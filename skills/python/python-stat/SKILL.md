---
name: python-stat
description: "Program with Python's stat module: Constants/functions for interpreting results of os.stat() and os.lstat()."
version: 1.0.0
tags: [programming, python, stat, stdlib]
---

# Python: `stat`

## Overview

Constants/functions for interpreting results of os.stat() and os.lstat().

Suggested usage: from stat import *

## When to use

Reach for `stat` when your task calls for Constants/functions for interpreting results of os.stat() and os.lstat(). It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import stat
```

## Key functions

- `stat.S_IFMT(object, /)`
- `stat.S_IMODE(object, /)`
- `stat.S_ISBLK(object, /)`
- `stat.S_ISCHR(object, /)`
- `stat.S_ISDIR(object, /)`
- `stat.S_ISDOOR(object, /)`
- `stat.S_ISFIFO(object, /)`
- `stat.S_ISLNK(object, /)`
- `stat.S_ISPORT(object, /)`
- `stat.S_ISREG(object, /)`
- `stat.S_ISSOCK(object, /)`
- `stat.S_ISWHT(object, /)`
- `stat.filemode(object, /)`

## Constants / attributes

`FILE_ATTRIBUTE_ARCHIVE`, `FILE_ATTRIBUTE_COMPRESSED`, `FILE_ATTRIBUTE_DEVICE`, `FILE_ATTRIBUTE_DIRECTORY`, `FILE_ATTRIBUTE_ENCRYPTED`, `FILE_ATTRIBUTE_HIDDEN`, `FILE_ATTRIBUTE_INTEGRITY_STREAM`, `FILE_ATTRIBUTE_NORMAL`, `FILE_ATTRIBUTE_NOT_CONTENT_INDEXED`, `FILE_ATTRIBUTE_NO_SCRUB_DATA`, `FILE_ATTRIBUTE_OFFLINE`, `FILE_ATTRIBUTE_READONLY`, `FILE_ATTRIBUTE_REPARSE_POINT`, `FILE_ATTRIBUTE_SPARSE_FILE`, `FILE_ATTRIBUTE_SYSTEM`, `FILE_ATTRIBUTE_TEMPORARY`, `FILE_ATTRIBUTE_VIRTUAL`, `IO_REPARSE_TAG_APPEXECLINK`, `IO_REPARSE_TAG_MOUNT_POINT`, `IO_REPARSE_TAG_SYMLINK`, `SF_APPEND`, `SF_ARCHIVED`, `SF_DATALESS`, `SF_FIRMLINK`, `SF_IMMUTABLE`, `SF_NOUNLINK`, `SF_RESTRICTED`, `SF_SETTABLE`, `SF_SNAPSHOT`, `ST_ATIME`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import stat

def do_work(...):
    """Use stat to accomplish one well-defined task."""
    result = stat.S_IFMT(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `stat` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module stat

NAME
    stat - Constants/functions for interpreting results of os.stat() and os.lstat().

MODULE REFERENCE
    https://docs.python.org/3.14/library/stat.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Suggested usage: from stat import *

DATA
    FILE_ATTRIBUTE_ARCHIVE = 32
    FILE_ATTRIBUTE_COMPRESSED = 2048
    FILE_ATTRIBUTE_DEVICE = 64
    FILE_ATTRIBUTE_DIRECTORY = 16
    FILE_ATTRIBUTE_ENCRYPTED = 16384
    FILE_ATTRIBUTE_HIDDEN = 2
    FILE_ATTRIBUTE_INTEGRITY_STREAM = 32768
    FILE_ATTRIBUTE_NORMAL = 128
    FILE_ATTRIBUTE_NOT_CONTENT_INDEXED = 8192
    FILE_ATTRIBUTE_NO_SCRUB_DATA = 131072
    FILE_ATTRIBUTE_OFFLINE = 4096
    FILE_ATTRIBUTE_READONLY = 1
    FILE_ATTRIBUTE_REPARSE_POINT = 1024
    FILE_ATTRIBUTE_SPARSE_FILE = 512
    FILE_ATTRIBUTE_SYSTEM = 4
    FILE_ATTRIBUTE_TEMPORARY = 256
    FILE_ATTRIBUTE_VIRTUAL = 65536
    IO_REPARSE_TAG_APPEXECLINK = 2147483675
    IO_REPARSE_TAG_MOUNT_POINT = 2684354563
    IO_REPARSE_TAG_SYMLINK = 2684354572
    SF_APPEND = 262144
    SF_ARCHIVED = 65536
    SF_DATALESS = 1073741824
    SF_FIRMLINK = 8388608
    SF_IMMUTABLE = 131072
    SF_NOUNLINK = 1048576
    SF_RESTRICTED = 524288
    SF_SETTABLE = -65536
    SF_SNAPSHOT = 2097152
    ST_ATIME = 7
    ST_CTIME = 9
    ST_DEV = 2
    ST_GID = 5
    ST_INO = 1
    ST_MODE = 0
    ST_MTIME = 8
    ST_NLINK = 3
    ST_SIZE = 6
    ST_UID = 4
    S_ENFMT = 1024
    S_IEXEC = 64
    S_IFBLK = 24576
    S_IFCHR = 8192
    S_IFDIR = 16384
    S_IFDOOR = 0
    S_IFIFO = 4096
    S_IFLNK = 40960
    S_IFPORT = 0
    S_IFREG = 32768
    S_IFSOCK = 49152
    S_IFWHT = 0
    S_IREAD = 256
    S_IRGRP = 32
    S_IROTH = 4
    S_IRUSR = 256
    S_IRWXG = 56
    S_IRWXO = 7
    S_IRWXU = 448
    S_ISGID = 1024
    S_ISUID = 2048
    S_ISVTX = 512
    S_IWGRP = 16
    S_IWOTH = 2
    S_IWRITE = 128
    S_IWUSR = 128
    S_IXGRP = 8
    S_IXOTH = 1
    S_IXUSR = 64
    UF_APPEND = 4
    UF_COMPRESSED = 32
    UF_DATAVAULT = 128
    UF_HIDDEN = 32768
    UF_IMMUTABLE = 2
    UF_NODUMP = 1
    UF_NOUNLINK = 16
    UF_OPAQUE = 8
    UF_SETTABLE = 65535
    UF_TRACKED = 64

FILE
    c:\python314\lib\stat.py


```

## Related

Other standard-library modules pair well with `stat`; explore the `python` domain of this catalog.
