---
name: builtin-staticmethod
description: "Program with Python's built-in staticmethod: Convert a function to be a static method."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `staticmethod`

    ## Overview

    `staticmethod` is a Python built-in class — always available, no import required.

    Convert a function to be a static method.

A static method does not receive an implicit first argument.
To declare a static method, use this idiom:

     class C:
         @staticmethod
         def f(arg1, arg2, argN):
             ...

It can be called either on the class (e.g. C.f()) or on an instance
(e.g. C().f()). Both the class and the instance are ignored, and
neither is passed implicitly as the first argument to the method.

Static methods in Python are similar to those found in Java or C++.
For a more advanced concept, see the classmethod builtin.

    ## Signature

    ```python
    staticmethod(function, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `staticmethod` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = staticmethod(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class staticmethod in module builtins

class staticmethod(object)
 |  staticmethod(function, /)
 |
 |  Convert a function to be a static method.
 |
 |  A static method does not receive an implicit first argument.
 |  To declare a static method, use this idiom:
 |
 |       class C:
 |           @staticmethod
 |           def f(arg1, arg2, argN):
 |               ...
 |
 |  It can be called either on the class (e.g. C.f()) or on an instance
 |  (e.g. C().f()). Both the class and the instance are ignored, and
 |  neither is passed implicitly as the first argument to the method.
 |
 |  Static methods in Python are similar to those found in Java or C++.
 |  For a more advanced concept, see the classmethod builtin.
 |
 |  Methods defined here:
 |
 |  __call__(self, /, *args, **kwargs)
 |      Call self as a function.
 |
 |  __get__(self, instance, owner=None, /)
 |      Return an attribute of instance, which is of type owner.
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __class_getitem__(object, /)
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
 |  __annotate__
 |
 |  __annotations__
 |
 |  __dict__
 |
 |  __func__
 |
 |  __isabstractmethod__
 |
 |  __wrapped__

    ```
