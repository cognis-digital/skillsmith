---
name: git-log
description: "Program git log: Show the commit history, with formatting and filtering options."
version: 1.0.0
tags: [cli, git, version-control]
---

    # Git: `git log`

    ## Overview

    Show the commit history, with formatting and filtering options.

    ## When to use

    `git log` is part of an everyday version-control workflow. Know exactly what
    it changes before you run it — some git operations rewrite history.

    ## Worked example

    ```bash
    git log --help     # read the options first
    git log ...        # then run it deliberately
    ```

    ## Structuring it in a workflow

    Script git operations idempotently and check status between steps:

    ```bash
    git log ... || { echo "git log failed" >&2; exit 1; }
    git status --short
    ```

    ## Full reference (`git log --help`)

```
usage: git log [<options>] [<revision-range>] [[--] <path>...]
   or: git show [<options>] <object>...

    -q, --quiet           suppress diff output
    --source              show source
    --use-mailmap         use mail map file
    --mailmap             alias of --use-mailmap
    --decorate-refs <pattern>
                          only decorate refs that match <pattern>
    --decorate-refs-exclude <pattern>
                          do not decorate refs that match <pattern>
    --decorate[=...]      decorate options
    -L <range:file>       trace the evolution of line range <start>,<end> or function :<funcname> in <file>
```

    ## Related

    Other `git` subcommands in this catalog's `git` domain.
