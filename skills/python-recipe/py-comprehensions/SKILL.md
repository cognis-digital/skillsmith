---
name: py-comprehensions
description: "Build lists, dicts, and sets declaratively with comprehensions instead of manual loops and appends."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: List / dict / set comprehensions

    ## Overview

    A comprehension expresses 'transform and filter this iterable into a new collection' in one readable expression. It is faster than an append loop and signals intent.

    ## When to use

    Build lists, dicts, and sets declaratively with comprehensions instead of manual loops and appends.

    ## Worked examples

    **List**

```python
squares = [n * n for n in range(10)]
evens = [n for n in nums if n % 2 == 0]
```

**Dict**

```python
by_id = {u.id: u for u in users}
lengths = {w: len(w) for w in words}
```

**Set**

```python
unique_domains = {email.split('@')[1] for email in emails}
```

**Nested**

```python
flat = [x for row in matrix for x in row]
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Do not build a comprehension for its side effects — use a plain for loop when you are not collecting a result.
- Deeply nested comprehensions hurt readability; switch to a loop or generator past two clauses.

    ## Related

    `generators`, `enumerate-zip`, `map-filter`
