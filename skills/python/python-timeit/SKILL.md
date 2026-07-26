---
name: python-timeit
description: "Program with Python's timeit module: Tool for measuring execution time of small code snippets."
version: 1.0.0
tags: [programming, python, stdlib, timeit]
---

# Python: `timeit`

## Overview

Tool for measuring execution time of small code snippets.

This module avoids a number of common traps for measuring execution
times.  See also Tim Peters' introduction to the Algorithms chapter in
the Python Cookbook, published by O'Reilly.

Library usage: see the Timer class.

Command line usage:
    python timeit.py [-n N] [-r N] [-s S] [-p] [-h] [--] [statement]

Options:
  -n/--number N: how many times to execute 'statement' (default: see below)
  -r/--repeat N: how many times to repeat the timer (default 5)
  -s/--setup S: statement to be executed once initially (default 'pass').
                Execution time of this setup statement is NOT timed.
  -p/--process: use time.process_time() (default is time.perf_counter())
  -v/--verbose: print raw timing results; repeat for more digits precision
  -u/--unit: set the output time unit (nsec, usec, msec, or sec)
  -h/--help: print this usage message and exit
  --: separate options from statement, use when statement starts with -
  statement: statement to be timed (default 'pass')

A multi-line statement may be given by specifying each line as a
separate argument; indented lines are possible by enclosing an
argument in quotes and using leading spaces.  Multiple -s options are
treated similarly.

If -n is not given, a suitable number of loops is calculated by trying
increasing numbers from the sequence 1, 2, 5, 10, 20, 50, ... until the
total time is at least 0.2 seconds.

Note: there is a certain baseline overhead associated with executing a
pass statement.  It differs between versions.  The code here doesn't try
to hide it, but you should be aware of it.  The baseline overhead can be
measured by invoking the program without arguments.

Classes:

    Timer

Functions:

    timeit(string, string) -> float
    repeat(string, string) -> list
    default_timer() -> float

## When to use

Reach for `timeit` when your task calls for Tool for measuring execution time of small code snippets. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import timeit
```

## Key functions

- `timeit.default_timer()`
- `timeit.main(args=None, *, _wrap_timer=None)`
- `timeit.reindent(src, indent)`
- `timeit.repeat(stmt='pass', setup='pass', timer=<built-in function perf_counter>, repeat=5, number=1000000, globals=None)`
- `timeit.timeit(stmt='pass', setup='pass', timer=<built-in function perf_counter>, number=1000000, globals=None)`

## Key classes

`Timer`

## Constants / attributes

`default_number`, `default_repeat`, `dummy_src_name`, `template`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import timeit

def do_work(...):
    """Use timeit to accomplish one well-defined task."""
    result = timeit.default_timer(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `timeit` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module timeit

NAME
    timeit - Tool for measuring execution time of small code snippets.

MODULE REFERENCE
    https://docs.python.org/3.14/library/timeit.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module avoids a number of common traps for measuring execution
    times.  See also Tim Peters' introduction to the Algorithms chapter in
    the Python Cookbook, published by O'Reilly.

    Library usage: see the Timer class.

    Command line usage:
        python timeit.py [-n N] [-r N] [-s S] [-p] [-h] [--] [statement]

    Options:
      -n/--number N: how many times to execute 'statement' (default: see below)
      -r/--repeat N: how many times to repeat the timer (default 5)
      -s/--setup S: statement to be executed once initially (default 'pass').
                    Execution time of this setup statement is NOT timed.
      -p/--process: use time.process_time() (default is time.perf_counter())
      -v/--verbose: print raw timing results; repeat for more digits precision
      -u/--unit: set the output time unit (nsec, usec, msec, or sec)
      -h/--help: print this usage message and exit
      --: separate options from statement, use when statement starts with -
      statement: statement to be timed (default 'pass')

    A multi-line statement may be given by specifying each line as a
    separate argument; indented lines are possible by enclosing an
    argument in quotes and using leading spaces.  Multiple -s options are
    treated similarly.

    If -n is not given, a suitable number of loops is calculated by trying
    increasing numbers from the sequence 1, 2, 5, 10, 20, 50, ... until the
    total time is at least 0.2 seconds.

    Note: there is a certain baseline overhead associated with executing a
    pass statement.  It differs between versions.  The code here doesn't try
    to hide it, but you should be aware of it.  The baseline overhead can be
    measured by invoking the program without arguments.

    Classes:

        Timer

    Functions:

        timeit(string, string) -> float
        repeat(string, string) -> list
        default_timer() -> float

CLASSES
    builtins.object
        Timer

    class Timer(builtins.object)
     |  Timer(
     |      stmt='pass',
     |      setup='pass',
     |      timer=<built-in function perf_counter>,
     |      globals=None
     |  )
     |
     |  Class for timing execution speed of small code snippets.
     |
     |  The constructor takes a statement to be timed, an additional
     |  statement used for setup, and a timer function.  Both statements
     |  default to 'pass'; the timer function is platform-dependent (see
     |  module doc string).  If 'globals' is specified, the code will be
     |  executed within that namespace (as opposed to inside timeit's
     |  namespace).
     |
     |  To measure the execution time of the first statement, use the
     |  timeit() method.  The repeat() method is a convenience to call
     |  timeit() multiple times and return a list of results.
     |
     |  The statements may contain newlines, as long as they don't contain
     |  multi-line string literals.
     |
     |  Methods defined here:
     |
     |  __init__(
     |      self,
     |      stmt='pass',
     |      setup='pass',
     |      timer=<built-in function perf_counter>,
     |      globals=None
     |  )
     |      Constructor.  See class doc string.
     |
     |  autorange(self, callback=None)
     |      Return the number of loops and time taken so that total time >= 0.2.
     |
     |      Calls the timeit method with increasing numbers from the sequence
     |      1, 2, 5, 10, 20, 50, ... until the time taken is at least 0.2
     |      second.  Returns (number, time_taken).
     |
     |      If *callback* is given and is not None, it will be called after
     |      each trial with two arguments: ``callback(number, time_taken)``.
     |
     |  print_exc(self, file=None)
     |      Helper to print a traceback from the timed code.
     |
     |      Typical use:
     |
     |          t = Timer(...)       # outside the try/except
     |          try:
     |              t.timeit(...)    # or t.repeat(...)
     |          except:
     |              t.print_exc()
     |
     |      The advantage over the standard traceback is that source lines
     |      in the compiled template will be displayed.
     |
     |      The optional file argument directs where the traceback is
     |      sent; it defaults to sys.stderr.
     |
     |  repeat(self, repeat=5, number=1000000)
     |      Call timeit() a few times.
     |
     |      This is a convenience function that calls the timeit()
     |      repeatedly, returning a list of results.  The first argument
     |      specifies how many times to call timeit(), defaulting to 5;
     |      the second argument specifies the timer argument, defaulting
     |      to one million.
     |
     |      Note: it's tempting to calculate mean and standard deviation
     |      from the result vector and report these.  However, this is not
     |      very useful.  In a typical case, the lowest value gives a
     |      lower bound for how fast your machine can run the given code
     |      snippet; higher values in the result vector are typically not
     |      caused by variability in Python's speed, but by other
     |      processes interfering with your timing accuracy.  So the min()
     |      of the result is probably the only number you should be
     |      interested in.  After that, you should look at the entire
     |      vector and apply common sense rather than statistics.
     |
     |  timeit(self, number=1000000
```

## Related

Other standard-library modules pair well with `timeit`; explore the `python` domain of this catalog.
