---
name: py-decorators
description: "Wrap functions to add behavior (timing, caching, retries, auth) without touching their bodies."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Decorators

    ## Overview

    A decorator is a callable that takes a function and returns a replacement. Use `functools.wraps` to preserve the original's identity. It is the idiomatic way to add cross-cutting behavior.

    ## When to use

    Wrap functions to add behavior (timing, caching, retries, auth) without touching their bodies.

    ## Worked examples

    **Define**

```python
import functools

def timed(fn):
    @functools.wraps(fn)
    def inner(*a, **k):
        import time; t = time.perf_counter()
        try:
            return fn(*a, **k)
        finally:
            print(fn.__name__, time.perf_counter() - t)
    return inner
```

**Use**

```python
@timed
def work():
    ...
```

**Parameterized**

```python
def retry(n):
    def deco(fn):
        @functools.wraps(fn)
        def inner(*a, **k):
            for _ in range(n):
                try: return fn(*a, **k)
                except Exception: pass
            raise
        return inner
    return deco
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Always use functools.wraps or you lose the wrapped function's name and docstring.
- A parameterized decorator needs three nested layers — factory, decorator, wrapper.

    ## Related

    `star-args`, `memoization`
