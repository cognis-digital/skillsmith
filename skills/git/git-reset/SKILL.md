---
name: git-reset
description: "Program git reset: Move HEAD and optionally the index/working tree to a state."
version: 1.0.0
tags: [cli, git, version-control]
---

    # Git: `git reset`

    ## Overview

    Move HEAD and optionally the index/working tree to a state.

    ## When to use

    `git reset` is part of an everyday version-control workflow. Know exactly what
    it changes before you run it — some git operations rewrite history.

    ## Worked example

    ```bash
    git reset --help     # read the options first
    git reset ...        # then run it deliberately
    ```

    ## Structuring it in a workflow

    Script git operations idempotently and check status between steps:

    ```bash
    git reset ... || { echo "git reset failed" >&2; exit 1; }
    git status --short
    ```

    ## Full reference (`git reset --help`)

```
usage: git reset [--mixed | --soft | --hard | --merge | --keep] [-q] [<commit>]
   or: git reset [-q] [<tree-ish>] [--] <pathspec>...
   or: git reset [-q] [--pathspec-from-file [--pathspec-file-nul]] [<tree-ish>]
   or: git reset --patch [<tree-ish>] [--] [<pathspec>...]
   or: DEPRECATED: git reset [-q] [--stdin [-z]] [<tree-ish>]

    -q, --quiet           be quiet, only report errors
    --mixed               reset HEAD and index
    --soft                reset only HEAD
    --hard                reset HEAD, index and working tree
    --merge               reset HEAD, index and working tree
    --keep                reset HEAD but keep local changes
    --recurse-submodules[=<reset>]
                          control recursive updating of submodules
    -p, --patch           select hunks interactively
    -N, --intent-to-add   record only the fact that removed paths will be added later
    --pathspec-from-file <file>
                          read pathspec from file
    --pathspec-file-nul   with --pathspec-from-file, pathspec elements are separated with NUL character
    -z                    DEPRECATED (use --pathspec-file-nul instead): paths are separated with NUL character
    --stdin               DEPRECATED (use --pathspec-from-file=- instead): read paths from <stdin>
```

    ## Related

    Other `git` subcommands in this catalog's `git` domain.
