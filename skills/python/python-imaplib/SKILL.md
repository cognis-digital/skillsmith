---
name: python-imaplib
description: "Program with Python's imaplib module: IMAP4 client."
version: 1.0.0
tags: [imaplib, programming, python, stdlib]
---

# Python: `imaplib`

## Overview

IMAP4 client.

Based on RFC 2060.

Public class:           IMAP4
Public variable:        Debug
Public functions:       Internaldate2tuple
                        Int2AP
                        ParseFlags
                        Time2Internaldate

## When to use

Reach for `imaplib` when your task calls for IMAP4 client. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import imaplib
```

## Key functions

- `imaplib.Int2AP(num)`
- `imaplib.Internaldate2tuple(resp)`
- `imaplib.ParseFlags(resp)`
- `imaplib.Time2Internaldate(date_time)`

## Key classes

`IMAP4`, `IMAP4_SSL`, `IMAP4_stream`, `Idler`, `datetime`, `timedelta`, `timezone`

## Constants / attributes

`AllowedVersions`, `CRLF`, `Commands`, `Continuation`, `DEFAULT_BUFFER_SIZE`, `Debug`, `Flags`, `HAVE_SSL`, `IMAP4_PORT`, `IMAP4_SSL_PORT`, `InternalDate`, `Literal`, `MapCRLF`, `Mon2num`, `Months`, `Response_code`, `Untagged_response`, `Untagged_status`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import imaplib

def do_work(...):
    """Use imaplib to accomplish one well-defined task."""
    result = imaplib.Int2AP(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `imaplib` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module imaplib

NAME
    imaplib - IMAP4 client.

MODULE REFERENCE
    https://docs.python.org/3.14/library/imaplib.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Based on RFC 2060.

    Public class:           IMAP4
    Public variable:        Debug
    Public functions:       Internaldate2tuple
                            Int2AP
                            ParseFlags
                            Time2Internaldate

CLASSES
    builtins.object
        IMAP4
            IMAP4_SSL
            IMAP4_stream

    class IMAP4(builtins.object)
     |  IMAP4(host='', port=143, timeout=None)
     |
     |  IMAP4 client class.
     |
     |  Instantiate with: IMAP4([host[, port[, timeout=None]]])
     |
     |          host - host's name (default: localhost);
     |          port - port number (default: standard IMAP4 port).
     |          timeout - socket timeout (default: None)
     |                    If timeout is not given or is None,
     |                    the global default socket timeout is used
     |
     |  All IMAP4rev1 commands are supported by methods of the same
     |  name (in lowercase).
     |
     |  All arguments to commands are converted to strings, except for
     |  AUTHENTICATE, and the last argument to APPEND which is passed as
     |  an IMAP4 literal.  If necessary (the string contains any
     |  non-printing characters or white-space and isn't enclosed with
     |  either parentheses or double quotes) each string is quoted.
     |  However, the 'password' argument to the LOGIN command is always
     |  quoted.  If you want to avoid having an argument string quoted
     |  (eg: the 'flags' argument to STORE) then enclose the string in
     |  parentheses (eg: "(\Deleted)").
     |
     |  Each command returns a tuple: (type, [data, ...]) where 'type'
     |  is usually 'OK' or 'NO', and 'data' is either the text from the
     |  tagged response, or untagged results from command. Each 'data'
     |  is either a string, or a tuple. If a tuple, then the first part
     |  is the header of the response, and the second part contains
     |  the data (ie: 'literal' value).
     |
     |  Errors raise the exception class <instance>.error("<reason>").
     |  IMAP4 server errors raise <instance>.abort("<reason>"),
     |  which is a sub-class of 'error'. Mailbox status changes
     |  from READ-WRITE to READ-ONLY raise the exception class
     |  <instance>.readonly("<reason>"), which is a sub-class of 'abort'.
     |
     |  "error" exceptions imply a program error.
     |  "abort" exceptions imply the connection should be reset, and
     |          the command re-tried.
     |  "readonly" exceptions imply the command should be re-tried.
     |
     |  Note: to use this module, you must read the RFCs pertaining to the
     |  IMAP4 protocol, as the semantics of the arguments to each IMAP4
     |  command are left to the invoker, not to mention the results. Also,
     |  most IMAP servers implement a sub-set of the commands available here.
     |
     |  Methods defined here:
     |
     |  __enter__(self)
     |
     |  __exit__(self, *args)
     |
     |  __getattr__(self, attr)
     |
     |  __init__(self, host='', port=143, timeout=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  append(self, mailbox, flags, date_time, message)
     |      Append message to named mailbox.
     |
     |      (typ, [data]) = <instance>.append(mailbox, flags, date_time, message)
     |
     |              All args except 'message' can be None.
     |
     |  authenticate(self, mechanism, authobject)
     |      Authenticate command - requires response processing.
     |
     |      'mechanism' specifies which authentication mechanism is to
     |      be used - it must appear in <instance>.capabilities in the
     |      form AUTH=<mechanism>.
     |
     |      'authobject' must be a callable object:
     |
     |              data = authobject(response)
     |
     |      It will be called to process server continuation responses; the
     |      response argument it is passed will be a bytes.  It should return bytes
     |      data that will be base64 encoded and sent to the server.  It should
     |      return None if the client abort response '*' should be sent instead.
     |
     |  capability(self)
     |      (typ, [data]) = <instance>.capability()
     |      Fetch capabilities list from server.
     |
     |  check(self)
     |      Checkpoint mailbox on server.
     |
     |      (typ, [data]) = <instance>.check()
     |
     |  close(self)
     |      Close currently selected mailbox.
     |
     |      Deleted messages are removed from writable mailbox.
     |      This is the recommended command before 'LOGOUT'.
     |
     |      (typ, [data]) = <instance>.close()
     |
     |  copy(self, message_set, new_mailbox)
     |      Copy 'message_set' messages onto end of 'new_mailbox'.
     |
     |      (typ, [data]) = <instance>.copy(message_set, new_mailbox)
     |
     |  create(self, mailbox)
     |      Create new mailbox.
     |
     |      (typ, [data]) = <instance>.create(mailbox)
     |
     |  delete(self, mailbox)
     |      Delete old mailbox.
     |
     |      (typ, [data]) = <instance>.delete(mailbox)
     |
     |  deleteacl(self, mailbox, who)
     |      Delete the ACLs (remove any rights) set for who on mailbox.
     |
     |      (typ, [data]) = <instance>.deleteacl(mailbox, who)
     |
     |  enable(self, capability)
     |      Send an RFC5161 enable string to the server.
     |
     |      (typ, [data]) = <instance>.enable(capability)
     |
     |  expunge(self)
     |      Permanen
```

## Related

Other standard-library modules pair well with `imaplib`; explore the `python` domain of this catalog.
