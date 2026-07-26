---
name: py-uuid-recipe
description: "Create globally unique identifiers with the uuid module for records, files, and correlation."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Generating unique IDs with uuid

    ## Overview

    `uuid.uuid4()` returns a random 128-bit identifier with negligible collision risk — the go-to for IDs you generate without a central authority.

    ## When to use

    Create globally unique identifiers with the uuid module for records, files, and correlation.

    ## Worked examples

    **Random ID**

```python
import uuid
id = uuid.uuid4()
id_str = str(uuid.uuid4())          # '3f2504e0-...'
id_hex = uuid.uuid4().hex           # no dashes
```

**Deterministic (namespaced)**

```python
uuid.uuid5(uuid.NAMESPACE_URL, 'https://x/y')
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Use uuid4 for random IDs; uuid1 embeds the MAC/time and can leak host info.
- Store as a string or the native 16 bytes consistently; don't mix representations.

    ## Related

    `hashlib-recipe`, `datetime-recipe`
