---
name: git-switch
description: "Program git switch: Switch branches (a clearer alternative to checkout)."
version: 1.0.0
tags: [cli, git, version-control]
---

    # Git: `git switch`

    ## Overview

    Switch branches (a clearer alternative to checkout).

    ## When to use

    `git switch` is part of an everyday version-control workflow. Know exactly what
    it changes before you run it — some git operations rewrite history.

    ## Worked example

    ```bash
    git switch --help     # read the options first
    git switch ...        # then run it deliberately
    ```

    ## Structuring it in a workflow

    Script git operations idempotently and check status between steps:

    ```bash
    git switch ... || { echo "git switch failed" >&2; exit 1; }
    git status --short
    ```

    ## Full reference (`git switch --help`)

```
usage: git switch [<options>] [<branch>]

    -c, --create <branch>
                          create and switch to a new branch
    -C, --force-create <branch>
                          create/reset and switch to a branch
    --guess               second guess 'git switch <no-such-branch>'
    --discard-changes     throw away local modifications
    -q, --quiet           suppress progress reporting
    --recurse-submodules[=<checkout>]
                          control recursive updating of submodules
    --progress            force progress reporting
    -m, --merge           perform a 3-way merge with the new branch
    --conflict <style>    conflict style (merge, diff3, or zdiff3)
    -d, --detach          detach HEAD at named commit
    -t, --track[=(direct|inherit)]
                          set branch tracking configuration
    -f, --force           force checkout (throw away local modifications)
    --orphan <new-branch>
                          new unparented branch
    --overwrite-ignore    update ignored files (default)
    --ignore-other-worktrees
                          do not check if another worktree is holding the given ref
```

    ## Related

    Other `git` subcommands in this catalog's `git` domain.
