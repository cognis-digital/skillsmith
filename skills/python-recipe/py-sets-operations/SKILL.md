---
name: py-sets-operations
description: "Deduplicate and compute unions, intersections, and differences with set operators."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Set operations

    ## Overview

    Sets store unique, unordered, hashable items and support fast membership and algebra: `|` union, `&` intersection, `-` difference, `^` symmetric difference.

    ## When to use

    Deduplicate and compute unions, intersections, and differences with set operators.

    ## Worked examples

    **Dedup + membership**

```python
unique = set(items)
if x in unique: ...
```

**Algebra**

```python
common = a & b
only_a = a - b
either = a | b
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Sets are unordered — do not rely on iteration order.
- Elements must be hashable; use frozenset for a set you can put inside another set.

    ## Related

    `collections-toolkit`, `comprehensions`
