---
name: py-string-methods
description: "Split, join, strip, replace, and test strings with their built-in methods instead of manual loops."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: String manipulation

    ## Overview

    `str` methods cover most text work: `split`/`join` for tokenizing, `strip` for trimming, `startswith`/`endswith` for tests, `replace` and `translate` for edits.

    ## When to use

    Split, join, strip, replace, and test strings with their built-in methods instead of manual loops.

    ## Worked examples

    **Split / join**

```python
parts = line.split(',')
csv = ','.join(fields)
```

**Trim / case**

```python
clean = raw.strip().lower()
title = name.title()
```

**Test / find**

```python
if path.endswith('.py'): ...
if 'error' in log_line.lower(): ...
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Strings are immutable — every method returns a new string; assign the result.
- Build big strings with ''.join(list) in a loop, not repeated += concatenation.

    ## Related

    `f-strings`, `regex-recipe`
