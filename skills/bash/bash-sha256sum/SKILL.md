---
name: bash-sha256sum
description: "Program the sha256sum command: Compute and verify SHA-256 checksums — the default for integrity."
version: 1.0.0
tags: [bash, cli, command-line, hash, integrity]
---

    # Command: `sha256sum`

    ## Overview

    Compute and verify SHA-256 checksums — the default for integrity.

    ## When to use

    Use `sha256sum` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
sha256sum file
```
```bash
sha256sum * > SHA256SUMS
```
```bash
sha256sum -c SHA256SUMS
```

    ## Structuring it in a program

    `sha256sum` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if sha256sum ... ; then
        echo "ok"
    else
        echo "sha256sum failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`sha256sum --help` on this machine)

```
Usage: sha256sum [OPTION]... [FILE]...
Print or check SHA256 (256-bit) checksums.

With no FILE, or when FILE is -, read standard input.

  -b, --binary         read in binary mode (default unless reading tty stdin)
  -c, --check          read SHA256 sums from the FILEs and check them
      --tag            create a BSD-style checksum
  -t, --text           read in text mode (default if reading tty stdin)
  -z, --zero           end each output line with NUL, not newline,
                       and disable file name escaping

The following five options are useful only when verifying checksums:
      --ignore-missing  don't fail or report status for missing files
      --quiet          don't print OK for each successfully verified file
      --status         don't output anything, status code shows success
      --strict         exit non-zero for improperly formatted checksum lines
  -w, --warn           warn about improperly formatted checksum lines

      --help     display this help and exit
      --version  output version information and exit

The sums are computed as described in FIPS-180-2.  When checking, the input
should be a former output of this program.  The default mode is to print a
line with checksum, a space, a character indicating input mode ('*' for binary,
' ' for text or where binary is insignificant), and name for each FILE.

Note: There is no difference between binary mode and text mode on GNU systems.

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/sha256sum>
or available locally via: info '(coreutils) sha2 utilities'
```

    ## Related

    `md5sum`, `openssl`
