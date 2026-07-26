---
name: py-property-descriptors
description: "Expose computed or validated attributes with @property instead of getter/setter methods."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Properties and computed attributes

    ## Overview

    `@property` turns a method into an attribute access, letting you compute or validate on get/set while keeping a clean attribute interface.

    ## When to use

    Expose computed or validated attributes with @property instead of getter/setter methods.

    ## Worked examples

    **Computed**

```python
class Circle:
    def __init__(self, r): self.r = r
    @property
    def area(self):
        return 3.14159 * self.r ** 2
```

**Validated setter**

```python
class Temp:
    def __init__(self): self._c = 0
    @property
    def c(self): return self._c
    @c.setter
    def c(self, v):
        if v < -273.15: raise ValueError('too cold')
        self._c = v
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Don't hide expensive work behind a property that looks like a cheap attribute.
- Back a settable property with a private attribute (self._x) to avoid infinite recursion.

    ## Related

    `dataclasses`, `class-methods`
