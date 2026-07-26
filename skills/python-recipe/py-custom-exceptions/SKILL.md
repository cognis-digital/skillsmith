---
name: py-custom-exceptions
description: "Define your own exception hierarchy so callers can catch your errors specifically."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Custom exceptions

    ## Overview

    Subclass `Exception` (not BaseException) to create meaningful, catchable error types. A small hierarchy lets callers handle categories of failure.

    ## When to use

    Define your own exception hierarchy so callers can catch your errors specifically.

    ## Worked examples

    **Define a hierarchy**

```python
class AppError(Exception):
    pass

class ConfigError(AppError):
    pass

class NetworkError(AppError):
    pass
```

**Raise with detail**

```python
raise ConfigError(f'missing key: {key}')
```

**Catch a category**

```python
try:
    run()
except AppError as e:
    report(e)
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Inherit from Exception, never BaseException, for application errors.
- Carry structured data as attributes, not just a formatted string, when callers need it.

    ## Related

    `exception-handling`
