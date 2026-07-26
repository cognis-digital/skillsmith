---
name: builtin-slice
description: "Program with Python's built-in slice: slice(stop) slice(start, stop[, step]) Create a slice object."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `slice`

    ## Overview

    `slice` is a Python built-in class — always available, no import required.

    slice(stop)
slice(start, stop[, step])

Create a slice object.  This is used for extended slicing (e.g. a[0:10:2]).

    ## Signature

    ```python
    slice
    ```

    ## When to use

    Built-ins are the first tool to reach for: `slice` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = slice(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class slice in module builtins

class slice(object)
 |  slice(stop)
 |  slice(start, stop[, step])
 |
 |  Create a slice object.  This is used for extended slicing (e.g. a[0:10:2]).
 |
 |  Methods defined here:
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
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __reduce__(self, /)
 |      Return state information for pickling.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  indices(self, object, /)
 |      S.indices(len) -> (start, stop, stride)
 |
 |      Assuming a sequence of length len, calculate the start and stop
 |      indices, and the stride length of the extended slice described by
 |      S. Out of bounds indices are clipped in a manner consistent with the
 |      handling of normal slices.
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
 |  start
 |
 |  step
 |
 |  stop

    ```
