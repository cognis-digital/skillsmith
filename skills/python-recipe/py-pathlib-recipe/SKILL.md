---
name: py-pathlib-recipe
description: "Manipulate paths and do file I/O with the object-oriented pathlib.Path instead of os.path string juggling."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Filesystem paths with pathlib

    ## Overview

    `pathlib.Path` treats paths as objects with methods — joining with `/`, reading/writing text, globbing, and existence checks — clearer and safer than string concatenation.

    ## When to use

    Manipulate paths and do file I/O with the object-oriented pathlib.Path instead of os.path string juggling.

    ## Worked examples

    **Build + read**

```python
from pathlib import Path
p = Path.home() / 'data' / 'in.txt'
text = p.read_text(encoding='utf-8')
```

**Glob + iterate**

```python
for f in Path('src').rglob('*.py'):
    print(f, f.stat().st_size)
```

**Create + write**

```python
out = Path('build/out.json')
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(data)
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Use `/` to join, never string '+' with os.sep.
- read_text/write_text handle open+close for you — pass encoding='utf-8' explicitly.

    ## Related

    `python-pathlib`, `context-managers`
