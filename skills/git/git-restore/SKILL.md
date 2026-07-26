---
name: git-restore
description: "Program git restore: Restore working-tree files from a source (undo local changes)."
version: 1.0.0
tags: [cli, git, version-control]
---

    # Git: `git restore`

    ## Overview

    Restore working-tree files from a source (undo local changes).

    ## When to use

    `git restore` is part of an everyday version-control workflow. Know exactly what
    it changes before you run it — some git operations rewrite history.

    ## Worked example

    ```bash
    git restore --help     # read the options first
    git restore ...        # then run it deliberately
    ```

    ## Structuring it in a workflow

    Script git operations idempotently and check status between steps:

    ```bash
    git restore ... || { echo "git restore failed" >&2; exit 1; }
    git status --short
    ```

    ## Full reference (`git restore --help`)

```
usage: git restore [<options>] [--source=<branch>] <file>...

    -s, --source <tree-ish>
                          which tree-ish to checkout from
    -S, --staged          restore the index
    -W, --worktree        restore the working tree (default)
    --ignore-unmerged     ignore unmerged entries
    --overlay             use overlay mode
    -q, --quiet           suppress progress reporting
    --recurse-submodules[=<checkout>]
                          control recursive updating of submodules
    --progress            force progress reporting
    -m, --merge           perform a 3-way merge with the new branch
    --conflict <style>    conflict style (merge, diff3, or zdiff3)
    -2, --ours            checkout our version for unmerged files
    -3, --theirs          checkout their version for unmerged files
    -p, --patch           select hunks interactively
    --ignore-skip-worktree-bits
                          do not limit pathspecs to sparse entries only
    --pathspec-from-file <file>
                          read pathspec from file
    --pathspec-file-nul   with --pathspec-from-file, pathspec elements are separated with NUL character
```

    ## Related

    Other `git` subcommands in this catalog's `git` domain.
