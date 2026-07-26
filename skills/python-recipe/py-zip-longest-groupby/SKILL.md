---
name: py-zip-longest-groupby
description: "Combine and group iterables with itertools' zip_longest, groupby, and chain."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: itertools: zip_longest, groupby, chain

    ## Overview

    `itertools` composes iterators efficiently: `chain` concatenates, `zip_longest` pads uneven inputs, and `groupby` clusters consecutive equal keys (sort first for global grouping).

    ## When to use

    Combine and group iterables with itertools' zip_longest, groupby, and chain.

    ## Worked examples

    **chain / zip_longest**

```python
from itertools import chain, zip_longest
all_items = list(chain(a, b, c))
pairs = list(zip_longest(x, y, fillvalue=0))
```

**groupby (sorted!)**

```python
from itertools import groupby
data.sort(key=lambda r: r.dept)
for dept, rows in groupby(data, key=lambda r: r.dept):
    print(dept, len(list(rows)))
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - groupby groups only *consecutive* equal keys — sort by the same key first.
- The groups from groupby are one-shot iterators; consume each before advancing.

    ## Related

    `python-itertools`, `sorting-key`
