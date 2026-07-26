---
name: py-f-strings
description: "Interpolate and format values directly in string literals with f-strings, including alignment and precision."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: f-strings and formatting

    ## Overview

    f-strings embed expressions in `{}` and support the full format mini-language: width, alignment, precision, and thousands separators. They are the clearest, fastest way to build strings.

    ## When to use

    Interpolate and format values directly in string literals with f-strings, including alignment and precision.

    ## Worked examples

    **Basic**

```python
name = 'Ada'
print(f'Hello, {name}!')
```

**Format spec**

```python
print(f'{price:>10.2f}')   # right-aligned, 2 decimals
print(f'{n:,}')            # thousands separator
```

**Debug (=)**

```python
x = 42
print(f'{x=}')            # -> x=42
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Braces need doubling to be literal: f'{{not a field}}'.
- Keep heavy logic out of the braces — compute first, interpolate second.

    ## Related

    `string-formatting`, `python-string`
