---
name: python-sys
description: "Program with Python's sys module: This module provides access to some objects used or maintained by the interpreter and to functions that interact strongly with the interpreter."
version: 1.0.0
tags: [programming, python, stdlib, sys]
---

# Python: `sys`

## Overview

This module provides access to some objects used or maintained by the
interpreter and to functions that interact strongly with the interpreter.

Dynamic objects:

argv -- command line arguments; argv[0] is the script pathname if known
path -- module search path; path[0] is the script directory, else ''
modules -- dictionary of loaded modules

displayhook -- called to show results in an interactive session
excepthook -- called to handle any uncaught exception other than SystemExit
  To customize printing in an interactive session or to install a custom
  top-level exception handler, assign other functions to replace these.

stdin -- standard input file object; used by input()
stdout -- standard output file object; used by print()
stderr -- standard error object; used for error messages
  By assigning other file objects (or objects that behave like files)
  to these, it is possible to redirect all of the interpreter's I/O.

last_exc - the last uncaught exception
  Only available in an interactive session after a
  traceback has been printed.
last_type -- type of last uncaught exception
last_value -- value of last uncaught exception
last_traceback -- traceback of last uncaught exception
  These three are the (deprecated) legacy representation of last_exc.

Static objects:

builtin_module_names -- tuple of module names built into this interpreter
copyright -- copyright notice pertaining to this interpreter
exec_prefix -- prefix used to find the machine-specific Python library
executable -- absolute path of the executable binary of the Python interpreter
float_info -- a named tuple with information about the float implementation.
float_repr_style -- string indicating the style of repr() output for floats
hash_info -- a named tuple with information about the hash algorithm.
hexversion -- version information encoded as a single integer
implementation -- Python implementation information.
int_info -- a named tuple with information about the int implementation.
maxsize -- the largest supported length of containers.
maxunicode -- the value of the largest Unicode code point
platform -- platform identifier
prefix -- prefix used to find the Python library
thread_info -- a named tuple with information about the thread implementation.
version -- the version of this interpreter as a string
version_info -- version information as a named tuple
dllhandle -- [Windows only] integer handle of the Python DLL
winver -- [Windows only] version number of the Python DLL
_enablelegacywindowsfsencoding -- [Windows only]
__stdin__ -- the original stdin; don't touch!
__stdout__ -- the original stdout; don't touch!
__stderr__ -- the original stderr; don't touch!
__displayhook__ -- the original displayhook; don't touch!
__excepthook__ -- the original excepthook; don't touch!

Functions:

displayhook() -- print an object to the screen, and save it in builtins._
excepthook() -- print an exception and its traceback to sys.stderr
exception() -- return the current thread's active exception
exc_info() -- return information about the current thread's active exception
exit() -- exit the interpreter by raising SystemExit
getdlopenflags() -- returns flags to be used for dlopen() calls
getprofile() -- get the global profiling function
getrefcount() -- return the reference count for an object (plus one :-)
getrecursionlimit() -- return the max recursion depth for the interpreter
getsizeof() -- return the size of an object in bytes
gettrace() -- get the global debug tracing function
setdlopenflags() -- set the flags to be used for dlopen() calls
setprofile() -- set the global profiling function
setrecursionlimit() -- set the max recursion depth for the interpreter
settrace() -- set the global debug tracing function

## When to use

Reach for `sys` when your task calls for This module provides access to some objects used or maintained by the interpreter and to functions that interact strongl. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import sys
```

## Key functions

- `sys.activate_stack_trampoline(backend, /)`
- `sys.addaudithook(hook)`
- `sys.audit(event, /, *args)`
- `sys.breakpointhook(*args, **kwargs)`
- `sys.call_tracing(func, args, /)`
- `sys.deactivate_stack_trampoline()`
- `sys.displayhook(object, /)`
- `sys.exc_info()`
- `sys.excepthook(exctype, value, traceback, /)`
- `sys.exception()`
- `sys.exit(status=None, /)`
- `sys.get_asyncgen_hooks()`
- `sys.get_coroutine_origin_tracking_depth()`
- `sys.get_int_max_str_digits()`
- `sys.getallocatedblocks()`
- `sys.getdefaultencoding()`
- `sys.getfilesystemencodeerrors()`
- `sys.getfilesystemencoding()`
- `sys.getprofile()`
- `sys.getrecursionlimit()`
- `sys.getrefcount(object, /)`
- `sys.getsizeof(...)`
- `sys.getswitchinterval()`
- `sys.gettrace()`
- `sys.getunicodeinternedsize(*, _only_immortal=False)`
- `sys.getwindowsversion()`
- `sys.intern(string, /)`
- `sys.is_finalizing()`
- `sys.is_remote_debug_enabled()`
- `sys.is_stack_trampoline_active()`

## Constants / attributes

`api_version`, `argv`, `base_exec_prefix`, `base_prefix`, `builtin_module_names`, `byteorder`, `copyright`, `dllhandle`, `dont_write_bytecode`, `exec_prefix`, `executable`, `flags`, `float_info`, `float_repr_style`, `hash_info`, `hexversion`, `implementation`, `int_info`, `maxsize`, `maxunicode`, `meta_path`, `modules`, `orig_argv`, `path`, `path_hooks`, `path_importer_cache`, `platform`, `platlibdir`, `prefix`, `pycache_prefix`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import sys

def do_work(...):
    """Use sys to accomplish one well-defined task."""
    result = sys.activate_stack_trampoline(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `sys` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: built-in module sys

NAME
    sys

MODULE REFERENCE
    https://docs.python.org/3.14/library/sys.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides access to some objects used or maintained by the
    interpreter and to functions that interact strongly with the interpreter.

    Dynamic objects:

    argv -- command line arguments; argv[0] is the script pathname if known
    path -- module search path; path[0] is the script directory, else ''
    modules -- dictionary of loaded modules

    displayhook -- called to show results in an interactive session
    excepthook -- called to handle any uncaught exception other than SystemExit
      To customize printing in an interactive session or to install a custom
      top-level exception handler, assign other functions to replace these.

    stdin -- standard input file object; used by input()
    stdout -- standard output file object; used by print()
    stderr -- standard error object; used for error messages
      By assigning other file objects (or objects that behave like files)
      to these, it is possible to redirect all of the interpreter's I/O.

    last_exc - the last uncaught exception
      Only available in an interactive session after a
      traceback has been printed.
    last_type -- type of last uncaught exception
    last_value -- value of last uncaught exception
    last_traceback -- traceback of last uncaught exception
      These three are the (deprecated) legacy representation of last_exc.

    Static objects:

    builtin_module_names -- tuple of module names built into this interpreter
    copyright -- copyright notice pertaining to this interpreter
    exec_prefix -- prefix used to find the machine-specific Python library
    executable -- absolute path of the executable binary of the Python interpreter
    float_info -- a named tuple with information about the float implementation.
    float_repr_style -- string indicating the style of repr() output for floats
    hash_info -- a named tuple with information about the hash algorithm.
    hexversion -- version information encoded as a single integer
    implementation -- Python implementation information.
    int_info -- a named tuple with information about the int implementation.
    maxsize -- the largest supported length of containers.
    maxunicode -- the value of the largest Unicode code point
    platform -- platform identifier
    prefix -- prefix used to find the Python library
    thread_info -- a named tuple with information about the thread implementation.
    version -- the version of this interpreter as a string
    version_info -- version information as a named tuple
    dllhandle -- [Windows only] integer handle of the Python DLL
    winver -- [Windows only] version number of the Python DLL
    _enablelegacywindowsfsencoding -- [Windows only]
    __stdin__ -- the original stdin; don't touch!
    __stdout__ -- the original stdout; don't touch!
    __stderr__ -- the original stderr; don't touch!
    __displayhook__ -- the original displayhook; don't touch!
    __excepthook__ -- the original excepthook; don't touch!

    Functions:

    displayhook() -- print an object to the screen, and save it in builtins._
    excepthook() -- print an exception and its traceback to sys.stderr
    exception() -- return the current thread's active exception
    exc_info() -- return information about the current thread's active exception
    exit() -- exit the interpreter by raising SystemExit
    getdlopenflags() -- returns flags to be used for dlopen() calls
    getprofile() -- get the global profiling function
    getrefcount() -- return the reference count for an object (plus one :-)
    getrecursionlimit() -- return the max recursion depth for the interpreter
    getsizeof() -- return the size of an object in bytes
    gettrace() -- get the global debug tracing function
    setdlopenflags() -- set the flags to be used for dlopen() calls
    setprofile() -- set the global profiling function
    setrecursionlimit() -- set the max recursion depth for the interpreter
    settrace() -- set the global debug tracing function

SUBMODULES
    _jit
    monitoring

FUNCTIONS
    __breakpointhook__ = breakpointhook(*args, **kwargs)
        This hook function is called by built-in breakpoint().

    __displayhook__ = displayhook(object, /)
        Print an object to sys.stdout and also save it in builtins._

    __excepthook__ = excepthook(exctype, value, traceback, /)
        Handle an exception by displaying it with a traceback on sys.stderr.

    __unraisablehook__ = unraisablehook(unraisable, /)
        Handle an unraisable exception.

        The unraisable argument has the following attributes:

        * exc_type: Exception type.
        * exc_value: Exception value, can be None.
        * exc_traceback: Exception traceback, can be None.
        * err_msg: Error message, can be None.
        * object: Object causing the exception, can be None.

    activate_stack_trampoline(backend, /)
        Activate stack profiler trampoline *backend*.

    addaudithook(hook)
        Adds a new audit hook callback.

    audit(event, /, *args)
        Passes the event to any audit hooks that are attached.

    breakpointhook(*args, **kwargs)
        This hook function is called by built-in breakpoint().

    call_tracing(func, args, /)
        Call func(*args), while tracing is enabled.

        The tracing state is saved, and restored afterwards.  This is intended
        to be called from a debugger from a checkpoint, to recursively debug
        some other code.

    deactivate_stack_trampoline()
        Deactivate the current stack profiler tram
```

## Related

Other standard-library modules pair well with `sys`; explore the `python` domain of this catalog.
