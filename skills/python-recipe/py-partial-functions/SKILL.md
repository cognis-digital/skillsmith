---
name: py-partial-functions
description: "Pre-bind some arguments of a function to make a simpler, specialized callable."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Partial application with functools.partial

    ## Overview

    `functools.partial` freezes some arguments, returning a new callable that needs only the rest — cleaner than a lambda for adapting callbacks and configuring functions.

    ## When to use

    Pre-bind some arguments of a function to make a simpler, specialized callable.

    ## Worked examples

    **Specialize**

```python
from functools import partial
int2 = partial(int, base=2)
int2('1010')                 # 10
```

**Adapt a callback**

```python
handler = partial(save, directory='/out')
for item in items:
    handler(item)
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - partial is picklable and introspectable; a lambda is often neither.
- Bind keyword args by name to avoid ambiguity with the remaining positional args.

    ## Related

    `decorators`, `sorting-key`
