---
name: py-main-guard
description: "Separate a module's importable definitions from its script entry point with the main-guard."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: The `if __name__ == '__main__'` guard

    ## Overview

    Code under `if __name__ == '__main__':` runs only when the file is executed directly, not when imported. It lets one file be both a reusable library and a runnable script.

    ## When to use

    Separate a module's importable definitions from its script entry point with the main-guard.

    ## Worked examples

    **Pattern**

```python
def main() -> int:
    ...
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Keep top-level code minimal; put logic in functions so importing the module has no side effects.
- Return an int from main() and pass it to sys.exit() to set the process exit code.

    ## Related

    `argparse-recipe`, `subprocess-recipe`
