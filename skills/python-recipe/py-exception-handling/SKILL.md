---
name: py-exception-handling
description: "Handle errors precisely with try/except/else/finally, catching narrow exception types."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Exception handling

    ## Overview

    Catch the specific exceptions you can handle, keep the try body small, use `else` for the success path, and `finally` for cleanup. Broad excepts hide bugs.

    ## When to use

    Handle errors precisely with try/except/else/finally, catching narrow exception types.

    ## Worked examples

    **Narrow**

```python
try:
    value = int(s)
except ValueError:
    value = 0
```

**else / finally**

```python
try:
    f = open(path)
except OSError as e:
    log(e); raise
else:
    use(f)
finally:
    f.close()
```

**Re-raise with context**

```python
try:
    parse()
except ValueError as e:
    raise ConfigError('bad config') from e
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Avoid bare `except:` — it catches KeyboardInterrupt and SystemExit too.
- Keep the try block to the single statement that can fail, so you don't mask unrelated errors.

    ## Related

    `custom-exceptions`, `context-managers`
