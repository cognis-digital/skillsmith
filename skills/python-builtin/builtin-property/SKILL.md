---
name: builtin-property
description: "Program with Python's built-in property: Property attribute."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `property`

    ## Overview

    `property` is a Python built-in class — always available, no import required.

    Property attribute.

  fget
    function to be used for getting an attribute value
  fset
    function to be used for setting an attribute value
  fdel
    function to be used for del'ing an attribute
  doc
    docstring

Typical use is to define a managed attribute x:

class C(object):
    def getx(self): return self._x
    def setx(self, value): self._x = value
    def delx(self): del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")

Decorators make defining new properties or modifying existing ones easy:

class C(object):
    @property
    def x(self):
        "I am the 'x' property."
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    @x.deleter
    def x(self):
        del self._x

    ## Signature

    ```python
    property(fget=None, fset=None, fdel=None, doc=None)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `property` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = property(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class property in module builtins

class property(object)
 |  property(fget=None, fset=None, fdel=None, doc=None)
 |
 |  Property attribute.
 |
 |    fget
 |      function to be used for getting an attribute value
 |    fset
 |      function to be used for setting an attribute value
 |    fdel
 |      function to be used for del'ing an attribute
 |    doc
 |      docstring
 |
 |  Typical use is to define a managed attribute x:
 |
 |  class C(object):
 |      def getx(self): return self._x
 |      def setx(self, value): self._x = value
 |      def delx(self): del self._x
 |      x = property(getx, setx, delx, "I'm the 'x' property.")
 |
 |  Decorators make defining new properties or modifying existing ones easy:
 |
 |  class C(object):
 |      @property
 |      def x(self):
 |          "I am the 'x' property."
 |          return self._x
 |      @x.setter
 |      def x(self, value):
 |          self._x = value
 |      @x.deleter
 |      def x(self):
 |          del self._x
 |
 |  Methods defined here:
 |
 |  __delete__(self, instance, /)
 |      Delete an attribute of instance.
 |
 |  __get__(self, instance, owner=None, /)
 |      Return an attribute of instance, which is of type owner.
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __set__(self, instance, value, /)
 |      Set an attribute of instance to value.
 |
 |  __set_name__(self, owner, name, /)
 |      Method to set name of a property.
 |
 |  deleter(self, object, /)
 |      Descriptor to obtain a copy of the property with a different deleter.
 |
 |  getter(self, object, /)
 |      Descriptor to obtain a copy of the property with a different getter.
 |
 |  setter(self, object, /)
 |      Descriptor to obtain a copy of the property with a different setter.
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
 |  __isabstractmethod__
 |
 |  fdel
 |
 |  fget
 |
 |  fset

    ```
