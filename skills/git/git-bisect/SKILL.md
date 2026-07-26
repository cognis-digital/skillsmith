---
name: git-bisect
description: "Program git bisect: Binary-search history to find the commit that introduced a bug."
version: 1.0.0
tags: [cli, git, version-control]
---

    # Git: `git bisect`

    ## Overview

    Binary-search history to find the commit that introduced a bug.

    ## When to use

    `git bisect` is part of an everyday version-control workflow. Know exactly what
    it changes before you run it — some git operations rewrite history.

    ## Worked example

    ```bash
    git bisect --help     # read the options first
    git bisect ...        # then run it deliberately
    ```

    ## Structuring it in a workflow

    Script git operations idempotently and check status between steps:

    ```bash
    git bisect ... || { echo "git bisect failed" >&2; exit 1; }
    git status --short
    ```

    ## Full reference (`git bisect --help`)

```
usage: git bisect [help|start|bad|good|new|old|terms|skip|next|reset|visualize|view|replay|log|run]

git bisect help
	print this long help message.
git bisect start [--term-{new,bad}=<term> --term-{old,good}=<term>]
		 [--no-checkout] [--first-parent] [<bad> [<good>...]] [--] [<pathspec>...]
	reset bisect state and start bisection.
git bisect (bad|new) [<rev>]
	mark <rev> a known-bad revision/
		a revision after change in a given property.
git bisect (good|old) [<rev>...]
	mark <rev>... known-good revisions/
		revisions before change in a given property.
git bisect terms [--term-good | --term-bad]
	show the terms used for old and new commits (default: bad, good)
git bisect skip [(<rev>|<range>)...]
	mark <rev>... untestable revisions.
git bisect next
	find next bisection to test and check it out.
git bisect reset [<commit>]
	finish bisection search and go back to commit.
git bisect (visualize|view)
	show bisect status in gitk.
git bisect replay <logfile>
	replay bisection log.
git bisect log
	show bisect log.
git bisect run <cmd>...
	use <cmd>... to automatically bisect.

Please use "git help bisect" to get the full man page.
```

    ## Related

    Other `git` subcommands in this catalog's `git` domain.
