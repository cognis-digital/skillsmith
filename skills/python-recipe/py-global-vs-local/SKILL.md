---
name: py-global-vs-local
description: "Know where names resolve (Local, Enclosing, Global, Built-in) and avoid the global statement."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Scope: local, global, and the LEGB rule

    ## Overview

    Python resolves names by the LEGB rule. Assignment inside a function creates a local unless declared `global`/`nonlocal`. Prefer passing and returning values over mutating globals.

    ## When to use

    Know where names resolve (Local, Enclosing, Global, Built-in) and avoid the global statement.

    ## Worked examples

    **Read vs assign**

```python
x = 10
def show(): print(x)      # reads global fine
def bad():
    x = x + 1              # UnboundLocalError: x is local here
```

**Explicit global (avoid)**

```python
def set_flag():
    global FLAG
    FLAG = True
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Assigning to a name anywhere in a function makes it local throughout — read-before-assign then fails.
- Global mutable state is hard to test; pass arguments and return results instead.

    ## Related

    `closures`, `main-guard`
