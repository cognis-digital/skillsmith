---
name: py-closures
description: "Capture enclosing-scope variables in nested functions, and mutate them with nonlocal."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Closures and nonlocal

    ## Overview

    A closure is a nested function that remembers variables from the scope where it was defined. `nonlocal` lets it rebind those variables; without it, assignment creates a new local.

    ## When to use

    Capture enclosing-scope variables in nested functions, and mutate them with nonlocal.

    ## Worked examples

    **Capture**

```python
def multiplier(k):
    def mul(x):
        return x * k
    return mul
triple = multiplier(3)
```

**nonlocal counter**

```python
def make_counter():
    n = 0
    def inc():
        nonlocal n
        n += 1
        return n
    return inc
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Late binding: closures capture the variable, not its value — loop-created closures all see the final value unless you bind it (e.g. default arg).
- Use nonlocal to rebind an enclosing variable; without it, assignment shadows it locally.

    ## Related

    `decorators`, `class-methods`
