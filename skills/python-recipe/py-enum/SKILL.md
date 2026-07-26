---
name: py-enum
description: "Give a fixed set of related constants real names and type-safety with the enum module."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Enumerations (`enum`)

    ## Overview

    An `Enum` replaces magic strings/numbers with named, comparable, self-documenting members. Use it for states, modes, and categories.

    ## When to use

    Give a fixed set of related constants real names and type-safety with the enum module.

    ## Worked examples

    **Define**

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```

**Use**

```python
c = Color.RED
if c is Color.RED: ...
print(c.name, c.value)
```

**String enum**

```python
from enum import StrEnum

class Env(StrEnum):
    DEV = 'dev'
    PROD = 'prod'
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Compare members with `is`, not `==` to string values.
- Members are singletons — don't instantiate the enum class to make one.

    ## Related

    `dataclasses`, `match-statement`
