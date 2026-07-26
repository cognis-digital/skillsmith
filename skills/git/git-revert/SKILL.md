---
name: git-revert
description: "Program git revert: Create a new commit that undoes a previous commit safely."
version: 1.0.0
tags: [cli, git, version-control]
---

    # Git: `git revert`

    ## Overview

    Create a new commit that undoes a previous commit safely.

    ## When to use

    `git revert` is part of an everyday version-control workflow. Know exactly what
    it changes before you run it — some git operations rewrite history.

    ## Worked example

    ```bash
    git revert --help     # read the options first
    git revert ...        # then run it deliberately
    ```

    ## Structuring it in a workflow

    Script git operations idempotently and check status between steps:

    ```bash
    git revert ... || { echo "git revert failed" >&2; exit 1; }
    git status --short
    ```

    ## Full reference (`git revert --help`)

```
usage: git revert [<options>] <commit-ish>...
   or: git revert <subcommand>

    --quit                end revert or cherry-pick sequence
    --continue            resume revert or cherry-pick sequence
    --abort               cancel revert or cherry-pick sequence
    --skip                skip current commit and continue
    --cleanup <mode>      how to strip spaces and #comments from message
    -n, --no-commit       don't automatically commit
    -e, --edit            edit the commit message
    -s, --signoff         add a Signed-off-by trailer
    -m, --mainline <parent-number>
                          select mainline parent
    --rerere-autoupdate   update the index with reused conflict resolution if possible
    --strategy <strategy>
                          merge strategy
    -X, --strategy-option <option>
                          option for merge strategy
    -S, --gpg-sign[=<key-id>]
                          GPG sign commit
```

    ## Related

    Other `git` subcommands in this catalog's `git` domain.
