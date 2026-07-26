---
name: git-clean
description: "Program git clean: Remove untracked files from the working tree."
version: 1.0.0
tags: [cli, git, version-control]
---

    # Git: `git clean`

    ## Overview

    Remove untracked files from the working tree.

    ## When to use

    `git clean` is part of an everyday version-control workflow. Know exactly what
    it changes before you run it — some git operations rewrite history.

    ## Worked example

    ```bash
    git clean --help     # read the options first
    git clean ...        # then run it deliberately
    ```

    ## Structuring it in a workflow

    Script git operations idempotently and check status between steps:

    ```bash
    git clean ... || { echo "git clean failed" >&2; exit 1; }
    git status --short
    ```

    ## Full reference (`git clean --help`)

```
usage: git clean [-d] [-f] [-i] [-n] [-q] [-e <pattern>] [-x | -X] [--] <paths>...

    -q, --quiet           do not print names of files removed
    -n, --dry-run         dry run
    -f, --force           force
    -i, --interactive     interactive cleaning
    -d                    remove whole directories
    -e, --exclude <pattern>
                          add <pattern> to ignore rules
    -x                    remove ignored files, too
    -X                    remove only ignored files
```

    ## Related

    Other `git` subcommands in this catalog's `git` domain.
