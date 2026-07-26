---
name: py-os-environ
description: "Read configuration from the environment and command-line arguments the standard way."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Environment variables and sys.argv

    ## Overview

    `os.environ` is a dict of environment variables; `sys.argv` is the list of command-line arguments. Read config from the environment for 12-factor style apps, with sensible defaults.

    ## When to use

    Read configuration from the environment and command-line arguments the standard way.

    ## Worked examples

    **Env with default**

```python
import os
port = int(os.environ.get('PORT', '8080'))
token = os.environ['API_TOKEN']       # required: KeyError if unset
```

**Args**

```python
import sys
script, *args = sys.argv
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - os.environ values are always strings — convert types explicitly.
- For anything beyond a couple of flags, use argparse instead of parsing sys.argv by hand.

    ## Related

    `argparse-recipe`, `main-guard`
