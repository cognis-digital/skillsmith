---
name: python-graphlib
description: "Program with Python's graphlib module: The Python standard-library module `graphlib`."
version: 1.0.0
tags: [graphlib, programming, python, stdlib]
---

# Python: `graphlib`

## Overview

`graphlib` is part of the Python standard library.

## When to use

Reach for `graphlib` when your task calls for The Python standard-library module `graphlib`. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import graphlib
```

## Key classes

`CycleError`, `GenericAlias`, `TopologicalSorter`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import graphlib

def do_work(...):
    """Use graphlib to accomplish one well-defined task."""
    result = graphlib.CycleError(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `graphlib` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module graphlib

NAME
    graphlib

MODULE REFERENCE
    https://docs.python.org/3.14/library/graphlib.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.ValueError(builtins.Exception)
        CycleError
    builtins.object
        TopologicalSorter

    class CycleError(builtins.ValueError)
     |  Subclass of ValueError raised by TopologicalSorter.prepare if cycles
     |  exist in the working graph.
     |
     |  If multiple cycles exist, only one undefined choice among them will be reported
     |  and included in the exception. The detected cycle can be accessed via the second
     |  element in the *args* attribute of the exception instance and consists in a list
     |  of nodes, such that each node is, in the graph, an immediate predecessor of the
     |  next node in the list. In the reported list, the first and the last node will be
     |  the same, to make it clear that it is cyclic.
     |
     |  Method resolution order:
     |      CycleError
     |      builtins.ValueError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors defined here:
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.ValueError:
     |
     |  __new__(*args, **kwargs) class method of builtins.ValueError
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__(self, /)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setstate__(self, state, /)
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  add_note(self, note, /)
     |      Add a note to the exception
     |
     |  with_traceback(self, tb, /)
     |      Set self.__traceback__ to tb and return self.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |
     |  __cause__
     |
     |  __context__
     |
     |  __dict__
     |
     |  __suppress_context__
     |
     |  __traceback__
     |
     |  args

    class TopologicalSorter(builtins.object)
     |  TopologicalSorter(graph=None)
     |
     |  Provides functionality to topologically sort a graph of hashable nodes
     |
     |  Methods defined here:
     |
     |  __bool__(self)
     |
     |  __init__(self, graph=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  add(self, node, *predecessors)
     |      Add a new node and its predecessors to the graph.
     |
     |      Both the *node* and all elements in *predecessors* must be hashable.
     |
     |      If called multiple times with the same node argument, the set of dependencies
     |      will be the union of all dependencies passed in.
     |
     |      It is possible to add a node with no dependencies (*predecessors* is not provided)
     |      as well as provide a dependency twice. If a node that has not been provided before
     |      is included among *predecessors* it will be automatically added to the graph with
     |      no predecessors of its own.
     |
     |      Raises ValueError if called after "prepare".
     |
     |  done(self, *nodes)
     |      Marks a set of nodes returned by "get_ready" as processed.
     |
     |      This method unblocks any successor of each node in *nodes* for being returned
     |      in the future by a call to "get_ready".
     |
     |      Raises ValueError if any node in *nodes* has already been marked as
     |      processed by a previous call to this method, if a node was not added to the
     |      graph by using "add" or if called without calling "prepare" previously or if
     |      node has not yet been returned by "get_ready".
     |
     |  get_ready(self)
     |      Return a tuple of all the nodes that are ready.
     |
     |      Initially it returns all nodes with no predecessors; once those are marked
     |      as processed by calling "done", further calls will return all new nodes that
     |      have all their predecessors already processed. Once no more progress can be made,
     |      empty tuples are returned.
     |
     |      Raises ValueError if called without calling "prepare" previously.
     |
     |  is_active(self)
     |      Return ``True`` if more progress can be made and ``False`` otherwise.
     |
     |      Progress can be made if cycles do not block the resolution and either there
     |      are still nodes ready that haven't yet been returned by "get_ready" or the
     |      number of nodes marked "done" is less than the number that have been returned
     |      by "get_ready".
     |
     |      Raises ValueError if called without calling "prepare" previously.
     |
     |  prepare(self)
     |      Mark the graph as finished and check for cycles in the graph.
     |
     |      If any cycle is detected, "CycleError" will be raised, but "get_ready" can
     |      still be used to obtain as many nodes as possible until cycles block more
     |      progress. After a call to this function, the graph cannot be modified and
     |      therefore no more nodes can be added using "add".
     |
     |      Raise ValueError if nodes have al
```

## Related

Other standard-library modules pair well with `graphlib`; explore the `python` domain of this catalog.
