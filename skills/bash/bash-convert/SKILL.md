---
name: bash-convert
description: "Program the convert command: ImageMagick: convert and manipulate images from the command line."
version: 1.0.0
tags: [bash, cli, command-line, images, media]
---

    # Command: `convert`

    ## Overview

    ImageMagick: convert and manipulate images from the command line.

    ## When to use

    Use `convert` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
convert in.png -resize 50% out.png
```
```bash
convert *.png doc.pdf
```
```bash
convert img.jpg -quality 80 out.jpg
```

    ## Structuring it in a program

    `convert` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if convert ... ; then
        echo "ok"
    else
        echo "convert failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Reference

`--help` was not capturable on this host; consult `man convert` on a POSIX system.

    ## Related

    `ffmpeg`
