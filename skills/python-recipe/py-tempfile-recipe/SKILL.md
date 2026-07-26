---
name: py-tempfile-recipe
description: "Create secure, auto-cleaned temporary files and directories with the tempfile module."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Temporary files and directories

    ## Overview

    `tempfile` makes uniquely named temp files/dirs in the right location, and its context managers remove them automatically — safer than hand-rolled /tmp paths.

    ## When to use

    Create secure, auto-cleaned temporary files and directories with the tempfile module.

    ## Worked examples

    **Temp dir**

```python
import tempfile, pathlib
with tempfile.TemporaryDirectory() as d:
    p = pathlib.Path(d) / 'work.txt'
    p.write_text('scratch')
# directory removed here
```

**Named temp file**

```python
with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as f:
    f.write(data)
    path = f.name
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Prefer the context managers so cleanup is automatic even on error.
- Never build temp paths by hand in /tmp — race conditions and collisions.

    ## Related

    `pathlib-recipe`, `context-managers`
