---
name: builtin-reversed
description: "Program with Python's built-in reversed: Return a reverse iterator over the values of the given sequence."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `reversed`

    ## Overview

    `reversed` is a Python built-in class — always available, no import required.

    Return a reverse iterator over the values of the given sequence.

    ## Signature

    ```python
    reversed(sequence, /)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `reversed` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = reversed(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class reversed in module builtins

class reversed(object)
 |  reversed(sequence, /)
 |
 |  Return a reverse iterator over the values of the given sequence.
 |
 |  Methods defined here:
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __length_hint__(self, /)
 |      Private method returning an estimate of len(list(it)).
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
