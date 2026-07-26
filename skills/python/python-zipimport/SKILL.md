---
name: python-zipimport
description: "Program with Python's zipimport module: zipimport provides support for importing Python modules from Zip archives."
version: 1.0.0
tags: [programming, python, stdlib, zipimport]
---

# Python: `zipimport`

## Overview

zipimport provides support for importing Python modules from Zip archives.

This module exports two objects:
- zipimporter: a class; its constructor takes a path to a Zip archive.
- ZipImportError: exception raised by zipimporter objects. It's a
  subclass of ImportError, so it can be caught as ImportError, too.

It is usually not needed to use the zipimport module explicitly; it is
used by the builtin import mechanism for sys.path items that are paths
to Zip archives.

## When to use

Reach for `zipimport` when your task calls for zipimport provides support for importing Python modules from Zip archives. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import zipimport
```

## Key classes

`ZipImportError`, `zipimporter`

## Constants / attributes

`END_CENTRAL_DIR_LOCATOR_SIZE_64`, `END_CENTRAL_DIR_SIZE`, `END_CENTRAL_DIR_SIZE_64`, `MAX_COMMENT_LEN`, `MAX_UINT32`, `STRING_END_ARCHIVE`, `STRING_END_LOCATOR_64`, `STRING_END_ZIP_64`, `ZIP64_EXTRA_TAG`, `alt_path_sep`, `cp437_table`, `path_sep`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import zipimport

def do_work(...):
    """Use zipimport to accomplish one well-defined task."""
    result = zipimport.ZipImportError(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `zipimport` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module zipimport

NAME
    zipimport - zipimport provides support for importing Python modules from Zip archives.

MODULE REFERENCE
    https://docs.python.org/3.14/library/zipimport.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module exports two objects:
    - zipimporter: a class; its constructor takes a path to a Zip archive.
    - ZipImportError: exception raised by zipimporter objects. It's a
      subclass of ImportError, so it can be caught as ImportError, too.

    It is usually not needed to use the zipimport module explicitly; it is
    used by the builtin import mechanism for sys.path items that are paths
    to Zip archives.

CLASSES
    _frozen_importlib_external._LoaderBasics(builtins.object)
        zipimporter
    builtins.ImportError(builtins.Exception)
        ZipImportError

    class ZipImportError(builtins.ImportError)
     |  Method resolution order:
     |      ZipImportError
     |      builtins.ImportError
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
     |  Methods inherited from builtins.ImportError:
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
     |  Data descriptors inherited from builtins.ImportError:
     |
     |  msg
     |      exception message
     |
     |  name
     |      module name
     |
     |  name_from
     |      name imported from module
     |
     |  path
     |      module path
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

    class zipimporter(_frozen_importlib_external._LoaderBasics)
     |  zipimporter(path)
     |
     |  zipimporter(archivepath) -> zipimporter object
     |
     |  Create a new zipimporter instance. 'archivepath' must be a path to
     |  a zipfile, or to a specific path inside a zipfile. For example, it can be
     |  '/tmp/myimport.zip', or '/tmp/myimport.zip/mydirectory', if mydirectory is a
     |  valid directory inside the archive.
     |
     |  'ZipImportError is raised if 'archivepath' doesn't point to a valid Zip
     |  archive.
     |
     |  The 'archive' attribute of zipimporter objects contains the name of the
     |  zipfile targeted.
     |
     |  Method resolution order:
     |      zipimporter
     |      _frozen_importlib_external._LoaderBasics
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, path)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  find_spec(self, fullname, target=None)
     |      Create a ModuleSpec for the specified module.
     |
     |      Returns None if the module cannot be found.
     |
     |  get_code(self, fullname)
     |      get_code(fullname) -> code object.
     |
     |      Return the code object for the specified module. Raise ZipImportError
     |      if the module couldn't be imported.
     |
     |  get_data(self, pathname)
     |      get_data(pathname) -> string with file data.
     |
     |      Return the data associated with 'pathname'. Raise OSError if
     |      the file wasn't found.
     |
     |  get_filename(self, fullname)
     |      get_filename(fullname) -> filename string.
     |
     |      Return the filename for the specified module or raise ZipImportError
     |      if it couldn't be imported.
     |
     |  get_resource_reader(self, fullname)
     |      Return the ResourceReader for a module in a zip file.
     |
     |  get_source(self, fullname)
     |      get_source(fullname) -> source string.
     |
     |      Return the source code for the specified module. Raise ZipImportError
     |      if the module couldn't be found, return None if the archive does
     |      contain the module, but has no source for it.
     |
     |  invalidate_caches(self)
     |      Invalidates the cache of file data of the archive path.
     |
     |  is_package(self, fullname)
     |      is_package(fullname) -> bool.
     |
     |      Return True if the module specified by fullname is a package.
     |      Raise ZipImportError if the module couldn't be found.
     |
     |  load_module(self, fullname)
     |      load_module(fullname) -> module.
     |

```

## Related

Other standard-library modules pair well with `zipimport`; explore the `python` domain of this catalog.
