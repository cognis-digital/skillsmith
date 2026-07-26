---
name: bash-which
description: "Program the which command: Locate a command in PATH."
version: 1.0.0
tags: [bash, cli, command-line, shell]
---

    # Command: `which`

    ## Overview

    Locate a command in PATH.

    ## When to use

    Use `which` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
which python
```
```bash
which -a node
```

    ## Structuring it in a program

    `which` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if which ... ; then
        echo "ok"
    else
        echo "which failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`which --help` on this machine)

```
Usage: which [options] [--] COMMAND [...]
Write the full path of COMMAND(s) to standard output.

  --version, -[vV] Print version and exit successfully.
  --help,          Print this help and exit successfully.
  --skip-dot       Skip directories in PATH that start with a dot.
  --skip-tilde     Skip directories in PATH that start with a tilde.
  --show-dot       Don't expand a dot to current directory in output.
  --show-tilde     Output a tilde for HOME directory for non-root.
  --tty-only       Stop processing options on the right if not on tty.
  --all, -a        Print all matches in PATH, not just the first
  --read-alias, -i Read list of aliases from stdin.
  --skip-alias     Ignore option --read-alias; don't read stdin.
  --read-functions Read shell functions from stdin.
  --skip-functions Ignore option --read-functions; don't read stdin.

Recommended use is to write the output of (alias; declare -f) to standard
input, so that which can show aliases and shell functions. See which(1) for
examples.

If the options --read-alias and/or --read-functions are specified then the
output can be a full alias or function definition, optionally followed by
the full path of each command used inside of those.

Report bugs to <which-bugs@gnu.org>.
```

    ## Related

    `type`, `command`
