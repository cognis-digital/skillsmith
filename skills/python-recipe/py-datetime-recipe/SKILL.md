---
name: py-datetime-recipe
description: "Work with timestamps, durations, and formatting using datetime, timezone, and timedelta."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Dates and times

    ## Overview

    `datetime` handles points in time and `timedelta` handles durations. Prefer timezone-aware UTC for storage and convert for display.

    ## When to use

    Work with timestamps, durations, and formatting using datetime, timezone, and timedelta.

    ## Worked examples

    **Now / UTC**

```python
from datetime import datetime, timezone, timedelta
now = datetime.now(timezone.utc)
```

**Arithmetic**

```python
yesterday = now - timedelta(days=1)
```

**Parse / format**

```python
d = datetime.strptime('2026-07-25', '%Y-%m-%d')
s = now.strftime('%Y-%m-%dT%H:%M:%SZ')
```

**ISO**

```python
d = datetime.fromisoformat('2026-07-25T12:00:00+00:00')
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Prefer timezone-aware datetimes (attach tz) — naive datetimes cause silent bugs.
- Store/transport in UTC; convert to local only for display.

    ## Related

    `python-datetime`
