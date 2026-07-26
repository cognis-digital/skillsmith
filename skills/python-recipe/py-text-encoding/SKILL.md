---
name: py-text-encoding
description: "Convert between str and bytes explicitly with encode/decode, always naming the encoding."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Text encoding and bytes

    ## Overview

    `str` is Unicode text; `bytes` is raw octets. Convert at the boundaries with `.encode()`/`.decode()` and always specify `utf-8` — never rely on the platform default.

    ## When to use

    Convert between str and bytes explicitly with encode/decode, always naming the encoding.

    ## Worked examples

    **Encode / decode**

```python
data = text.encode('utf-8')
text = data.decode('utf-8')
```

**Robust decode**

```python
text = data.decode('utf-8', errors='replace')
```

**File I/O**

```python
open('f.txt', encoding='utf-8')
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Always pass encoding='utf-8' to open() — the default varies by OS and burns you on Windows.
- Hash, network, and file bytes are bytes; convert to str only when you need text operations.

    ## Related

    `string-methods`, `hashlib-recipe`
