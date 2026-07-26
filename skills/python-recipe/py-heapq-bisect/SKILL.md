---
name: py-heapq-bisect
description: "Keep the smallest items handy with heapq, and insert into sorted lists with bisect."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Priority queues and sorted insertion (heapq, bisect)

    ## Overview

    `heapq` maintains a min-heap in a list for O(log n) push/pop of the smallest item; `bisect` finds insertion points to keep a list sorted without a full re-sort.

    ## When to use

    Keep the smallest items handy with heapq, and insert into sorted lists with bisect.

    ## Worked examples

    **Heap / top-k**

```python
import heapq
heapq.nlargest(3, data)
h = []
heapq.heappush(h, 5); smallest = heapq.heappop(h)
```

**Bisect insert**

```python
import bisect
bisect.insort(sorted_list, value)
i = bisect.bisect_left(sorted_list, target)
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - heapq is a min-heap; negate values (or use tuples) for a max-heap.
- bisect assumes the list is already sorted — it does not check.

    ## Related

    `sorting-key`, `collections-toolkit`
