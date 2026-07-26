---
name: builtin-set
description: "Program with Python's built-in set: Build an unordered collection of unique elements."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `set`

    ## Overview

    `set` is a Python built-in class — always available, no import required.

    Build an unordered collection of unique elements.

    ## Signature

    ```python
    set(iterable=(), /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `set` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = set(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class set in module builtins

class set(object)
 |  set(iterable=(), /)
 |
 |  Build an unordered collection of unique elements.
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
 |  __iand__(self, value, /)
 |      Return self&=value.
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __ior__(self, value, /)
 |      Return self|=value.
 |
 |  __isub__(self, value, /)
 |      Return self-=value.
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __ixor__(self, value, /)
 |      Return self^=value.
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
 |  add(self, object, /)
 |      Add an element to a set.
 |
 |      This has no effect if the element is already present.
 |
 |  clear(self, /)
 |      Remove all elements from this set.
 |
 |  copy(self, /)
 |      Return a shallow copy of a set.
 |
 |  difference(self, /, *others)
 |      Return a new set with elements in the set that are not in the others.
 |
 |  difference_update(self, /, *others)
 |      Update the set, removing elements found in others.
 |
 |  discard(self, object, /)
 |      Remove an element from a set if it is a member.
 |
 |      Unlike set.remove(), the discard() method does not raise
 |      an exception when an element is missing from the set.
 |
 |  intersection(self, /, *others)
 |      Return a new set with elements common to the set and all others.
 |
 |  intersection_update(self, /, *others)
 |      Update the set, keeping only elements found in it and all others.
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
 |  pop(self, /)
 |      Remove and return an arbitrary set element.
 |
 |      Raises KeyError if the set is empty.
 |
 |  remove(self, object, /)
 |      Remove an element from a set; it must be a member.
 |
 |      If the element is not a member, raise a KeyError.
 |
 |  symmetric_difference(self, other, /)
 |      Return a new set with elements in either the set or other but not both.
 |
 |  symmetric_difference_update(self, other, /)
 |      Update the set, keeping only elements found in either set, but not in both.
 |
 |  union(self, /, *others)
 |      Return a new set with elements from the set and all others.
 |
 |  update(self, /, *others)
 |      Update the set, adding elements from all others.
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
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __hash__ = None

    ```
