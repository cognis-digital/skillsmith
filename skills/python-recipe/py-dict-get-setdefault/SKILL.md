---
name: py-dict-get-setdefault
description: "Read possibly-missing keys with get(), and initialize-then-append with setdefault()."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: dict.get and setdefault

    ## Overview

    `dict.get(key, default)` avoids KeyError; `dict.setdefault(key, default)` returns the existing value or inserts and returns a default — a one-liner for grouping without defaultdict.

    ## When to use

    Read possibly-missing keys with get(), and initialize-then-append with setdefault().

    ## Worked examples

    **Safe read**

```python
count = counts.get(word, 0)
config.get('timeout', 30)
```

**Group**

```python
groups = {}
for w in words:
    groups.setdefault(w[0], []).append(w)
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - setdefault always evaluates its default argument — for expensive defaults prefer defaultdict.
- get() returns None by default; pass an explicit default when None is a valid value.

    ## Related

    `collections-toolkit`, `comprehensions`
