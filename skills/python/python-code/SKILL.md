---
name: python-code
description: "Program with Python's code module: Utilities needed to emulate Python's interactive interpreter."
version: 1.0.0
tags: [code, programming, python, stdlib]
---

# Python: `code`

## Overview

Utilities needed to emulate Python's interactive interpreter.

## When to use

Reach for `code` when your task calls for Utilities needed to emulate Python's interactive interpreter. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import code
```

## Key functions

- `code.compile_command(source, filename='<input>', symbol='single', flags=0)`
- `code.interact(banner=None, readfunc=None, local=None, exitmsg=None, local_exit=False)`

## Key classes

`CommandCompiler`, `InteractiveConsole`, `InteractiveInterpreter`, `Quitter`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import code

def do_work(...):
    """Use code to accomplish one well-defined task."""
    result = code.compile_command(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `code` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module code

NAME
    code - Utilities needed to emulate Python's interactive interpreter.

MODULE REFERENCE
    https://docs.python.org/3.14/library/code.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.object
        InteractiveInterpreter
            InteractiveConsole

    class InteractiveConsole(InteractiveInterpreter)
     |  InteractiveConsole(locals=None, filename='<console>', *, local_exit=False)
     |
     |  Closely emulate the behavior of the interactive Python interpreter.
     |
     |  This class builds on InteractiveInterpreter and adds prompting
     |  using the familiar sys.ps1 and sys.ps2, and input buffering.
     |
     |  Method resolution order:
     |      InteractiveConsole
     |      InteractiveInterpreter
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, locals=None, filename='<console>', *, local_exit=False)
     |      Constructor.
     |
     |      The optional locals argument will be passed to the
     |      InteractiveInterpreter base class.
     |
     |      The optional filename argument should specify the (file)name
     |      of the input stream; it will show up in tracebacks.
     |
     |  interact(self, banner=None, exitmsg=None)
     |      Closely emulate the interactive Python console.
     |
     |      The optional banner argument specifies the banner to print
     |      before the first interaction; by default it prints a banner
     |      similar to the one printed by the real Python interpreter,
     |      followed by the current class name in parentheses (so as not
     |      to confuse this with the real interpreter -- since it's so
     |      close!).
     |
     |      The optional exitmsg argument specifies the exit message
     |      printed when exiting. Pass the empty string to suppress
     |      printing an exit message. If exitmsg is not given or None,
     |      a default message is printed.
     |
     |  push(self, line, filename=None, _symbol='single')
     |      Push a line to the interpreter.
     |
     |      The line should not have a trailing newline; it may have
     |      internal newlines.  The line is appended to a buffer and the
     |      interpreter's runsource() method is called with the
     |      concatenated contents of the buffer as source.  If this
     |      indicates that the command was executed or invalid, the buffer
     |      is reset; otherwise, the command is incomplete, and the buffer
     |      is left as it was after the line was appended.  The return
     |      value is 1 if more input is required, 0 if the line was dealt
     |      with in some way (this is the same as runsource()).
     |
     |  raw_input(self, prompt='')
     |      Write a prompt and read a line.
     |
     |      The returned line does not include the trailing newline.
     |      When the user enters the EOF key sequence, EOFError is raised.
     |
     |      The base implementation uses the built-in function
     |      input(); a subclass may replace this with a different
     |      implementation.
     |
     |  resetbuffer(self)
     |      Reset the input buffer.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from InteractiveInterpreter:
     |
     |  runcode(self, code)
     |      Execute a code object.
     |
     |      When an exception occurs, self.showtraceback() is called to
     |      display a traceback.  All exceptions are caught except
     |      SystemExit, which is reraised.
     |
     |      A note about KeyboardInterrupt: this exception may occur
     |      elsewhere in this code, and may not always be caught.  The
     |      caller should be prepared to deal with it.
     |
     |  runsource(self, source, filename='<input>', symbol='single')
     |      Compile and run some source in the interpreter.
     |
     |      Arguments are as for compile_command().
     |
     |      One of several things can happen:
     |
     |      1) The input is incorrect; compile_command() raised an
     |      exception (SyntaxError or OverflowError).  A syntax traceback
     |      will be printed by calling the showsyntaxerror() method.
     |
     |      2) The input is incomplete, and more input is required;
     |      compile_command() returned None.  Nothing happens.
     |
     |      3) The input is complete; compile_command() returned a code
     |      object.  The code is executed by calling self.runcode() (which
     |      also handles run-time exceptions, except for SystemExit).
     |
     |      The return value is True in case 2, False in the other cases (unless
     |      an exception is raised).  The return value can be used to
     |      decide whether to use sys.ps1 or sys.ps2 to prompt the next
     |      line.
     |
     |  showsyntaxerror(self, filename=None, **kwargs)
     |      Display the syntax error that just occurred.
     |
     |      This doesn't display a stack trace because there isn't one.
     |
     |      If a filename is given, it is stuffed in the exception instead
     |      of what was there before (because Python's parser always uses
     |      "<string>" when reading from a string).
     |
     |      The output is written by self.write(), below.
     |
     |  showtraceback(self)
     |      Display the exception that just occurred.
     |
     |      We remove the first stack item because it is our own code.
     |
     |      The output is written by self.write(), below.
     |
     |  write(self, data)
     |      Write a string.
     |
     |      The base implementation writes to sys.stderr; a s
```

## Related

Other standard-library modules pair well with `code`; explore the `python` domain of this catalog.
