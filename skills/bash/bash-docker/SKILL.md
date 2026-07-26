---
name: bash-docker
description: "Program the docker command: Build, run, and manage containers."
version: 1.0.0
tags: [bash, cli, command-line, container]
---

    # Command: `docker`

    ## Overview

    Build, run, and manage containers.

    ## When to use

    Use `docker` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
docker build -t img .
```
```bash
docker run --rm img
```
```bash
docker ps
```

    ## Structuring it in a program

    `docker` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if docker ... ; then
        echo "ok"
    else
        echo "docker failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man docker` on a POSIX system.

    ## Related

    `podman`, `kubectl`
