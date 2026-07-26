---
name: python-site
description: "Program with Python's site module: Append module search paths for third-party packages to sys.path."
version: 1.0.0
tags: [programming, python, site, stdlib]
---

# Python: `site`

## Overview

Append module search paths for third-party packages to sys.path.

****************************************************************
* This module is automatically imported during initialization. *
****************************************************************

This will append site-specific paths to the module search path.  On
Unix (including Mac OSX), it starts with sys.prefix and
sys.exec_prefix (if different) and appends
lib/python<version>/site-packages.
On other platforms (such as Windows), it tries each of the
prefixes directly, as well as with lib/site-packages appended.  The
resulting directories, if they exist, are appended to sys.path, and
also inspected for path configuration files.

If a file named "pyvenv.cfg" exists one directory above sys.executable,
sys.prefix and sys.exec_prefix are set to that directory and
it is also checked for site-packages (sys.base_prefix and
sys.base_exec_prefix will always be the "real" prefixes of the Python
installation). If "pyvenv.cfg" (a bootstrap configuration file) contains
the key "include-system-site-packages" set to anything other than "false"
(case-insensitive), the system-level prefixes will still also be
searched for site-packages; otherwise they won't.

All of the resulting site-specific directories, if they exist, are
appended to sys.path, and also inspected for path configuration
files.

A path configuration file is a file whose name has the form
<package>.pth; its contents are additional directories (one per line)
to be added to sys.path.  Non-existing directories (or
non-directories) are never added to sys.path; no directory is added to
sys.path more than once.  Blank lines and lines beginning with
'#' are skipped. Lines starting with 'import' are executed.

For example, suppose sys.prefix and sys.exec_prefix are set to
/usr/local and there is a directory /usr/local/lib/python2.5/site-packages
with three subdirectories, foo, bar and spam, and two path
configuration files, foo.pth and bar.pth.  Assume foo.pth contains the
following:

  # foo package configuration
  foo
  bar
  bletch

and bar.pth contains:

  # bar package configuration
  bar

Then the following directories are added to sys.path, in this order:

  /usr/local/lib/python2.5/site-packages/bar
  /usr/local/lib/python2.5/site-packages/foo

Note that bletch is omitted because it doesn't exist; bar precedes foo
because bar.pth comes alphabetically before foo.pth; and spam is
omitted because it is not mentioned in either path configuration file.

The readline module is also automatically configured to enable
completion for systems that support it.  This can be overridden in
sitecustomize, usercustomize or PYTHONSTARTUP.  Starting Python in
isolated mode (-I) disables automatic readline configuration.

After these operations, an attempt is made to import a module
named sitecustomize, which can perform arbitrary additional
site-specific customizations.  If this import fails with an
ImportError exception, it is silently ignored.

## When to use

Reach for `site` when your task calls for Append module search paths for third-party packages to sys.path. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import site
```

## Key functions

- `site.abs_paths()`
- `site.addpackage(sitedir, name, known_paths)`
- `site.addsitedir(sitedir, known_paths=None)`
- `site.addsitepackages(known_paths, prefixes=None)`
- `site.addusersitepackages(known_paths)`
- `site.check_enableusersite()`
- `site.enablerlcompleter()`
- `site.execsitecustomize()`
- `site.execusercustomize()`
- `site.gethistoryfile()`
- `site.getsitepackages(prefixes=None)`
- `site.getuserbase()`
- `site.getusersitepackages()`
- `site.main()`
- `site.makepath(*paths)`
- `site.register_readline()`
- `site.removeduppaths()`
- `site.setcopyright()`
- `site.sethelper()`
- `site.setquit()`
- `site.venv(known_paths)`

## Constants / attributes

`ENABLE_USER_SITE`, `PREFIXES`, `USER_BASE`, `USER_SITE`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import site

def do_work(...):
    """Use site to accomplish one well-defined task."""
    result = site.abs_paths(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `site` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module site

NAME
    site - Append module search paths for third-party packages to sys.path.

MODULE REFERENCE
    https://docs.python.org/3.14/library/site.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    ****************************************************************
    * This module is automatically imported during initialization. *
    ****************************************************************

    This will append site-specific paths to the module search path.  On
    Unix (including Mac OSX), it starts with sys.prefix and
    sys.exec_prefix (if different) and appends
    lib/python<version>/site-packages.
    On other platforms (such as Windows), it tries each of the
    prefixes directly, as well as with lib/site-packages appended.  The
    resulting directories, if they exist, are appended to sys.path, and
    also inspected for path configuration files.

    If a file named "pyvenv.cfg" exists one directory above sys.executable,
    sys.prefix and sys.exec_prefix are set to that directory and
    it is also checked for site-packages (sys.base_prefix and
    sys.base_exec_prefix will always be the "real" prefixes of the Python
    installation). If "pyvenv.cfg" (a bootstrap configuration file) contains
    the key "include-system-site-packages" set to anything other than "false"
    (case-insensitive), the system-level prefixes will still also be
    searched for site-packages; otherwise they won't.

    All of the resulting site-specific directories, if they exist, are
    appended to sys.path, and also inspected for path configuration
    files.

    A path configuration file is a file whose name has the form
    <package>.pth; its contents are additional directories (one per line)
    to be added to sys.path.  Non-existing directories (or
    non-directories) are never added to sys.path; no directory is added to
    sys.path more than once.  Blank lines and lines beginning with
    '#' are skipped. Lines starting with 'import' are executed.

    For example, suppose sys.prefix and sys.exec_prefix are set to
    /usr/local and there is a directory /usr/local/lib/python2.5/site-packages
    with three subdirectories, foo, bar and spam, and two path
    configuration files, foo.pth and bar.pth.  Assume foo.pth contains the
    following:

      # foo package configuration
      foo
      bar
      bletch

    and bar.pth contains:

      # bar package configuration
      bar

    Then the following directories are added to sys.path, in this order:

      /usr/local/lib/python2.5/site-packages/bar
      /usr/local/lib/python2.5/site-packages/foo

    Note that bletch is omitted because it doesn't exist; bar precedes foo
    because bar.pth comes alphabetically before foo.pth; and spam is
    omitted because it is not mentioned in either path configuration file.

    The readline module is also automatically configured to enable
    completion for systems that support it.  This can be overridden in
    sitecustomize, usercustomize or PYTHONSTARTUP.  Starting Python in
    isolated mode (-I) disables automatic readline configuration.

    After these operations, an attempt is made to import a module
    named sitecustomize, which can perform arbitrary additional
    site-specific customizations.  If this import fails with an
    ImportError exception, it is silently ignored.

FUNCTIONS
    abs_paths()
        Set all module __file__ and __cached__ attributes to an absolute path

    addpackage(sitedir, name, known_paths)
        Process a .pth file within the site-packages directory:
        For each line in the file, either combine it with sitedir to a path
        and add that to known_paths, or execute it if it starts with 'import '.

    addsitedir(sitedir, known_paths=None)
        Add 'sitedir' argument to sys.path if missing and handle .pth files in
        'sitedir'

    addsitepackages(known_paths, prefixes=None)
        Add site-packages to sys.path

    addusersitepackages(known_paths)
        Add a per user site-package to sys.path

        Each user has its own python directory with site-packages in the
        home directory.

    check_enableusersite()
        Check if user site directory is safe for inclusion

        The function tests for the command line flag (including environment var),
        process uid/gid equal to effective uid/gid.

        None: Disabled for security reasons
        False: Disabled by user (command line option)
        True: Safe and enabled

    enablerlcompleter()
        Enable default readline configuration on interactive prompts, by
        registering a sys.__interactivehook__.

    execsitecustomize()
        Run custom site specific code, if available.

    execusercustomize()
        Run custom user specific code, if available.

    gethistoryfile()
        Check if the PYTHON_HISTORY environment variable is set and define
        it as the .python_history file.  If PYTHON_HISTORY is not set, use the
        default .python_history file.

    getsitepackages(prefixes=None)
        Returns a list containing all global site-packages directories.

        For each directory present in ``prefixes`` (or the global ``PREFIXES``),
        this function will find its `site-packages` subdirectory depending on the
        system environment, and will return a list of full paths.

    getuserbase()
        Returns the `user base` directory path.

        The `user base` directory can be used to store data. If the global
        variable ``USER_BASE`` is not initialized yet, this function will also set
        it.

    getusersitepackages()
        Returns the user-specific site-packages directory path.

        If
```

## Related

Other standard-library modules pair well with `site`; explore the `python` domain of this catalog.
