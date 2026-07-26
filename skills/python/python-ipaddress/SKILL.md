---
name: python-ipaddress
description: "Program with Python's ipaddress module: A fast, lightweight IPv4/IPv6 manipulation library in Python."
version: 1.0.0
tags: [ipaddress, programming, python, stdlib]
---

# Python: `ipaddress`

## Overview

A fast, lightweight IPv4/IPv6 manipulation library in Python.

This library is used to create/poke/manipulate IPv4 and IPv6 addresses
and networks.

## When to use

Reach for `ipaddress` when your task calls for A fast, lightweight IPv4/IPv6 manipulation library in Python. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import ipaddress
```

## Key functions

- `ipaddress.collapse_addresses(addresses)`
- `ipaddress.get_mixed_type_key(obj)`
- `ipaddress.ip_address(address)`
- `ipaddress.ip_interface(address)`
- `ipaddress.ip_network(address, strict=True)`
- `ipaddress.summarize_address_range(first, last)`
- `ipaddress.v4_int_to_packed(address)`
- `ipaddress.v6_int_to_packed(address)`

## Key classes

`AddressValueError`, `IPv4Address`, `IPv4Interface`, `IPv4Network`, `IPv6Address`, `IPv6Interface`, `IPv6Network`, `NetmaskValueError`

## Constants / attributes

`IPV4LENGTH`, `IPV6LENGTH`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import ipaddress

def do_work(...):
    """Use ipaddress to accomplish one well-defined task."""
    result = ipaddress.collapse_addresses(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `ipaddress` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module ipaddress

NAME
    ipaddress - A fast, lightweight IPv4/IPv6 manipulation library in Python.

MODULE REFERENCE
    https://docs.python.org/3.14/library/ipaddress.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This library is used to create/poke/manipulate IPv4 and IPv6 addresses
    and networks.

CLASSES
    builtins.ValueError(builtins.Exception)
        AddressValueError
        NetmaskValueError
    _BaseAddress(_IPAddressBase)
        IPv4Address(_BaseV4, _BaseAddress)
            IPv4Interface
        IPv6Address(_BaseV6, _BaseAddress)
            IPv6Interface
    _BaseNetwork(_IPAddressBase)
        IPv4Network(_BaseV4, _BaseNetwork)
        IPv6Network(_BaseV6, _BaseNetwork)
    _BaseV4(builtins.object)
        IPv4Address(_BaseV4, _BaseAddress)
            IPv4Interface
        IPv4Network(_BaseV4, _BaseNetwork)
    _BaseV6(builtins.object)
        IPv6Address(_BaseV6, _BaseAddress)
            IPv6Interface
        IPv6Network(_BaseV6, _BaseNetwork)

    class AddressValueError(builtins.ValueError)
     |  A Value Error related to the address.
     |
     |  Method resolution order:
     |      AddressValueError
     |      builtins.ValueError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors defined here:
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.ValueError:
     |
     |  __new__(*args, **kwargs) class method of builtins.ValueError
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__(self, /)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setstate__(self, state, /)
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  add_note(self, note, /)
     |      Add a note to the exception
     |
     |  with_traceback(self, tb, /)
     |      Set self.__traceback__ to tb and return self.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |
     |  __cause__
     |
     |  __context__
     |
     |  __dict__
     |
     |  __suppress_context__
     |
     |  __traceback__
     |
     |  args

    class IPv4Address(_BaseV4, _BaseAddress)
     |  IPv4Address(address)
     |
     |  Represent and manipulate single IPv4 Addresses.
     |
     |  Method resolution order:
     |      IPv4Address
     |      _BaseV4
     |      _BaseAddress
     |      _IPAddressBase
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, address)
     |      Args:
     |          address: A string or integer representing the IP
     |
     |            Additionally, an integer can be passed, so
     |            IPv4Address('192.0.2.1') == IPv4Address(3221225985).
     |            or, more generally
     |            IPv4Address(int(IPv4Address('192.0.2.1'))) ==
     |              IPv4Address('192.0.2.1')
     |
     |      Raises:
     |          AddressValueError: If ipaddress isn't a valid IPv4 address.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  ipv6_mapped
     |      Return the IPv4-mapped IPv6 address.
     |
     |      Returns:
     |          The IPv4-mapped IPv6 address per RFC 4291.
     |
     |  is_global
     |      ``True`` if the address is defined as globally reachable by
     |      iana-ipv4-special-registry_ (for IPv4) or iana-ipv6-special-registry_
     |      (for IPv6) with the following exception:
     |
     |      For IPv4-mapped IPv6-addresses the ``is_private`` value is determined by the
     |      semantics of the underlying IPv4 addresses and the following condition holds
     |      (see :attr:`IPv6Address.ipv4_mapped`)::
     |
     |          address.is_global == address.ipv4_mapped.is_global
     |
     |      ``is_global`` has value opposite to :attr:`is_private`, except for the ``100.64.0.0/10``
     |      IPv4 range where they are both ``False``.
     |
     |  is_link_local
     |      Test if the address is reserved for link-local.
     |
     |      Returns:
     |          A boolean, True if the address is link-local per RFC 3927.
     |
     |  is_loopback
     |      Test if the address is a loopback address.
     |
     |      Returns:
     |          A boolean, True if the address is a loopback per RFC 3330.
     |
     |  is_multicast
     |      Test if the address is reserved for multicast use.
     |
     |      Returns:
     |          A boolean, True if the address is multicast.
     |          See RFC 3171 for details.
     |
     |  is_private
     |      ``True`` if the address is defined as not globally reachable by
     |      iana-ipv4-special-registry_ (for IPv4) or iana-ipv6-special-registry_
     |      (for IPv6) with the following exceptions:
     |
     |      * ``is_private`` is ``False`` for ``100.64.0.0/10``
     |      * For IPv4-mapped IPv6-addresses the ``is_private`` value is determined by the
     |          semantics of the underlying IPv4 addresses and the following condition holds
     |          (see :attr:`IPv6Address.i
```

## Related

Other standard-library modules pair well with `ipaddress`; explore the `python` domain of this catalog.
