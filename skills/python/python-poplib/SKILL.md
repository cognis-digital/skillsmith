---
name: python-poplib
description: "Program with Python's poplib module: A POP3 client class."
version: 1.0.0
tags: [poplib, programming, python, stdlib]
---

# Python: `poplib`

## Overview

A POP3 client class.

Based on the J. Myers POP3 draft, Jan. 96

## When to use

Reach for `poplib` when your task calls for A POP3 client class. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import poplib
```

## Key classes

`POP3`, `POP3_SSL`, `error_proto`

## Constants / attributes

`CR`, `CRLF`, `HAVE_SSL`, `LF`, `POP3_PORT`, `POP3_SSL_PORT`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import poplib

def do_work(...):
    """Use poplib to accomplish one well-defined task."""
    result = poplib.POP3(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `poplib` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module poplib

NAME
    poplib - A POP3 client class.

MODULE REFERENCE
    https://docs.python.org/3.14/library/poplib.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Based on the J. Myers POP3 draft, Jan. 96

CLASSES
    builtins.Exception(builtins.BaseException)
        error_proto
    builtins.object
        POP3
            POP3_SSL

    class POP3(builtins.object)
     |  POP3(host, port=110, timeout=<object object at 0x000001B05F3318D0>)
     |
     |  This class supports both the minimal and optional command sets.
     |  Arguments can be strings or integers (where appropriate)
     |  (e.g.: retr(1) and retr('1') both work equally well.
     |
     |  Minimal Command Set:
     |          USER name               user(name)
     |          PASS string             pass_(string)
     |          STAT                    stat()
     |          LIST [msg]              list(msg = None)
     |          RETR msg                retr(msg)
     |          DELE msg                dele(msg)
     |          NOOP                    noop()
     |          RSET                    rset()
     |          QUIT                    quit()
     |
     |  Optional Commands (some servers support these):
     |          RPOP name               rpop(name)
     |          APOP name digest        apop(name, digest)
     |          TOP msg n               top(msg, n)
     |          UIDL [msg]              uidl(msg = None)
     |          CAPA                    capa()
     |          STLS                    stls()
     |          UTF8                    utf8()
     |
     |  Raises one exception: 'error_proto'.
     |
     |  Instantiate with:
     |          POP3(hostname, port=110)
     |
     |  NB:     the POP protocol locks the mailbox from user
     |          authorization until QUIT, so be sure to get in, suck
     |          the messages, and quit, each time you access the
     |          mailbox.
     |
     |          POP is a line-based protocol, which means large mail
     |          messages consume lots of python cycles reading them
     |          line-by-line.
     |
     |          If it's available on your mail server, use IMAP4
     |          instead, it doesn't suffer from the two problems
     |          above.
     |
     |  Methods defined here:
     |
     |  __init__(self, host, port=110, timeout=<object object at 0x000001B05F3318D0>)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  apop(self, user, password)
     |      Authorisation
     |
     |      - only possible if server has supplied a timestamp in initial greeting.
     |
     |      Args:
     |              user     - mailbox user;
     |              password - mailbox password.
     |
     |      NB: mailbox is locked by server from here to 'quit()'
     |
     |  capa(self)
     |      Return server capabilities (RFC 2449) as a dictionary
     |      >>> c=poplib.POP3('localhost')
     |      >>> c.capa()
     |      {'IMPLEMENTATION': ['Cyrus', 'POP3', 'server', 'v2.2.12'],
     |       'TOP': [], 'LOGIN-DELAY': ['0'], 'AUTH-RESP-CODE': [],
     |       'EXPIRE': ['NEVER'], 'USER': [], 'STLS': [], 'PIPELINING': [],
     |       'UIDL': [], 'RESP-CODES': []}
     |      >>>
     |
     |      Really, according to RFC 2449, the cyrus folks should avoid
     |      having the implementation split into multiple arguments...
     |
     |  close(self)
     |      Close the connection without assuming anything about it.
     |
     |  dele(self, which)
     |      Delete message number 'which'.
     |
     |      Result is 'response'.
     |
     |  getwelcome(self)
     |
     |  list(self, which=None)
     |      Request listing, return result.
     |
     |      Result without a message number argument is in form
     |      ['response', ['mesg_num octets', ...], octets].
     |
     |      Result when a message number argument is given is a
     |      single response: the "scan listing" for that message.
     |
     |  noop(self)
     |      Does nothing.
     |
     |      One supposes the response indicates the server is alive.
     |
     |  pass_(self, pswd)
     |      Send password, return response
     |
     |      (response includes message count, mailbox size).
     |
     |      NB: mailbox is locked by server from here to 'quit()'
     |
     |  quit(self)
     |      Signoff: commit changes on server, unlock mailbox, close connection.
     |
     |  retr(self, which)
     |      Retrieve whole message number 'which'.
     |
     |      Result is in form ['response', ['line', ...], octets].
     |
     |  rpop(self, user)
     |      Send RPOP command to access the mailbox with an alternate user.
     |
     |  rset(self)
     |      Unmark all messages marked for deletion.
     |
     |  set_debuglevel(self, level)
     |
     |  stat(self)
     |      Get mailbox status.
     |
     |      Result is tuple of 2 ints (message count, mailbox size)
     |
     |  stls(self, context=None)
     |      Start a TLS session on the active connection as specified in RFC 2595.
     |
     |      context - a ssl.SSLContext
     |
     |  top(self, which, howmuch)
     |      Retrieve message header of message number 'which'
     |      and first 'howmuch' lines of message body.
     |
     |      Result is in form ['response', ['line', ...], octets].
     |
     |  uidl(self, which=None)
     |      Return message digest (unique id) list.
     |
     |      If 'which', result contains unique id for that message
     |      in the form 'response mesgnum uid', otherwise result is
     |      the list ['response', ['mesgnum uid', ...], octets]
     |
     |  user(
```

## Related

Other standard-library modules pair well with `poplib`; explore the `python` domain of this catalog.
