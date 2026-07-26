---
name: git-status
description: "Program git status: Show the working tree status: staged, unstaged, and untracked changes."
version: 1.0.0
tags: [cli, git, version-control]
---

    # Git: `git status`

    ## Overview

    Show the working tree status: staged, unstaged, and untracked changes.

    ## When to use

    `git status` is part of an everyday version-control workflow. Know exactly what
    it changes before you run it — some git operations rewrite history.

    ## Worked example

    ```bash
    git status --help     # read the options first
    git status ...        # then run it deliberately
    ```

    ## Structuring it in a workflow

    Script git operations idempotently and check status between steps:

    ```bash
    git status ... || { echo "git status failed" >&2; exit 1; }
    git status --short
    ```

    ## Full reference (`git status --help`)

```
usage: git status [<options>] [--] <pathspec>...

    -v, --verbose         be verbose
    -s, --short           show status concisely
    -b, --branch          show branch information
    --show-stash          show stash information
    --ahead-behind        compute full ahead/behind values
    --porcelain[=<version>]
                          machine-readable output
    --long                show status in long format (default)
    -z, --null            terminate entries with NUL
    -u, --untracked-files[=<mode>]
                          show untracked files, optional modes: all, normal, no. (Default: all)
    --ignored[=<mode>]    show ignored files, optional modes: traditional, matching, no. (Default: traditional)
    --ignore-submodules[=<when>]
                          ignore changes to submodules, optional when: all, dirty, untracked. (Default: all)
    --column[=<style>]    list untracked files in columns
    --no-renames          do not detect renames
    -M, --find-renames[=<n>]
                          detect renames, optionally set similarity index
    --show-ignored-directory
                          (DEPRECATED: use --ignore=matching instead) Only show directories that match an ignore pattern name.
    --no-lock-index       (DEPRECATED: use `git --no-optional-locks status` instead) Do not lock the index
```

    ## Related

    Other `git` subcommands in this catalog's `git` domain.
