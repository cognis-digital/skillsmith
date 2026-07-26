---
name: bash-umount
description: "Program the umount command: Detach a mounted filesystem."
version: 1.0.0
tags: [bash, cli, command-line, filesystem]
---

    # Command: `umount`

    ## Overview

    Detach a mounted filesystem.

    ## When to use

    Use `umount` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
umount /mnt
```
```bash
umount -l /mnt
```

    ## Structuring it in a program

    `umount` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if umount ... ; then
        echo "ok"
    else
        echo "umount failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`umount --help` on this machine)

```
Usage: umount [-f] <-a | drive_letters | network_mounts> 

-a	Delete all NFS network mount points
-f	Force delete NFS network mount points
```

    ## Related

    `mount`
