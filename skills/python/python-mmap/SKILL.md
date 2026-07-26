---
name: python-mmap
description: "Program with Python's mmap module: The Python standard-library module `mmap`."
version: 1.0.0
tags: [mmap, programming, python, stdlib]
---

# Python: `mmap`

## Overview

`mmap` is part of the Python standard library.

## When to use

Reach for `mmap` when your task calls for The Python standard-library module `mmap`. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import mmap
```

## Key classes

`error`, `mmap`

## Constants / attributes

`ACCESS_COPY`, `ACCESS_DEFAULT`, `ACCESS_READ`, `ACCESS_WRITE`, `ALLOCATIONGRANULARITY`, `PAGESIZE`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import mmap

def do_work(...):
    """Use mmap to accomplish one well-defined task."""
    result = mmap.error(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `mmap` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: built-in module mmap

NAME
    mmap

CLASSES
    builtins.object
        mmap

    class mmap(builtins.object)
     |  Windows: mmap(fileno, length[, tagname[, access[, offset]]])
     |
     |  Maps length bytes from the file specified by the file handle fileno,
     |  and returns a mmap object.  If length is larger than the current size
     |  of the file, the file is extended to contain length bytes.  If length
     |  is 0, the maximum length of the map is the current size of the file,
     |  except that if the file is empty Windows raises an exception (you cannot
     |  create an empty mapping on Windows).
     |
     |  Unix: mmap(fileno, length[, flags[, prot[, access[, offset[, trackfd]]]]])
     |
     |  Maps length bytes from the file specified by the file descriptor fileno,
     |  and returns a mmap object.  If length is 0, the maximum length of the map
     |  will be the current size of the file when mmap is called.
     |  flags specifies the nature of the mapping. MAP_PRIVATE creates a
     |  private copy-on-write mapping, so changes to the contents of the mmap
     |  object will be private to this process, and MAP_SHARED creates a mapping
     |  that's shared with all other processes mapping the same areas of the file.
     |  The default value is MAP_SHARED.
     |
     |  To map anonymous memory, pass -1 as the fileno (both versions).
     |
     |  Methods defined here:
     |
     |  __buffer__(self, flags, /)
     |      Return a buffer object that exposes the underlying memory of the object.
     |
     |  __delitem__(self, key, /)
     |      Delete self[key].
     |
     |  __enter__(self, /)
     |
     |  __exit__(...)
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __getitem__(self, key, /)
     |      Return self[key].
     |
     |  __len__(self, /)
     |      Return len(self).
     |
     |  __release_buffer__(self, buffer, /)
     |      Release the buffer object that exposes the underlying memory of the object.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setitem__(self, key, value, /)
     |      Set self[key] to value.
     |
     |  __sizeof__(self, /)
     |      Size of object in memory, in bytes.
     |
     |  close(self, /)
     |
     |  find(...)
     |
     |  flush(...)
     |
     |  move(...)
     |
     |  read(...)
     |
     |  read_byte(self, /)
     |
     |  readline(self, /)
     |
     |  resize(...)
     |
     |  rfind(...)
     |
     |  seek(...)
     |
     |  seekable(self, /)
     |
     |  size(self, /)
     |
     |  tell(self, /)
     |
     |  write(...)
     |
     |  write_byte(...)
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
     |  closed

DATA
    ACCESS_COPY = 3
    ACCESS_DEFAULT = 0
    ACCESS_READ = 1
    ACCESS_WRITE = 2
    ALLOCATIONGRANULARITY = 65536
    PAGESIZE = 4096

FILE
    (built-in)


```

## Related

Other standard-library modules pair well with `mmap`; explore the `python` domain of this catalog.
