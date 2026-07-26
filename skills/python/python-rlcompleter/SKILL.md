---
name: python-rlcompleter
description: "Program with Python's rlcompleter module: Word completion for GNU readline."
version: 1.0.0
tags: [programming, python, rlcompleter, stdlib]
---

# Python: `rlcompleter`

## Overview

Word completion for GNU readline.

The completer completes keywords, built-ins and globals in a selectable
namespace (which defaults to __main__); when completing NAME.NAME..., it
evaluates (!) the expression up to the last dot and completes its attributes.

It's very cool to do "import sys" type "sys.", hit the completion key (twice),
and see the list of names defined by the sys module!

Tip: to use the tab key as the completion key, call

    readline.parse_and_bind("tab: complete")

Notes:

- Exceptions raised by the completer function are *ignored* (and generally cause
  the completion to fail).  This is a feature -- since readline sets the tty
  device in raw (or cbreak) mode, printing a traceback wouldn't work well
  without some complicated hoopla to save, reset and restore the tty state.

- The evaluation of the NAME.NAME... form may cause arbitrary application
  defined code to be executed if an object with a __getattr__ hook is found.
  Since it is the responsibility of the application (or the user) to enable this
  feature, I consider this an acceptable risk.  More complicated expressions
  (e.g. function calls or indexing operations) are *not* evaluated.

- When the original stdin is not a tty device, GNU readline is never
  used, and this module (and the readline module) are silently inactive.

## When to use

Reach for `rlcompleter` when your task calls for Word completion for GNU readline. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import rlcompleter
```

## Key functions

- `rlcompleter.get_class_members(klass)`

## Key classes

`Completer`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import rlcompleter

def do_work(...):
    """Use rlcompleter to accomplish one well-defined task."""
    result = rlcompleter.get_class_members(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `rlcompleter` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module rlcompleter

NAME
    rlcompleter - Word completion for GNU readline.

MODULE REFERENCE
    https://docs.python.org/3.14/library/rlcompleter.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    The completer completes keywords, built-ins and globals in a selectable
    namespace (which defaults to __main__); when completing NAME.NAME..., it
    evaluates (!) the expression up to the last dot and completes its attributes.

    It's very cool to do "import sys" type "sys.", hit the completion key (twice),
    and see the list of names defined by the sys module!

    Tip: to use the tab key as the completion key, call

        readline.parse_and_bind("tab: complete")

    Notes:

    - Exceptions raised by the completer function are *ignored* (and generally cause
      the completion to fail).  This is a feature -- since readline sets the tty
      device in raw (or cbreak) mode, printing a traceback wouldn't work well
      without some complicated hoopla to save, reset and restore the tty state.

    - The evaluation of the NAME.NAME... form may cause arbitrary application
      defined code to be executed if an object with a __getattr__ hook is found.
      Since it is the responsibility of the application (or the user) to enable this
      feature, I consider this an acceptable risk.  More complicated expressions
      (e.g. function calls or indexing operations) are *not* evaluated.

    - When the original stdin is not a tty device, GNU readline is never
      used, and this module (and the readline module) are silently inactive.

CLASSES
    builtins.object
        Completer

    class Completer(builtins.object)
     |  Completer(namespace=None)
     |
     |  Methods defined here:
     |
     |  __init__(self, namespace=None)
     |      Create a new completer for the command line.
     |
     |      Completer([namespace]) -> completer instance.
     |
     |      If unspecified, the default namespace where completions are performed
     |      is __main__ (technically, __main__.__dict__). Namespaces should be
     |      given as dictionaries.
     |
     |      Completer instances should be used as the completion mechanism of
     |      readline via the set_completer() call:
     |
     |      readline.set_completer(Completer(my_namespace).complete)
     |
     |  attr_matches(self, text)
     |      Compute matches when text contains a dot.
     |
     |      Assuming the text is of the form NAME.NAME....[NAME], and is
     |      evaluable in self.namespace, it will be evaluated and its attributes
     |      (as revealed by dir()) are used as possible completions.  (For class
     |      instances, class members are also considered.)
     |
     |      WARNING: this can still invoke arbitrary C code, if an object
     |      with a __getattr__ hook is evaluated.
     |
     |  complete(self, text, state)
     |      Return the next possible completion for 'text'.
     |
     |      This is called successively with state == 0, 1, 2, ... until it
     |      returns None.  The completion should begin with 'text'.
     |
     |  global_matches(self, text)
     |      Compute matches when text is a simple name.
     |
     |      Return a list of all keywords, built-in functions and names currently
     |      defined in self.namespace that match.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

DATA
    __all__ = ['Completer']

FILE
    c:\python314\lib\rlcompleter.py


```

## Related

Other standard-library modules pair well with `rlcompleter`; explore the `python` domain of this catalog.
