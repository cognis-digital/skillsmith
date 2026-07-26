---
name: py-regex-recipe
description: "Match, extract, and replace text with the re module — compiled patterns, groups, and substitution."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Regular expressions in Python

    ## Overview

    `re` provides regular expressions. Compile hot patterns once, use raw strings, name your groups, and prefer `search`/`finditer` for scanning.

    ## When to use

    Match, extract, and replace text with the re module — compiled patterns, groups, and substitution.

    ## Worked examples

    **Search + groups**

```python
import re
m = re.search(r'(?P<user>\w+)@(?P<host>[\w.]+)', s)
if m:
    print(m.group('user'), m.group('host'))
```

**Find all / iterate**

```python
for m in re.finditer(r'\d+', text):
    print(m.group())
```

**Substitute**

```python
clean = re.sub(r'\s+', ' ', messy).strip()
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Use raw strings (r'...') so backslashes reach the regex engine intact.
- Compile with re.compile when reusing a pattern in a loop.

    ## Related

    `python-re`, `f-strings`
