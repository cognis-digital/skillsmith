---
name: py-generators
description: "Produce values lazily with yield so you can stream large or infinite sequences without holding them in memory."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Generators and lazy iteration

    ## Overview

    A generator function uses `yield` to produce a stream of values on demand. It keeps memory flat regardless of how much data flows through, which is essential for large files and pipelines.

    ## When to use

    Produce values lazily with yield so you can stream large or infinite sequences without holding them in memory.

    ## Worked examples

    **Generator function**

```python
def read_chunks(f, size=4096):
    while chunk := f.read(size):
        yield chunk
```

**Generator expression**

```python
total = sum(len(line) for line in open('big.txt'))
```

**Pipeline**

```python
lines = (l.strip() for l in f)
nonempty = (l for l in lines if l)
for l in nonempty:
    handle(l)
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - A generator is single-use: once exhausted, iterating again yields nothing.
- Do not call len() on a generator; materialize with list() only when you truly need all of it.

    ## Related

    `comprehensions`, `python-itertools`, `iterators`
