---
name: py-assertions
description: "State internal invariants with assert during development — but never for user input validation."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Assertions and invariants

    ## Overview

    `assert cond, msg` documents and checks an assumption. It is a debugging aid for programmer errors, and can be stripped with `python -O`, so it must not guard real logic.

    ## When to use

    State internal invariants with assert during development — but never for user input validation.

    ## Worked examples

    **Invariant**

```python
def average(xs):
    assert xs, 'average of empty sequence'
    return sum(xs) / len(xs)
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Never use assert to validate untrusted input or enforce security — `-O` removes it.
- Assert conditions that should be impossible if the code is correct, not conditions that can legitimately occur.

    ## Related

    `custom-exceptions`, `exception-handling`
