---
name: python-wsgiref
description: "Program with Python's wsgiref module: wsgiref -- a WSGI (PEP 3333) Reference Library Current Contents: * util -- Miscellaneous useful functions and wrappers * headers -- Manage response headers * handlers -- base classes for server/gateway implementations * simple_server -- a simple BaseHTTPServer that supports WSGI * validate -- validation wrapper that sits between an app and a server to detect errors in either * types -- collection of WSGI-related types for static type checking To-Do: * cgi_gateway -- Run WSGI apps under CGI (pending a deployment standard) * cgi_wrapper -- Run CGI apps under WSGI * router -- a simple middleware component that handles URL traversal"
version: 1.0.0
tags: [programming, python, stdlib, wsgiref]
---

# Python: `wsgiref`

## Overview

wsgiref -- a WSGI (PEP 3333) Reference Library

Current Contents:

* util -- Miscellaneous useful functions and wrappers

* headers -- Manage response headers

* handlers -- base classes for server/gateway implementations

* simple_server -- a simple BaseHTTPServer that supports WSGI

* validate -- validation wrapper that sits between an app and a server
  to detect errors in either

* types -- collection of WSGI-related types for static type checking

To-Do:

* cgi_gateway -- Run WSGI apps under CGI (pending a deployment standard)

* cgi_wrapper -- Run CGI apps under WSGI

* router -- a simple middleware component that handles URL traversal

## When to use

Reach for `wsgiref` when your task calls for wsgiref -- a WSGI (PEP 3333) Reference Library Current Contents: * util -- Miscellaneous useful functions and wrappers *. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import wsgiref
```

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import wsgiref

def do_work(...):
    """Use wsgiref to accomplish one well-defined task."""
    result = wsgiref. ...
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `wsgiref` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: package wsgiref

NAME
    wsgiref - wsgiref -- a WSGI (PEP 3333) Reference Library

MODULE REFERENCE
    https://docs.python.org/3.14/library/wsgiref.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Current Contents:

    * util -- Miscellaneous useful functions and wrappers

    * headers -- Manage response headers

    * handlers -- base classes for server/gateway implementations

    * simple_server -- a simple BaseHTTPServer that supports WSGI

    * validate -- validation wrapper that sits between an app and a server
      to detect errors in either

    * types -- collection of WSGI-related types for static type checking

    To-Do:

    * cgi_gateway -- Run WSGI apps under CGI (pending a deployment standard)

    * cgi_wrapper -- Run CGI apps under WSGI

    * router -- a simple middleware component that handles URL traversal

PACKAGE CONTENTS
    handlers
    headers
    simple_server
    types
    util
    validate

FILE
    c:\python314\lib\wsgiref\__init__.py


```

## Related

Other standard-library modules pair well with `wsgiref`; explore the `python` domain of this catalog.
