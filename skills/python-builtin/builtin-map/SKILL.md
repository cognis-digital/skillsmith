---
name: builtin-map
description: "Program with Python's built-in map: Make an iterator that computes the function using arguments from each of the iterables."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `map`

    ## Overview

    `map` is a Python built-in class — always available, no import required.

    Make an iterator that computes the function using arguments from
each of the iterables.  Stops when the shortest iterable is exhausted.

If strict is true and one of the arguments is exhausted before the others,
raise a ValueError.

    ## Signature

    ```python
    map(function, iterable, /, *iterables, strict=False)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `map` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = map(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class map in module builtins

class map(object)
 |  map(function, iterable, /, *iterables, strict=False)
 |
 |  Make an iterator that computes the function using arguments from
 |  each of the iterables.  Stops when the shortest iterable is exhausted.
 |
 |  If strict is true and one of the arguments is exhausted before the others,
 |  raise a ValueError.
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
 |  __setstate__(self, object, /)
 |      Set state information for unpickling.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.

    ```
