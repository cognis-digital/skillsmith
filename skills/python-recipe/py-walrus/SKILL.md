---
name: py-walrus
description: "Assign and use a value in the same expression with := to avoid recomputation or extra lines."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Assignment expressions (walrus :=)

    ## Overview

    The walrus operator `:=` binds a name as part of an expression — handy in while-conditions, comprehension filters, and to avoid calling something twice.

    ## When to use

    Assign and use a value in the same expression with := to avoid recomputation or extra lines.

    ## Worked examples

    **While read**

```python
while (chunk := f.read(8192)):
    process(chunk)
```

**Filter + reuse**

```python
results = [y for x in data if (y := f(x)) is not None]
```

**Avoid double call**

```python
if (n := len(items)) > 10:
    print(f'{n} is a lot')
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Wrap the walrus in parentheses where precedence is ambiguous.
- Use it to remove repetition, not to cram unrelated logic into one line.

    ## Related

    `generators`, `comprehensions`
