---
name: py-context-managers
description: "Acquire and release resources safely using with-statements and custom context managers so cleanup always runs."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Context managers (`with`)

    ## Overview

    The `with` statement guarantees teardown (close, unlock, restore) even when the body raises. Write your own with `contextlib.contextmanager` or `__enter__`/`__exit__`.

    ## When to use

    Acquire and release resources safely using with-statements and custom context managers so cleanup always runs.

    ## Worked examples

    **Files**

```python
with open('f.txt') as f:
    data = f.read()
# f is closed here, even on error
```

**Multiple**

```python
with open('a') as a, open('b', 'w') as b:
    b.write(a.read())
```

**Custom**

```python
from contextlib import contextmanager

@contextmanager
def timer():
    import time; t = time.perf_counter()
    try:
        yield
    finally:
        print(time.perf_counter() - t)
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Do not manually call close() when a with-block can do it for you.
- In a @contextmanager, put teardown in a finally so it runs even if the body raises.

    ## Related

    `exception-handling`, `python-contextlib`
