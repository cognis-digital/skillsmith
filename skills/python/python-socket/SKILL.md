---
name: python-socket
description: "Program with Python's socket module: This module provides socket operations and some related functions."
version: 1.0.0
tags: [programming, python, socket, stdlib]
---

# Python: `socket`

## Overview

This module provides socket operations and some related functions.
On Unix, it supports IP (Internet Protocol) and Unix domain sockets.
On other systems, it only supports IP. Functions specific for a
socket are available as methods of the socket object.

Functions:

socket() -- create a new socket object
socketpair() -- create a pair of new socket objects [*]
fromfd() -- create a socket object from an open file descriptor [*]
send_fds() -- Send file descriptor to the socket.
recv_fds() -- Receive file descriptors from the socket.
fromshare() -- create a socket object from data received from socket.share() [*]
gethostname() -- return the current hostname
gethostbyname() -- map a hostname to its IP number
gethostbyaddr() -- map an IP number or hostname to DNS info
getservbyname() -- map a service name and a protocol name to a port number
getprotobyname() -- map a protocol name (e.g. 'tcp') to a number
ntohs(), ntohl() -- convert 16, 32 bit int from network to host byte order
htons(), htonl() -- convert 16, 32 bit int from host to network byte order
inet_aton() -- convert IP addr string (123.45.67.89) to 32-bit packed format
inet_ntoa() -- convert 32-bit packed format IP to string (123.45.67.89)
socket.getdefaulttimeout() -- get the default timeout value
socket.setdefaulttimeout() -- set the default timeout value
create_connection() -- connects to an address, with an optional timeout and
                       optional source address.
create_server() -- create a TCP socket and bind it to a specified address.

 [*] not available on all platforms!

Special objects:

SocketType -- type object for socket objects
error -- exception raised for I/O errors
has_ipv6 -- boolean value indicating if IPv6 is supported

IntEnum constants:

AF_INET, AF_UNIX -- socket domains (first argument to socket() call)
SOCK_STREAM, SOCK_DGRAM, SOCK_RAW -- socket types (second argument)

Integer constants:

Many other constants may be defined; these may be used in calls to
the setsockopt() and getsockopt() methods.

## When to use

Reach for `socket` when your task calls for This module provides socket operations and some related functions. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import socket
```

## Key functions

- `socket.close(object, /)`
- `socket.create_connection(address, timeout=<object object at 0x000001B05F3318D0>, source_address=None, *, all_errors=False)`
- `socket.create_server(address, *, family=<AddressFamily.AF_INET: 2>, backlog=None, reuse_port=False, dualstack_ipv6=False)`
- `socket.dup(object, /)`
- `socket.fromfd(fd, family, type, proto=0)`
- `socket.fromshare(info)`
- `socket.getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)`
- `socket.getdefaulttimeout()`
- `socket.getfqdn(name='')`
- `socket.gethostbyaddr(...)`
- `socket.gethostbyname(...)`
- `socket.gethostbyname_ex(...)`
- `socket.gethostname()`
- `socket.getnameinfo(...)`
- `socket.getprotobyname(...)`
- `socket.getservbyname(...)`
- `socket.getservbyport(...)`
- `socket.has_dualstack_ipv6()`
- `socket.htonl(integer, /)`
- `socket.htons(integer, /)`
- `socket.if_indextoname(if_index, /)`
- `socket.if_nameindex()`
- `socket.if_nametoindex(oname, /)`
- `socket.inet_aton(ip_addr, /)`
- `socket.inet_ntoa(packed_ip, /)`
- `socket.inet_ntop(...)`
- `socket.inet_pton(...)`
- `socket.ntohl(integer, /)`
- `socket.ntohs(integer, /)`
- `socket.setdefaulttimeout(object, /)`

## Key classes

`AddressFamily`, `AddressInfo`, `IntEnum`, `IntFlag`, `MsgFlag`, `SocketIO`, `SocketKind`, `SocketType`, `error`, `gaierror`, `herror`, `socket`, `timeout`

## Constants / attributes

`AF_APPLETALK`, `AF_BLUETOOTH`, `AF_DECnet`, `AF_HYPERV`, `AF_INET`, `AF_INET6`, `AF_IPX`, `AF_IRDA`, `AF_LINK`, `AF_SNA`, `AF_UNSPEC`, `AI_ADDRCONFIG`, `AI_ALL`, `AI_CANONNAME`, `AI_NUMERICHOST`, `AI_NUMERICSERV`, `AI_PASSIVE`, `AI_V4MAPPED`, `BDADDR_ANY`, `BDADDR_LOCAL`, `BTPROTO_RFCOMM`, `CAPI`, `EAGAIN`, `EAI_AGAIN`, `EAI_BADFLAGS`, `EAI_FAIL`, `EAI_FAMILY`, `EAI_MEMORY`, `EAI_NODATA`, `EAI_NONAME`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import socket

def do_work(...):
    """Use socket to accomplish one well-defined task."""
    result = socket.close(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `socket` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module socket

NAME
    socket

MODULE REFERENCE
    https://docs.python.org/3.14/library/socket.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides socket operations and some related functions.
    On Unix, it supports IP (Internet Protocol) and Unix domain sockets.
    On other systems, it only supports IP. Functions specific for a
    socket are available as methods of the socket object.

    Functions:

    socket() -- create a new socket object
    socketpair() -- create a pair of new socket objects [*]
    fromfd() -- create a socket object from an open file descriptor [*]
    send_fds() -- Send file descriptor to the socket.
    recv_fds() -- Receive file descriptors from the socket.
    fromshare() -- create a socket object from data received from socket.share() [*]
    gethostname() -- return the current hostname
    gethostbyname() -- map a hostname to its IP number
    gethostbyaddr() -- map an IP number or hostname to DNS info
    getservbyname() -- map a service name and a protocol name to a port number
    getprotobyname() -- map a protocol name (e.g. 'tcp') to a number
    ntohs(), ntohl() -- convert 16, 32 bit int from network to host byte order
    htons(), htonl() -- convert 16, 32 bit int from host to network byte order
    inet_aton() -- convert IP addr string (123.45.67.89) to 32-bit packed format
    inet_ntoa() -- convert 32-bit packed format IP to string (123.45.67.89)
    socket.getdefaulttimeout() -- get the default timeout value
    socket.setdefaulttimeout() -- set the default timeout value
    create_connection() -- connects to an address, with an optional timeout and
                           optional source address.
    create_server() -- create a TCP socket and bind it to a specified address.

     [*] not available on all platforms!

    Special objects:

    SocketType -- type object for socket objects
    error -- exception raised for I/O errors
    has_ipv6 -- boolean value indicating if IPv6 is supported

    IntEnum constants:

    AF_INET, AF_UNIX -- socket domains (first argument to socket() call)
    SOCK_STREAM, SOCK_DGRAM, SOCK_RAW -- socket types (second argument)

    Integer constants:

    Many other constants may be defined; these may be used in calls to
    the setsockopt() and getsockopt() methods.

CLASSES
    builtins.Exception(builtins.BaseException)
        builtins.OSError
            builtins.TimeoutError
            gaierror
            herror
    builtins.object
        _socket.socket
            socket
    enum.IntEnum(builtins.int, enum.ReprEnum)
        AddressFamily
        SocketKind

    class AddressFamily(enum.IntEnum)
     |  AddressFamily(*values)
     |
     |  An enumeration.
     |
     |  Method resolution order:
     |      AddressFamily
     |      enum.IntEnum
     |      builtins.int
     |      enum.ReprEnum
     |      enum.Enum
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __format__(self, format_spec, /) from builtins.int
     |      Convert to a string according to format_spec.
     |
     |  __new__(cls, value) from enum.Enum
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  AF_APPLETALK = <AddressFamily.AF_APPLETALK: 16>
     |
     |  AF_BLUETOOTH = <AddressFamily.AF_BLUETOOTH: 32>
     |
     |  AF_HYPERV = <AddressFamily.AF_HYPERV: 34>
     |
     |  AF_INET = <AddressFamily.AF_INET: 2>
     |
     |  AF_INET6 = <AddressFamily.AF_INET6: 23>
     |
     |  AF_IPX = <AddressFamily.AF_IPX: 6>
     |
     |  AF_IRDA = <AddressFamily.AF_IRDA: 26>
     |
     |  AF_LINK = <AddressFamily.AF_LINK: 33>
     |
     |  AF_SNA = <AddressFamily.AF_SNA: 11>
     |
     |  AF_UNSPEC = <AddressFamily.AF_UNSPEC: 0>
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from enum.IntEnum:
     |
     |  __repr__(self) from enum.Enum
     |      Return repr(self).
     |
     |  __str__ = __repr__(self, /) from builtins.int
     |      Return repr(self).
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.int:
     |
     |  __abs__(self, /)
     |      abs(self)
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __and__(self, value, /)
     |      Return self&value.
     |
     |  __bool__(self, /)
     |      True if self else False
     |
     |  __ceil__(self, /)
     |      Ceiling of an Integral returns itself.
     |
     |  __divmod__(self, value, /)
     |      Return divmod(self, value).
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __float__(self, /)
     |      float(self)
     |
     |  __floor__(self, /)
     |      Flooring an Integral returns itself.
     |
     |  __floordiv__(self, value, /)
     |      Return self//value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getnewargs__(self, /)
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __index__(self, /)
     |      Return self converted to an integer, if self is suitable for use as an index into a list.
     |
     |  __int__(self, /)
     |      int(self)
     |
     |  __invert__(self, /)
     |      ~self
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __lshift__(self, value, /)
     |      Return self<<value.
     |
     |  
```

## Related

Other standard-library modules pair well with `socket`; explore the `python` domain of this catalog.
