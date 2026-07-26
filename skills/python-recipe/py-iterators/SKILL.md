---
name: py-iterators
description: "Make your own objects iterable by implementing __iter__/__next__, and consume iterators lazily."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: The iterator protocol

    ## Overview

    An iterable returns an iterator from `__iter__`; an iterator produces values via `__next__` and raises StopIteration when done. Understanding it demystifies for-loops and generators.

    ## When to use

    Make your own objects iterable by implementing __iter__/__next__, and consume iterators lazily.

    ## Worked examples

    **Custom iterator**

```python
class Count:
    def __init__(self, stop):
        self.i, self.stop = 0, stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.i >= self.stop:
            raise StopIteration
        self.i += 1
        return self.i - 1
```

**Consume**

```python
it = iter([1, 2, 3])
next(it)          # 1
next(it, None)    # default avoids StopIteration
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Prefer a generator function over a hand-written iterator class when you can.
- next(it, default) is the safe way to pull one value without catching StopIteration.

    ## Related

    `generators`, `python-itertools`
