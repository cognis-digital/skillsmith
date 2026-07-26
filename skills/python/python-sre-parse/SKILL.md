---
name: python-sre-parse
description: "Program with Python's sre_parse module: The Python standard-library module `sre_parse`."
version: 1.0.0
tags: [programming, python, sre-parse, stdlib]
---

# Python: `sre_parse`

## Overview

`sre_parse` is part of the Python standard library.

## When to use

Reach for `sre_parse` when your task calls for The Python standard-library module `sre_parse`. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import sre_parse
```

## Key functions

- `sre_parse.fix_flags(src, flags)`
- `sre_parse.parse(str, flags=0, state=None)`
- `sre_parse.parse_template(source, pattern)`

## Key classes

`PatternError`, `State`, `SubPattern`, `Tokenizer`, `error`

## Constants / attributes

`ANY`, `ANY_ALL`, `ASCIILETTERS`, `ASSERT`, `ASSERT_NOT`, `AT`, `ATCODES`, `ATOMIC_GROUP`, `AT_BEGINNING`, `AT_BEGINNING_LINE`, `AT_BEGINNING_STRING`, `AT_BOUNDARY`, `AT_END`, `AT_END_LINE`, `AT_END_STRING`, `AT_LOCALE`, `AT_LOC_BOUNDARY`, `AT_LOC_NON_BOUNDARY`, `AT_MULTILINE`, `AT_NON_BOUNDARY`, `AT_UNICODE`, `AT_UNI_BOUNDARY`, `AT_UNI_NON_BOUNDARY`, `BIGCHARSET`, `BRANCH`, `CATEGORIES`, `CATEGORY`, `CATEGORY_DIGIT`, `CATEGORY_LINEBREAK`, `CATEGORY_LOC_NOT_WORD`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import sre_parse

def do_work(...):
    """Use sre_parse to accomplish one well-defined task."""
    result = sre_parse.fix_flags(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `sre_parse` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module sre_parse

NAME
    sre_parse

MODULE REFERENCE
    https://docs.python.org/3.14/library/sre_parse.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DATA
    ANY = ANY
    ANY_ALL = ANY_ALL
    ASCIILETTERS = frozenset({'A', 'B', 'C', 'D', 'E', 'F', ...})
    ASSERT = ASSERT
    ASSERT_NOT = ASSERT_NOT
    AT = AT
    ATCODES = [AT_BEGINNING, AT_BEGINNING_LINE, AT_BEGINNING_STRING, AT_BO...
    ATOMIC_GROUP = ATOMIC_GROUP
    AT_BEGINNING = AT_BEGINNING
    AT_BEGINNING_LINE = AT_BEGINNING_LINE
    AT_BEGINNING_STRING = AT_BEGINNING_STRING
    AT_BOUNDARY = AT_BOUNDARY
    AT_END = AT_END
    AT_END_LINE = AT_END_LINE
    AT_END_STRING = AT_END_STRING
    AT_LOCALE = {AT_BOUNDARY: AT_LOC_BOUNDARY, AT_NON_BOUNDARY: AT_LOC_NON...
    AT_LOC_BOUNDARY = AT_LOC_BOUNDARY
    AT_LOC_NON_BOUNDARY = AT_LOC_NON_BOUNDARY
    AT_MULTILINE = {AT_BEGINNING: AT_BEGINNING_LINE, AT_END: AT_END_LINE}
    AT_NON_BOUNDARY = AT_NON_BOUNDARY
    AT_UNICODE = {AT_BOUNDARY: AT_UNI_BOUNDARY, AT_NON_BOUNDARY: AT_UNI_NO...
    AT_UNI_BOUNDARY = AT_UNI_BOUNDARY
    AT_UNI_NON_BOUNDARY = AT_UNI_NON_BOUNDARY
    BIGCHARSET = BIGCHARSET
    BRANCH = BRANCH
    CATEGORIES = {r'\A': (AT, AT_BEGINNING_STRING), r'\B': (AT, AT_NON_BOU...
    CATEGORY = CATEGORY
    CATEGORY_DIGIT = CATEGORY_DIGIT
    CATEGORY_LINEBREAK = CATEGORY_LINEBREAK
    CATEGORY_LOC_NOT_WORD = CATEGORY_LOC_NOT_WORD
    CATEGORY_LOC_WORD = CATEGORY_LOC_WORD
    CATEGORY_NOT_DIGIT = CATEGORY_NOT_DIGIT
    CATEGORY_NOT_LINEBREAK = CATEGORY_NOT_LINEBREAK
    CATEGORY_NOT_SPACE = CATEGORY_NOT_SPACE
    CATEGORY_NOT_WORD = CATEGORY_NOT_WORD
    CATEGORY_SPACE = CATEGORY_SPACE
    CATEGORY_UNI_DIGIT = CATEGORY_UNI_DIGIT
    CATEGORY_UNI_LINEBREAK = CATEGORY_UNI_LINEBREAK
    CATEGORY_UNI_NOT_DIGIT = CATEGORY_UNI_NOT_DIGIT
    CATEGORY_UNI_NOT_LINEBREAK = CATEGORY_UNI_NOT_LINEBREAK
    CATEGORY_UNI_NOT_SPACE = CATEGORY_UNI_NOT_SPACE
    CATEGORY_UNI_NOT_WORD = CATEGORY_UNI_NOT_WORD
    CATEGORY_UNI_SPACE = CATEGORY_UNI_SPACE
    CATEGORY_UNI_WORD = CATEGORY_UNI_WORD
    CATEGORY_WORD = CATEGORY_WORD
    CHARSET = CHARSET
    CHCODES = [CATEGORY_DIGIT, CATEGORY_NOT_DIGIT, CATEGORY_SPACE, CATEGOR...
    CH_LOCALE = {CATEGORY_DIGIT: CATEGORY_DIGIT, CATEGORY_NOT_DIGIT: CATEG...
    CH_NEGATE = {CATEGORY_DIGIT: CATEGORY_NOT_DIGIT, CATEGORY_NOT_DIGIT: C...
    CH_UNICODE = {CATEGORY_DIGIT: CATEGORY_UNI_DIGIT, CATEGORY_NOT_DIGIT: ...
    DIGITS = frozenset({'0', '1', '2', '3', '4', '5', ...})
    ESCAPES = {r'\\': (LITERAL, 92), r'\a': (LITERAL, 7), r'\b': (LITERAL,...
    FAILURE = FAILURE
    FLAGS = {'L': 4, 'a': 256, 'i': 2, 'm': 8, 's': 16, 'u': 32, 'x': 64}
    GLOBAL_FLAGS = 128
    GROUPREF = GROUPREF
    GROUPREF_EXISTS = GROUPREF_EXISTS
    GROUPREF_IGNORE = GROUPREF_IGNORE
    GROUPREF_LOC_IGNORE = GROUPREF_LOC_IGNORE
    GROUPREF_UNI_IGNORE = GROUPREF_UNI_IGNORE
    HEXDIGITS = frozenset({'0', '1', '2', '3', '4', '5', ...})
    IN = IN
    INFO = INFO
    IN_IGNORE = IN_IGNORE
    IN_LOC_IGNORE = IN_LOC_IGNORE
    IN_UNI_IGNORE = IN_UNI_IGNORE
    JUMP = JUMP
    LITERAL = LITERAL
    LITERAL_IGNORE = LITERAL_IGNORE
    LITERAL_LOC_IGNORE = LITERAL_LOC_IGNORE
    LITERAL_UNI_IGNORE = LITERAL_UNI_IGNORE
    MAGIC = 20230612
    MARK = MARK
    MAXGROUPS = 1073741823
    MAXREPEAT = MAXREPEAT
    MAXWIDTH = 18446744073709551616
    MAX_REPEAT = MAX_REPEAT
    MAX_UNTIL = MAX_UNTIL
    MIN_REPEAT = MIN_REPEAT
    MIN_REPEAT_ONE = MIN_REPEAT_ONE
    MIN_UNTIL = MIN_UNTIL
    NEGATE = NEGATE
    NOT_LITERAL = NOT_LITERAL
    NOT_LITERAL_IGNORE = NOT_LITERAL_IGNORE
    NOT_LITERAL_LOC_IGNORE = NOT_LITERAL_LOC_IGNORE
    NOT_LITERAL_UNI_IGNORE = NOT_LITERAL_UNI_IGNORE
    OCTDIGITS = frozenset({'0', '1', '2', '3', '4', '5', ...})
    OPCODES = [FAILURE, SUCCESS, ANY, ANY_ALL, ASSERT, ASSERT_NOT, AT, BRA...
    OP_IGNORE = {LITERAL: LITERAL_IGNORE, NOT_LITERAL: NOT_LITERAL_IGNORE}
    OP_LOCALE_IGNORE = {LITERAL: LITERAL_LOC_IGNORE, NOT_LITERAL: NOT_LITE...
    OP_UNICODE_IGNORE = {LITERAL: LITERAL_UNI_IGNORE, NOT_LITERAL: NOT_LIT...
    POSSESSIVE_REPEAT = POSSESSIVE_REPEAT
    POSSESSIVE_REPEAT_ONE = POSSESSIVE_REPEAT_ONE
    RANGE = RANGE
    RANGE_UNI_IGNORE = RANGE_UNI_IGNORE
    REPEAT = REPEAT
    REPEAT_CHARS = '*+?{'
    REPEAT_ONE = REPEAT_ONE
    SPECIAL_CHARS = r'.\[{()*+?^$|'
    SRE_FLAG_ASCII = 256
    SRE_FLAG_DEBUG = 128
    SRE_FLAG_DOTALL = 16
    SRE_FLAG_IGNORECASE = 2
    SRE_FLAG_LOCALE = 4
    SRE_FLAG_MULTILINE = 8
    SRE_FLAG_UNICODE = 32
    SRE_FLAG_VERBOSE = 64
    SRE_INFO_CHARSET = 4
    SRE_INFO_LITERAL = 2
    SRE_INFO_PREFIX = 1
    SUBPATTERN = SUBPATTERN
    SUCCESS = SUCCESS
    TYPE_FLAGS = 292
    WHITESPACE = frozenset({'\t', '\n', '\x0b', '\x0c', '\r', ' '})

FILE
    c:\python314\lib\sre_parse.py


```

## Related

Other standard-library modules pair well with `sre_parse`; explore the `python` domain of this catalog.
