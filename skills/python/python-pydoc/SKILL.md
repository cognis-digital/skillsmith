---
name: python-pydoc
description: "Program with Python's pydoc module: Generate Python documentation in HTML or text for interactive use."
version: 1.0.0
tags: [programming, pydoc, python, stdlib]
---

# Python: `pydoc`

## Overview

Generate Python documentation in HTML or text for interactive use.

At the Python interactive prompt, calling help(thing) on a Python object
documents the object, and calling help() starts up an interactive
help session.

Or, at the shell command line outside of Python:

Run "pydoc <name>" to show documentation on something.  <name> may be
the name of a function, module, package, or a dotted reference to a
class or function within a module or module in a package.  If the
argument contains a path segment delimiter (e.g. slash on Unix,
backslash on Windows) it is treated as the path to a Python source file.

Run "pydoc -k <keyword>" to search for a keyword in the synopsis lines
of all available modules.

Run "pydoc -n <hostname>" to start an HTTP server with the given
hostname (default: localhost) on the local machine.

Run "pydoc -p <port>" to start an HTTP server on the given port on the
local machine.  Port number 0 can be used to get an arbitrary unused port.

Run "pydoc -b" to start an HTTP server on an arbitrary unused port and
open a web browser to interactively browse documentation.  Combine with
the -n and -p options to control the hostname and port used.

Run "pydoc -w <name>" to write out the HTML documentation for a module
to a file named "<name>.html".

Module docs for core modules are assumed to be in

    https://docs.python.org/X.Y/library/

This can be overridden by setting the PYTHONDOCS environment variable
to a different URL or to a local directory containing the Library
Reference Manual pages.

## When to use

Reach for `pydoc` when your task calls for Generate Python documentation in HTML or text for interactive use. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import pydoc
```

## Key functions

- `pydoc.allmethods(cl)`
- `pydoc.apropos(key)`
- `pydoc.browse(port=0, *, open_browser=True, hostname='localhost')`
- `pydoc.classify_class_attrs(object)`
- `pydoc.classname(object, modname)`
- `pydoc.cli()`
- `pydoc.cram(text, maxlen)`
- `pydoc.describe(thing)`
- `pydoc.doc(thing, title='Python Library Documentation: %s', forceload=0, output=None, is_cli=False)`
- `pydoc.format_exception_only(exc, /, value=<implicit>, *, show_group=False, **kwargs)`
- `pydoc.get_pager() -> 'Pager'`
- `pydoc.getdoc(object)`
- `pydoc.getpager() -> 'Pager'`
- `pydoc.help(request=<object object at 0x000001B05F3308E0>)`
- `pydoc.importfile(path)`
- `pydoc.isdata(object)`
- `pydoc.ispackage(path)`
- `pydoc.ispath(x)`
- `pydoc.locate(path, forceload=0)`
- `pydoc.pager(text, title='')`
- `pydoc.parentname(object, modname)`
- `pydoc.pathdirs()`
- `pydoc.pipe_pager(text: 'str', cmd: 'str', title: 'str' = '') -> 'None'`
- `pydoc.pipepager(text: 'str', cmd: 'str', title: 'str' = '') -> 'None'`
- `pydoc.plain(text: 'str') -> 'str'`
- `pydoc.plain_pager(text: 'str', title: 'str' = '') -> 'None'`
- `pydoc.plainpager(text: 'str', title: 'str' = '') -> 'None'`
- `pydoc.render_doc(thing, title='Python Library Documentation: %s', forceload=0, renderer=None)`
- `pydoc.replace(text, *pairs)`
- `pydoc.resolve(thing, forceload=0)`

## Key classes

`Doc`, `ErrorDuringImport`, `Format`, `HTMLDoc`, `HTMLRepr`, `Helper`, `ModuleScanner`, `Repr`, `TextDoc`, `TextRepr`, `deque`

## Constants / attributes

`html`, `plaintext`, `text`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import pydoc

def do_work(...):
    """Use pydoc to accomplish one well-defined task."""
    result = pydoc.allmethods(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `pydoc` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module pydoc

NAME
    pydoc - Generate Python documentation in HTML or text for interactive use.

MODULE REFERENCE
    https://docs.python.org/3.14/library/pydoc.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    At the Python interactive prompt, calling help(thing) on a Python object
    documents the object, and calling help() starts up an interactive
    help session.

    Or, at the shell command line outside of Python:

    Run "pydoc <name>" to show documentation on something.  <name> may be
    the name of a function, module, package, or a dotted reference to a
    class or function within a module or module in a package.  If the
    argument contains a path segment delimiter (e.g. slash on Unix,
    backslash on Windows) it is treated as the path to a Python source file.

    Run "pydoc -k <keyword>" to search for a keyword in the synopsis lines
    of all available modules.

    Run "pydoc -n <hostname>" to start an HTTP server with the given
    hostname (default: localhost) on the local machine.

    Run "pydoc -p <port>" to start an HTTP server on the given port on the
    local machine.  Port number 0 can be used to get an arbitrary unused port.

    Run "pydoc -b" to start an HTTP server on an arbitrary unused port and
    open a web browser to interactively browse documentation.  Combine with
    the -n and -p options to control the hostname and port used.

    Run "pydoc -w <name>" to write out the HTML documentation for a module
    to a file named "<name>.html".

    Module docs for core modules are assumed to be in

        https://docs.python.org/X.Y/library/

    This can be overridden by setting the PYTHONDOCS environment variable
    to a different URL or to a local directory containing the Library
    Reference Manual pages.

DATA
    __all__ = ['help']
    help = <pydoc.Helper instance>

DATE
    26 February 2001

AUTHOR
    Ka-Ping Yee <ping@lfw.org>

CREDITS
    Guido van Rossum, for an excellent programming language.
    Tommy Burnette, the original creator of manpy.
    Paul Prescod, for all his work on onlinehelp.
    Richard Chamberlain, for the first implementation of textdoc.

FILE
    c:\python314\lib\pydoc.py


```

## Related

Other standard-library modules pair well with `pydoc`; explore the `python` domain of this catalog.
