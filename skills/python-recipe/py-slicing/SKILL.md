---
name: py-slicing
description: "Extract, reverse, and step through parts of sequences with slice notation [start:stop:step]."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Sequence slicing

    ## Overview

    Slicing produces a subsequence with `seq[start:stop:step]`. Omitted bounds default to the ends; a negative step reverses.

    ## When to use

    Extract, reverse, and step through parts of sequences with slice notation [start:stop:step].

    ## Worked examples

    **Basics**

```python
xs[1:4]     # items 1,2,3
xs[:3]      # first three
xs[-2:]     # last two
```

**Step / reverse**

```python
xs[::2]     # every other
xs[::-1]    # reversed
s = text[::-1]
```

**Assign to a slice**

```python
xs[1:3] = [10, 20, 30]   # lists only
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Slicing a list copies (shallow); slicing a string/tuple makes a new one.
- Out-of-range slice bounds are clamped, not errors — unlike single-index access.

    ## Related

    `unpacking`, `string-methods`
