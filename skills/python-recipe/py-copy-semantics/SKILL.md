---
name: py-copy-semantics
description: "Understand that assignment shares references, and copy explicitly with slicing, copy(), or deepcopy()."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Copying: references, shallow, and deep

    ## Overview

    Assignment binds another name to the same object; mutating through one name is visible through the other. Copy explicitly when you need independence.

    ## When to use

    Understand that assignment shares references, and copy explicitly with slicing, copy(), or deepcopy().

    ## Worked examples

    **Shared vs copied**

```python
a = [1, 2]; b = a          # same list
c = a[:]                    # shallow copy
import copy
d = copy.deepcopy(nested)   # fully independent
```

**Gotcha**

```python
grid = [[0] * 3] * 3        # WRONG: three refs to one row
grid = [[0] * 3 for _ in range(3)]  # right
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - `[[0]*3]*3` makes three references to the same inner list — a classic bug. Use a comprehension.
- Shallow copy duplicates the outer container only; nested objects are still shared.

    ## Related

    `slicing`, `dataclasses`
