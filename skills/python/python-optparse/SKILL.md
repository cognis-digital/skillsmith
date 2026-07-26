---
name: python-optparse
description: "Program with Python's optparse module: A powerful, extensible, and easy-to-use option parser."
version: 1.0.0
tags: [optparse, programming, python, stdlib]
---

# Python: `optparse`

## Overview

A powerful, extensible, and easy-to-use option parser.

By Greg Ward <gward@python.net>

Originally distributed as Optik.

For support, use the optik-users@lists.sourceforge.net mailing list
(http://lists.sourceforge.net/lists/listinfo/optik-users).

Simple usage example:

   from optparse import OptionParser

   parser = OptionParser()
   parser.add_option("-f", "--file", dest="filename",
                     help="write report to FILE", metavar="FILE")
   parser.add_option("-q", "--quiet",
                     action="store_false", dest="verbose", default=True,
                     help="don't print status messages to stdout")

   (options, args) = parser.parse_args()

## When to use

Reach for `optparse` when your task calls for A powerful, extensible, and easy-to-use option parser. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import optparse
```

## Key functions

- `optparse.check_builtin(option, opt, value)`
- `optparse.check_choice(option, opt, value)`
- `optparse.ngettext(msgid1, msgid2, n)`

## Key classes

`AmbiguousOptionError`, `BadOptionError`, `HelpFormatter`, `IndentedHelpFormatter`, `OptParseError`, `Option`, `OptionConflictError`, `OptionContainer`, `OptionError`, `OptionGroup`, `OptionParser`, `OptionValueError`, `TitledHelpFormatter`, `Values`, `make_option`

## Constants / attributes

`NO_DEFAULT`, `SUPPRESS_HELP`, `SUPPRESS_USAGE`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import optparse

def do_work(...):
    """Use optparse to accomplish one well-defined task."""
    result = optparse.check_builtin(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `optparse` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module optparse

NAME
    optparse - A powerful, extensible, and easy-to-use option parser.

MODULE REFERENCE
    https://docs.python.org/3.14/library/optparse.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    By Greg Ward <gward@python.net>

    Originally distributed as Optik.

    For support, use the optik-users@lists.sourceforge.net mailing list
    (http://lists.sourceforge.net/lists/listinfo/optik-users).

    Simple usage example:

       from optparse import OptionParser

       parser = OptionParser()
       parser.add_option("-f", "--file", dest="filename",
                         help="write report to FILE", metavar="FILE")
       parser.add_option("-q", "--quiet",
                         action="store_false", dest="verbose", default=True,
                         help="don't print status messages to stdout")

       (options, args) = parser.parse_args()

CLASSES
    builtins.Exception(builtins.BaseException)
        OptParseError
            BadOptionError
            OptionError
                OptionConflictError
            OptionValueError
    builtins.object
        HelpFormatter
            IndentedHelpFormatter
            TitledHelpFormatter
        Option
        OptionContainer
            OptionGroup
            OptionParser
        Values

    class BadOptionError(OptParseError)
     |  BadOptionError(opt_str)
     |
     |  Raised if an invalid option is seen on the command line.
     |
     |  Method resolution order:
     |      BadOptionError
     |      OptParseError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, opt_str)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __str__(self)
     |      Return str(self).
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from OptParseError:
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |
     |  __new__(*args, **kwargs) class method of builtins.Exception
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __reduce__(self, /)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setstate__(self, state, /)
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

    class HelpFormatter(builtins.object)
     |  HelpFormatter(indent_increment, max_help_position, width, short_first)
     |
     |  Abstract base class for formatting option help.  OptionParser
     |  instances should use one of the HelpFormatter subclasses for
     |  formatting help; by default IndentedHelpFormatter is used.
     |
     |  Instance attributes:
     |    parser : OptionParser
     |      the controlling OptionParser instance
     |    indent_increment : int
     |      the number of columns to indent per nesting level
     |    max_help_position : int
     |      the maximum starting column for option help text
     |    help_position : int
     |      the calculated starting column for option help text;
     |      initially the same as the maximum
     |    width : int
     |      total number of columns for output (pass None to constructor for
     |      this value to be taken from the $COLUMNS environment variable)
     |    level : int
     |      current indentation level
     |    current_indent : int
     |      current indentation level (in columns)
     |    help_width : int
     |      number of columns available for option help text (calculated)
     |    default_tag : str
     |      text to replace with each option's default value, "%default"
     |      by default.  Set to false value to disable default value expansion.
     |    option_strings : { Option : str }
     |      maps Option instances to the snippet of help text explaining
     |      the syntax of that option, e.g. "-h, --help" or
     |      "-fFILE, --file=FILE"
     |    _short_opt_fmt : str
     |      format string controlling how short options with values are
     |      printed in help text.  Must be either "%s%s" ("-fFILE") or
     |      "%s %s" ("-f FILE"), because those are the two syntaxes that
     |      Optik supports.
     |    _long_opt_fmt : str
     |      similar but for long options; must be either "%s %s" ("--file FILE")
     |      or "%s=%s" ("--file=FILE").
     |
     |  Methods defined here:
     |
     |  __init__(self, indent_increment, max_help_position, width, short_first)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  dedent(self)
     |
     |  expand_default(self, option)
     |
     |  format_description(self, description)
     |
     |  format_epilog(self, epilog)
     |
     |  format_heading(self, heading)
     |
     |  format_option(self, option)
     |
     |  format_option_strings(self, option
```

## Related

Other standard-library modules pair well with `optparse`; explore the `python` domain of this catalog.
