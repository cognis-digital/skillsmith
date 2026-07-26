---
name: py-memoization
description: "Cache expensive pure-function results automatically with functools.lru_cache / cache."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Memoization with lru_cache

    ## Overview

    `@functools.lru_cache` memoizes results keyed by arguments, turning repeated or recursive calls into O(1) lookups. Use it for pure, hashable-argument functions.

    ## When to use

    Cache expensive pure-function results automatically with functools.lru_cache / cache.

    ## Worked examples

    **Cache**

```python
import functools

@functools.lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)
```

**Unbounded**

```python
@functools.cache   # 3.9+, == lru_cache(maxsize=None)
def load(path): ...
```

**Inspect / clear**

```python
fib.cache_info()
fib.cache_clear()
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Only decorate pure functions with hashable args; caching side-effecting functions hides bugs.
- An unbounded cache can grow forever — set maxsize for hot paths with many distinct keys.

    ## Related

    `decorators`, `generators`
