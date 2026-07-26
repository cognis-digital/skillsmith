---
name: bash-shred
description: "Program the shred command: Overwrite a file repeatedly to make recovery hard, then optionally delete."
version: 1.0.0
tags: [bash, cli, command-line, files, security]
---

    # Command: `shred`

    ## Overview

    Overwrite a file repeatedly to make recovery hard, then optionally delete.

    ## When to use

    Use `shred` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
shred -u secret
```
```bash
shred -n3 -z file
```

    ## Structuring it in a program

    `shred` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if shred ... ; then
        echo "ok"
    else
        echo "shred failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`shred --help` on this machine)

```
Usage: shred [OPTION]... FILE...
Overwrite the specified FILE(s) repeatedly, in order to make it harder
for even very expensive hardware probing to recover the data.

If FILE is -, shred standard output.

Mandatory arguments to long options are mandatory for short options too.
  -f, --force    change permissions to allow writing if necessary
  -n, --iterations=N  overwrite N times instead of the default (3)
      --random-source=FILE  get random bytes from FILE
  -s, --size=N   shred this many bytes (suffixes like K, M, G accepted)
  -u             deallocate and remove file after overwriting
      --remove[=HOW]  like -u but give control on HOW to delete;  See below
  -v, --verbose  show progress
  -x, --exact    do not round file sizes up to the next full block;
                   this is the default for non-regular files
  -z, --zero     add a final overwrite with zeros to hide shredding
      --help     display this help and exit
      --version  output version information and exit

Delete FILE(s) if --remove (-u) is specified.  The default is not to remove
the files because it is common to operate on device files like /dev/hda,
and those files usually should not be removed.
The optional HOW parameter indicates how to remove a directory entry:
'unlink' => use a standard unlink call.
'wipe' => also first obfuscate bytes in the name.
'wipesync' => also sync each obfuscated byte to disk.
The default mode is 'wipesync', but note it can be expensive.

CAUTION: shred assumes the file system and hardware overwrite data in place.
Although this is common, many platforms operate otherwise.  Also, backups
and mirrors may contain unremovable copies that will let a shredded file
be recovered later.  See the GNU coreutils manual for details.

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/shred>
or available locally via: info '(coreutils) shred invocation'
```

    ## Related

    `rm`
