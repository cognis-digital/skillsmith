---
name: py-json-io
description: "Serialize and parse JSON with the json module, including files and pretty-printing."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Reading and writing JSON

    ## Overview

    `json` converts between Python objects and JSON text. Use `dump`/`load` for files and `dumps`/`loads` for strings; set `indent` for human-readable output.

    ## When to use

    Serialize and parse JSON with the json module, including files and pretty-printing.

    ## Worked examples

    **String**

```python
import json
obj = json.loads('{"a": 1}')
text = json.dumps(obj, indent=2)
```

**File**

```python
with open('data.json') as f:
    data = json.load(f)
with open('out.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Set ensure_ascii=False to keep non-ASCII readable.
- JSON keys are always strings; integer dict keys become strings on round-trip.

    ## Related

    `python-json`, `pathlib-recipe`
