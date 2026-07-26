---
name: py-class-methods
description: "Use @classmethod for alternative constructors and @staticmethod for namespaced helpers."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: classmethod and staticmethod

    ## Overview

    `@classmethod` receives the class (great for factory constructors); `@staticmethod` receives nothing (a plain function living in the class namespace).

    ## When to use

    Use @classmethod for alternative constructors and @staticmethod for namespaced helpers.

    ## Worked examples

    **Alternative constructor**

```python
class Date:
    def __init__(self, y, m, d): self.y, self.m, self.d = y, m, d
    @classmethod
    def from_iso(cls, s):
        return cls(*map(int, s.split('-')))
```

**Static helper**

```python
class MathUtil:
    @staticmethod
    def clamp(x, lo, hi):
        return max(lo, min(hi, x))
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Use classmethod (cls) for factories so subclasses build the right type.
- If a method uses neither self nor cls, make it a staticmethod (or a module function).

    ## Related

    `property-descriptors`, `dataclasses`
