---
name: python-bdb
description: "Program with Python's bdb module: Debugger basics"
version: 1.0.0
tags: [bdb, programming, python, stdlib]
---

# Python: `bdb`

## Overview

Debugger basics

## When to use

Reach for `bdb` when your task calls for Debugger basics. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import bdb
```

## Key functions

- `bdb.bar(a)`
- `bdb.checkfuncname(b, frame)`
- `bdb.contextmanager(func)`
- `bdb.effective(file, line, frame)`
- `bdb.foo(n)`
- `bdb.set_trace()`
- `bdb.test()`

## Key classes

`Bdb`, `BdbQuit`, `Breakpoint`, `Tdb`

## Constants / attributes

`CO_ASYNC_GENERATOR`, `CO_COROUTINE`, `CO_GENERATOR`, `E`, `GENERATOR_AND_COROUTINE_FLAGS`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import bdb

def do_work(...):
    """Use bdb to accomplish one well-defined task."""
    result = bdb.bar(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `bdb` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module bdb

NAME
    bdb - Debugger basics

MODULE REFERENCE
    https://docs.python.org/3.14/library/bdb.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.Exception(builtins.BaseException)
        BdbQuit
    builtins.object
        Bdb
        Breakpoint

    class Bdb(builtins.object)
     |  Bdb(skip=None, backend='settrace')
     |
     |  Generic Python debugger base class.
     |
     |  This class takes care of details of the trace facility;
     |  a derived class should implement user interaction.
     |  The standard debugger class (pdb.Pdb) is an example.
     |
     |  The optional skip argument must be an iterable of glob-style
     |  module name patterns.  The debugger will not step into frames
     |  that originate in a module that matches one of these patterns.
     |  Whether a frame is considered to originate in a certain module
     |  is determined by the __name__ in the frame globals.
     |
     |  Methods defined here:
     |
     |  __init__(self, skip=None, backend='settrace')
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  break_anywhere(self, frame)
     |      Return True if there is any breakpoint in that frame
     |
     |  break_here(self, frame)
     |      Return True if there is an effective breakpoint for this line.
     |
     |      Check for line or function breakpoint and if in effect.
     |      Delete temporary breakpoints if effective() says to.
     |
     |  canonic(self, filename)
     |      Return canonical form of filename.
     |
     |      For real filenames, the canonical form is a case-normalized (on
     |      case insensitive filesystems) absolute path.  'Filenames' with
     |      angle brackets, such as "<stdin>", generated in interactive
     |      mode, are returned unchanged.
     |
     |  clear_all_breaks(self)
     |      Delete all existing breakpoints.
     |
     |      If none were set, return an error message.
     |
     |  clear_all_file_breaks(self, filename)
     |      Delete all breakpoints in filename.
     |
     |      If none were set, return an error message.
     |
     |  clear_bpbynumber(self, arg)
     |      Delete a breakpoint by its index in Breakpoint.bpbynumber.
     |
     |      If arg is invalid, return an error message.
     |
     |  clear_break(self, filename, lineno)
     |      Delete breakpoints for filename:lineno.
     |
     |      If no breakpoints were set, return an error message.
     |
     |  disable_current_event(self)
     |      Disable the current event.
     |
     |  dispatch_call(self, frame, arg)
     |      Invoke user function and return trace function for call event.
     |
     |      If the debugger stops on this function call, invoke
     |      self.user_call(). Raise BdbQuit if self.quitting is set.
     |      Return self.trace_dispatch to continue tracing in this scope.
     |
     |  dispatch_exception(self, frame, arg)
     |      Invoke user function and return trace function for exception event.
     |
     |      If the debugger stops on this exception, invoke
     |      self.user_exception(). Raise BdbQuit if self.quitting is set.
     |      Return self.trace_dispatch to continue tracing in this scope.
     |
     |  dispatch_line(self, frame)
     |      Invoke user function and return trace function for line event.
     |
     |      If the debugger stops on the current line, invoke
     |      self.user_line(). Raise BdbQuit if self.quitting is set.
     |      Return self.trace_dispatch to continue tracing in this scope.
     |
     |  dispatch_opcode(self, frame, arg)
     |      Invoke user function and return trace function for opcode event.
     |      If the debugger stops on the current opcode, invoke
     |      self.user_opcode(). Raise BdbQuit if self.quitting is set.
     |      Return self.trace_dispatch to continue tracing in this scope.
     |
     |      Opcode event will always trigger the user callback. For now the only
     |      opcode event is from an inline set_trace() and we want to stop there
     |      unconditionally.
     |
     |  dispatch_return(self, frame, arg)
     |      Invoke user function and return trace function for return event.
     |
     |      If the debugger stops on this function return, invoke
     |      self.user_return(). Raise BdbQuit if self.quitting is set.
     |      Return self.trace_dispatch to continue tracing in this scope.
     |
     |  do_clear(self, arg)
     |      Remove temporary breakpoint.
     |
     |      Must implement in derived classes or get NotImplementedError.
     |
     |  format_stack_entry(self, frame_lineno, lprefix=': ')
     |      Return a string with information about a stack entry.
     |
     |      The stack entry frame_lineno is a (frame, lineno) tuple.  The
     |      return string contains the canonical filename, the function name
     |      or '<lambda>', the input arguments, the return value, and the
     |      line of code (if it exists).
     |
     |  get_all_breaks(self)
     |      Return all breakpoints that are set.
     |
     |  get_bpbynumber(self, arg)
     |      Return a breakpoint by its index in Breakpoint.bybpnumber.
     |
     |      For invalid arg values or if the breakpoint doesn't exist,
     |      raise a ValueError.
     |
     |  get_break(self, filename, lineno)
     |      Return True if there is a breakpoint for filename:lineno.
     |
     |  get_breaks(self, filename, lineno)
     |      Return all breakpoints for filename:lineno.
     |
     |      If no breakpoints are set, return an empty list.
     |
     |  get_file_breaks(self, filename)
     |      Ret
```

## Related

Other standard-library modules pair well with `bdb`; explore the `python` domain of this catalog.
