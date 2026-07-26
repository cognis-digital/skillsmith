---
name: builtin-frozenset
description: "Program with Python's built-in frozenset: Build an immutable unordered collection of unique elements."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `frozenset`

    ## Overview

    `frozenset` is a Python built-in class — always available, no import required.

    Build an immutable unordered collection of unique elements.

    ## Signature

    ```python
    frozenset(iterable=(), /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `frozenset` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = frozenset(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class frozenset in module builtins

class frozenset(object)
 |  frozenset(iterable=(), /)
 |
 |  Build an immutable unordered collection of unique elements.
 |
 |  Methods defined here:
 |
 |  __and__(self, value, /)
 |      Return self&value.
 |
 |  __contains__(self, object, /)
 |      x.__contains__(y) <==> y in x.
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __len__(self, /)
 |      Return len(self).
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __or__(self, value, /)
 |      Return self|value.
 |
 |  __rand__(self, value, /)
 |      Return value&self.
 |
 |  __reduce__(self, /)
 |      Return state information for pickling.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __ror__(self, value, /)
 |      Return value|self.
 |
 |  __rsub__(self, value, /)
 |      Return value-self.
 |
 |  __rxor__(self, value, /)
 |      Return value^self.
 |
 |  __sizeof__(self, /)
 |      S.__sizeof__() -> size of S in memory, in bytes.
 |
 |  __sub__(self, value, /)
 |      Return self-value.
 |
 |  __xor__(self, value, /)
 |      Return self^value.
 |
 |  copy(self, /)
 |      Return a shallow copy of a set.
 |
 |  difference(self, /, *others)
 |      Return a new set with elements in the set that are not in the others.
 |
 |  intersection(self, /, *others)
 |      Return a new set with elements common to the set and all others.
 |
 |  isdisjoint(self, other, /)
 |      Return True if two sets have a null intersection.
 |
 |  issubset(self, other, /)
 |      Report whether another set contains this set.
 |
 |  issuperset(self, other, /)
 |      Report whether this set contains another set.
 |
 |  symmetric_difference(self, other, /)
 |      Return a new set with elements in either the set or other but not both.
 |
 |  union(self, /, *others)
 |      Return a new set with elements from the set and all others.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __class_getitem__(object, /)
 |      See PEP 585
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.

    ```
