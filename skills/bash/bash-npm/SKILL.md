---
name: bash-npm
description: "Program the npm command: Install and manage Node.js packages and scripts."
version: 1.0.0
tags: [bash, cli, command-line, packaging]
---

    # Command: `npm`

    ## Overview

    Install and manage Node.js packages and scripts.

    ## When to use

    Use `npm` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
npm install
```
```bash
npm run build
```
```bash
npm ci
```

    ## Structuring it in a program

    `npm` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if npm ... ; then
        echo "ok"
    else
        echo "npm failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man npm` on a POSIX system.

    ## Related

    `node`, `yarn`, `pnpm`
