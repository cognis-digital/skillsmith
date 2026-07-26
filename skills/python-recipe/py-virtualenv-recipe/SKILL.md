---
name: py-virtualenv-recipe
description: "Isolate a project's dependencies in a virtual environment so installs don't collide globally."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Virtual environments

    ## Overview

    A venv is a self-contained Python with its own site-packages. Create one per project so dependencies are reproducible and isolated.

    ## When to use

    Isolate a project's dependencies in a virtual environment so installs don't collide globally.

    ## Worked examples

    **Create + activate**

```python
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
```

**Install + freeze**

```python
pip install requests
pip freeze > requirements.txt
```

**Recreate elsewhere**

```python
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Never commit the .venv directory; commit requirements.txt instead.
- Activate the venv (or use its python directly) before pip install, or you pollute the global env.

    ## Related

    `argparse-recipe`, `subprocess-recipe`
