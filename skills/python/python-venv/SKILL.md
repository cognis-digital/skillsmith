---
name: python-venv
description: "Program with Python's venv module: Virtual environment (venv) package for Python."
version: 1.0.0
tags: [programming, python, stdlib, venv]
---

# Python: `venv`

## Overview

Virtual environment (venv) package for Python. Based on PEP 405.

Copyright (C) 2011-2014 Vinay Sajip.
Licensed to the PSF under a contributor agreement.

## When to use

Reach for `venv` when your task calls for Virtual environment (venv) package for Python. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import venv
```

## Key functions

- `venv.create(env_dir, system_site_packages=False, clear=False, symlinks=False, with_pip=False, prompt=None, upgrade_deps=False, *, scm_ignore_files=frozenset())`
- `venv.main(args=None)`

## Key classes

`EnvBuilder`

## Constants / attributes

`CORE_VENV_DEPS`, `logger`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import venv

def do_work(...):
    """Use venv to accomplish one well-defined task."""
    result = venv.create(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `venv` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: package venv

NAME
    venv - Virtual environment (venv) package for Python. Based on PEP 405.

MODULE REFERENCE
    https://docs.python.org/3.14/library/venv.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Copyright (C) 2011-2014 Vinay Sajip.
    Licensed to the PSF under a contributor agreement.

PACKAGE CONTENTS
    __main__

CLASSES
    builtins.object
        EnvBuilder

    class EnvBuilder(builtins.object)
     |  EnvBuilder(
     |      system_site_packages=False,
     |      clear=False,
     |      symlinks=False,
     |      upgrade=False,
     |      with_pip=False,
     |      prompt=None,
     |      upgrade_deps=False,
     |      *,
     |      scm_ignore_files=frozenset()
     |  )
     |
     |  This class exists to allow virtual environment creation to be
     |  customized. The constructor parameters determine the builder's
     |  behaviour when called upon to create a virtual environment.
     |
     |  By default, the builder makes the system (global) site-packages dir
     |  *un*available to the created environment.
     |
     |  If invoked using the Python -m option, the default is to use copying
     |  on Windows platforms but symlinks elsewhere. If instantiated some
     |  other way, the default is to *not* use symlinks.
     |
     |  :param system_site_packages: If True, the system (global) site-packages
     |                               dir is available to created environments.
     |  :param clear: If True, delete the contents of the environment directory if
     |                it already exists, before environment creation.
     |  :param symlinks: If True, attempt to symlink rather than copy files into
     |                   virtual environment.
     |  :param upgrade: If True, upgrade an existing virtual environment.
     |  :param with_pip: If True, ensure pip is installed in the virtual
     |                   environment
     |  :param prompt: Alternative terminal prefix for the environment.
     |  :param upgrade_deps: Update the base venv modules to the latest on PyPI
     |  :param scm_ignore_files: Create ignore files for the SCMs specified by the
     |                           iterable.
     |
     |  Methods defined here:
     |
     |  __init__(
     |      self,
     |      system_site_packages=False,
     |      clear=False,
     |      symlinks=False,
     |      upgrade=False,
     |      with_pip=False,
     |      prompt=None,
     |      upgrade_deps=False,
     |      *,
     |      scm_ignore_files=frozenset()
     |  )
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  clear_directory(self, path)
     |
     |  create(self, env_dir)
     |      Create a virtual environment in a directory.
     |
     |      :param env_dir: The target directory to create an environment in.
     |
     |  create_configuration(self, context)
     |      Create a configuration file indicating where the environment's Python
     |      was copied from, and whether the system site-packages should be made
     |      available in the environment.
     |
     |      :param context: The information for the environment creation request
     |                      being processed.
     |
     |  create_git_ignore_file(self, context)
     |      Create a .gitignore file in the environment directory.
     |
     |      The contents of the file cause the entire environment directory to be
     |      ignored by git.
     |
     |  ensure_directories(self, env_dir)
     |      Create the directories for the environment.
     |
     |      Returns a context object which holds paths in the environment,
     |      for use by subsequent logic.
     |
     |  install_scripts(self, context, path)
     |      Install scripts into the created environment from a directory.
     |
     |      :param context: The information for the environment creation request
     |                      being processed.
     |      :param path:    Absolute pathname of a directory containing script.
     |                      Scripts in the 'common' subdirectory of this directory,
     |                      and those in the directory named for the platform
     |                      being run on, are installed in the created environment.
     |                      Placeholder variables are replaced with environment-
     |                      specific values.
     |
     |  post_setup(self, context)
     |      Hook for post-setup modification of the venv. Subclasses may install
     |      additional packages or scripts here, add activation shell scripts, etc.
     |
     |      :param context: The information for the environment creation request
     |                      being processed.
     |
     |  replace_variables(self, text, context)
     |      Replace variable placeholders in script text with context-specific
     |      variables.
     |
     |      Return the text passed in , but with variables replaced.
     |
     |      :param text: The text in which to replace placeholder variables.
     |      :param context: The information for the environment creation request
     |                      being processed.
     |
     |  setup_python(self, context)
     |      Set up a Python executable in the environment.
     |
     |      :param context: The information for the environment creation request
     |                      being processed.
     |
     |  setup_scripts(self, context)
     |      Set up scripts into the created environment from a directory.
     |
     |      This method installs the default scripts into the environment
     |      being created. You can prevent the default installatio
```

## Related

Other standard-library modules pair well with `venv`; explore the `python` domain of this catalog.
