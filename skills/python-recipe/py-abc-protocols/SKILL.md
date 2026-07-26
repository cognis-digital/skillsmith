---
name: py-abc-protocols
description: "Define interfaces with abc.ABC (nominal) or typing.Protocol (structural, duck-typed)."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Abstract base classes and Protocols

    ## Overview

    An ABC declares methods subclasses must implement; a Protocol describes a shape any object can satisfy without inheritance. Use ABCs for your own hierarchies, Protocols to type duck-typed inputs.

    ## When to use

    Define interfaces with abc.ABC (nominal) or typing.Protocol (structural, duck-typed).

    ## Worked examples

    **ABC**

```python
from abc import ABC, abstractmethod
class Store(ABC):
    @abstractmethod
    def get(self, k): ...
    @abstractmethod
    def put(self, k, v): ...
```

**Protocol**

```python
from typing import Protocol
class Reader(Protocol):
    def read(self, n: int) -> bytes: ...
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - An ABC with an unimplemented abstractmethod cannot be instantiated — that's the point.
- Protocols are checked structurally by type checkers; no explicit subclassing needed.

    ## Related

    `typing-hints`, `dunder-methods`
