---
name: py-unpacking
description: "Destructure sequences and dicts into variables, including starred rest-capture, for clean assignments."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Tuple / iterable unpacking

    ## Overview

    Unpacking binds multiple names at once and captures the 'rest' with `*`. It makes swaps, multiple returns, and head/tail splits obvious.

    ## When to use

    Destructure sequences and dicts into variables, including starred rest-capture, for clean assignments.

    ## Worked examples

    **Basic + swap**

```python
a, b = 1, 2
a, b = b, a
```

**Starred**

```python
first, *middle, last = [1, 2, 3, 4, 5]
```

**In loops / returns**

```python
for key, value in d.items():
    ...

def minmax(xs):
    return min(xs), max(xs)
lo, hi = minmax(data)
```

**Merge dicts**

```python
merged = {**defaults, **overrides}
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Starred target captures a list, possibly empty — handle the empty case.
- The number of non-starred targets must match, or you get a ValueError.

    ## Related

    `star-args`, `enumerate-zip`
