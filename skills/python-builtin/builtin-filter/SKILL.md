---
name: builtin-filter
description: "Program with Python's built-in filter: Return an iterator yielding those items of iterable for which function(item) is true."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `filter`

    ## Overview

    `filter` is a Python built-in class — always available, no import required.

    Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.

    ## Signature

    ```python
    filter(function, iterable, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `filter` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = filter(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class filter in module builtins

class filter(object)
 |  filter(function, iterable, /)
 |
 |  Return an iterator yielding those items of iterable for which function(item)
 |  is true. If function is None, return the items that are true.
 |
 |  Methods defined here:
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __next__(self, /)
 |      Implement next(self).
 |
 |  __reduce__(self, /)
 |      Return state information for pickling.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.

    ```
