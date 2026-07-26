---
name: git-describe
description: "Program git describe: Give an object a human-readable name based on the nearest tag."
version: 1.0.0
tags: [cli, git, version-control]
---

    # Git: `git describe`

    ## Overview

    Give an object a human-readable name based on the nearest tag.

    ## When to use

    `git describe` is part of an everyday version-control workflow. Know exactly what
    it changes before you run it — some git operations rewrite history.

    ## Worked example

    ```bash
    git describe --help     # read the options first
    git describe ...        # then run it deliberately
    ```

    ## Structuring it in a workflow

    Script git operations idempotently and check status between steps:

    ```bash
    git describe ... || { echo "git describe failed" >&2; exit 1; }
    git status --short
    ```

    ## Full reference (`git describe --help`)

```
usage: git describe [<options>] [<commit-ish>...]
   or: git describe [<options>] --dirty

    --contains            find the tag that comes after the commit
    --debug               debug search strategy on stderr
    --all                 use any ref
    --tags                use any tag, even unannotated
    --long                always use long format
    --first-parent        only follow first parent
    --abbrev[=<n>]        use <n> digits to display object names
    --exact-match         only output exact matches
    --candidates <n>      consider <n> most recent tags (default: 10)
    --match <pattern>     only consider tags matching <pattern>
    --exclude <pattern>   do not consider tags matching <pattern>
    --always              show abbreviated commit object as fallback
    --dirty[=<mark>]      append <mark> on dirty working tree (default: "-dirty")
    --broken[=<mark>]     append <mark> on broken working tree (default: "-broken")
```

    ## Related

    Other `git` subcommands in this catalog's `git` domain.
