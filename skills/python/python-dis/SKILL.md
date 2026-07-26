---
name: python-dis
description: "Program with Python's dis module: Disassembler of Python byte code into mnemonics."
version: 1.0.0
tags: [dis, programming, python, stdlib]
---

# Python: `dis`

## Overview

Disassembler of Python byte code into mnemonics.

## When to use

Reach for `dis` when your task calls for Disassembler of Python byte code into mnemonics. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import dis
```

## Key functions

- `dis.code_info(x)`
- `dis.dis(x=None, *, file=None, depth=None, show_caches=False, adaptive=False, show_offsets=False, show_positions=False)`
- `dis.disassemble(co, lasti=-1, *, file=None, show_caches=False, adaptive=False, show_offsets=False, show_positions=False)`
- `dis.disco(co, lasti=-1, *, file=None, show_caches=False, adaptive=False, show_offsets=False, show_positions=False)`
- `dis.distb(tb=None, *, file=None, show_caches=False, adaptive=False, show_offsets=False, show_positions=False)`
- `dis.findlabels(code)`
- `dis.findlinestarts(code)`
- `dis.get_executor(code, offset)`
- `dis.get_instructions(x, *, first_line=None, show_caches=None, adaptive=False)`
- `dis.main(args=None)`
- `dis.pretty_flags(flags)`
- `dis.print_instructions(instrs, exception_entries, formatter, lasti=-1)`
- `dis.show_code(co, *, file=None)`
- `dis.stack_effect(opcode, oparg=None, /, *, jump=None)`

## Key classes

`ArgResolver`, `Bytecode`, `Formatter`, `Instruction`, `Positions`

## Constants / attributes

`BINARY_OP`, `CACHE`, `CALL_INTRINSIC_1`, `CALL_INTRINSIC_2`, `COMPILER_FLAG_NAMES`, `CONTAINS_OP`, `CONVERT_VALUE`, `END_ASYNC_FOR`, `ENTER_EXECUTOR`, `EXTENDED_ARG`, `FOR_ITER`, `FUNCTION_ATTR_FLAGS`, `HAVE_ARGUMENT`, `IS_OP`, `JUMP_BACKWARD`, `LOAD_ATTR`, `LOAD_COMMON_CONSTANT`, `LOAD_FAST_BORROW_LOAD_FAST_BORROW`, `LOAD_FAST_LOAD_FAST`, `LOAD_GLOBAL`, `LOAD_SMALL_INT`, `LOAD_SPECIAL`, `LOAD_SUPER_ATTR`, `SEND`, `SET_FUNCTION_ATTRIBUTE`, `STORE_FAST_LOAD_FAST`, `STORE_FAST_STORE_FAST`, `UNKNOWN`, `cmp_op`, `deoptmap`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import dis

def do_work(...):
    """Use dis to accomplish one well-defined task."""
    result = dis.code_info(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `dis` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module dis

NAME
    dis - Disassembler of Python byte code into mnemonics.

MODULE REFERENCE
    https://docs.python.org/3.14/library/dis.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.object
        Bytecode
    _Instruction(builtins.tuple)
        Instruction

    class Bytecode(builtins.object)
     |  Bytecode(
     |      x,
     |      *,
     |      first_line=None,
     |      current_offset=None,
     |      show_caches=False,
     |      adaptive=False,
     |      show_offsets=False,
     |      show_positions=False
     |  )
     |
     |  The bytecode operations of a piece of code
     |
     |  Instantiate this with a function, method, other compiled object, string of
     |  code, or a code object (as returned by compile()).
     |
     |  Iterating over this yields the bytecode operations as Instruction instances.
     |
     |  Methods defined here:
     |
     |  __init__(
     |      self,
     |      x,
     |      *,
     |      first_line=None,
     |      current_offset=None,
     |      show_caches=False,
     |      adaptive=False,
     |      show_offsets=False,
     |      show_positions=False
     |  )
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __iter__(self)
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  dis(self)
     |      Return a formatted view of the bytecode operations.
     |
     |  info(self)
     |      Return formatted information about the code object.
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  from_traceback(tb, *, show_caches=False, adaptive=False)
     |      Construct a Bytecode from the given traceback
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class Instruction(_Instruction)
     |  Instruction(
     |      opname,
     |      opcode,
     |      arg,
     |      argval,
     |      argrepr,
     |      offset,
     |      start_offset,
     |      starts_line,
     |      line_number,
     |      label=None,
     |      positions=None,
     |      cache_info=None
     |  )
     |
     |  Details for a bytecode operation.
     |
     |  Defined fields:
     |    opname - human readable name for operation
     |    opcode - numeric code for operation
     |    arg - numeric argument to operation (if any), otherwise None
     |    argval - resolved arg value (if known), otherwise same as arg
     |    argrepr - human readable description of operation argument
     |    offset - start index of operation within bytecode sequence
     |    start_offset - start index of operation within bytecode sequence including extended args if present;
     |                   otherwise equal to Instruction.offset
     |    starts_line - True if this opcode starts a source line, otherwise False
     |    line_number - source line number associated with this opcode (if any), otherwise None
     |    label - A label if this instruction is a jump target, otherwise None
     |    positions - Optional dis.Positions object holding the span of source code
     |                covered by this instruction
     |    cache_info - information about the format and content of the instruction's cache
     |                   entries (if any)
     |
     |  Method resolution order:
     |      Instruction
     |      _Instruction
     |      builtins.tuple
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __str__(self)
     |      Return str(self).
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  make(
     |      opname,
     |      arg,
     |      argval,
     |      argrepr,
     |      offset,
     |      start_offset,
     |      starts_line,
     |      line_number,
     |      label=None,
     |      positions=None,
     |      cache_info=None
     |  )
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  baseopcode
     |      Numeric code for the base operation if operation is specialized.
     |
     |      Otherwise equal to Instruction.opcode.
     |
     |  baseopname
     |      Human readable name for the base operation if operation is specialized.
     |
     |      Otherwise equal to Instruction.opname.
     |
     |  cache_offset
     |      Start index of the cache entries following the operation.
     |
     |  end_offset
     |      End index of the cache entries following the operation.
     |
     |  is_jump_target
     |      True if other code jumps to here, otherwise False
     |
     |  jump_target
     |      Bytecode index of the jump target if this is a jump operation.
     |
     |      Otherwise return None.
     |
     |  oparg
     |      Alias for Instruction.arg.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from _Instruction:
     |
     |  __getnewargs__(self) from collections._Instruction
     |      Return self as a plain tuple.  Used by copy and pickle.
     |
     |  __replace__ = _replace(self, /, **kwds)
     |
     |  __repr__(self) from collecti
```

## Related

Other standard-library modules pair well with `dis`; explore the `python` domain of this catalog.
