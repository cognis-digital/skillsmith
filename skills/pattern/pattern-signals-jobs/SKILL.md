---
name: pattern-signals-jobs
description: "Manage background jobs and signals: &, jobs, fg, bg, wait, kill."
version: 1.0.0
tags: [bash, command-structure, pattern, shell]
---

# Pattern: Background jobs and signals

## Overview

The shell can run commands in the background and coordinate them. Signals let you
interrupt, terminate, or notify processes.

## Worked examples

```bash
long_task &                 # start in background
pid=$!                      # remember its PID
jobs -l                     # list jobs
wait "$pid"                 # block until it finishes
echo "task exited $?"

server & sleep 1; kill -TERM $!   # start, use, stop
```

## Common signals

- `TERM` (15) — polite termination (default for `kill`).
- `INT` (2) — Ctrl-C.
- `KILL` (9) — unblockable, last resort (no cleanup runs).
- `HUP` (1) — terminal closed; often used to reload daemons.

## Structuring it in a program

- Capture `$!` right after `&` to track each background job.
- `wait` for all children before exiting so nothing is orphaned.
- Prefer `TERM` and let the process clean up; reserve `KILL` for the unresponsive.
