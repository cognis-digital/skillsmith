---
name: git-worktree
description: "Program git worktree: Manage multiple working trees attached to one repository."
version: 1.0.0
tags: [cli, git, version-control]
---

    # Git: `git worktree`

    ## Overview

    Manage multiple working trees attached to one repository.

    ## When to use

    `git worktree` is part of an everyday version-control workflow. Know exactly what
    it changes before you run it — some git operations rewrite history.

    ## Worked example

    ```bash
    git worktree --help     # read the options first
    git worktree ...        # then run it deliberately
    ```

    ## Structuring it in a workflow

    Script git operations idempotently and check status between steps:

    ```bash
    git worktree ... || { echo "git worktree failed" >&2; exit 1; }
    git status --short
    ```

    ## Full reference (`git worktree --help`)

```
usage: git worktree add [<options>] <path> [<commit-ish>]
   or: git worktree list [<options>]
   or: git worktree lock [<options>] <path>
   or: git worktree move <worktree> <new-path>
   or: git worktree prune [<options>]
   or: git worktree remove [<options>] <worktree>
   or: git worktree unlock <path>
```

    ## Related

    Other `git` subcommands in this catalog's `git` domain.
