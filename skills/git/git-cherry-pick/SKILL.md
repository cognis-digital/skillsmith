---
name: git-cherry-pick
description: "Program git cherry-pick: Apply the changes introduced by an existing commit."
version: 1.0.0
tags: [cli, git, version-control]
---

    # Git: `git cherry-pick`

    ## Overview

    Apply the changes introduced by an existing commit.

    ## When to use

    `git cherry-pick` is part of an everyday version-control workflow. Know exactly what
    it changes before you run it — some git operations rewrite history.

    ## Worked example

    ```bash
    git cherry-pick --help     # read the options first
    git cherry-pick ...        # then run it deliberately
    ```

    ## Structuring it in a workflow

    Script git operations idempotently and check status between steps:

    ```bash
    git cherry-pick ... || { echo "git cherry-pick failed" >&2; exit 1; }
    git status --short
    ```

    ## Full reference (`git cherry-pick --help`)

```
usage: git cherry-pick [<options>] <commit-ish>...
   or: git cherry-pick <subcommand>

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
    -x                    append commit name
    --ff                  allow fast-forward
    --allow-empty         preserve initially empty commits
    --allow-empty-message
                          allow commits with empty messages
    --keep-redundant-commits
                          keep redundant, empty commits
```

    ## Related

    Other `git` subcommands in this catalog's `git` domain.
