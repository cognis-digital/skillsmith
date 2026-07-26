---
name: git-shortlog
description: "Program git shortlog: Summarize git log output, grouped by author."
version: 1.0.0
tags: [cli, git, version-control]
---

    # Git: `git shortlog`

    ## Overview

    Summarize git log output, grouped by author.

    ## When to use

    `git shortlog` is part of an everyday version-control workflow. Know exactly what
    it changes before you run it — some git operations rewrite history.

    ## Worked example

    ```bash
    git shortlog --help     # read the options first
    git shortlog ...        # then run it deliberately
    ```

    ## Structuring it in a workflow

    Script git operations idempotently and check status between steps:

    ```bash
    git shortlog ... || { echo "git shortlog failed" >&2; exit 1; }
    git status --short
    ```

    ## Full reference (`git shortlog --help`)

```
usage: git shortlog [<options>] [<revision-range>] [[--] <path>...]
   or: git log --pretty=short | git shortlog [<options>]

    -c, --committer       group by committer rather than author
    -n, --numbered        sort output according to the number of commits per author
    -s, --summary         suppress commit descriptions, only provides commit count
    -e, --email           show the email address of each author
    -w[<w>[,<i1>[,<i2>]]]
                          linewrap output
    --group <field>       group by field
```

    ## Related

    Other `git` subcommands in this catalog's `git` domain.
