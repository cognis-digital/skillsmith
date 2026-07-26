---
name: python-symtable
description: "Program with Python's symtable module: Interface to the compiler's internal symbol tables"
version: 1.0.0
tags: [programming, python, stdlib, symtable]
---

# Python: `symtable`

## Overview

Interface to the compiler's internal symbol tables

## When to use

Reach for `symtable` when your task calls for Interface to the compiler's internal symbol tables. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import symtable
```

## Key functions

- `symtable.main(args)`
- `symtable.symtable(code, filename, compile_type)`

## Key classes

`Class`, `Function`, `StrEnum`, `Symbol`, `SymbolTable`, `SymbolTableFactory`, `SymbolTableType`

## Constants / attributes

`CELL`, `DEF_ANNOT`, `DEF_BOUND`, `DEF_COMP_CELL`, `DEF_COMP_ITER`, `DEF_FREE_CLASS`, `DEF_GLOBAL`, `DEF_IMPORT`, `DEF_LOCAL`, `DEF_NONLOCAL`, `DEF_PARAM`, `DEF_TYPE_PARAM`, `FREE`, `GLOBAL_EXPLICIT`, `GLOBAL_IMPLICIT`, `LOCAL`, `SCOPE_MASK`, `SCOPE_OFF`, `USE`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import symtable

def do_work(...):
    """Use symtable to accomplish one well-defined task."""
    result = symtable.main(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `symtable` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module symtable

NAME
    symtable - Interface to the compiler's internal symbol tables

MODULE REFERENCE
    https://docs.python.org/3.14/library/symtable.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.object
        Symbol
        SymbolTable
            Class
            Function
    enum.StrEnum(builtins.str, enum.ReprEnum)
        SymbolTableType

    class Class(SymbolTable)
     |  Class(raw_table, filename)
     |
     |  Method resolution order:
     |      Class
     |      SymbolTable
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  get_methods(self)
     |      Return a tuple of methods declared in the class.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from SymbolTable:
     |
     |  __init__(self, raw_table, filename)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  get_children(self)
     |      Return a list of the nested symbol tables.
     |
     |  get_id(self)
     |      Return an identifier for the table.
     |
     |  get_identifiers(self)
     |      Return a view object containing the names of symbols in the table.
     |
     |  get_lineno(self)
     |      Return the number of the first line in the
     |      block for the table.
     |
     |  get_name(self)
     |      Return the table's name.
     |
     |      This corresponds to the name of the class, function
     |      or 'top' if the table is for a class, function or
     |      global respectively.
     |
     |  get_symbols(self)
     |      Return a list of *Symbol* instances for
     |      names in the table.
     |
     |  get_type(self)
     |      Return the type of the symbol table.
     |
     |      The value returned is one of the values in
     |      the ``SymbolTableType`` enumeration.
     |
     |  has_children(self)
     |      Return *True* if the block has nested namespaces.
     |
     |  is_nested(self)
     |      Return *True* if the block is a nested class
     |      or function.
     |
     |  is_optimized(self)
     |      Return *True* if the locals in the table
     |      are optimizable.
     |
     |  lookup(self, name)
     |      Lookup a *name* in the table.
     |
     |      Returns a *Symbol* instance.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from SymbolTable:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class Function(SymbolTable)
     |  Function(raw_table, filename)
     |
     |  Method resolution order:
     |      Function
     |      SymbolTable
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  get_frees(self)
     |      Return a tuple of free variables in the function.
     |
     |  get_globals(self)
     |      Return a tuple of globals in the function.
     |
     |  get_locals(self)
     |      Return a tuple of locals in the function.
     |
     |  get_nonlocals(self)
     |      Return a tuple of nonlocals in the function.
     |
     |  get_parameters(self)
     |      Return a tuple of parameters to the function.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from SymbolTable:
     |
     |  __init__(self, raw_table, filename)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  get_children(self)
     |      Return a list of the nested symbol tables.
     |
     |  get_id(self)
     |      Return an identifier for the table.
     |
     |  get_identifiers(self)
     |      Return a view object containing the names of symbols in the table.
     |
     |  get_lineno(self)
     |      Return the number of the first line in the
     |      block for the table.
     |
     |  get_name(self)
     |      Return the table's name.
     |
     |      This corresponds to the name of the class, function
     |      or 'top' if the table is for a class, function or
     |      global respectively.
     |
     |  get_symbols(self)
     |      Return a list of *Symbol* instances for
     |      names in the table.
     |
     |  get_type(self)
     |      Return the type of the symbol table.
     |
     |      The value returned is one of the values in
     |      the ``SymbolTableType`` enumeration.
     |
     |  has_children(self)
     |      Return *True* if the block has nested namespaces.
     |
     |  is_nested(self)
     |      Return *True* if the block is a nested class
     |      or function.
     |
     |  is_optimized(self)
     |      Return *True* if the locals in the table
     |      are optimizable.
     |
     |  lookup(self, name)
     |      Lookup a *name* in the table.
     |
     |      Returns a *Symbol* instance.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from SymbolTable:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class Symbol(builtins.object)
     |  Symbol(name, flags, namespaces=None, *, module_scope=False)
     |
     |  Methods defined here:
     |
     |  __init__(self, name, flags, namespaces=None, *, module_scope=False)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __repr__(self)
     |      Return re
```

## Related

Other standard-library modules pair well with `symtable`; explore the `python` domain of this catalog.
