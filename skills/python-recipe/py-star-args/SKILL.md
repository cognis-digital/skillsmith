---
name: py-star-args
description: "Write functions that accept any number of positional and keyword arguments and forward them cleanly."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: *args and **kwargs

    ## Overview

    `*args` collects extra positionals into a tuple; `**kwargs` collects extra keywords into a dict. Use them for wrappers, decorators, and flexible APIs.

    ## When to use

    Write functions that accept any number of positional and keyword arguments and forward them cleanly.

    ## Worked examples

    **Accept**

```python
def log_call(*args, **kwargs):
    print(args, kwargs)
```

**Forward**

```python
def wrapper(*args, **kwargs):
    return real(*args, **kwargs)
```

**Keyword-only**

```python
def connect(host, *, timeout=30, retries=3):
    ...   # timeout/retries must be passed by name
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - A bare `*` in the signature forces the following params to be keyword-only.
- Unpacking at the call site (*seq, **dict) is the mirror image of collecting.

    ## Related

    `unpacking`, `decorators`
