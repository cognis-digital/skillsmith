---
name: bash-sync
description: "Program the sync command: Flush filesystem buffers to disk."
version: 1.0.0
tags: [bash, cli, command-line, disk]
---

    # Command: `sync`

    ## Overview

    Flush filesystem buffers to disk.

    ## When to use

    Use `sync` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
sync
```

    ## Structuring it in a program

    `sync` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if sync ... ; then
        echo "ok"
    else
        echo "sync failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`sync --help` on this machine)

```
Usage: sync [OPTION] [FILE]...
Synchronize cached writes to persistent storage

If one or more files are specified, sync only them,
or their containing file systems.

  -d, --data             sync only file data, no unneeded metadata
  -f, --file-system      sync the file systems that contain the files
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/sync>
or available locally via: info '(coreutils) sync invocation'
```

    ## Related

    `dd`
