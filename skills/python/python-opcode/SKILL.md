---
name: python-opcode
description: "Program with Python's opcode module: opcode module - potentially shared between dis and other modules which operate on bytecodes (e.g."
version: 1.0.0
tags: [opcode, programming, python, stdlib]
---

# Python: `opcode`

## Overview

opcode module - potentially shared between dis and other modules which
operate on bytecodes (e.g. peephole optimizers).

## When to use

Reach for `opcode` when your task calls for opcode module - potentially shared between dis and other modules which operate on bytecodes (e.g. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import opcode
```

## Key functions

- `opcode.stack_effect(opcode, oparg=None, /, *, jump=None)`

## Constants / attributes

`EXTENDED_ARG`, `HAVE_ARGUMENT`, `MIN_INSTRUMENTED_OPCODE`, `cmp_op`, `hasarg`, `hascompare`, `hasconst`, `hasexc`, `hasfree`, `hasjabs`, `hasjrel`, `hasjump`, `haslocal`, `hasname`, `i`, `m`, `op`, `opmap`, `opname`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import opcode

def do_work(...):
    """Use opcode to accomplish one well-defined task."""
    result = opcode.stack_effect(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `opcode` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module opcode

NAME
    opcode

MODULE REFERENCE
    https://docs.python.org/3.14/library/opcode.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    opcode module - potentially shared between dis and other modules which
    operate on bytecodes (e.g. peephole optimizers).

FUNCTIONS
    stack_effect(opcode, oparg=None, /, *, jump=None)
        Compute the stack effect of the opcode.

DATA
    EXTENDED_ARG = 69
    HAVE_ARGUMENT = 43
    __all__ = ['cmp_op', 'stack_effect', 'hascompare', 'opname', 'opmap', ...
    cmp_op = ('<', '<=', '==', '!=', '>', '>=')
    hasarg = [128, 255, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56...
    hascompare = [56]
    hasconst = [82]
    hasexc = [263, 264, 265]
    hasfree = [62, 90, 97, 111]
    hasjabs = []
    hasjrel = [68, 70, 75, 76, 77, 100, 101, 102, 103, 106, 237, 248, 257,...
    hasjump = [68, 70, 75, 76, 77, 100, 101, 102, 103, 106, 237, 248, 257,...
    haslocal = [63, 83, 84, 85, 86, 87, 88, 89, 112, 113, 114, 261, 266]
    hasname = [61, 64, 65, 72, 73, 80, 91, 92, 93, 96, 110, 115, 116, 249]
    opmap = {'ANNOTATIONS_PLACEHOLDER': 256, 'BINARY_OP': 44, 'BINARY_SLIC...
    opname = ['CACHE', 'BINARY_SLICE', 'BUILD_TEMPLATE', 'BINARY_OP_INPLAC...

FILE
    c:\python314\lib\opcode.py


```

## Related

Other standard-library modules pair well with `opcode`; explore the `python` domain of this catalog.
