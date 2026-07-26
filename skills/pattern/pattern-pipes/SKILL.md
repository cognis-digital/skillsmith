---
name: pattern-pipes
description: "Connect commands with the pipe operator so one program's stdout becomes the next one's stdin."
version: 1.0.0
tags: [bash, command-structure, pattern, shell]
---

# Pattern: Pipes (`|`)

## Overview

A pipe connects the standard output of one command to the standard input of the
next, forming a data-processing assembly line. Each stage does one job; the
pipeline composes them. This is the single most important idea in shell programming.

## When to use

Whenever you can express a task as "produce a stream, then transform it step by
step": search, filter, count, reshape, summarize.

## How it works

```bash
producer | filter | transformer | consumer
```

Every stage runs concurrently; data flows as it is produced. The exit status of the
whole pipeline is the status of the **last** command unless `set -o pipefail` is on.

## Worked examples

```bash
# top 10 most common client IPs in an access log
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head

# count Python files, excluding the virtualenv
find . -name '*.py' -not -path './.venv/*' | wc -l

# extract and de-duplicate all URLs from a document
grep -oE 'https?://[^ ]+' page.html | sort -u
```

## Structuring it in a program

- Keep each stage single-purpose; if a stage grows complex, move it to a function
  or a small script and pipe into that.
- Turn on `set -o pipefail` so a failure in any stage fails the pipeline.
- Prefer streaming tools (`grep`, `awk`, `sed`) over buffering the whole input in
  memory.

## Pitfalls

- Without `pipefail`, `false | true` exits `0` — the first failure is hidden.
- A pipeline runs each stage in a **subshell**; variables set inside a piped
  `while read` loop do not persist after the pipeline. Use process substitution or
  a here-string to avoid the subshell.
