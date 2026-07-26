---
name: python-inspect
description: "Program with Python's inspect module: Get useful information from live Python objects."
version: 1.0.0
tags: [inspect, programming, python, stdlib]
---

# Python: `inspect`

## Overview

Get useful information from live Python objects.

This module encapsulates the interface provided by the internal special
attributes (co_*, im_*, tb_*, etc.) in a friendlier fashion.
It also provides some help for examining source code and class layout.

Here are some of the useful functions provided by this module:

    ismodule(), isclass(), ismethod(), ispackage(), isfunction(),
        isgeneratorfunction(), isgenerator(), istraceback(), isframe(),
        iscode(), isbuiltin(), isroutine() - check object types
    getmembers() - get members of an object that satisfy a given condition

    getfile(), getsourcefile(), getsource() - find an object's source code
    getdoc(), getcomments() - get documentation on an object
    getmodule() - determine the module that an object came from
    getclasstree() - arrange classes so as to represent their hierarchy

    getargvalues(), getcallargs() - get info about function arguments
    getfullargspec() - same, with support for Python 3 features
    formatargvalues() - format an argument spec
    getouterframes(), getinnerframes() - get info about frames
    currentframe() - get the current stack frame
    stack(), trace() - get info about frames on the stack or in a traceback

    signature() - get a Signature object for the callable

## When to use

Reach for `inspect` when your task calls for Get useful information from live Python objects. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import inspect
```

## Key functions

- `inspect.classify_class_attrs(cls)`
- `inspect.cleandoc(doc)`
- `inspect.currentframe()`
- `inspect.findsource(object)`
- `inspect.formatannotation(annotation, base_module=None, *, quote_annotation_strings=True)`
- `inspect.formatannotationrelativeto(object)`
- `inspect.formatargvalues(args, varargs, varkw, locals, formatarg=<class 'str'>, formatvarargs=<function <lambda> at 0x000001B05FFA9220>, formatvarkw=<function <lambda> at 0x000001B05FFA92D0>, formatvalue=<function <lambda> at 0x000001B05FFA9380>)`
- `inspect.get_annotations(obj, *, globals=None, locals=None, eval_str=False, format=<Format.VALUE: 1>)`
- `inspect.getabsfile(object, _filename=None)`
- `inspect.getargs(co)`
- `inspect.getargvalues(frame)`
- `inspect.getasyncgenlocals(agen)`
- `inspect.getasyncgenstate(agen)`
- `inspect.getattr_static(obj, attr, default=<object object at 0x000001B05F330850>)`
- `inspect.getblock(lines)`
- `inspect.getcallargs(func, /, *positional, **named)`
- `inspect.getclasstree(classes, unique=False)`
- `inspect.getclosurevars(func)`
- `inspect.getcomments(object)`
- `inspect.getcoroutinelocals(coroutine)`
- `inspect.getcoroutinestate(coroutine)`
- `inspect.getdoc(object)`
- `inspect.getfile(object)`
- `inspect.getframeinfo(frame, context=1)`
- `inspect.getfullargspec(func)`
- `inspect.getgeneratorlocals(generator)`
- `inspect.getgeneratorstate(generator)`
- `inspect.getinnerframes(tb, context=1)`
- `inspect.getlineno(frame)`
- `inspect.getmembers(object, predicate=None)`

## Key classes

`ArgInfo`, `Arguments`, `Attribute`, `BlockFinder`, `BoundArguments`, `BufferFlags`, `ClassFoundException`, `ClosureVars`, `EndOfBlock`, `Format`, `ForwardRef`, `FrameInfo`, `FullArgSpec`, `OrderedDict`, `Parameter`, `Signature`, `Traceback`, `attrgetter`, `make_weakref`

## Constants / attributes

`AGEN_CLOSED`, `AGEN_CREATED`, `AGEN_RUNNING`, `AGEN_SUSPENDED`, `CORO_CLOSED`, `CORO_CREATED`, `CORO_RUNNING`, `CORO_SUSPENDED`, `CO_ASYNC_GENERATOR`, `CO_COROUTINE`, `CO_GENERATOR`, `CO_HAS_DOCSTRING`, `CO_ITERABLE_COROUTINE`, `CO_METHOD`, `CO_NESTED`, `CO_NEWLOCALS`, `CO_NOFREE`, `CO_OPTIMIZED`, `CO_VARARGS`, `CO_VARKEYWORDS`, `GEN_CLOSED`, `GEN_CREATED`, `GEN_RUNNING`, `GEN_SUSPENDED`, `TPFLAGS_IS_ABSTRACT`, `modulesbyfile`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import inspect

def do_work(...):
    """Use inspect to accomplish one well-defined task."""
    result = inspect.classify_class_attrs(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `inspect` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module inspect

NAME
    inspect - Get useful information from live Python objects.

MODULE REFERENCE
    https://docs.python.org/3.14/library/inspect.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module encapsulates the interface provided by the internal special
    attributes (co_*, im_*, tb_*, etc.) in a friendlier fashion.
    It also provides some help for examining source code and class layout.

    Here are some of the useful functions provided by this module:

        ismodule(), isclass(), ismethod(), ispackage(), isfunction(),
            isgeneratorfunction(), isgenerator(), istraceback(), isframe(),
            iscode(), isbuiltin(), isroutine() - check object types
        getmembers() - get members of an object that satisfy a given condition

        getfile(), getsourcefile(), getsource() - find an object's source code
        getdoc(), getcomments() - get documentation on an object
        getmodule() - determine the module that an object came from
        getclasstree() - arrange classes so as to represent their hierarchy

        getargvalues(), getcallargs() - get info about function arguments
        getfullargspec() - same, with support for Python 3 features
        formatargvalues() - format an argument spec
        getouterframes(), getinnerframes() - get info about frames
        currentframe() - get the current stack frame
        stack(), trace() - get info about frames on the stack or in a traceback

        signature() - get a Signature object for the callable

CLASSES
    builtins.Exception(builtins.BaseException)
        ClassFoundException
        EndOfBlock
    builtins.object
        BlockFinder
        BoundArguments
        Parameter
        Signature
    builtins.tuple(builtins.object)
        ArgInfo
        Arguments
        Attribute
        ClosureVars
        FullArgSpec
    enum.IntFlag(builtins.int, enum.ReprEnum, enum.Flag)
        BufferFlags
    _FrameInfo(builtins.tuple)
        FrameInfo
    _Traceback(builtins.tuple)
        Traceback

    class ArgInfo(builtins.tuple)
     |  ArgInfo(args, varargs, keywords, locals)
     |
     |  ArgInfo(args, varargs, keywords, locals)
     |
     |  Method resolution order:
     |      ArgInfo
     |      builtins.tuple
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __getnewargs__(self) from collections.ArgInfo
     |      Return self as a plain tuple.  Used by copy and pickle.
     |
     |  __replace__ = _replace(self, /, **kwds)
     |
     |  __repr__(self) from collections.ArgInfo
     |      Return a nicely formatted representation string
     |
     |  _asdict(self) from collections.ArgInfo
     |      Return a new dict which maps field names to their values.
     |
     |  _replace(self, /, **kwds) from collections.ArgInfo
     |      Return a new ArgInfo object replacing specified fields with new values
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  _make(iterable) from collections.ArgInfo
     |      Make a new ArgInfo object from a sequence or iterable
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(_cls, args, varargs, keywords, locals) from namedtuple_ArgInfo.ArgInfo
     |      Create new instance of ArgInfo(args, varargs, keywords, locals)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  args
     |      Alias for field number 0
     |
     |  varargs
     |      Alias for field number 1
     |
     |  keywords
     |      Alias for field number 2
     |
     |  locals
     |      Alias for field number 3
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __match_args__ = ('args', 'varargs', 'keywords', 'locals')
     |
     |  _field_defaults = {}
     |
     |  _fields = ('args', 'varargs', 'keywords', 'locals')
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __contains__(self, key, /)
     |      Return bool(key in self).
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getitem__(self, key, /)
     |      Return self[key].
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __len__(self, /)
     |      Return len(self).
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __mul__(self, value, /)
     |      Return self*value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __rmul__(self, value, /)
     |      Return value*self.
     |
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |
     |      Raises ValueError if the value is not present.
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from builtins.tuple:
     |
     |  __class_getitem__(object, /)
     |      See PEP 
```

## Related

Other standard-library modules pair well with `inspect`; explore the `python` domain of this catalog.
