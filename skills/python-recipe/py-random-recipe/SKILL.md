---
name: py-random-recipe
description: "Generate random numbers, choices, and shuffles — and know when you need secrets instead."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Randomness with the random module

    ## Overview

    `random` covers simulations and sampling: `randint`, `choice`, `sample`, `shuffle`, `random`. For tokens and passwords, use `secrets`, which is cryptographically secure.

    ## When to use

    Generate random numbers, choices, and shuffles — and know when you need secrets instead.

    ## Worked examples

    **Common draws**

```python
import random
random.randint(1, 6)
random.choice(items)
random.sample(pool, 3)
random.shuffle(deck)
```

**Secure tokens**

```python
import secrets
secrets.token_hex(16)
secrets.choice(items)
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Never use random for passwords, tokens, or keys — use secrets.
- Seed random only for reproducible tests; never seed a security-sensitive generator.

    ## Related

    `hashlib-recipe`, `uuid-recipe`
