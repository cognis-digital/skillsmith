---
name: python-shelve
description: "Program with Python's shelve module: Manage shelves of pickled objects."
version: 1.0.0
tags: [programming, python, shelve, stdlib]
---

# Python: `shelve`

## Overview

Manage shelves of pickled objects.

A "shelf" is a persistent, dictionary-like object.  The difference
with dbm databases is that the values (not the keys!) in a shelf can
be essentially arbitrary Python objects -- anything that the "pickle"
module can handle.  This includes most class instances, recursive data
types, and objects containing lots of shared sub-objects.  The keys
are ordinary strings.

To summarize the interface (key is a string, data is an arbitrary
object):

        import shelve
        d = shelve.open(filename) # open, with (g)dbm filename -- no suffix

        d[key] = data   # store data at key (overwrites old data if
                        # using an existing key)
        data = d[key]   # retrieve a COPY of the data at key (raise
                        # KeyError if no such key) -- NOTE that this
                        # access returns a *copy* of the entry!
        del d[key]      # delete data stored at key (raises KeyError
                        # if no such key)
        flag = key in d # true if the key exists
        list = d.keys() # a list of all existing keys (slow!)

        d.close()       # close it

Dependent on the implementation, closing a persistent dictionary may
or may not be necessary to flush changes to disk.

Normally, d[key] returns a COPY of the entry.  This needs care when
mutable entries are mutated: for example, if d[key] is a list,
        d[key].append(anitem)
does NOT modify the entry d[key] itself, as stored in the persistent
mapping -- it only modifies the copy, which is then immediately
discarded, so that the append has NO effect whatsoever.  To append an
item to d[key] in a way that will affect the persistent mapping, use:
        data = d[key]
        data.append(anitem)
        d[key] = data

To avoid the problem with mutable entries, you may pass the keyword
argument writeback=True in the call to shelve.open.  When you use:
        d = shelve.open(filename, writeback=True)
then d keeps a cache of all entries you access, and writes them all back
to the persistent mapping when you call d.close().  This ensures that
such usage as d[key].append(anitem) works as intended.

However, using keyword argument writeback=True may consume vast amount
of memory for the cache, and it may make d.close() very slow, if you
access many of d's entries after opening it in this way: d has no way to
check which of the entries you access are mutable and/or which ones you
actually mutate, so it must cache, and write back at close, all of the
entries that you access.  You can call d.sync() to write back all the
entries in the cache, and empty the cache (d.sync() also synchronizes
the persistent dictionary on disk, if feasible).

## When to use

Reach for `shelve` when your task calls for Manage shelves of pickled objects. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import shelve
```

## Key functions

- `shelve.open(filename, flag='c', protocol=None, writeback=False)`

## Key classes

`BsdDbShelf`, `BytesIO`, `DbfilenameShelf`, `Pickler`, `Shelf`, `Unpickler`

## Constants / attributes

`DEFAULT_PROTOCOL`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import shelve

def do_work(...):
    """Use shelve to accomplish one well-defined task."""
    result = shelve.open(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `shelve` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module shelve

NAME
    shelve - Manage shelves of pickled objects.

MODULE REFERENCE
    https://docs.python.org/3.14/library/shelve.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    A "shelf" is a persistent, dictionary-like object.  The difference
    with dbm databases is that the values (not the keys!) in a shelf can
    be essentially arbitrary Python objects -- anything that the "pickle"
    module can handle.  This includes most class instances, recursive data
    types, and objects containing lots of shared sub-objects.  The keys
    are ordinary strings.

    To summarize the interface (key is a string, data is an arbitrary
    object):

            import shelve
            d = shelve.open(filename) # open, with (g)dbm filename -- no suffix

            d[key] = data   # store data at key (overwrites old data if
                            # using an existing key)
            data = d[key]   # retrieve a COPY of the data at key (raise
                            # KeyError if no such key) -- NOTE that this
                            # access returns a *copy* of the entry!
            del d[key]      # delete data stored at key (raises KeyError
                            # if no such key)
            flag = key in d # true if the key exists
            list = d.keys() # a list of all existing keys (slow!)

            d.close()       # close it

    Dependent on the implementation, closing a persistent dictionary may
    or may not be necessary to flush changes to disk.

    Normally, d[key] returns a COPY of the entry.  This needs care when
    mutable entries are mutated: for example, if d[key] is a list,
            d[key].append(anitem)
    does NOT modify the entry d[key] itself, as stored in the persistent
    mapping -- it only modifies the copy, which is then immediately
    discarded, so that the append has NO effect whatsoever.  To append an
    item to d[key] in a way that will affect the persistent mapping, use:
            data = d[key]
            data.append(anitem)
            d[key] = data

    To avoid the problem with mutable entries, you may pass the keyword
    argument writeback=True in the call to shelve.open.  When you use:
            d = shelve.open(filename, writeback=True)
    then d keeps a cache of all entries you access, and writes them all back
    to the persistent mapping when you call d.close().  This ensures that
    such usage as d[key].append(anitem) works as intended.

    However, using keyword argument writeback=True may consume vast amount
    of memory for the cache, and it may make d.close() very slow, if you
    access many of d's entries after opening it in this way: d has no way to
    check which of the entries you access are mutable and/or which ones you
    actually mutate, so it must cache, and write back at close, all of the
    entries that you access.  You can call d.sync() to write back all the
    entries in the cache, and empty the cache (d.sync() also synchronizes
    the persistent dictionary on disk, if feasible).

CLASSES
    collections.abc.MutableMapping(collections.abc.Mapping)
        Shelf
            BsdDbShelf
            DbfilenameShelf

    class BsdDbShelf(Shelf)
     |  BsdDbShelf(dict, protocol=None, writeback=False, keyencoding='utf-8')
     |
     |  Shelf implementation using the "BSD" db interface.
     |
     |  This adds methods first(), next(), previous(), last() and
     |  set_location() that have no counterpart in [g]dbm databases.
     |
     |  The actual database must be opened using one of the "bsddb"
     |  modules "open" routines (i.e. bsddb.hashopen, bsddb.btopen or
     |  bsddb.rnopen) and passed to the constructor.
     |
     |  See the module's __doc__ string for an overview of the interface.
     |
     |  Method resolution order:
     |      BsdDbShelf
     |      Shelf
     |      collections.abc.MutableMapping
     |      collections.abc.Mapping
     |      collections.abc.Collection
     |      collections.abc.Sized
     |      collections.abc.Iterable
     |      collections.abc.Container
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, dict, protocol=None, writeback=False, keyencoding='utf-8')
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  first(self)
     |
     |  last(self)
     |
     |  next(self)
     |
     |  previous(self)
     |
     |  set_location(self, key)
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __abstractmethods__ = frozenset()
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Shelf:
     |
     |  __contains__(self, key)
     |
     |  __del__(self)
     |
     |  __delitem__(self, key)
     |
     |  __enter__(self)
     |
     |  __exit__(self, type, value, traceback)
     |
     |  __getitem__(self, key)
     |
     |  __iter__(self)
     |
     |  __len__(self)
     |
     |  __setitem__(self, key, value)
     |
     |  close(self)
     |
     |  get(self, key, default=None)
     |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
     |
     |  sync(self)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Shelf:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.M
```

## Related

Other standard-library modules pair well with `shelve`; explore the `python` domain of this catalog.
