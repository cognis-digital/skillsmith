---
name: bash-getfacl
description: "Program the getfacl command: Show a file's POSIX access-control lists."
version: 1.0.0
tags: [bash, cli, command-line, perms]
---

    # Command: `getfacl`

    ## Overview

    Show a file's POSIX access-control lists.

    ## When to use

    Use `getfacl` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
getfacl file
```

    ## Structuring it in a program

    `getfacl` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if getfacl ... ; then
        echo "ok"
    else
        echo "getfacl failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`getfacl --help` on this machine)

```
Usage: getfacl [-adn] FILE [FILE2...]

Display file and directory access control lists (ACLs).

  -a, --access        display the file access control list only
  -d, --default       display the default access control list only
  -c, --omit-header   do not display the comment header
  -e, --all-effective print all effective rights
  -E, --no-effective  print no effective rights
  -n, --numeric       print numeric user/group identifiers
  -V, --version       print version and exit
  -h, --help          this help text

When multiple files are specified on the command line, a blank
line separates the ACLs for each file.
For each argument that is a regular file, special file or
directory, getfacl displays the owner, the group, and the ACL.
For directories getfacl displays additionally the default ACL.

With no options specified, getfacl displays the filename, the
owner, the group, the setuid (s), setgid (s), and sticky (t)
bits if available, and both the ACL and the default ACL, if it
exists.

The format for ACL output is as follows:
     # file: filename
     # owner: name or uid
     # group: name or uid
     # flags: sst
     user::perm
     user:name or uid:perm
     group::perm
     group:name or gid:perm
     mask::perm
     other::perm
     default:user::perm
     default:user:name or uid:perm
     default:group::perm
     default:group:name or gid:perm
     default:mask::perm
     default:other::perm
```

    ## Related

    `setfacl`, `chmod`
