---
name: py-chained-comparison
description: "Write range and multi-way comparisons the mathematical way: lo <= x < hi."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Chained comparisons

    ## Overview

    Python evaluates `a < b < c` as `a < b and b < c`, each operand once. It reads like math and prevents off-by-one mistakes in bounds checks.

    ## When to use

    Write range and multi-way comparisons the mathematical way: lo <= x < hi.

    ## Worked examples

    **Range check**

```python
if 0 <= i < len(xs):
    return xs[i]
```

**Equality chain**

```python
if a == b == c:
    ...
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Each middle operand is evaluated once; avoid side effects there anyway.
- Don't over-chain — three comparisons is usually the readable limit.

    ## Related

    `ternary-truthiness`, `slicing`
