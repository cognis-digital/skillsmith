---
name: py-ternary-truthiness
description: "Choose values inline with the ternary, and lean on Python's truthiness rules cleanly."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Conditional expressions and truthiness

    ## Overview

    `a if cond else b` selects a value in an expression. Empty containers, 0, '', and None are falsy — exploit this for concise, readable defaults.

    ## When to use

    Choose values inline with the ternary, and lean on Python's truthiness rules cleanly.

    ## Worked examples

    **Ternary**

```python
label = 'even' if n % 2 == 0 else 'odd'
```

**Truthy defaults**

```python
name = user_input or 'anonymous'
if not items:
    return 'empty'
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - `or` returns the first truthy operand, not a bool — great for defaults, surprising if you expected True/False.
- Compare to None with `is None`, not truthiness, when 0/'' are valid values.

    ## Related

    `walrus`, `match-statement`
