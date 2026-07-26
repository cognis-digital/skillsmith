---
name: builtin-classmethod
description: "Program with Python's built-in classmethod: Convert a function to be a class method."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `classmethod`

    ## Overview

    `classmethod` is a Python built-in class — always available, no import required.

    Convert a function to be a class method.

A class method receives the class as implicit first argument,
just like an instance method receives the instance.
To declare a class method, use this idiom:

  class C:
      @classmethod
      def f(cls, arg1, arg2, argN):
          ...

It can be called either on the class (e.g. C.f()) or on an instance
(e.g. C().f()).  The instance is ignored except for its class.
If a class method is called for a derived class, the derived class
object is passed as the implied first argument.

Class methods are different than C++ or Java static methods.
If you want those, see the staticmethod builtin.

    ## Signature

    ```python
    classmethod(function, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `classmethod` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = classmethod(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class classmethod in module builtins

class classmethod(object)
 |  classmethod(function, /)
 |
 |  Convert a function to be a class method.
 |
 |  A class method receives the class as implicit first argument,
 |  just like an instance method receives the instance.
 |  To declare a class method, use this idiom:
 |
 |    class C:
 |        @classmethod
 |        def f(cls, arg1, arg2, argN):
 |            ...
 |
 |  It can be called either on the class (e.g. C.f()) or on an instance
 |  (e.g. C().f()).  The instance is ignored except for its class.
 |  If a class method is called for a derived class, the derived class
 |  object is passed as the implied first argument.
 |
 |  Class methods are different than C++ or Java static methods.
 |  If you want those, see the staticmethod builtin.
 |
 |  Methods defined here:
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
