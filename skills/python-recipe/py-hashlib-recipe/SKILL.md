---
name: py-hashlib-recipe
description: "Compute cryptographic and content hashes of bytes and files with hashlib."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Hashing with hashlib

    ## Overview

    `hashlib` provides SHA-256 and friends for integrity checks, content addressing, and dedup. Hash bytes, and stream large files in chunks.

    ## When to use

    Compute cryptographic and content hashes of bytes and files with hashlib.

    ## Worked examples

    **Hash bytes/text**

```python
import hashlib
h = hashlib.sha256(b'hello').hexdigest()
hashlib.sha256(text.encode()).hexdigest()
```

**Stream a file**

```python
h = hashlib.sha256()
with open(path, 'rb') as f:
    for chunk in iter(lambda: f.read(8192), b''):
        h.update(chunk)
print(h.hexdigest())
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Hash bytes, not str — encode text first with a fixed encoding.
- Do not use MD5/SHA-1 for security; they are fine only for non-adversarial checksums.

    ## Related

    `json-io`, `pathlib-recipe`
