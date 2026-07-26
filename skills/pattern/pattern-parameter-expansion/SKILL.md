---
name: pattern-parameter-expansion
description: "Transform shell variables inline: defaults, slicing, substitution, and case."
version: 1.0.0
tags: [bash, command-structure, pattern, shell]
---

# Pattern: Parameter expansion (`${...}`)

## Overview

Parameter expansion manipulates variable values without spawning external commands
— defaults, substrings, pattern removal, replacement, length, and case changes.

## Cheat sheet

```bash
${var:-default}    # value, or 'default' if unset/empty
${var:=default}    # assign default if unset, then expand
${var:?message}    # error out with message if unset
${#var}            # length
${var#prefix}      ${var##prefix}   # strip shortest/longest prefix
${var%suffix}      ${var%%suffix}   # strip shortest/longest suffix
${var/old/new}     ${var//old/new}  # replace first / all
${var:offset:len}  # substring
${var^^}  ${var,,} # upper / lower (bash)
```

## Worked examples

```bash
name=${1:?usage: script NAME}
base=${file%.*}          # drop extension
ext=${file##*.}          # keep extension
path=${PATH//:/$'\n'}    # colons -> newlines
```

## Why it matters

It is faster and safer than shelling out to `sed`/`basename`/`tr` for simple string
work, and it has no subprocess or quoting surprises.
