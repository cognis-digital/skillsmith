---
name: py-logging-recipe
description: "Emit structured, level-based diagnostics with the logging module instead of print."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Logging done right

    ## Overview

    `logging` gives you levels (DEBUG..CRITICAL), configurable handlers, and per-module loggers. Use a module-level logger and configure once at the entry point.

    ## When to use

    Emit structured, level-based diagnostics with the logging module instead of print.

    ## Worked examples

    **Set up**

```python
import logging
logging.basicConfig(level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s: %(message)s')
log = logging.getLogger(__name__)
```

**Use**

```python
log.info('processing %s', path)
log.warning('retrying (%d/%d)', i, n)
log.exception('failed')   # inside an except: adds traceback
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Pass args to the logger (log.info('x=%s', x)) — don't f-string, so formatting is lazy.
- Configure logging once at the program's entry point, not in library modules.

    ## Related

    `python-logging`, `exception-handling`
