---
name: python-token
description: "Program with Python's token module: Token constants."
version: 1.0.0
tags: [programming, python, stdlib, token]
---

# Python: `token`

## Overview

Token constants.

## When to use

Reach for `token` when your task calls for Token constants. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import token
```

## Key functions

- `token.ISEOF(x: int) -> bool`
- `token.ISNONTERMINAL(x: int) -> bool`
- `token.ISTERMINAL(x: int) -> bool`

## Constants / attributes

`AMPER`, `AMPEREQUAL`, `AT`, `ATEQUAL`, `CIRCUMFLEX`, `CIRCUMFLEXEQUAL`, `COLON`, `COLONEQUAL`, `COMMA`, `COMMENT`, `DEDENT`, `DOT`, `DOUBLESLASH`, `DOUBLESLASHEQUAL`, `DOUBLESTAR`, `DOUBLESTAREQUAL`, `ELLIPSIS`, `ENCODING`, `ENDMARKER`, `EQEQUAL`, `EQUAL`, `ERRORTOKEN`, `EXACT_TOKEN_TYPES`, `EXCLAMATION`, `FSTRING_END`, `FSTRING_MIDDLE`, `FSTRING_START`, `GREATER`, `GREATEREQUAL`, `INDENT`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import token

def do_work(...):
    """Use token to accomplish one well-defined task."""
    result = token.ISEOF(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `token` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module token

NAME
    token - Token constants.

MODULE REFERENCE
    https://docs.python.org/3.14/library/token.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

FUNCTIONS
    ISEOF(x: int) -> bool

    ISNONTERMINAL(x: int) -> bool

    ISTERMINAL(x: int) -> bool

DATA
    AMPER = 19
    AMPEREQUAL = 41
    AT = 49
    ATEQUAL = 50
    CIRCUMFLEX = 32
    CIRCUMFLEXEQUAL = 43
    COLON = 11
    COLONEQUAL = 53
    COMMA = 12
    COMMENT = 65
    DEDENT = 6
    DOT = 23
    DOUBLESLASH = 47
    DOUBLESLASHEQUAL = 48
    DOUBLESTAR = 35
    DOUBLESTAREQUAL = 46
    ELLIPSIS = 52
    ENCODING = 68
    ENDMARKER = 0
    EQEQUAL = 27
    EQUAL = 22
    ERRORTOKEN = 67
    EXACT_TOKEN_TYPES = {'!': 54, '!=': 28, '%': 24, '%=': 40, '&': 19, '&...
    EXCLAMATION = 54
    FSTRING_END = 61
    FSTRING_MIDDLE = 60
    FSTRING_START = 59
    GREATER = 21
    GREATEREQUAL = 30
    INDENT = 5
    LBRACE = 25
    LEFTSHIFT = 33
    LEFTSHIFTEQUAL = 44
    LESS = 20
    LESSEQUAL = 29
    LPAR = 7
    LSQB = 9
    MINEQUAL = 37
    MINUS = 15
    NAME = 1
    NEWLINE = 4
    NL = 66
    NOTEQUAL = 28
    NT_OFFSET = 256
    NUMBER = 2
    N_TOKENS = 69
    OP = 55
    PERCENT = 24
    PERCENTEQUAL = 40
    PLUS = 14
    PLUSEQUAL = 36
    RARROW = 51
    RBRACE = 26
    RIGHTSHIFT = 34
    RIGHTSHIFTEQUAL = 45
    RPAR = 8
    RSQB = 10
    SEMI = 13
    SLASH = 17
    SLASHEQUAL = 39
    SOFT_KEYWORD = 58
    STAR = 16
    STAREQUAL = 38
    STRING = 3
    TILDE = 31
    TSTRING_END = 64
    TSTRING_MIDDLE = 63
    TSTRING_START = 62
    TYPE_COMMENT = 57
    TYPE_IGNORE = 56
    VBAR = 18
    VBAREQUAL = 42
    __all__ = ['tok_name', 'ISTERMINAL', 'ISNONTERMINAL', 'ISEOF', 'EXACT_...
    tok_name = {0: 'ENDMARKER', 1: 'NAME', 2: 'NUMBER', 3: 'STRING', 4: 'N...

FILE
    c:\python314\lib\token.py


```

## Related

Other standard-library modules pair well with `token`; explore the `python` domain of this catalog.
