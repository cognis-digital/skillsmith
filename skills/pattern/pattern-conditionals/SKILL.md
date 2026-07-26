---
name: pattern-conditionals
description: "Branch on conditions with if/elif/else and the test operators."
version: 1.0.0
tags: [bash, command-structure, pattern, shell]
---

# Pattern: Conditionals (`if`, `[[ ]]`, `case`)

## Overview

Conditionals branch on the exit status of a test. Bash's `[[ ]]` is safer and more
capable than the POSIX `[ ]` command.

## Test operators

```bash
[[ -f path ]]   # file exists and is regular
[[ -d path ]]   # directory exists
[[ -z $s ]]     # string empty      [[ -n $s ]]  non-empty
[[ $a == $b ]]  # string equal      [[ $a != $b ]]
[[ $a =~ ^re ]] # regex match
(( n > 3 ))     # arithmetic comparison
```

## Worked examples

```bash
if [[ -f config.yml ]]; then
    load config.yml
elif [[ -f config.json ]]; then
    load config.json
else
    echo "no config" >&2
    exit 1
fi

case $1 in
    start) run ;;
    stop)  halt ;;
    *)     echo "usage: $0 {start|stop}"; exit 2 ;;
esac
```

## Pitfalls

- Inside `[ ]`, always quote `"$var"` to avoid word-splitting bugs; `[[ ]]` does not
  split, so it is preferred in bash.
- `==` is string comparison; use `(( ))` or `-eq` for numbers.
