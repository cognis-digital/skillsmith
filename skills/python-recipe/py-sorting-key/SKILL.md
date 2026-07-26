---
name: py-sorting-key
description: "Sort and find extremes by a computed key with sorted, min, max, and operator helpers."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Sorting with keys

    ## Overview

    The `key=` argument computes a sort value per element without mutating it. Combine with `reverse=`, `operator.itemgetter`, and tuples for multi-level sorts.

    ## When to use

    Sort and find extremes by a computed key with sorted, min, max, and operator helpers.

    ## Worked examples

    **By attribute/field**

```python
people.sort(key=lambda p: p.age)
rows = sorted(rows, key=lambda r: (r['dept'], -r['salary']))
```

**operator helpers**

```python
from operator import itemgetter, attrgetter
sorted(pairs, key=itemgetter(1))
sorted(objs, key=attrgetter('name'))
```

**Extremes**

```python
oldest = max(people, key=lambda p: p.age)
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Return a tuple from key= for multi-level sorts; negate a numeric field to reverse just that level.
- sorted() returns a new list; list.sort() sorts in place and returns None.

    ## Related

    `comprehensions`, `collections-toolkit`
