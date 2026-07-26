---
name: py-reduce-accumulate
description: "Collapse an iterable to one value (reduce) or a running series (itertools.accumulate)."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Folding with reduce and accumulate

    ## Overview

    `functools.reduce` folds a binary function across items to a single result; `itertools.accumulate` yields the running results. Reach for them for products, running totals, and custom folds.

    ## When to use

    Collapse an iterable to one value (reduce) or a running series (itertools.accumulate).

    ## Worked examples

    **reduce**

```python
from functools import reduce
product = reduce(lambda a, b: a * b, nums, 1)
```

**accumulate**

```python
from itertools import accumulate
running = list(accumulate(nums))          # running sum
running_max = list(accumulate(nums, max))
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Prefer sum()/min()/max()/math.prod() over reduce when one exists — clearer and faster.
- Always give reduce an explicit initializer to handle empty iterables safely.

    ## Related

    `collections-toolkit`, `map-filter`
