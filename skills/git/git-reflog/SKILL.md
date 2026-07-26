---
name: git-reflog
description: "Program git reflog: Show a log of where HEAD and refs have been (recover lost commits)."
version: 1.0.0
tags: [cli, git, version-control]
---

    # Git: `git reflog`

    ## Overview

    Show a log of where HEAD and refs have been (recover lost commits).

    ## When to use

    `git reflog` is part of an everyday version-control workflow. Know exactly what
    it changes before you run it — some git operations rewrite history.

    ## Worked example

    ```bash
    git reflog --help     # read the options first
    git reflog ...        # then run it deliberately
    ```

    ## Structuring it in a workflow

    Script git operations idempotently and check status between steps:

    ```bash
    git reflog ... || { echo "git reflog failed" >&2; exit 1; }
    git status --short
    ```

    ## Full reference (`git reflog --help`)

```
usage: git reflog [ show | expire | delete | exists ]
```

    ## Related

    Other `git` subcommands in this catalog's `git` domain.
