---
name: git-mv
description: "Program git mv: Move or rename a file and stage the change."
version: 1.0.0
tags: [cli, git, version-control]
---

    # Git: `git mv`

    ## Overview

    Move or rename a file and stage the change.

    ## When to use

    `git mv` is part of an everyday version-control workflow. Know exactly what
    it changes before you run it — some git operations rewrite history.

    ## Worked example

    ```bash
    git mv --help     # read the options first
    git mv ...        # then run it deliberately
    ```

    ## Structuring it in a workflow

    Script git operations idempotently and check status between steps:

    ```bash
    git mv ... || { echo "git mv failed" >&2; exit 1; }
    git status --short
    ```

    ## Full reference (`git mv --help`)

```
usage: git mv [<options>] <source>... <destination>

    -v, --verbose         be verbose
    -n, --dry-run         dry run
    -f, --force           force move/rename even if target exists
    -k                    skip move/rename errors
    --sparse              allow updating entries outside of the sparse-checkout cone
```

    ## Related

    Other `git` subcommands in this catalog's `git` domain.
