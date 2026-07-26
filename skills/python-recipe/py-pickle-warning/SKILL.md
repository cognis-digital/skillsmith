---
name: py-pickle-warning
description: "Persist Python objects with pickle for trusted data, and prefer json for anything crossing a trust boundary."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Serialization: pickle vs json (and when not to)

    ## Overview

    `pickle` serializes almost any Python object but executes code on load — never unpickle untrusted data. Use JSON for interchange and untrusted input; use pickle only for your own local caches.

    ## When to use

    Persist Python objects with pickle for trusted data, and prefer json for anything crossing a trust boundary.

    ## Worked examples

    **Pickle (trusted only)**

```python
import pickle
with open('cache.pkl', 'wb') as f:
    pickle.dump(obj, f)
with open('cache.pkl', 'rb') as f:
    obj = pickle.load(f)   # only on data YOU wrote
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Unpickling untrusted data can execute arbitrary code — a remote-code-execution risk. Use JSON instead.
- Pickle format is Python- and version-specific; don't use it as a long-term or cross-language format.

    ## Related

    `json-io`, `hashlib-recipe`
