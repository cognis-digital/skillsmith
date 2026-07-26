---
name: builtin-type
description: "Program with Python's built-in type: type(object) -> the object's type type(name, bases, dict, **kwds) -> a new type"
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `type`

    ## Overview

    `type` is a Python built-in class — always available, no import required.

    type(object) -> the object's type
type(name, bases, dict, **kwds) -> a new type

    ## Signature

    ```python
    type
    ```

    ## When to use

    Built-ins are the first tool to reach for: `type` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = type(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class type in module builtins

class type(object)
 |  type(object) -> the object's type
 |  type(name, bases, dict, **kwds) -> a new type
 |
 |  Methods defined here:
 |
 |  __call__(self, /, *args, **kwargs)
 |      Call self as a function.
 |
 |  __delattr__(self, name, /)
 |      Implement delattr(self, name).
 |
 |  __dir__(self, /)
 |      Specialized __dir__ implementation for types.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __instancecheck__(self, instance, /)
 |      Check if an object is an instance.
 |
 |  __or__(self, value, /)
 |      Return self|value.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __ror__(self, value, /)
 |      Return value|self.
 |
 |  __setattr__(self, name, value, /)
 |      Implement setattr(self, name, value).
 |
 |  __sizeof__(self, /)
 |      Return memory consumption of the type object.
 |
 |  __subclasscheck__(self, subclass, /)
 |      Check if a class is a subclass.
 |
 |  __subclasses__(self, /)
 |      Return a list of immediate subclasses.
 |
 |  mro(self, /)
 |      Return a type's method resolution order.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __prepare__(name, bases, /, **kwds)
 |      Create the namespace for the class statement
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
 |  __abstractmethods__
 |
 |  __annotate__
 |
 |  __annotations__
 |
 |  __dict__
 |
 |  __text_signature__
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __base__ = <class 'object'>
 |      The base class of the class hierarchy.
 |
 |      When called, it accepts no arguments and returns a new featureless
 |      instance that has no instance attributes and cannot be given any.
 |
 |
 |  __bases__ = (<class 'object'>,)
 |
 |  __basicsize__ = 936
 |
 |  __dictoffset__ = 264
 |
 |  __flags__ = 2155896066
 |
 |  __itemsize__ = 40
 |
 |  __mro__ = (<class 'type'>, <class 'object'>)
 |
 |  __type_params__ = ()
 |
 |  __weakrefoffset__ = 368

    ```
