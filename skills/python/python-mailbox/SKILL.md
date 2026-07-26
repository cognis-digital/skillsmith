---
name: python-mailbox
description: "Program with Python's mailbox module: Read/write support for Maildir, mbox, MH, Babyl, and MMDF mailboxes."
version: 1.0.0
tags: [mailbox, programming, python, stdlib]
---

# Python: `mailbox`

## Overview

Read/write support for Maildir, mbox, MH, Babyl, and MMDF mailboxes.

## When to use

Reach for `mailbox` when your task calls for Read/write support for Maildir, mbox, MH, Babyl, and MMDF mailboxes. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import mailbox
```

## Key classes

`Babyl`, `BabylMessage`, `Error`, `ExternalClashError`, `FormatError`, `GenericAlias`, `MH`, `MHMessage`, `MMDF`, `MMDFMessage`, `Mailbox`, `Maildir`, `MaildirMessage`, `Message`, `NoSuchMailboxError`, `NotEmptyError`, `mbox`, `mboxMessage`

## Constants / attributes

`fcntl`, `linesep`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import mailbox

def do_work(...):
    """Use mailbox to accomplish one well-defined task."""
    result = mailbox.Babyl(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `mailbox` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module mailbox

NAME
    mailbox - Read/write support for Maildir, mbox, MH, Babyl, and MMDF mailboxes.

MODULE REFERENCE
    https://docs.python.org/3.14/library/mailbox.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.Exception(builtins.BaseException)
        Error
            ExternalClashError
            FormatError
            NoSuchMailboxError
            NotEmptyError
    builtins.object
        Mailbox
            MH
            Maildir
    email.message.Message(builtins.object)
        Message
            BabylMessage
            MHMessage
            MaildirMessage
    _mboxMMDF(_singlefileMailbox)
        MMDF
        mbox
    _mboxMMDFMessage(Message)
        MMDFMessage
        mboxMessage
    _singlefileMailbox(Mailbox)
        Babyl

    class Babyl(_singlefileMailbox)
     |  Babyl(path, factory=None, create=True)
     |
     |  An Rmail-style Babyl mailbox.
     |
     |  Method resolution order:
     |      Babyl
     |      _singlefileMailbox
     |      Mailbox
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, path, factory=None, create=True)
     |      Initialize a Babyl mailbox.
     |
     |  __setitem__(self, key, message)
     |      Replace the keyed message; raise KeyError if it doesn't exist.
     |
     |  add(self, message)
     |      Add message and return assigned key.
     |
     |  get_bytes(self, key)
     |      Return a string representation or raise a KeyError.
     |
     |  get_file(self, key)
     |      Return a file-like representation or raise a KeyError.
     |
     |  get_labels(self)
     |      Return a list of user-defined labels in the mailbox.
     |
     |  get_message(self, key)
     |      Return a Message representation or raise a KeyError.
     |
     |  remove(self, key)
     |      Remove the keyed message; raise KeyError if it doesn't exist.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from _singlefileMailbox:
     |
     |  __contains__(self, key)
     |      Return True if the keyed message exists, False otherwise.
     |
     |  __len__(self)
     |      Return a count of messages in the mailbox.
     |
     |  close(self)
     |      Flush and close the mailbox.
     |
     |  flush(self)
     |      Write any pending changes to disk.
     |
     |  iterkeys(self)
     |      Return an iterator over keys.
     |
     |  lock(self)
     |      Lock the mailbox.
     |
     |  unlock(self)
     |      Unlock the mailbox if it is locked.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Mailbox:
     |
     |  __delitem__(self, key)
     |
     |  __getitem__(self, key)
     |      Return the keyed message; raise KeyError if it doesn't exist.
     |
     |  __iter__(self)
     |
     |  clear(self)
     |      Delete all messages.
     |
     |  discard(self, key)
     |      If the keyed message exists, remove it.
     |
     |  get(self, key, default=None)
     |      Return the keyed message, or default if it doesn't exist.
     |
     |  get_string(self, key)
     |      Return a string representation or raise a KeyError.
     |
     |      Uses email.message.Message to create a 7bit clean string
     |      representation of the message.
     |
     |  items(self)
     |      Return a list of (key, message) tuples. Memory intensive.
     |
     |  iteritems(self)
     |      Return an iterator over (key, message) tuples.
     |
     |  itervalues(self)
     |      Return an iterator over all messages.
     |
     |  keys(self)
     |      Return a list of keys.
     |
     |  pop(self, key, default=None)
     |      Delete the keyed message and return it, or default.
     |
     |  popitem(self)
     |      Delete an arbitrary (key, message) pair and return it.
     |
     |  update(self, arg=None)
     |      Change the messages that correspond to certain keys.
     |
     |  values(self)
     |      Return a list of messages. Memory intensive.
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from Mailbox:
     |
     |  __class_getitem__ = GenericAlias(args, /)
     |      Represent a PEP 585 generic type
     |
     |      E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Mailbox:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class BabylMessage(Message)
     |  BabylMessage(message=None)
     |
     |  Message with Babyl-specific properties.
     |
     |  Method resolution order:
     |      BabylMessage
     |      Message
     |      email.message.Message
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, message=None)
     |      Initialize a BabylMessage instance.
     |
     |  add_label(self, label)
     |      Add label to list of labels on the message.
     |
     |  get_labels(self)
     |      Return a list of labels on the message.
     |
     |  get_visible(self)
     |      Return a Message representation of visible headers.
     |
     |  remove_label(self, label)
     |      Remove label from the list of labels on the message.
     |
     |  set_labels(self, labels)
     |      Set the list of labels on the message.
     |
     |  set_visible(self, visible)
     |      Set the Message representation of visible headers.
     |
     |  update_vis
```

## Related

Other standard-library modules pair well with `mailbox`; explore the `python` domain of this catalog.
