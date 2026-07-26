---
name: py-collections-toolkit
description: "Reach for specialized containers — defaultdict, Counter, deque — instead of reinventing them."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: collections: defaultdict, Counter, deque

    ## Overview

    The `collections` module ships containers that make common tasks trivial: grouping (defaultdict), tallying (Counter), and O(1) ends (deque).

    ## When to use

    Reach for specialized containers — defaultdict, Counter, deque — instead of reinventing them.

    ## Worked examples

    **defaultdict grouping**

```python
from collections import defaultdict
g = defaultdict(list)
for w in words:
    g[w[0]].append(w)
```

**Counter**

```python
from collections import Counter
c = Counter(text.split())
c.most_common(3)
```

**deque**

```python
from collections import deque
q = deque(maxlen=100)
q.append(x); q.popleft()
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - A deque with maxlen drops from the far end automatically — great for rolling windows.
- defaultdict creates missing keys on access; use dict.get if you don't want that.

    ## Related

    `python-collections`, `comprehensions`
