---
name: python-pyclbr
description: "Program with Python's pyclbr module: Parse a Python module and describe its classes and functions."
version: 1.0.0
tags: [programming, pyclbr, python, stdlib]
---

# Python: `pyclbr`

## Overview

Parse a Python module and describe its classes and functions.

Parse enough of a Python file to recognize imports and class and
function definitions, and to find out the superclasses of a class.

The interface consists of a single function:
    readmodule_ex(module, path=None)
where module is the name of a Python module, and path is an optional
list of directories where the module is to be searched.  If present,
path is prepended to the system search path sys.path.  The return value
is a dictionary.  The keys of the dictionary are the names of the
classes and functions defined in the module (including classes that are
defined via the from XXX import YYY construct).  The values are
instances of classes Class and Function.  One special key/value pair is
present for packages: the key '__path__' has a list as its value which
contains the package search path.

Classes and Functions have a common superclass: _Object.  Every instance
has the following attributes:
    module  -- name of the module;
    name    -- name of the object;
    file    -- file in which the object is defined;
    lineno  -- line in the file where the object's definition starts;
    end_lineno -- line in the file where the object's definition ends;
    parent  -- parent of this object, if any;
    children -- nested objects contained in this object.
The 'children' attribute is a dictionary mapping names to objects.

Instances of Function describe functions with the attributes from _Object,
plus the following:
    is_async -- if a function is defined with an 'async' prefix

Instances of Class describe classes with the attributes from _Object,
plus the following:
    super   -- list of super classes (Class instances if possible);
    methods -- mapping of method names to beginning line numbers.
If the name of a super class is not recognized, the corresponding
entry in the list of super classes is not a class instance but a
string giving the name of the super class.  Since import statements
are recognized and imported modules are scanned as well, this
shouldn't happen often.

## When to use

Reach for `pyclbr` when your task calls for Parse a Python module and describe its classes and functions. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import pyclbr
```

## Key functions

- `pyclbr.readmodule(module, path=None)`
- `pyclbr.readmodule_ex(module, path=None)`

## Key classes

`Class`, `Function`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import pyclbr

def do_work(...):
    """Use pyclbr to accomplish one well-defined task."""
    result = pyclbr.readmodule(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `pyclbr` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module pyclbr

NAME
    pyclbr - Parse a Python module and describe its classes and functions.

MODULE REFERENCE
    https://docs.python.org/3.14/library/pyclbr.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Parse enough of a Python file to recognize imports and class and
    function definitions, and to find out the superclasses of a class.

    The interface consists of a single function:
        readmodule_ex(module, path=None)
    where module is the name of a Python module, and path is an optional
    list of directories where the module is to be searched.  If present,
    path is prepended to the system search path sys.path.  The return value
    is a dictionary.  The keys of the dictionary are the names of the
    classes and functions defined in the module (including classes that are
    defined via the from XXX import YYY construct).  The values are
    instances of classes Class and Function.  One special key/value pair is
    present for packages: the key '__path__' has a list as its value which
    contains the package search path.

    Classes and Functions have a common superclass: _Object.  Every instance
    has the following attributes:
        module  -- name of the module;
        name    -- name of the object;
        file    -- file in which the object is defined;
        lineno  -- line in the file where the object's definition starts;
        end_lineno -- line in the file where the object's definition ends;
        parent  -- parent of this object, if any;
        children -- nested objects contained in this object.
    The 'children' attribute is a dictionary mapping names to objects.

    Instances of Function describe functions with the attributes from _Object,
    plus the following:
        is_async -- if a function is defined with an 'async' prefix

    Instances of Class describe classes with the attributes from _Object,
    plus the following:
        super   -- list of super classes (Class instances if possible);
        methods -- mapping of method names to beginning line numbers.
    If the name of a super class is not recognized, the corresponding
    entry in the list of super classes is not a class instance but a
    string giving the name of the super class.  Since import statements
    are recognized and imported modules are scanned as well, this
    shouldn't happen often.

CLASSES
    _Object(builtins.object)
        Class
        Function

    class Class(_Object)
     |  Class(module, name, super_, file, lineno, parent=None, *, end_lineno=None)
     |
     |  Information about a Python class.
     |
     |  Method resolution order:
     |      Class
     |      _Object
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(
     |      self,
     |      module,
     |      name,
     |      super_,
     |      file,
     |      lineno,
     |      parent=None,
     |      *,
     |      end_lineno=None
     |  )
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _Object:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class Function(_Object)
     |  Function(
     |      module,
     |      name,
     |      file,
     |      lineno,
     |      parent=None,
     |      is_async=False,
     |      *,
     |      end_lineno=None
     |  )
     |
     |  Information about a Python function, including methods.
     |
     |  Method resolution order:
     |      Function
     |      _Object
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(
     |      self,
     |      module,
     |      name,
     |      file,
     |      lineno,
     |      parent=None,
     |      is_async=False,
     |      *,
     |      end_lineno=None
     |  )
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _Object:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

FUNCTIONS
    readmodule(module, path=None)
        Return Class objects for the top-level classes in module.

        This is the original interface, before Functions were added.

    readmodule_ex(module, path=None)
        Return a dictionary with all functions and classes in module.

        Search for module in PATH + sys.path.
        If possible, include imported superclasses.
        Do this by reading source, without importing (and executing) it.

DATA
    __all__ = ['readmodule', 'readmodule_ex', 'Class', 'Function']

FILE
    c:\python314\lib\pyclbr.py


```

## Related

Other standard-library modules pair well with `pyclbr`; explore the `python` domain of this catalog.
