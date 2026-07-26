---
name: git-init
description: "Program git init: Create a new git repository in the current directory."
version: 1.0.0
tags: [cli, git, version-control]
---

    # Git: `git init`

    ## Overview

    Create a new git repository in the current directory.

    ## When to use

    `git init` is part of an everyday version-control workflow. Know exactly what
    it changes before you run it — some git operations rewrite history.

    ## Worked example

    ```bash
    git init --help     # read the options first
    git init ...        # then run it deliberately
    ```

    ## Structuring it in a workflow

    Script git operations idempotently and check status between steps:

    ```bash
    git init ... || { echo "git init failed" >&2; exit 1; }
    git status --short
    ```

    ## Full reference (`git init --help`)

```
usage: git init [-q | --quiet] [--bare] [--template=<template-directory>] [--shared[=<permissions>]] [<directory>]

    --template <template-directory>
                          directory from which templates will be used
    --bare                create a bare repository
    --shared[=<permissions>]
                          specify that the git repository is to be shared amongst several users
    -q, --quiet           be quiet
    --separate-git-dir <gitdir>
                          separate git dir from working tree
    -b, --initial-branch <name>
                          override the name of the initial branch
    --object-format <hash>
                          specify the hash algorithm to use
```

    ## Related

    Other `git` subcommands in this catalog's `git` domain.
