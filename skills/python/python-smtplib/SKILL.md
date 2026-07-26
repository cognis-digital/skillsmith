---
name: python-smtplib
description: "Program with Python's smtplib module: SMTP/ESMTP client class."
version: 1.0.0
tags: [programming, python, smtplib, stdlib]
---

# Python: `smtplib`

## Overview

SMTP/ESMTP client class.

This should follow RFC 821 (SMTP), RFC 1869 (ESMTP), RFC 2554 (SMTP
Authentication) and RFC 2487 (Secure SMTP over TLS).

Notes:

Please remember, when doing ESMTP, that the names of the SMTP service
extensions are NOT the same thing as the option keywords for the RCPT
and MAIL commands!

Example:

  >>> import smtplib
  >>> s=smtplib.SMTP("localhost")
  >>> print(s.help())
  This is Sendmail version 8.8.4
  Topics:
      HELO    EHLO    MAIL    RCPT    DATA
      RSET    NOOP    QUIT    HELP    VRFY
      EXPN    VERB    ETRN    DSN
  For more info use "HELP <topic>".
  To report bugs in the implementation send email to
      sendmail-bugs@sendmail.org.
  For local information send email to Postmaster at your site.
  End of HELP info
  >>> s.putcmd("vrfy","someone@here")
  >>> s.getreply()
  (250, "Somebody OverHere <somebody@here.my.org>")
  >>> s.quit()

## When to use

Reach for `smtplib` when your task calls for SMTP/ESMTP client class. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import smtplib
```

## Key functions

- `smtplib.encode_base64(s, maxlinelen=76, eol='\n')`
- `smtplib.quoteaddr(addrstring)`
- `smtplib.quotedata(data)`

## Key classes

`LMTP`, `SMTP`, `SMTPAuthenticationError`, `SMTPConnectError`, `SMTPDataError`, `SMTPException`, `SMTPHeloError`, `SMTPNotSupportedError`, `SMTPRecipientsRefused`, `SMTPResponseException`, `SMTPSenderRefused`, `SMTPServerDisconnected`, `SMTP_SSL`

## Constants / attributes

`CRLF`, `LMTP_PORT`, `OLDSTYLE_AUTH`, `SMTP_PORT`, `SMTP_SSL_PORT`, `bCRLF`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import smtplib

def do_work(...):
    """Use smtplib to accomplish one well-defined task."""
    result = smtplib.encode_base64(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `smtplib` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module smtplib

NAME
    smtplib - SMTP/ESMTP client class.

MODULE REFERENCE
    https://docs.python.org/3.14/library/smtplib.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This should follow RFC 821 (SMTP), RFC 1869 (ESMTP), RFC 2554 (SMTP
    Authentication) and RFC 2487 (Secure SMTP over TLS).

    Notes:

    Please remember, when doing ESMTP, that the names of the SMTP service
    extensions are NOT the same thing as the option keywords for the RCPT
    and MAIL commands!

    Example:

      >>> import smtplib
      >>> s=smtplib.SMTP("localhost")
      >>> print(s.help())
      This is Sendmail version 8.8.4
      Topics:
          HELO    EHLO    MAIL    RCPT    DATA
          RSET    NOOP    QUIT    HELP    VRFY
          EXPN    VERB    ETRN    DSN
      For more info use "HELP <topic>".
      To report bugs in the implementation send email to
          sendmail-bugs@sendmail.org.
      For local information send email to Postmaster at your site.
      End of HELP info
      >>> s.putcmd("vrfy","someone@here")
      >>> s.getreply()
      (250, "Somebody OverHere <somebody@here.my.org>")
      >>> s.quit()

CLASSES
    builtins.OSError(builtins.Exception)
        SMTPException
            SMTPNotSupportedError
            SMTPRecipientsRefused
            SMTPResponseException
                SMTPAuthenticationError
                SMTPConnectError
                SMTPDataError
                SMTPHeloError
                SMTPSenderRefused
            SMTPServerDisconnected
    builtins.object
        SMTP
            SMTP_SSL

    class SMTP(builtins.object)
     |  SMTP(
     |      host='',
     |      port=0,
     |      local_hostname=None,
     |      timeout=<object object at 0x000001B05F3318D0>,
     |      source_address=None
     |  )
     |
     |  This class manages a connection to an SMTP or ESMTP server.
     |  SMTP Objects:
     |      SMTP objects have the following attributes:
     |          helo_resp
     |              This is the message given by the server in response to the
     |              most recent HELO command.
     |
     |          ehlo_resp
     |              This is the message given by the server in response to the
     |              most recent EHLO command. This is usually multiline.
     |
     |          does_esmtp
     |              This is a True value _after you do an EHLO command_, if the
     |              server supports ESMTP.
     |
     |          esmtp_features
     |              This is a dictionary, which, if the server supports ESMTP,
     |              will _after you do an EHLO command_, contain the names of the
     |              SMTP service extensions this server supports, and their
     |              parameters (if any).
     |
     |              Note, all extension names are mapped to lower case in the
     |              dictionary.
     |
     |      See each method's docstrings for details.  In general, there is a
     |      method of the same name to perform each SMTP command.  There is also a
     |      method called 'sendmail' that will do an entire mail transaction.
     |
     |  Methods defined here:
     |
     |  __enter__(self)
     |
     |  __exit__(self, *args)
     |
     |  __init__(
     |      self,
     |      host='',
     |      port=0,
     |      local_hostname=None,
     |      timeout=<object object at 0x000001B05F3318D0>,
     |      source_address=None
     |  )
     |      Initialize a new instance.
     |
     |      If specified, `host` is the name of the remote host to which to
     |      connect.  If specified, `port` specifies the port to which to connect.
     |      By default, smtplib.SMTP_PORT is used.  If a host is specified the
     |      connect method is called, and if it returns anything other than a
     |      success code an SMTPConnectError is raised.  If specified,
     |      `local_hostname` is used as the FQDN of the local host in the HELO/EHLO
     |      command.  Otherwise, the local hostname is found using
     |      socket.getfqdn(). The `source_address` parameter takes a 2-tuple (host,
     |      port) for the socket to bind to as its source address before
     |      connecting. If the host is '' and port is 0, the OS default behavior
     |      will be used.
     |
     |  auth(self, mechanism, authobject, *, initial_response_ok=True)
     |      Authentication command - requires response processing.
     |
     |      'mechanism' specifies which authentication mechanism is to
     |      be used - the valid values are those listed in the 'auth'
     |      element of 'esmtp_features'.
     |
     |      'authobject' must be a callable object taking a single argument:
     |
     |              data = authobject(challenge)
     |
     |      It will be called to process the server's challenge response; the
     |      challenge argument it is passed will be a bytes.  It should return
     |      an ASCII string that will be base64 encoded and sent to the server.
     |
     |      Keyword arguments:
     |          - initial_response_ok: Allow sending the RFC 4954 initial-response
     |            to the AUTH command, if the authentication methods supports it.
     |
     |  auth_cram_md5(self, challenge=None)
     |      Authobject to use with CRAM-MD5 authentication. Requires self.user
     |      and self.password to be set.
     |
     |  auth_login(self, challenge=None)
     |      Authobject to use with LOGIN authentication. Requires self.user and
     |      self.password to be set.
     |
     |  auth_plain(self, challenge=None)
     |      Authobject to use with PLAIN authentication. Requires self.user and
     |
```

## Related

Other standard-library modules pair well with `smtplib`; explore the `python` domain of this catalog.
