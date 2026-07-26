---
name: python-ftplib
description: "Program with Python's ftplib module: An FTP client class and some helper functions."
version: 1.0.0
tags: [ftplib, programming, python, stdlib]
---

# Python: `ftplib`

## Overview

An FTP client class and some helper functions.

Based on RFC 959: File Transfer Protocol (FTP), by J. Postel and J. Reynolds

Example:

>>> from ftplib import FTP
>>> ftp = FTP('ftp.python.org') # connect to host, default port
>>> ftp.login() # default, i.e.: user anonymous, passwd anonymous@
'230 Guest login ok, access restrictions apply.'
>>> ftp.retrlines('LIST') # list directory contents
total 9
drwxr-xr-x   8 root     wheel        1024 Jan  3  1994 .
drwxr-xr-x   8 root     wheel        1024 Jan  3  1994 ..
drwxr-xr-x   2 root     wheel        1024 Jan  3  1994 bin
drwxr-xr-x   2 root     wheel        1024 Jan  3  1994 etc
d-wxrwxr-x   2 ftp      wheel        1024 Sep  5 13:43 incoming
drwxr-xr-x   2 root     wheel        1024 Nov 17  1993 lib
drwxr-xr-x   6 1094     wheel        1024 Sep 13 19:07 pub
drwxr-xr-x   3 root     wheel        1024 Jan  3  1994 usr
-rw-r--r--   1 root     root          312 Aug  1  1994 welcome.msg
'226 Transfer complete.'
>>> ftp.quit()
'221 Goodbye.'
>>>

A nice test that reveals some of the network dialogue would be:
python ftplib.py -d localhost -l -p -l

## When to use

Reach for `ftplib` when your task calls for An FTP client class and some helper functions. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import ftplib
```

## Key functions

- `ftplib.ftpcp(source, sourcename, target, targetname='', type='I')`
- `ftplib.parse150(resp)`
- `ftplib.parse227(resp)`
- `ftplib.parse229(resp, peer)`
- `ftplib.parse257(resp)`
- `ftplib.print_line(line)`
- `ftplib.test()`

## Key classes

`Error`, `FTP`, `FTP_TLS`, `error_perm`, `error_proto`, `error_reply`, `error_temp`

## Constants / attributes

`B_CRLF`, `CRLF`, `FTP_PORT`, `MAXLINE`, `MSG_OOB`, `all_errors`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import ftplib

def do_work(...):
    """Use ftplib to accomplish one well-defined task."""
    result = ftplib.ftpcp(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `ftplib` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module ftplib

NAME
    ftplib - An FTP client class and some helper functions.

MODULE REFERENCE
    https://docs.python.org/3.14/library/ftplib.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Based on RFC 959: File Transfer Protocol (FTP), by J. Postel and J. Reynolds

    Example:

    >>> from ftplib import FTP
    >>> ftp = FTP('ftp.python.org') # connect to host, default port
    >>> ftp.login() # default, i.e.: user anonymous, passwd anonymous@
    '230 Guest login ok, access restrictions apply.'
    >>> ftp.retrlines('LIST') # list directory contents
    total 9
    drwxr-xr-x   8 root     wheel        1024 Jan  3  1994 .
    drwxr-xr-x   8 root     wheel        1024 Jan  3  1994 ..
    drwxr-xr-x   2 root     wheel        1024 Jan  3  1994 bin
    drwxr-xr-x   2 root     wheel        1024 Jan  3  1994 etc
    d-wxrwxr-x   2 ftp      wheel        1024 Sep  5 13:43 incoming
    drwxr-xr-x   2 root     wheel        1024 Nov 17  1993 lib
    drwxr-xr-x   6 1094     wheel        1024 Sep 13 19:07 pub
    drwxr-xr-x   3 root     wheel        1024 Jan  3  1994 usr
    -rw-r--r--   1 root     root          312 Aug  1  1994 welcome.msg
    '226 Transfer complete.'
    >>> ftp.quit()
    '221 Goodbye.'
    >>>

    A nice test that reveals some of the network dialogue would be:
    python ftplib.py -d localhost -l -p -l

CLASSES
    builtins.object
        FTP
            FTP_TLS
    Error(builtins.Exception)
        error_perm
        error_proto
        error_reply
        error_temp

    class FTP(builtins.object)
     |  FTP(
     |      host='',
     |      user='',
     |      passwd='',
     |      acct='',
     |      timeout=<object object at 0x000001B05F3318D0>,
     |      source_address=None,
     |      *,
     |      encoding='utf-8'
     |  )
     |
     |  An FTP client class.
     |
     |  To create a connection, call the class using these arguments:
     |          host, user, passwd, acct, timeout, source_address, encoding
     |
     |  The first four arguments are all strings, and have default value ''.
     |  The parameter ´timeout´ must be numeric and defaults to None if not
     |  passed, meaning that no timeout will be set on any ftp socket(s).
     |  If a timeout is passed, then this is now the default timeout for all ftp
     |  socket operations for this instance.
     |  The last parameter is the encoding of filenames, which defaults to utf-8.
     |
     |  Then use self.connect() with optional host and port argument.
     |
     |  To download a file, use ftp.retrlines('RETR ' + filename),
     |  or ftp.retrbinary() with slightly different arguments.
     |  To upload a file, use ftp.storlines() or ftp.storbinary(),
     |  which have an open file as argument (see their definitions
     |  below for details).
     |  The download/upload functions first issue appropriate TYPE
     |  and PORT or PASV commands.
     |
     |  Methods defined here:
     |
     |  __enter__(self)
     |
     |  __exit__(self, *args)
     |      # Context management protocol: try to quit() if active
     |
     |  __init__(
     |      self,
     |      host='',
     |      user='',
     |      passwd='',
     |      acct='',
     |      timeout=<object object at 0x000001B05F3318D0>,
     |      source_address=None,
     |      *,
     |      encoding='utf-8'
     |  )
     |      Initialization method (called by class instantiation).
     |      Initialize host to localhost, port to standard ftp port.
     |      Optional arguments are host (for connect()),
     |      and user, passwd, acct (for login()).
     |
     |  abort(self)
     |      Abort a file transfer.  Uses out-of-band data.
     |      This does not follow the procedure from the RFC to send Telnet
     |      IP and Synch; that doesn't seem to work with the servers I've
     |      tried.  Instead, just send the ABOR command as OOB data.
     |
     |  acct(self, password)
     |      Send new account name.
     |
     |  close(self)
     |      Close the connection without assuming anything about it.
     |
     |  connect(self, host='', port=0, timeout=-999, source_address=None)
     |      Connect to host.  Arguments are:
     |      - host: hostname to connect to (string, default previous host)
     |      - port: port to connect to (integer, default previous port)
     |      - timeout: the timeout to set against the ftp socket(s)
     |      - source_address: a 2-tuple (host, port) for the socket to bind
     |        to as its source address before connecting.
     |
     |  cwd(self, dirname)
     |      Change to a directory.
     |
     |  debug = set_debuglevel(self, level)
     |
     |  delete(self, filename)
     |      Delete a file.
     |
     |  dir(self, *args)
     |      List a directory in long form.
     |      By default list current directory to stdout.
     |      Optional last argument is callback function; all
     |      non-empty arguments before it are concatenated to the
     |      LIST command.  (This *should* only be used for a pathname.)
     |
     |  getline(self)
     |      # Internal: return one line from the server, stripping CRLF.
     |      # Raise EOFError if the connection is closed
     |
     |  getmultiline(self)
     |      # Internal: get a response from the server, which may possibly
     |      # consist of multiple lines.  Return a single string with no
     |      # trailing CRLF.  If the response consists of multiple lines,
     |      # these are separated by '\n' characters in the string
     |
     |  getresp(self)
     |      # Internal: get a response from the server.
     |      # Raise various errors if the response indicates
```

## Related

Other standard-library modules pair well with `ftplib`; explore the `python` domain of this catalog.
