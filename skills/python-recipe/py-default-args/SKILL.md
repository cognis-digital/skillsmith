---
name: py-default-args
description: "Give parameters sensible defaults, and never use a mutable object as a default value."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Default arguments (and the mutable-default trap)

    ## Overview

    Default argument values are evaluated once, at definition time. A mutable default (list/dict) is shared across all calls — a notorious bug. Use None and create inside.

    ## When to use

    Give parameters sensible defaults, and never use a mutable object as a default value.

    ## Worked examples

    **Wrong vs right**

```python
def add(x, bucket=[]):        # BUG: shared list
    bucket.append(x); return bucket

def add(x, bucket=None):      # correct
    if bucket is None:
        bucket = []
    bucket.append(x); return bucket
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - A mutable default is created once and reused across calls — use None as the sentinel.
- Keyword defaults document intent; keep them immutable (numbers, strings, tuples, None).

    ## Related

    `star-args`, `dict-get-setdefault`
