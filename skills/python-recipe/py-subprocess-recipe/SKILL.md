---
name: py-subprocess-recipe
description: "Invoke other programs safely from Python with subprocess.run, capturing output and checking status."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Running external commands

    ## Overview

    `subprocess.run` is the modern entry point: pass a list of arguments (no shell), capture output, and check the return code. Avoid shell=True with untrusted input.

    ## When to use

    Invoke other programs safely from Python with subprocess.run, capturing output and checking status.

    ## Worked examples

    **Capture + check**

```python
import subprocess
r = subprocess.run(['git', 'rev-parse', 'HEAD'],
    capture_output=True, text=True, check=True)
print(r.stdout.strip())
```

**Handle failure**

```python
try:
    subprocess.run(['make'], check=True)
except subprocess.CalledProcessError as e:
    print('build failed', e.returncode)
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Pass args as a list, not a string, and avoid shell=True to prevent injection.
- Use text=True to get str instead of bytes; set timeout= to avoid hangs.

    ## Related

    `python-subprocess`, `exception-handling`
