---
name: python-traceback
description: "Program with Python's traceback module: Extract, format and print information about Python stack traces."
version: 1.0.0
tags: [programming, python, stdlib, traceback]
---

# Python: `traceback`

## Overview

Extract, format and print information about Python stack traces.

## When to use

Reach for `traceback` when your task calls for Extract, format and print information about Python stack traces. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import traceback
```

## Key functions

- `traceback.clear_frames(tb)`
- `traceback.extract_stack(f=None, limit=None)`
- `traceback.extract_tb(tb, limit=None)`
- `traceback.format_exc(limit=None, chain=True)`
- `traceback.format_exception(exc, /, value=<implicit>, tb=<implicit>, limit=None, chain=True, **kwargs)`
- `traceback.format_exception_only(exc, /, value=<implicit>, *, show_group=False, **kwargs)`
- `traceback.format_list(extracted_list)`
- `traceback.format_stack(f=None, limit=None)`
- `traceback.format_tb(tb, limit=None)`
- `traceback.print_exc(limit=None, file=None, chain=True)`
- `traceback.print_exception(exc, /, value=<implicit>, tb=<implicit>, limit=None, file=None, chain=True, **kwargs)`
- `traceback.print_last(limit=None, file=None, chain=True)`
- `traceback.print_list(extracted_list, file=None)`
- `traceback.print_stack(f=None, limit=None, file=None)`
- `traceback.print_tb(tb, limit=None, file=None)`
- `traceback.walk_stack(f)`
- `traceback.walk_tb(tb)`

## Key classes

`FrameSummary`, `StackSummary`, `TracebackException`, `suppress`

## Constants / attributes

`BUILTIN_EXCEPTION_LIMIT`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import traceback

def do_work(...):
    """Use traceback to accomplish one well-defined task."""
    result = traceback.clear_frames(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `traceback` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module traceback

NAME
    traceback - Extract, format and print information about Python stack traces.

MODULE REFERENCE
    https://docs.python.org/3.14/library/traceback.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.list(builtins.object)
        StackSummary
    builtins.object
        FrameSummary
        TracebackException

    class FrameSummary(builtins.object)
     |  FrameSummary(
     |      filename,
     |      lineno,
     |      name,
     |      *,
     |      lookup_line=True,
     |      locals=None,
     |      line=None,
     |      end_lineno=None,
     |      colno=None,
     |      end_colno=None,
     |      **kwargs
     |  )
     |
     |  Information about a single frame from a traceback.
     |
     |  - :attr:`filename` The filename for the frame.
     |  - :attr:`lineno` The line within filename for the frame that was
     |    active when the frame was captured.
     |  - :attr:`name` The name of the function or method that was executing
     |    when the frame was captured.
     |  - :attr:`line` The text from the linecache module for the
     |    of code that was running when the frame was captured.
     |  - :attr:`locals` Either None if locals were not supplied, or a dict
     |    mapping the name to the repr() of the variable.
     |
     |  Methods defined here:
     |
     |  __eq__(self, other)
     |      Return self==value.
     |
     |  __getitem__(self, pos)
     |
     |  __init__(
     |      self,
     |      filename,
     |      lineno,
     |      name,
     |      *,
     |      lookup_line=True,
     |      locals=None,
     |      line=None,
     |      end_lineno=None,
     |      colno=None,
     |      end_colno=None,
     |      **kwargs
     |  )
     |      Construct a FrameSummary.
     |
     |      :param lookup_line: If True, `linecache` is consulted for the source
     |          code line. Otherwise, the line will be looked up when first needed.
     |      :param locals: If supplied the frame locals, which will be captured as
     |          object representations.
     |      :param line: If provided, use this instead of looking up the line in
     |          the linecache.
     |
     |  __iter__(self)
     |
     |  __len__(self)
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  line
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  colno
     |
     |  end_colno
     |
     |  end_lineno
     |
     |  filename
     |
     |  lineno
     |
     |  locals
     |
     |  name
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __hash__ = None

    class StackSummary(builtins.list)
     |  StackSummary(iterable=(), /)
     |
     |  A list of FrameSummary objects, representing a stack of frames.
     |
     |  Method resolution order:
     |      StackSummary
     |      builtins.list
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  format(self, **kwargs)
     |      Format the stack ready for printing.
     |
     |      Returns a list of strings ready for printing.  Each string in the
     |      resulting list corresponds to a single frame from the stack.
     |      Each string ends in a newline; the strings may contain internal
     |      newlines as well, for those items with source text lines.
     |
     |      For long sequences of the same frame and line, the first few
     |      repetitions are shown, followed by a summary line stating the exact
     |      number of further repetitions.
     |
     |  format_frame_summary(self, frame_summary, **kwargs)
     |      Format the lines for a single FrameSummary.
     |
     |      Returns a string representing one frame involved in the stack. This
     |      gets called for every frame to be printed in the stack summary.
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  extract(frame_gen, *, limit=None, lookup_lines=True, capture_locals=False)
     |      Create a StackSummary from a traceback or stack object.
     |
     |      :param frame_gen: A generator that yields (frame, lineno) tuples
     |          whose summaries are to be included in the stack.
     |      :param limit: None to include all frames or the number of frames to
     |          include.
     |      :param lookup_lines: If True, lookup lines for each frame immediately,
     |          otherwise lookup is deferred until the frame is rendered.
     |      :param capture_locals: If True, the local variables from each frame will
     |          be captured as object representations into the FrameSummary.
     |
     |  from_list(a_list)
     |      Create a StackSummary object from a supplied list of
     |      FrameSummary objects or old-style list of tuples.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.list:
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __contains__(self, key, /)
     |      Return bool(key in self).
     |
     
```

## Related

Other standard-library modules pair well with `traceback`; explore the `python` domain of this catalog.
