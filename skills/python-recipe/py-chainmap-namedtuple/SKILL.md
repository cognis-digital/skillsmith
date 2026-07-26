---
name: py-chainmap-namedtuple
description: "Make lightweight immutable records (namedtuple) and layered lookups (ChainMap)."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: namedtuple and ChainMap

    ## Overview

    `collections.namedtuple` gives tuples named fields (immutable, memory-light); `ChainMap` searches several dicts in order — perfect for layered config (CLI over env over defaults).

    ## When to use

    Make lightweight immutable records (namedtuple) and layered lookups (ChainMap).

    ## Worked examples

    **namedtuple**

```python
from collections import namedtuple
Point = namedtuple('Point', 'x y')
p = Point(1, 2); p.x
```

**ChainMap**

```python
from collections import ChainMap
cfg = ChainMap(cli_opts, env_opts, defaults)
cfg['timeout']       # first map that has it wins
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Prefer a dataclass over namedtuple when you need defaults, methods, or mutability.
- ChainMap writes go to the first mapping only — reads search all of them.

    ## Related

    `dataclasses`, `collections-toolkit`
