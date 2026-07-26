---
name: python-unittest
description: "Program with Python's unittest module: Python unit testing framework, based on Erich Gamma's JUnit and Kent Beck's Smalltalk testing framework (used with permission)."
version: 1.0.0
tags: [programming, python, stdlib, unittest]
---

# Python: `unittest`

## Overview

Python unit testing framework, based on Erich Gamma's JUnit and Kent Beck's
Smalltalk testing framework (used with permission).

This module contains the core framework classes that form the basis of
specific test cases and suites (TestCase, TestSuite etc.), and also a
text-based utility class for running the tests and reporting the results
 (TextTestRunner).

Simple usage:

    import unittest

    class IntegerArithmeticTestCase(unittest.TestCase):
        def testAdd(self):  # test method names begin with 'test'
            self.assertEqual((1 + 2), 3)
            self.assertEqual(0 + 1, 1)
        def testMultiply(self):
            self.assertEqual((0 * 10), 0)
            self.assertEqual((5 * 8), 40)

    if __name__ == '__main__':
        unittest.main()

Further information is available in the bundled documentation, and from

  http://docs.python.org/library/unittest.html

Copyright (c) 1999-2003 Steve Purcell
Copyright (c) 2003 Python Software Foundation
This module is free software, and you may redistribute it and/or modify
it under the same terms as Python itself, so long as this copyright message
and disclaimer are retained in their original form.

IN NO EVENT SHALL THE AUTHOR BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT,
SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OF
THIS CODE, EVEN IF THE AUTHOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH
DAMAGE.

THE AUTHOR SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE.  THE CODE PROVIDED HEREUNDER IS ON AN "AS IS" BASIS,
AND THERE IS NO OBLIGATION WHATSOEVER TO PROVIDE MAINTENANCE,
SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.

## When to use

Reach for `unittest` when your task calls for Python unit testing framework, based on Erich Gamma's JUnit and Kent Beck's Smalltalk testing framework (used with permi. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import unittest
```

## Key functions

- `unittest.addModuleCleanup(function, /, *args, **kwargs)`
- `unittest.doModuleCleanups()`
- `unittest.enterModuleContext(cm)`
- `unittest.expectedFailure(test_item)`
- `unittest.installHandler()`
- `unittest.registerResult(result)`
- `unittest.removeHandler(method=None)`
- `unittest.removeResult(result)`
- `unittest.skip(reason)`
- `unittest.skipIf(condition, reason)`
- `unittest.skipUnless(condition, reason)`

## Key classes

`BaseTestSuite`, `FunctionTestCase`, `IsolatedAsyncioTestCase`, `SkipTest`, `TestCase`, `TestLoader`, `TestProgram`, `TestResult`, `TestSuite`, `TextTestResult`, `TextTestRunner`, `main`

## Constants / attributes

`defaultTestLoader`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import unittest

def do_work(...):
    """Use unittest to accomplish one well-defined task."""
    result = unittest.addModuleCleanup(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `unittest` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: package unittest

NAME
    unittest

MODULE REFERENCE
    https://docs.python.org/3.14/library/unittest.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Python unit testing framework, based on Erich Gamma's JUnit and Kent Beck's
    Smalltalk testing framework (used with permission).

    This module contains the core framework classes that form the basis of
    specific test cases and suites (TestCase, TestSuite etc.), and also a
    text-based utility class for running the tests and reporting the results
     (TextTestRunner).

    Simple usage:

        import unittest

        class IntegerArithmeticTestCase(unittest.TestCase):
            def testAdd(self):  # test method names begin with 'test'
                self.assertEqual((1 + 2), 3)
                self.assertEqual(0 + 1, 1)
            def testMultiply(self):
                self.assertEqual((0 * 10), 0)
                self.assertEqual((5 * 8), 40)

        if __name__ == '__main__':
            unittest.main()

    Further information is available in the bundled documentation, and from

      http://docs.python.org/library/unittest.html

    Copyright (c) 1999-2003 Steve Purcell
    Copyright (c) 2003 Python Software Foundation
    This module is free software, and you may redistribute it and/or modify
    it under the same terms as Python itself, so long as this copyright message
    and disclaimer are retained in their original form.

    IN NO EVENT SHALL THE AUTHOR BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT,
    SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OF
    THIS CODE, EVEN IF THE AUTHOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH
    DAMAGE.

    THE AUTHOR SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT
    LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
    PARTICULAR PURPOSE.  THE CODE PROVIDED HEREUNDER IS ON AN "AS IS" BASIS,
    AND THERE IS NO OBLIGATION WHATSOEVER TO PROVIDE MAINTENANCE,
    SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.

PACKAGE CONTENTS
    __main__
    _log
    async_case
    case
    loader
    main
    mock
    result
    runner
    signals
    suite
    util

CLASSES
    builtins.Exception(builtins.BaseException)
        unittest.case.SkipTest
    builtins.object
        unittest.case.TestCase
            unittest.async_case.IsolatedAsyncioTestCase
            unittest.case.FunctionTestCase
        unittest.loader.TestLoader
        unittest.main.TestProgram
        unittest.result.TestResult
            unittest.runner.TextTestResult
        unittest.runner.TextTestRunner
    unittest.suite.BaseTestSuite(builtins.object)
        unittest.suite.TestSuite

    class FunctionTestCase(TestCase)
     |  FunctionTestCase(testFunc, setUp=None, tearDown=None, description=None)
     |
     |  A test case that wraps a test function.
     |
     |  This is useful for slipping pre-existing test functions into the
     |  unittest framework. Optionally, set-up and tidy-up functions can be
     |  supplied. As with TestCase, the tidy-up ('tearDown') function will
     |  always be called if the set-up ('setUp') function ran successfully.
     |
     |  Method resolution order:
     |      FunctionTestCase
     |      TestCase
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __eq__(self, other)
     |      Return self==value.
     |
     |  __hash__(self)
     |      Return hash(self).
     |
     |  __init__(self, testFunc, setUp=None, tearDown=None, description=None)
     |      Create an instance of the class that will use the named test
     |      method when executed. Raises a ValueError if the instance does
     |      not have a method with the specified name.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __str__(self)
     |      Return str(self).
     |
     |  id(self)
     |
     |  runTest(self)
     |
     |  setUp(self)
     |      Hook method for setting up the test fixture before exercising it.
     |
     |  shortDescription(self)
     |      Returns a one-line description of the test, or None if no
     |      description has been provided.
     |
     |      The default implementation of this method returns the first line of
     |      the specified test method's docstring.
     |
     |  tearDown(self)
     |      Hook method for deconstructing the test fixture after testing it.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from TestCase:
     |
     |  __call__(self, *args, **kwds)
     |      Call self as a function.
     |
     |  addCleanup(self, function, /, *args, **kwargs)
     |      Add a function, with arguments, to be called when the test is
     |      completed. Functions added are called on a LIFO basis and are
     |      called after tearDown on test failure or success.
     |
     |      Cleanup items are called even if setUp fails (unlike tearDown).
     |
     |  addTypeEqualityFunc(self, typeobj, function)
     |      Add a type specific assertEqual style function to compare a type.
     |
     |      This method is for use by TestCase subclasses that need to register
     |      their own type equality functions to provide nicer error messages.
     |
     |      Args:
     |          typeobj: The data type to call this function on when both values
     |                  are of the same type in assertEqual().
     |          function: The callable taking two arguments and an optional
     |                  msg= argument that raises self.failureException with a
     |                  useful error message when the two arguments are not equal.
     |

```

## Related

Other standard-library modules pair well with `unittest`; explore the `python` domain of this catalog.
