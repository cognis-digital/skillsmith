---
name: py-async-await
description: "Run many I/O-bound operations concurrently with coroutines instead of threads."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: async / await with asyncio

    ## Overview

    `async def` defines a coroutine; `await` yields control while I/O is pending. asyncio schedules thousands of concurrent I/O operations on one thread.

    ## When to use

    Run many I/O-bound operations concurrently with coroutines instead of threads.

    ## Worked examples

    **Coroutine + run**

```python
import asyncio

async def fetch(n):
    await asyncio.sleep(0.1)
    return n * 2

asyncio.run(fetch(21))
```

**Concurrent gather**

```python
async def main():
    results = await asyncio.gather(*(fetch(i) for i in range(10)))
    return results
asyncio.run(main())
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - await only inside async functions; call asyncio.run() once at the top level.
- asyncio helps I/O-bound work, not CPU-bound — use multiprocessing for CPU.

    ## Related

    `python-asyncio`, `generators`
