---
name: git-stash
description: "Program git stash: Shelve dirty working-tree changes and restore a clean state."
version: 1.0.0
tags: [cli, git, version-control]
---

    # Git: `git stash`

    ## Overview

    Shelve dirty working-tree changes and restore a clean state.

    ## When to use

    `git stash` is part of an everyday version-control workflow. Know exactly what
    it changes before you run it — some git operations rewrite history.

    ## Worked example

    ```bash
    git stash --help     # read the options first
    git stash ...        # then run it deliberately
    ```

    ## Structuring it in a workflow

    Script git operations idempotently and check status between steps:

    ```bash
    git stash ... || { echo "git stash failed" >&2; exit 1; }
    git status --short
    ```

    ## Full reference (`git stash --help`)

```
usage: git stash list [<options>]
   or: git stash show [<options>] [<stash>]
   or: git stash drop [-q|--quiet] [<stash>]
   or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]
   or: git stash branch <branchname> [<stash>]
   or: git stash clear
   or: git stash [push [-p|--patch] [-S|--staged] [-k|--[no-]keep-index] [-q|--quiet]
                 [-u|--include-untracked] [-a|--all] [-m|--message <message>]
                 [--pathspec-from-file=<file> [--pathspec-file-nul]]
                 [--] [<pathspec>...]]
   or: git stash save [-p|--patch] [-S|--staged] [-k|--[no-]keep-index] [-q|--quiet]
                 [-u|--include-untracked] [-a|--all] [<message>]
```

    ## Related

    Other `git` subcommands in this catalog's `git` domain.
