---
name: py-enumerate-zip
description: "Iterate with indices (enumerate) and over several sequences in lockstep (zip) instead of manual indexing."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: enumerate and zip

    ## Overview

    `enumerate` gives you index and value together; `zip` walks multiple iterables in parallel. Both replace error-prone `range(len(...))` indexing.

    ## When to use

    Iterate with indices (enumerate) and over several sequences in lockstep (zip) instead of manual indexing.

    ## Worked examples

    **enumerate**

```python
for i, item in enumerate(items, start=1):
    print(i, item)
```

**zip**

```python
for name, score in zip(names, scores):
    print(name, score)
```

**zip to dict / unzip**

```python
d = dict(zip(keys, values))
xs, ys = zip(*points)
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - zip stops at the shortest input; use itertools.zip_longest to pad instead.
- zip returns an iterator — wrap in list() if you need to reuse it.

    ## Related

    `comprehensions`, `unpacking`
