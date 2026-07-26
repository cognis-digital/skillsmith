---
name: py-typing-hints
description: "Annotate functions and variables with types so tools and readers catch mistakes early."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Type hints

    ## Overview

    Type hints document intent and enable static checkers (mypy, pyright) and editor help. They do not affect runtime behavior but massively improve maintainability.

    ## When to use

    Annotate functions and variables with types so tools and readers catch mistakes early.

    ## Worked examples

    **Functions**

```python
def greet(name: str, times: int = 1) -> str:
    return (f'hi {name} ' * times).strip()
```

**Collections + optional**

```python
from typing import Optional
def find(xs: list[int], target: int) -> Optional[int]:
    return xs.index(target) if target in xs else None
```

**Aliases**

```python
Vector = list[float]
def scale(v: Vector, k: float) -> Vector:
    return [x * k for x in v]
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Hints are not enforced at runtime — run a checker (mypy/pyright) to get value.
- Use built-in generics (list[int], dict[str, int]) on modern Python instead of typing.List.

    ## Related

    `dataclasses`, `protocols`
