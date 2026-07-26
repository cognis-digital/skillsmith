---
name: python-doctest
description: "Program with Python's doctest module: Module doctest -- a framework for running examples in docstrings."
version: 1.0.0
tags: [doctest, programming, python, stdlib]
---

# Python: `doctest`

## Overview

Module doctest -- a framework for running examples in docstrings.

In simplest use, end each module M to be tested with:

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()

Then running the module as a script will cause the examples in the
docstrings to get executed and verified:

python M.py

This won't display anything unless an example fails, in which case the
failing example(s) and the cause(s) of the failure(s) are printed to stdout
(why not stderr? because stderr is a lame hack <0.2 wink>), and the final
line of output is "Test failed.".

Run it with the -v switch instead:

python M.py -v

and a detailed report of all examples tried is printed to stdout, along
with assorted summaries at the end.

You can force verbose mode by passing "verbose=True" to testmod, or prohibit
it by passing "verbose=False".  In either of those cases, sys.argv is not
examined by testmod.

There are a variety of other ways to run doctests, including integration
with the unittest framework, and support for running non-Python text
files containing doctests.  There are also many ways to override parts
of doctest's default behaviors.  See the Library Reference Manual for
details.

## When to use

Reach for `doctest` when your task calls for Module doctest -- a framework for running examples in docstrings. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import doctest
```

## Key functions

- `doctest.DocFileSuite(*paths, **kw)`
- `doctest.DocFileTest(path, module_relative=True, package=None, globs=None, parser=<doctest.DocTestParser object at 0x000001B0627DD810>, encoding=None, **options)`
- `doctest.DocTestSuite(module=None, globs=None, extraglobs=None, test_finder=None, **options)`
- `doctest.can_colorize(...)`
- `doctest.debug(module, name, pm=False)`
- `doctest.debug_script(src, pm=False, globs=None)`
- `doctest.debug_src(src, pm=False, globs=None)`
- `doctest.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)`
- `doctest.register_optionflag(name)`
- `doctest.run_docstring_examples(f, globs, verbose=False, name='NoName', compileflags=None, optionflags=0)`
- `doctest.script_from_examples(s)`
- `doctest.set_unittest_reportflags(flags)`
- `doctest.testfile(filename, module_relative=True, name=None, package=None, globs=None, verbose=None, report=True, optionflags=0, extraglobs=None, raise_on_error=False, parser=<doctest.DocTestParser object at 0x000001B062767ED0>, encoding=None)`
- `doctest.testmod(m=None, name=None, globs=None, verbose=None, report=True, optionflags=0, extraglobs=None, raise_on_error=False, exclude_empty=False)`
- `doctest.testsource(module, name)`

## Key classes

`ANSIColors`, `DebugRunner`, `DocFileCase`, `DocTest`, `DocTestCase`, `DocTestFailure`, `DocTestFinder`, `DocTestParser`, `DocTestRunner`, `Example`, `IncrementalNewlineDecoder`, `OutputChecker`, `SkipDocTestCase`, `StringIO`, `TestResults`, `UnexpectedException`

## Constants / attributes

`BLANKLINE_MARKER`, `COMPARISON_FLAGS`, `DONT_ACCEPT_BLANKLINE`, `DONT_ACCEPT_TRUE_FOR_1`, `ELLIPSIS`, `ELLIPSIS_MARKER`, `FAIL_FAST`, `IGNORE_EXCEPTION_DETAIL`, `NORMALIZE_WHITESPACE`, `OPTIONFLAGS_BY_NAME`, `REPORTING_FLAGS`, `REPORT_CDIFF`, `REPORT_NDIFF`, `REPORT_ONLY_FIRST_FAILURE`, `REPORT_UDIFF`, `SKIP`, `master`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import doctest

def do_work(...):
    """Use doctest to accomplish one well-defined task."""
    result = doctest.DocFileSuite(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `doctest` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module doctest

NAME
    doctest - Module doctest -- a framework for running examples in docstrings.

MODULE REFERENCE
    https://docs.python.org/3.14/library/doctest.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    In simplest use, end each module M to be tested with:

    def _test():
        import doctest
        doctest.testmod()

    if __name__ == "__main__":
        _test()

    Then running the module as a script will cause the examples in the
    docstrings to get executed and verified:

    python M.py

    This won't display anything unless an example fails, in which case the
    failing example(s) and the cause(s) of the failure(s) are printed to stdout
    (why not stderr? because stderr is a lame hack <0.2 wink>), and the final
    line of output is "Test failed.".

    Run it with the -v switch instead:

    python M.py -v

    and a detailed report of all examples tried is printed to stdout, along
    with assorted summaries at the end.

    You can force verbose mode by passing "verbose=True" to testmod, or prohibit
    it by passing "verbose=False".  In either of those cases, sys.argv is not
    examined by testmod.

    There are a variety of other ways to run doctests, including integration
    with the unittest framework, and support for running non-Python text
    files containing doctests.  There are also many ways to override parts
    of doctest's default behaviors.  See the Library Reference Manual for
    details.

CLASSES
    builtins.Exception(builtins.BaseException)
        DocTestFailure
        UnexpectedException
    builtins.object
        DocTest
        DocTestFinder
        DocTestParser
        DocTestRunner
            DebugRunner
        Example
        OutputChecker

    class DebugRunner(DocTestRunner)
     |  DebugRunner(checker=None, verbose=None, optionflags=0)
     |
     |  Run doc tests but raise an exception as soon as there is a failure.
     |
     |  If an unexpected exception occurs, an UnexpectedException is raised.
     |  It contains the test, the example, and the original exception:
     |
     |    >>> runner = DebugRunner(verbose=False)
     |    >>> test = DocTestParser().get_doctest('>>> raise KeyError\n42',
     |    ...                                    {}, 'foo', 'foo.py', 0)
     |    >>> try:
     |    ...     runner.run(test)
     |    ... except UnexpectedException as f:
     |    ...     failure = f
     |
     |    >>> failure.test is test
     |    True
     |
     |    >>> failure.example.want
     |    '42\n'
     |
     |    >>> exc_info = failure.exc_info
     |    >>> raise exc_info[1] # Already has the traceback
     |    Traceback (most recent call last):
     |    ...
     |    KeyError
     |
     |  We wrap the original exception to give the calling application
     |  access to the test and example information.
     |
     |  If the output doesn't match, then a DocTestFailure is raised:
     |
     |    >>> test = DocTestParser().get_doctest('''
     |    ...      >>> x = 1
     |    ...      >>> x
     |    ...      2
     |    ...      ''', {}, 'foo', 'foo.py', 0)
     |
     |    >>> try:
     |    ...    runner.run(test)
     |    ... except DocTestFailure as f:
     |    ...    failure = f
     |
     |  DocTestFailure objects provide access to the test:
     |
     |    >>> failure.test is test
     |    True
     |
     |  As well as to the example:
     |
     |    >>> failure.example.want
     |    '2\n'
     |
     |  and the actual output:
     |
     |    >>> failure.got
     |    '1\n'
     |
     |  If a failure or error occurs, the globals are left intact:
     |
     |    >>> del test.globs['__builtins__']
     |    >>> test.globs
     |    {'x': 1}
     |
     |    >>> test = DocTestParser().get_doctest('''
     |    ...      >>> x = 2
     |    ...      >>> raise KeyError
     |    ...      ''', {}, 'foo', 'foo.py', 0)
     |
     |    >>> runner.run(test)
     |    Traceback (most recent call last):
     |    ...
     |    doctest.UnexpectedException: <DocTest foo from foo.py:0 (2 examples)>
     |
     |    >>> del test.globs['__builtins__']
     |    >>> test.globs
     |    {'x': 2}
     |
     |  But the globals are cleared if there is no error:
     |
     |    >>> test = DocTestParser().get_doctest('''
     |    ...      >>> x = 2
     |    ...      ''', {}, 'foo', 'foo.py', 0)
     |
     |    >>> runner.run(test)
     |    TestResults(failed=0, attempted=1)
     |
     |    >>> test.globs
     |    {}
     |
     |  Method resolution order:
     |      DebugRunner
     |      DocTestRunner
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  report_failure(self, out, test, example, got)
     |      Report that the given example failed.
     |
     |  report_unexpected_exception(self, out, test, example, exc_info)
     |      Report that the given example raised an unexpected exception.
     |
     |  run(self, test, compileflags=None, out=None, clear_globs=True)
     |      Run the examples in `test`, and display the results using the
     |      writer function `out`.
     |
     |      The examples are run in the namespace `test.globs`.  If
     |      `clear_globs` is true (the default), then this namespace will
     |      be cleared after the test runs, to help with garbage
     |      collection.  If you would like to examine the namespace after
     |      the test completes, then use `clear_globs=False`.
     |
     |      `compileflags` gives the set of flags that should be used by
     |      the Python compiler when running the examples.  If not
     |      specified, then it will default to the set of future-import
     |
```

## Related

Other standard-library modules pair well with `doctest`; explore the `python` domain of this catalog.
