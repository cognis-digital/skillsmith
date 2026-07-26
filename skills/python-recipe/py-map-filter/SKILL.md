---
name: py-map-filter
description: "Transform and select items functionally with map/filter, favouring comprehensions where clearer."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: map, filter, and functional transforms

    ## Overview

    `map(f, it)` and `filter(pred, it)` return lazy iterators. Comprehensions usually read better, but map/filter shine when you already have a named function to apply.

    ## When to use

    Transform and select items functionally with map/filter, favouring comprehensions where clearer.

    ## Worked examples

    **map / filter**

```python
lengths = list(map(len, words))
positives = list(filter(lambda n: n > 0, nums))
```

**With a named fn**

```python
cleaned = map(str.strip, lines)
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Both return lazy iterators — wrap in list() to materialize or reuse.
- For an inline expression, a comprehension is usually clearer than map/filter with a lambda.

    ## Related

    `comprehensions`, `partial-functions`
