---
name: python-socketserver
description: "Program with Python's socketserver module: Generic socket server classes."
version: 1.0.0
tags: [programming, python, socketserver, stdlib]
---

# Python: `socketserver`

## Overview

Generic socket server classes.

This module tries to capture the various aspects of defining a server:

For socket-based servers:

- address family:
        - AF_INET{,6}: IP (Internet Protocol) sockets (default)
        - AF_UNIX: Unix domain sockets
        - others, e.g. AF_DECNET are conceivable (see <socket.h>
- socket type:
        - SOCK_STREAM (reliable stream, e.g. TCP)
        - SOCK_DGRAM (datagrams, e.g. UDP)

For request-based servers (including socket-based):

- client address verification before further looking at the request
        (This is actually a hook for any processing that needs to look
         at the request before anything else, e.g. logging)
- how to handle multiple requests:
        - synchronous (one request is handled at a time)
        - forking (each request is handled by a new process)
        - threading (each request is handled by a new thread)

The classes in this module favor the server type that is simplest to
write: a synchronous TCP/IP server.  This is bad class design, but
saves some typing.  (There's also the issue that a deep class hierarchy
slows down method lookups.)

There are five classes in an inheritance diagram, four of which represent
synchronous servers of four types:

        +------------+
        | BaseServer |
        +------------+
              |
              v
        +-----------+        +------------------+
        | TCPServer |------->| UnixStreamServer |
        +-----------+        +------------------+
              |
              v
        +-----------+        +--------------------+
        | UDPServer |------->| UnixDatagramServer |
        +-----------+        +--------------------+

Note that UnixDatagramServer derives from UDPServer, not from
UnixStreamServer -- the only difference between an IP and a Unix
stream server is the address family, which is simply repeated in both
unix server classes.

Forking and threading versions of each type of server can be created
using the ForkingMixIn and ThreadingMixIn mix-in classes.  For
instance, a threading UDP server class is created as follows:

        class ThreadingUDPServer(ThreadingMixIn, UDPServer): pass

The Mix-in class must come first, since it overrides a method defined
in UDPServer! Setting the various member variables also changes
the behavior of the underlying server mechanism.

To implement a service, you must derive a class from
BaseRequestHandler and redefine its handle() method.  You can then run
various versions of the service by combining one of the server classes
with your request handler class.

The request handler class must be different for datagram or stream
services.  This can be hidden by using the request handler
subclasses StreamRequestHandler or DatagramRequestHandler.

Of course, you still have to use your head!

For instance, it makes no sense to use a forking server if the service
contains state in memory that can be modified by requests (since the
modifications in the child process would never reach the initial state
kept in the parent process and passed to each child).  In this case,
you can use a threading server, but you will probably have to use
locks to avoid two requests that come in nearly simultaneous to apply
conflicting changes to the server state.

On the other hand, if you are building e.g. an HTTP server, where all
data is stored externally (e.g. in the file system), a synchronous
class will essentially render the service "deaf" while one request is
being handled -- which may be for a very long time if a client is slow
to read all the data it has requested.  Here a threading or forking
server is appropriate.

In some cases, it may be appropriate to process part of a request
synchronously, but to finish processing in a forked child depending on
the request data.  This can be implemented by using a synchronous
server and doing an explicit fork in the request handler class
handle() method.

Another approach to handling multiple simultaneous requests in an
environment that supports neither threads nor fork (or where these are
too expensive or inappropriate for the service) is to maintain an
explicit table of partially finished requests and to use a selector to
decide which request to work on next (or whether to handle a new
incoming request).  This is particularly important for stream services
where each client can potentially be connected for a long time (if
threads or subprocesses cannot be used).

Future work:
- Standard classes for Sun RPC (which uses either UDP or TCP)
- Standard mix-in classes to implement various authentication
  and encryption schemes

XXX Open problems:
- What to do with out-of-band data?

BaseServer:
- split generic "request" functionality out into BaseServer class.
  Copyright (C) 2000  Luke Kenneth Casson Leighton <lkcl@samba.org>

  example: read entries from a SQL database (requires overriding
  get_request() to return a table entry from the database).
  entry is processed by a RequestHandlerClass.

## When to use

Reach for `socketserver` when your task calls for Generic socket server classes. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import socketserver
```

## Key functions

- `socketserver.time()`

## Key classes

`BaseRequestHandler`, `BaseServer`, `BufferedIOBase`, `DatagramRequestHandler`, `StreamRequestHandler`, `TCPServer`, `ThreadingMixIn`, `ThreadingTCPServer`, `ThreadingUDPServer`, `UDPServer`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import socketserver

def do_work(...):
    """Use socketserver to accomplish one well-defined task."""
    result = socketserver.time(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `socketserver` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module socketserver

NAME
    socketserver - Generic socket server classes.

MODULE REFERENCE
    https://docs.python.org/3.14/library/socketserver.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module tries to capture the various aspects of defining a server:

    For socket-based servers:

    - address family:
            - AF_INET{,6}: IP (Internet Protocol) sockets (default)
            - AF_UNIX: Unix domain sockets
            - others, e.g. AF_DECNET are conceivable (see <socket.h>
    - socket type:
            - SOCK_STREAM (reliable stream, e.g. TCP)
            - SOCK_DGRAM (datagrams, e.g. UDP)

    For request-based servers (including socket-based):

    - client address verification before further looking at the request
            (This is actually a hook for any processing that needs to look
             at the request before anything else, e.g. logging)
    - how to handle multiple requests:
            - synchronous (one request is handled at a time)
            - forking (each request is handled by a new process)
            - threading (each request is handled by a new thread)

    The classes in this module favor the server type that is simplest to
    write: a synchronous TCP/IP server.  This is bad class design, but
    saves some typing.  (There's also the issue that a deep class hierarchy
    slows down method lookups.)

    There are five classes in an inheritance diagram, four of which represent
    synchronous servers of four types:

            +------------+
            | BaseServer |
            +------------+
                  |
                  v
            +-----------+        +------------------+
            | TCPServer |------->| UnixStreamServer |
            +-----------+        +------------------+
                  |
                  v
            +-----------+        +--------------------+
            | UDPServer |------->| UnixDatagramServer |
            +-----------+        +--------------------+

    Note that UnixDatagramServer derives from UDPServer, not from
    UnixStreamServer -- the only difference between an IP and a Unix
    stream server is the address family, which is simply repeated in both
    unix server classes.

    Forking and threading versions of each type of server can be created
    using the ForkingMixIn and ThreadingMixIn mix-in classes.  For
    instance, a threading UDP server class is created as follows:

            class ThreadingUDPServer(ThreadingMixIn, UDPServer): pass

    The Mix-in class must come first, since it overrides a method defined
    in UDPServer! Setting the various member variables also changes
    the behavior of the underlying server mechanism.

    To implement a service, you must derive a class from
    BaseRequestHandler and redefine its handle() method.  You can then run
    various versions of the service by combining one of the server classes
    with your request handler class.

    The request handler class must be different for datagram or stream
    services.  This can be hidden by using the request handler
    subclasses StreamRequestHandler or DatagramRequestHandler.

    Of course, you still have to use your head!

    For instance, it makes no sense to use a forking server if the service
    contains state in memory that can be modified by requests (since the
    modifications in the child process would never reach the initial state
    kept in the parent process and passed to each child).  In this case,
    you can use a threading server, but you will probably have to use
    locks to avoid two requests that come in nearly simultaneous to apply
    conflicting changes to the server state.

    On the other hand, if you are building e.g. an HTTP server, where all
    data is stored externally (e.g. in the file system), a synchronous
    class will essentially render the service "deaf" while one request is
    being handled -- which may be for a very long time if a client is slow
    to read all the data it has requested.  Here a threading or forking
    server is appropriate.

    In some cases, it may be appropriate to process part of a request
    synchronously, but to finish processing in a forked child depending on
    the request data.  This can be implemented by using a synchronous
    server and doing an explicit fork in the request handler class
    handle() method.

    Another approach to handling multiple simultaneous requests in an
    environment that supports neither threads nor fork (or where these are
    too expensive or inappropriate for the service) is to maintain an
    explicit table of partially finished requests and to use a selector to
    decide which request to work on next (or whether to handle a new
    incoming request).  This is particularly important for stream services
    where each client can potentially be connected for a long time (if
    threads or subprocesses cannot be used).

    Future work:
    - Standard classes for Sun RPC (which uses either UDP or TCP)
    - Standard mix-in classes to implement various authentication
      and encryption schemes

    XXX Open problems:
    - What to do with out-of-band data?

    BaseServer:
    - split generic "request" functionality out into BaseServer class.
      Copyright (C) 2000  Luke Kenneth Casson Leighton <lkcl@samba.org>

      example: read entries from a SQL database (requires overriding
      get_request() to return a table entry from the database).
      entry is processed by a RequestHandlerClass.

CLASSES
    builtins.object
        BaseRequestHandler
            DatagramRequestHandler
            StreamRequestHandler
        BaseServer
            TCPServer
  
```

## Related

Other standard-library modules pair well with `socketserver`; explore the `python` domain of this catalog.
