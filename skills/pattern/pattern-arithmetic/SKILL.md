---
name: pattern-arithmetic
description: "Do integer math in the shell with (( )) and $(( ))."
version: 1.0.0
tags: [bash, command-structure, pattern, shell]
---

# Pattern: Arithmetic (`(( ))`, `$(( ))`)

## Overview

Bash evaluates integer arithmetic natively — no `expr` subprocess needed. `(( ))`
is a command (for conditions and side effects); `$(( ))` expands to a value.

## Worked examples

```bash
(( count++ ))               # increment
total=$(( a + b * c ))      # expression to value
(( n % 2 == 0 )) && echo even
for (( i = 0; i < 10; i++ )); do echo "$i"; done
hex=$(( 0xff ))             # bases: 0x, 0, 2#1010
```

## Operators

`+ - * / %`, comparison `< <= > >= == !=`, logical `&& || !`, bitwise `& | ^ << >>`,
ternary `a ? b : c`, and assignment forms `+= -= *=`.

## Pitfalls

- Integer only — for decimals use `bc -l` or `awk`.
- Inside `(( ))` you do **not** prefix variables with `$` (write `n`, not `$n`),
  though `$n` also works.
- Division truncates toward zero.
