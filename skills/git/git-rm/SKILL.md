---
name: git-rm
description: "Program git rm: Remove files from the working tree and the index."
version: 1.0.0
tags: [cli, git, version-control]
---

    # Git: `git rm`

    ## Overview

    Remove files from the working tree and the index.

    ## When to use

    `git rm` is part of an everyday version-control workflow. Know exactly what
    it changes before you run it — some git operations rewrite history.

    ## Worked example

    ```bash
    git rm --help     # read the options first
    git rm ...        # then run it deliberately
    ```

    ## Structuring it in a workflow

    Script git operations idempotently and check status between steps:

    ```bash
    git rm ... || { echo "git rm failed" >&2; exit 1; }
    git status --short
    ```

    ## Full reference (`git rm --help`)

```
usage: git rm [<options>] [--] <file>...

    -n, --dry-run         dry run
    -q, --quiet           do not list removed files
    --cached              only remove from the index
    -f, --force           override the up-to-date check
    -r                    allow recursive removal
    --ignore-unmatch      exit with a zero status even if nothing matched
    --sparse              allow updating entries outside of the sparse-checkout cone
    --pathspec-from-file <file>
                          read pathspec from file
    --pathspec-file-nul   with --pathspec-from-file, pathspec elements are separated with NUL character
```

    ## Related

    Other `git` subcommands in this catalog's `git` domain.
