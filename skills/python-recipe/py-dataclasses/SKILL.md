---
name: py-dataclasses
description: "Model plain data with @dataclass to get init, repr, and comparison for free instead of boilerplate classes."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Dataclasses

    ## Overview

    `@dataclass` generates `__init__`, `__repr__`, and `__eq__` from typed fields. Use it for records and value objects; it is the modern default over hand-written classes or bare tuples.

    ## When to use

    Model plain data with @dataclass to get init, repr, and comparison for free instead of boilerplate classes.

    ## Worked examples

    **Basic**

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float = 0.0
```

**Frozen (hashable)**

```python
@dataclass(frozen=True)
class Config:
    host: str
    port: int = 8080
```

**Defaults that are mutable**

```python
from dataclasses import field

@dataclass
class Bag:
    items: list = field(default_factory=list)
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Never use a mutable default directly (items: list = []); use field(default_factory=list).
- frozen=True makes instances immutable and hashable — but you cannot reassign fields.

    ## Related

    `namedtuple`, `typing-hints`, `enum`
