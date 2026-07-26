---
name: bash-mount
description: "Program the mount command: Attach a filesystem to the directory tree."
version: 1.0.0
tags: [bash, cli, command-line, filesystem]
---

    # Command: `mount`

    ## Overview

    Attach a filesystem to the directory tree.

    ## When to use

    Use `mount` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
mount /dev/sdb1 /mnt
```
```bash
mount -o ro dev dir
```
```bash
mount
```

    ## Structuring it in a program

    `mount` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if mount ... ; then
        echo "ok"
    else
        echo "mount failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`mount --help` on this machine)

```
Usage:  mount [-o options] [-u:username] [-p:<password | *>] <\\computername\sharename> <devicename | *>

-o rsize=size               To set the size of the read buffer in kilobytes.
-o wsize=size               To set the size of the write buffer in kilobytes.
-o timeout=time             To set the timeout value in seconds for an RPC call.
-o retry=number             To set the number of retries for a soft mount.
-o mtype=soft|hard          To set the mount type.
-o lang=euc-jp|euc-tw|euc-kr|shift-jis|big5|ksc5601|gb2312-80|ansi
                            To specify the encoding used for file and directory
                            names.
-o fileaccess=mode          To specify the permission mode of the file.
                            These are used for new files created on NFS
                            servers. Specified using UNIX style mode bits.
-o anon                     To mount as an anonymous user.
-o nolock                   To disable locking.
-o casesensitive=yes|no     To specify case sensitivity of file lookup on server.
-o sec=sys|krb5|krb5i|krb5p
```

    ## Related

    `umount`, `lsblk`, `df`
