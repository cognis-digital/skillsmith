---
name: py-logging-vs-print
description: "Send results to stdout, diagnostics to logging/stderr, and never mix the two streams."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Choosing output: print, logging, and stderr

    ## Overview

    A well-behaved program prints its *data* to stdout so pipelines can consume it, and its *diagnostics* (progress, warnings, errors) to stderr or the logging module. Mixing them corrupts downstream parsing.

    ## When to use

    Send results to stdout, diagnostics to logging/stderr, and never mix the two streams.

    ## Worked examples

    **Separate streams**

```python
import sys
print(result)                          # data -> stdout
print('processing...', file=sys.stderr) # status -> stderr
```

**Prefer logging for apps**

```python
import logging
log = logging.getLogger(__name__)
log.info('done')
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Emitting logs to stdout breaks tools that parse your output — use stderr or logging.
- print is fine for CLI results and quick scripts; use logging for anything long-lived.

    ## Related

    `logging-recipe`, `os-environ`
