---
name: builtin-super
description: "Program with Python's built-in super: super() -> same as super(__class__, <first argument>) super(type) -> unbound super object super(type, obj) -> bound super object; requires isinstance(obj, type) super(type, type2) -> bound super object; requires issubclass(type2, type) Typical use to call a cooperative superclass method: class C(B): def meth(self, arg): super().meth(arg) This works for class methods too: class C(B): @classmethod def cmeth(cls, arg): super().cmeth(arg)"
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `super`

    ## Overview

    `super` is a Python built-in class — always available, no import required.

    super() -> same as super(__class__, <first argument>)
super(type) -> unbound super object
super(type, obj) -> bound super object; requires isinstance(obj, type)
super(type, type2) -> bound super object; requires issubclass(type2, type)
Typical use to call a cooperative superclass method:
class C(B):
    def meth(self, arg):
        super().meth(arg)
This works for class methods too:
class C(B):
    @classmethod
    def cmeth(cls, arg):
        super().cmeth(arg)

    ## Signature

    ```python
    super
    ```

    ## When to use

    Built-ins are the first tool to reach for: `super` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = super(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class super in module builtins

class super(object)
 |  super() -> same as super(__class__, <first argument>)
 |  super(type) -> unbound super object
 |  super(type, obj) -> bound super object; requires isinstance(obj, type)
 |  super(type, type2) -> bound super object; requires issubclass(type2, type)
 |  Typical use to call a cooperative superclass method:
 |  class C(B):
 |      def meth(self, arg):
 |          super().meth(arg)
 |  This works for class methods too:
 |  class C(B):
 |      @classmethod
 |      def cmeth(cls, arg):
 |          super().cmeth(arg)
 |
 |  Methods defined here:
 |
 |  __get__(self, instance, owner=None, /)
 |      Return an attribute of instance, which is of type owner.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
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
 |  __self__
 |      the instance invoking super(); may be None
 |
 |  __self_class__
 |      the type of the instance invoking super(); may be None
 |
 |  __thisclass__
 |      the class invoking super()

    ```
