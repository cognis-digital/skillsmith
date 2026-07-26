---
name: py-shutil-recipe
description: "Copy trees, move, and remove directories, and find executables with the shutil module."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: High-level file operations with shutil

    ## Overview

    `shutil` provides the high-level file operations `os` lacks: recursive copy/remove, move across filesystems, archive make/unpack, and `which`.

    ## When to use

    Copy trees, move, and remove directories, and find executables with the shutil module.

    ## Worked examples

    **Copy / move / remove tree**

```python
import shutil
shutil.copy2('a', 'b')          # copy with metadata
shutil.copytree('src', 'dst')
shutil.move('a', 'archive/')
shutil.rmtree('build')
```

**Find a program**

```python
path = shutil.which('git')
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - rmtree is recursive and irreversible — double-check the target.
- copytree fails if the destination exists (unless dirs_exist_ok=True).

    ## Related

    `pathlib-recipe`, `subprocess-recipe`
