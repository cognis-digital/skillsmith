---
name: python-pickletools
description: "Program with Python's pickletools module: 'Executable documentation' for the pickle module."
version: 1.0.0
tags: [pickletools, programming, python, stdlib]
---

# Python: `pickletools`

## Overview

"Executable documentation" for the pickle module.

Extensive comments about the pickle protocols and pickle-machine opcodes
can be found here.  Some functions meant for external use:

genops(pickle)
   Generate all the opcodes in a pickle, as (opcode, arg, position) triples.

dis(pickle, out=None, memo=None, indentlevel=4)
   Print a symbolic disassembly of a pickle.

## When to use

Reach for `pickletools` when your task calls for "Executable documentation" for the pickle module. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import pickletools
```

## Key functions

- `pickletools.decode_long(data)`
- `pickletools.dis(pickle, out=None, memo=None, indentlevel=4, annotate=0)`
- `pickletools.genops(pickle)`
- `pickletools.optimize(p)`
- `pickletools.read_bytearray8(f)`
- `pickletools.read_bytes1(f)`
- `pickletools.read_bytes4(f)`
- `pickletools.read_bytes8(f)`
- `pickletools.read_decimalnl_long(f)`
- `pickletools.read_decimalnl_short(f)`
- `pickletools.read_float8(f)`
- `pickletools.read_floatnl(f)`
- `pickletools.read_int4(f)`
- `pickletools.read_long1(f)`
- `pickletools.read_long4(f)`
- `pickletools.read_string1(f)`
- `pickletools.read_string4(f)`
- `pickletools.read_stringnl(f, decode=True, stripquotes=True, *, encoding='latin-1')`
- `pickletools.read_stringnl_noescape(f)`
- `pickletools.read_stringnl_noescape_pair(f)`
- `pickletools.read_uint1(f)`
- `pickletools.read_uint2(f)`
- `pickletools.read_uint4(f)`
- `pickletools.read_uint8(f)`
- `pickletools.read_unicodestring1(f)`
- `pickletools.read_unicodestring4(f)`
- `pickletools.read_unicodestring8(f)`
- `pickletools.read_unicodestringnl(f)`

## Key classes

`ArgumentDescriptor`, `OpcodeInfo`, `StackObject`

## Constants / attributes

`TAKEN_FROM_ARGUMENT1`, `TAKEN_FROM_ARGUMENT4`, `TAKEN_FROM_ARGUMENT4U`, `TAKEN_FROM_ARGUMENT8U`, `UP_TO_NEWLINE`, `anyobject`, `bytearray8`, `bytes1`, `bytes4`, `bytes8`, `bytes_types`, `code2op`, `decimalnl_long`, `decimalnl_short`, `float8`, `floatnl`, `int4`, `long1`, `long4`, `markobject`, `opcodes`, `pybool`, `pybuffer`, `pybytearray`, `pybytes`, `pybytes_or_str`, `pydict`, `pyfloat`, `pyfrozenset`, `pyint`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import pickletools

def do_work(...):
    """Use pickletools to accomplish one well-defined task."""
    result = pickletools.decode_long(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `pickletools` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module pickletools

NAME
    pickletools - "Executable documentation" for the pickle module.

MODULE REFERENCE
    https://docs.python.org/3.14/library/pickletools.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Extensive comments about the pickle protocols and pickle-machine opcodes
    can be found here.  Some functions meant for external use:

    genops(pickle)
       Generate all the opcodes in a pickle, as (opcode, arg, position) triples.

    dis(pickle, out=None, memo=None, indentlevel=4)
       Print a symbolic disassembly of a pickle.

FUNCTIONS
    dis(pickle, out=None, memo=None, indentlevel=4, annotate=0)
        Produce a symbolic disassembly of a pickle.

        'pickle' is a file-like object, or string, containing a (at least one)
        pickle.  The pickle is disassembled from the current position, through
        the first STOP opcode encountered.

        Optional arg 'out' is a file-like object to which the disassembly is
        printed.  It defaults to sys.stdout.

        Optional arg 'memo' is a Python dict, used as the pickle's memo.  It
        may be mutated by dis(), if the pickle contains PUT or BINPUT opcodes.
        Passing the same memo object to another dis() call then allows disassembly
        to proceed across multiple pickles that were all created by the same
        pickler with the same memo.  Ordinarily you don't need to worry about this.

        Optional arg 'indentlevel' is the number of blanks by which to indent
        a new MARK level.  It defaults to 4.

        Optional arg 'annotate' if nonzero instructs dis() to add short
        description of the opcode on each line of disassembled output.
        The value given to 'annotate' must be an integer and is used as a
        hint for the column where annotation should start.  The default
        value is 0, meaning no annotations.

        In addition to printing the disassembly, some sanity checks are made:

        + All embedded opcode arguments "make sense".

        + Explicit and implicit pop operations have enough items on the stack.

        + When an opcode implicitly refers to a markobject, a markobject is
          actually on the stack.

        + A memo entry isn't referenced before it's defined.

        + The markobject isn't stored in the memo.

    genops(pickle)
        Generate all the opcodes in a pickle.

        'pickle' is a file-like object, or string, containing the pickle.

        Each opcode in the pickle is generated, from the current pickle position,
        stopping after a STOP opcode is delivered.  A triple is generated for
        each opcode:

            opcode, arg, pos

        opcode is an OpcodeInfo record, describing the current opcode.

        If the opcode has an argument embedded in the pickle, arg is its decoded
        value, as a Python object.  If the opcode doesn't have an argument, arg
        is None.

        If the pickle has a tell() method, pos was the value of pickle.tell()
        before reading the current opcode.  If the pickle is a bytes object,
        it's wrapped in a BytesIO object, and the latter's tell() result is
        used.  Else (the pickle doesn't have a tell(), and it's not obvious how
        to query its current position) pos is None.

    optimize(p)
        Optimize a pickle string by removing unused PUT opcodes

DATA
    __all__ = ['dis', 'genops', 'optimize']
    __test__ = {'disassembler_memo_test': '\n>>> import pickle\n>>> import...

FILE
    c:\python314\lib\pickletools.py


```

## Related

Other standard-library modules pair well with `pickletools`; explore the `python` domain of this catalog.
