---
name: py-format-numbers
description: "Present numbers precisely with format specs, and round correctly with round/Decimal."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Formatting and rounding numbers

    ## Overview

    Use the format mini-language for display (width, precision, separators, percent) and `decimal.Decimal` when exactness matters (money) — floats are binary approximations.

    ## When to use

    Present numbers precisely with format specs, and round correctly with round/Decimal.

    ## Worked examples

    **Display**

```python
f'{1234567:,}'          # 1,234,567
f'{0.1234:.1%}'         # 12.3%
f'{3.14159:8.2f}'       # '    3.14'
```

**Exact money**

```python
from decimal import Decimal
price = Decimal('19.99') * 3
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Never store money as float; use Decimal or integer cents.
- round() uses banker's rounding (round-half-to-even) — expected for stats, surprising for currency.

    ## Related

    `f-strings`, `datetime-recipe`
