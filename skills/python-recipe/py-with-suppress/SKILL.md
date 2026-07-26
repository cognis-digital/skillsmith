---
name: py-with-suppress
description: "Silence expected exceptions and adapt resources with contextlib's small context managers."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: contextlib helpers: suppress, closing, redirect

    ## Overview

    `contextlib.suppress` swallows named exceptions cleanly; `closing` adapts objects with only a close(); `redirect_stdout` captures prints. They replace boilerplate try/except/finally.

    ## When to use

    Silence expected exceptions and adapt resources with contextlib's small context managers.

    ## Worked examples

    **suppress**

```python
from contextlib import suppress
with suppress(FileNotFoundError):
    os.remove(path)
```

**redirect**

```python
import io, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    noisy()
captured = buf.getvalue()
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Only suppress exceptions you truly expect and intend to ignore — never blanket-suppress Exception.
- suppress is for 'best effort' cleanup, not for control flow.

    ## Related

    `context-managers`, `exception-handling`
