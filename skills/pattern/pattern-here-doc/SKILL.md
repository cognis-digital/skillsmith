---
name: pattern-here-doc
description: "Feed a multi-line block of text to a command's stdin with a heredoc."
version: 1.0.0
tags: [bash, command-structure, pattern, shell]
---

# Pattern: Here-documents (`<<EOF`)

## Overview

A heredoc streams a literal block of text into a command's stdin until a delimiter
line. Perfect for embedding config, SQL, or scripts inline.

## Worked examples

```bash
cat > config.yml <<'EOF'
name: app
port: 8080
EOF

mysql db <<SQL
SELECT count(*) FROM users;
SQL

ssh host bash <<'EOF'
uptime
df -h
EOF
```

## Structuring it in a program

- Quote the delimiter (`<<'EOF'`) to keep the body **literal** — no `$var` or
  backtick expansion. Unquote it to allow expansion.
- `<<-EOF` strips leading tabs so you can indent the heredoc with the code.

## Pitfalls

- The closing delimiter must be on its own line with no trailing spaces (and, for
  `<<-`, may be indented only with tabs).
