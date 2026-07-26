---
name: py-dunder-methods
description: "Make objects behave like built-ins by implementing __repr__, __eq__, __len__, __getitem__, and friends."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Dunder (magic) methods

    ## Overview

    Special 'dunder' methods hook your class into language operators and protocols — printing, equality, length, indexing, iteration, and arithmetic.

    ## When to use

    Make objects behave like built-ins by implementing __repr__, __eq__, __len__, __getitem__, and friends.

    ## Worked examples

    **Repr + eq**

```python
class Money:
    def __init__(self, c): self.c = c
    def __repr__(self): return f'Money({self.c})'
    def __eq__(self, o): return isinstance(o, Money) and o.c == self.c
    def __hash__(self): return hash(self.c)
```

**Container protocol**

```python
class Deck:
    def __init__(self, cards): self._c = cards
    def __len__(self): return len(self._c)
    def __getitem__(self, i): return self._c[i]
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - If you define __eq__, define __hash__ too (or set it to None for unhashable).
- Implement __repr__ for every class — it makes debugging and logs far clearer.

    ## Related

    `dataclasses`, `iterators`
