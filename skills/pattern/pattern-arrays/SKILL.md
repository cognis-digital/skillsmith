---
name: pattern-arrays
description: "Store and iterate lists safely with bash indexed and associative arrays."
version: 1.0.0
tags: [bash, command-structure, pattern, shell]
---

# Pattern: Arrays

## Overview

Arrays hold multiple values in one variable and, crucially, preserve elements that
contain spaces — unlike space-separated strings.

## Worked examples

```bash
files=(*.txt)                 # glob into an array
files+=("one more.txt")       # append
echo "${#files[@]}"           # count
for f in "${files[@]}"; do    # iterate safely (quoted!)
    echo "$f"
done

declare -A color              # associative array (bash 4+)
color[apple]=red
color[lime]=green
echo "${color[apple]}"
for k in "${!color[@]}"; do echo "$k=${color[$k]}"; done
```

## Pitfalls

- Always expand with `"${arr[@]}"` (quoted, `@`) to keep elements intact. `${arr[*]}`
  joins into one string; unquoted `${arr[@]}` re-splits and globs.
- `${arr[0]}` alone refers to the first element, not the whole array.
