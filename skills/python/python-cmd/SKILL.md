---
name: python-cmd
description: "Program with Python's cmd module: A generic class to build line-oriented command interpreters."
version: 1.0.0
tags: [cmd, programming, python, stdlib]
---

# Python: `cmd`

## Overview

A generic class to build line-oriented command interpreters.

Interpreters constructed with this class obey the following conventions:

1. End of file on input is processed as the command 'EOF'.
2. A command is parsed out of each line by collecting the prefix composed
   of characters in the identchars member.
3. A command 'foo' is dispatched to a method 'do_foo()'; the do_ method
   is passed a single argument consisting of the remainder of the line.
4. Typing an empty line repeats the last command.  (Actually, it calls the
   method 'emptyline', which may be overridden in a subclass.)
5. There is a predefined 'help' method.  Given an argument 'topic', it
   calls the command 'help_topic'.  With no arguments, it lists all topics
   with defined help_ functions, broken into up to three topics; documented
   commands, miscellaneous help topics, and undocumented commands.
6. The command '?' is a synonym for 'help'.  The command '!' is a synonym
   for 'shell', if a do_shell method exists.
7. If completion is enabled, completing commands will be done automatically,
   and completing of commands args is done by calling complete_foo() with
   arguments text, line, begidx, endidx.  text is string we are matching
   against, all returned matches must begin with it.  line is the current
   input line (lstripped), begidx and endidx are the beginning and end
   indexes of the text being matched, which could be used to provide
   different completion depending upon which position the argument is in.

The 'default' method may be overridden to intercept commands for which there
is no do_ method.

The 'completedefault' method may be overridden to intercept completions for
commands that have no complete_ method.

The data member 'self.ruler' sets the character used to draw separator lines
in the help messages.  If empty, no ruler line is drawn.  It defaults to "=".

If the value of 'self.intro' is nonempty when the cmdloop method is called,
it is printed out on interpreter startup.  This value may be overridden
via an optional argument to the cmdloop() method.

The data members 'self.doc_header', 'self.misc_header', and
'self.undoc_header' set the headers used for the help function's
listings of documented functions, miscellaneous topics, and undocumented
functions respectively.

## When to use

Reach for `cmd` when your task calls for A generic class to build line-oriented command interpreters. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import cmd
```

## Key classes

`Cmd`

## Constants / attributes

`IDENTCHARS`, `PROMPT`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import cmd

def do_work(...):
    """Use cmd to accomplish one well-defined task."""
    result = cmd.Cmd(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `cmd` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module cmd

NAME
    cmd - A generic class to build line-oriented command interpreters.

MODULE REFERENCE
    https://docs.python.org/3.14/library/cmd.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Interpreters constructed with this class obey the following conventions:

    1. End of file on input is processed as the command 'EOF'.
    2. A command is parsed out of each line by collecting the prefix composed
       of characters in the identchars member.
    3. A command 'foo' is dispatched to a method 'do_foo()'; the do_ method
       is passed a single argument consisting of the remainder of the line.
    4. Typing an empty line repeats the last command.  (Actually, it calls the
       method 'emptyline', which may be overridden in a subclass.)
    5. There is a predefined 'help' method.  Given an argument 'topic', it
       calls the command 'help_topic'.  With no arguments, it lists all topics
       with defined help_ functions, broken into up to three topics; documented
       commands, miscellaneous help topics, and undocumented commands.
    6. The command '?' is a synonym for 'help'.  The command '!' is a synonym
       for 'shell', if a do_shell method exists.
    7. If completion is enabled, completing commands will be done automatically,
       and completing of commands args is done by calling complete_foo() with
       arguments text, line, begidx, endidx.  text is string we are matching
       against, all returned matches must begin with it.  line is the current
       input line (lstripped), begidx and endidx are the beginning and end
       indexes of the text being matched, which could be used to provide
       different completion depending upon which position the argument is in.

    The 'default' method may be overridden to intercept commands for which there
    is no do_ method.

    The 'completedefault' method may be overridden to intercept completions for
    commands that have no complete_ method.

    The data member 'self.ruler' sets the character used to draw separator lines
    in the help messages.  If empty, no ruler line is drawn.  It defaults to "=".

    If the value of 'self.intro' is nonempty when the cmdloop method is called,
    it is printed out on interpreter startup.  This value may be overridden
    via an optional argument to the cmdloop() method.

    The data members 'self.doc_header', 'self.misc_header', and
    'self.undoc_header' set the headers used for the help function's
    listings of documented functions, miscellaneous topics, and undocumented
    functions respectively.

CLASSES
    builtins.object
        Cmd

    class Cmd(builtins.object)
     |  Cmd(completekey='tab', stdin=None, stdout=None)
     |
     |  A simple framework for writing line-oriented command interpreters.
     |
     |  These are often useful for test harnesses, administrative tools, and
     |  prototypes that will later be wrapped in a more sophisticated interface.
     |
     |  A Cmd instance or subclass instance is a line-oriented interpreter
     |  framework.  There is no good reason to instantiate Cmd itself; rather,
     |  it's useful as a superclass of an interpreter class you define yourself
     |  in order to inherit Cmd's methods and encapsulate action methods.
     |
     |  Methods defined here:
     |
     |  __init__(self, completekey='tab', stdin=None, stdout=None)
     |      Instantiate a line-oriented interpreter framework.
     |
     |      The optional argument 'completekey' is the readline name of a
     |      completion key; it defaults to the Tab key. If completekey is
     |      not None and the readline module is available, command completion
     |      is done automatically. The optional arguments stdin and stdout
     |      specify alternate input and output file objects; if not specified,
     |      sys.stdin and sys.stdout are used.
     |
     |  cmdloop(self, intro=None)
     |      Repeatedly issue a prompt, accept input, parse an initial prefix
     |      off the received input, and dispatch to action methods, passing them
     |      the remainder of the line as argument.
     |
     |  columnize(self, list, displaywidth=80)
     |      Display a list of strings as a compact set of columns.
     |
     |      Each column is only as wide as necessary.
     |      Columns are separated by two spaces (one was not legible enough).
     |
     |  complete(self, text, state)
     |      Return the next possible completion for 'text'.
     |
     |      If a command has not been entered, then complete against command list.
     |      Otherwise try to call complete_<command> to get list of completions.
     |
     |  complete_help(self, *args)
     |
     |  completedefault(self, *ignored)
     |      Method called to complete an input line when no command-specific
     |      complete_*() method is available.
     |
     |      By default, it returns an empty list.
     |
     |  completenames(self, text, *ignored)
     |
     |  default(self, line)
     |      Called on an input line when the command prefix is not recognized.
     |
     |      If this method is not overridden, it prints an error message and
     |      returns.
     |
     |  do_help(self, arg)
     |      List available commands with "help" or detailed help with "help cmd".
     |
     |  emptyline(self)
     |      Called when an empty line is entered in response to the prompt.
     |
     |      If this method is not overridden, it repeats the last nonempty
     |      command entered.
     |
     |  get_names(self)
     |
     |  onecmd(self, line)
     |      Interpret the argument as though it had been typed in response
     
```

## Related

Other standard-library modules pair well with `cmd`; explore the `python` domain of this catalog.
