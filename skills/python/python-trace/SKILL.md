---
name: python-trace
description: "Program with Python's trace module: program/module to trace Python program or function execution Sample use, command line: trace.py -c -f counts --ignore-dir '$prefix' spam.py eggs trace.py -t --ignore-dir '$prefix' spam.py eggs trace.py --trackcalls spam.py eggs Sample use, programmatically import sys  create a Trace object, telling it what to ignore, and whether to  do tracing or line-counting or both."
version: 1.0.0
tags: [programming, python, stdlib, trace]
---

# Python: `trace`

## Overview

program/module to trace Python program or function execution

Sample use, command line:
  trace.py -c -f counts --ignore-dir '$prefix' spam.py eggs
  trace.py -t --ignore-dir '$prefix' spam.py eggs
  trace.py --trackcalls spam.py eggs

Sample use, programmatically
  import sys

  # create a Trace object, telling it what to ignore, and whether to
  # do tracing or line-counting or both.
  tracer = trace.Trace(ignoredirs=[sys.base_prefix, sys.base_exec_prefix,],
                       trace=0, count=1)
  # run the new command using the given tracer
  tracer.run('main()')
  # make a report, placing output in /tmp
  r = tracer.results()
  r.write_results(show_missing=True, coverdir="/tmp")

## When to use

Reach for `trace` when your task calls for program/module to trace Python program or function execution Sample use, command line: trace.py -c -f counts --ignore-di. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import trace
```

## Key functions

- `trace.main()`

## Key classes

`CoverageResults`, `Trace`

## Constants / attributes

`PRAGMA_NOCOVER`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import trace

def do_work(...):
    """Use trace to accomplish one well-defined task."""
    result = trace.main(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `trace` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module trace

NAME
    trace - program/module to trace Python program or function execution

MODULE REFERENCE
    https://docs.python.org/3.14/library/trace.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Sample use, command line:
      trace.py -c -f counts --ignore-dir '$prefix' spam.py eggs
      trace.py -t --ignore-dir '$prefix' spam.py eggs
      trace.py --trackcalls spam.py eggs

    Sample use, programmatically
      import sys

      # create a Trace object, telling it what to ignore, and whether to
      # do tracing or line-counting or both.
      tracer = trace.Trace(ignoredirs=[sys.base_prefix, sys.base_exec_prefix,],
                           trace=0, count=1)
      # run the new command using the given tracer
      tracer.run('main()')
      # make a report, placing output in /tmp
      r = tracer.results()
      r.write_results(show_missing=True, coverdir="/tmp")

CLASSES
    builtins.object
        CoverageResults
        Trace

    class CoverageResults(builtins.object)
     |  CoverageResults(
     |      counts=None,
     |      calledfuncs=None,
     |      infile=None,
     |      callers=None,
     |      outfile=None
     |  )
     |
     |  Methods defined here:
     |
     |  __init__(
     |      self,
     |      counts=None,
     |      calledfuncs=None,
     |      infile=None,
     |      callers=None,
     |      outfile=None
     |  )
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  is_ignored_filename(self, filename)
     |      Return True if the filename does not refer to a file
     |      we want to have reported.
     |
     |  update(self, other)
     |      Merge in the data from another CoverageResults
     |
     |  write_results(
     |      self,
     |      show_missing=True,
     |      summary=False,
     |      coverdir=None,
     |      *,
     |      ignore_missing_files=False
     |  )
     |      Write the coverage results.
     |
     |      :param show_missing: Show lines that had no hits.
     |      :param summary: Include coverage summary per module.
     |      :param coverdir: If None, the results of each module are placed in its
     |                       directory, otherwise it is included in the directory
     |                       specified.
     |      :param ignore_missing_files: If True, counts for files that no longer
     |                       exist are silently ignored. Otherwise, a missing file
     |                       will raise a FileNotFoundError.
     |
     |  write_results_file(self, path, lines, lnotab, lines_hit, encoding=None)
     |      Return a coverage results file in path.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class Trace(builtins.object)
     |  Trace(
     |      count=1,
     |      trace=1,
     |      countfuncs=0,
     |      countcallers=0,
     |      ignoremods=(),
     |      ignoredirs=(),
     |      infile=None,
     |      outfile=None,
     |      timing=False
     |  )
     |
     |  Methods defined here:
     |
     |  __init__(
     |      self,
     |      count=1,
     |      trace=1,
     |      countfuncs=0,
     |      countcallers=0,
     |      ignoremods=(),
     |      ignoredirs=(),
     |      infile=None,
     |      outfile=None,
     |      timing=False
     |  )
     |      @param count true iff it should count number of times each
     |                   line is executed
     |      @param trace true iff it should print out each line that is
     |                   being counted
     |      @param countfuncs true iff it should just output a list of
     |                   (filename, modulename, funcname,) for functions
     |                   that were called at least once;  This overrides
     |                   'count' and 'trace'
     |      @param ignoremods a list of the names of modules to ignore
     |      @param ignoredirs a list of the names of directories to ignore
     |                   all of the (recursive) contents of
     |      @param infile file from which to read stored counts to be
     |                   added into the results
     |      @param outfile file in which to write the results
     |      @param timing true iff timing information be displayed
     |
     |  file_module_function_of(self, frame)
     |
     |  globaltrace_countfuncs(self, frame, why, arg)
     |      Handler for call events.
     |
     |      Adds (filename, modulename, funcname) to the self._calledfuncs dict.
     |
     |  globaltrace_lt(self, frame, why, arg)
     |      Handler for call events.
     |
     |      If the code block being entered is to be ignored, returns 'None',
     |      else returns self.localtrace.
     |
     |  globaltrace_trackcallers(self, frame, why, arg)
     |      Handler for call events.
     |
     |      Adds information about who called who to the self._callers dict.
     |
     |  localtrace_count(self, frame, why, arg)
     |
     |  localtrace_trace(self, frame, why, arg)
     |
     |  localtrace_trace_and_count(self, frame, why, arg)
     |
     |  results(self)
     |
     |  run(self, cmd)
     |
     |  runctx(self, cmd, globals=None, locals=None)
     |
     |  runfunc(self, func, /, *args, **kw)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
 
```

## Related

Other standard-library modules pair well with `trace`; explore the `python` domain of this catalog.
