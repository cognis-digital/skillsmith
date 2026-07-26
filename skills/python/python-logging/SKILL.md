---
name: python-logging
description: "Program with Python's logging module: Logging package for Python."
version: 1.0.0
tags: [logging, programming, python, stdlib]
---

# Python: `logging`

## Overview

Logging package for Python. Based on PEP 282 and comments thereto in
comp.lang.python.

Copyright (C) 2001-2022 Vinay Sajip. All Rights Reserved.

To use, simply 'import logging' and log away!

## When to use

Reach for `logging` when your task calls for Logging package for Python. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import logging
```

## Key functions

- `logging.addLevelName(level, levelName)`
- `logging.basicConfig(**kwargs)`
- `logging.captureWarnings(capture)`
- `logging.critical(msg, *args, **kwargs)`
- `logging.currentframe()`
- `logging.debug(msg, *args, **kwargs)`
- `logging.disable(level=50)`
- `logging.error(msg, *args, **kwargs)`
- `logging.exception(msg, *args, exc_info=True, **kwargs)`
- `logging.fatal(msg, *args, **kwargs)`
- `logging.getHandlerByName(name)`
- `logging.getHandlerNames()`
- `logging.getLevelName(level)`
- `logging.getLevelNamesMapping()`
- `logging.getLogRecordFactory()`
- `logging.getLogger(name=None)`
- `logging.getLoggerClass()`
- `logging.info(msg, *args, **kwargs)`
- `logging.log(level, msg, *args, **kwargs)`
- `logging.makeLogRecord(dict)`
- `logging.setLogRecordFactory(factory)`
- `logging.setLoggerClass(klass)`
- `logging.shutdown(handlerList=[<weakref at 0x000001B060AFC4A0; to 'logging._StderrHandler' at 0x000001B060A612B0>])`
- `logging.warn(msg, *args, **kwargs)`
- `logging.warning(msg, *args, **kwargs)`

## Key classes

`BufferingFormatter`, `FileHandler`, `Filter`, `Filterer`, `Formatter`, `GenericAlias`, `Handler`, `LogRecord`, `Logger`, `LoggerAdapter`, `Manager`, `NullHandler`, `PercentStyle`, `PlaceHolder`, `RootLogger`, `StrFormatStyle`, `StreamHandler`, `StringTemplateStyle`, `Template`

## Constants / attributes

`BASIC_FORMAT`, `CRITICAL`, `DEBUG`, `ERROR`, `FATAL`, `INFO`, `NOTSET`, `WARN`, `WARNING`, `lastResort`, `logAsyncioTasks`, `logMultiprocessing`, `logProcesses`, `logThreads`, `raiseExceptions`, `root`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import logging

def do_work(...):
    """Use logging to accomplish one well-defined task."""
    result = logging.addLevelName(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `logging` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: package logging

NAME
    logging

MODULE REFERENCE
    https://docs.python.org/3.14/library/logging.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Logging package for Python. Based on PEP 282 and comments thereto in
    comp.lang.python.

    Copyright (C) 2001-2022 Vinay Sajip. All Rights Reserved.

    To use, simply 'import logging' and log away!

PACKAGE CONTENTS
    config
    handlers

CLASSES
    builtins.object
        BufferingFormatter
        Filter
        Formatter
        LogRecord
        LoggerAdapter
    Filterer(builtins.object)
        Handler
            NullHandler
            StreamHandler
                FileHandler
        Logger

    class BufferingFormatter(builtins.object)
     |  BufferingFormatter(linefmt=None)
     |
     |  A formatter suitable for formatting a number of records.
     |
     |  Methods defined here:
     |
     |  __init__(self, linefmt=None)
     |      Optionally specify a formatter which will be used to format each
     |      individual record.
     |
     |  format(self, records)
     |      Format the specified records and return the result as a string.
     |
     |  formatFooter(self, records)
     |      Return the footer string for the specified records.
     |
     |  formatHeader(self, records)
     |      Return the header string for the specified records.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class FileHandler(StreamHandler)
     |  FileHandler(filename, mode='a', encoding=None, delay=False, errors=None)
     |
     |  A handler class which writes formatted logging records to disk files.
     |
     |  Method resolution order:
     |      FileHandler
     |      StreamHandler
     |      Handler
     |      Filterer
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, filename, mode='a', encoding=None, delay=False, errors=None)
     |      Open the specified file and use it as the stream for logging.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  close(self)
     |      Closes the stream.
     |
     |  emit(self, record)
     |      Emit a record.
     |
     |      If the stream was not opened because 'delay' was specified in the
     |      constructor, open it before calling the superclass's emit.
     |
     |      If stream is not open, current mode is 'w' and `_closed=True`, record
     |      will not be emitted (see Issue #42378).
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from StreamHandler:
     |
     |  flush(self)
     |      Flushes the stream.
     |
     |  setStream(self, stream)
     |      Sets the StreamHandler's stream to the specified value,
     |      if it is different.
     |
     |      Returns the old stream, if the stream was changed, or None
     |      if it wasn't.
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from StreamHandler:
     |
     |  __class_getitem__ = GenericAlias(args, /)
     |      Represent a PEP 585 generic type
     |
     |      E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from StreamHandler:
     |
     |  terminator = '\n'
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Handler:
     |
     |  acquire(self)
     |      Acquire the I/O thread lock.
     |
     |  createLock(self)
     |      Acquire a thread lock for serializing access to the underlying I/O.
     |
     |  format(self, record)
     |      Format the specified record.
     |
     |      If a formatter is set, use it. Otherwise, use the default formatter
     |      for the module.
     |
     |  get_name(self)
     |
     |  handle(self, record)
     |      Conditionally emit the specified logging record.
     |
     |      Emission depends on filters which may have been added to the handler.
     |      Wrap the actual emission of the record with acquisition/release of
     |      the I/O thread lock.
     |
     |      Returns an instance of the log record that was emitted
     |      if it passed all filters, otherwise a false value is returned.
     |
     |  handleError(self, record)
     |      Handle errors which occur during an emit() call.
     |
     |      This method should be called from handlers when an exception is
     |      encountered during an emit() call. If raiseExceptions is false,
     |      exceptions get silently ignored. This is what is mostly wanted
     |      for a logging system - most users will not care about errors in
     |      the logging system, they are more interested in application errors.
     |      You could, however, replace this with a custom handler if you wish.
     |      The record which was being processed is passed in to this method.
     |
     |  release(self)
     |      Release the I/O thread lock.
     |
     |  setFormatter(self, fmt)
     |      Set the formatter for this handler.
     |
     |  setLevel(self, level)
     |      Set the logging level of this handler.  level must be an int or a str.
     |
     |  set_name(self, name)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Handler:
```

## Related

Other standard-library modules pair well with `logging`; explore the `python` domain of this catalog.
