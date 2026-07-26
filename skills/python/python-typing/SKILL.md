---
name: python-typing
description: "Program with Python's typing module: The typing module: Support for gradual typing as defined by PEP 484 and subsequent PEPs."
version: 1.0.0
tags: [programming, python, stdlib, typing]
---

# Python: `typing`

## Overview

The typing module: Support for gradual typing as defined by PEP 484 and subsequent PEPs.

Among other things, the module includes the following:
* Generic, Protocol, and internal machinery to support generic aliases.
  All subscripted types like X[int], Union[int, str] are generic aliases.
* Various "special forms" that have unique meanings in type annotations:
  NoReturn, Never, ClassVar, Self, Concatenate, Unpack, and others.
* Classes whose instances can be type arguments to generic classes and functions:
  TypeVar, ParamSpec, TypeVarTuple.
* Public helper functions: get_type_hints, overload, cast, final, and others.
* Several protocols to support duck-typing:
  SupportsFloat, SupportsIndex, SupportsAbs, and others.
* Special types: NewType, NamedTuple, TypedDict.
* Deprecated aliases for builtin types and collections.abc ABCs.

Any name not present in __all__ is an implementation detail
that may be changed without notice. Use at your own risk!

## When to use

Reach for `typing` when your task calls for The typing module: Support for gradual typing as defined by PEP 484 and subsequent PEPs. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import typing
```

## Key functions

- `typing.AbstractSet(*args, **kwargs)`
- `typing.Annotated(*args, **kwds)`
- `typing.AsyncGenerator(*args, **kwargs)`
- `typing.AsyncIterable(*args, **kwargs)`
- `typing.AsyncIterator(*args, **kwargs)`
- `typing.Awaitable(*args, **kwargs)`
- `typing.ByteString(*args, **kwargs)`
- `typing.Callable(*args, **kwargs)`
- `typing.ChainMap(*args, **kwargs)`
- `typing.ClassVar(*args, **kwds)`
- `typing.Collection(*args, **kwargs)`
- `typing.Concatenate(*args, **kwds)`
- `typing.Container(*args, **kwargs)`
- `typing.Coroutine(*args, **kwargs)`
- `typing.Counter(*args, **kwargs)`
- `typing.DefaultDict(*args, **kwargs)`
- `typing.Deque(*args, **kwargs)`
- `typing.Dict(*args, **kwargs)`
- `typing.Final(*args, **kwds)`
- `typing.FrozenSet(*args, **kwargs)`
- `typing.Generator(*args, **kwargs)`
- `typing.Hashable(*args, **kwargs)`
- `typing.ItemsView(*args, **kwargs)`
- `typing.Iterable(*args, **kwargs)`
- `typing.Iterator(*args, **kwargs)`
- `typing.KeysView(*args, **kwargs)`
- `typing.List(*args, **kwargs)`
- `typing.Literal(*args, **kwds)`
- `typing.LiteralString(*args, **kwds)`
- `typing.Mapping(*args, **kwargs)`

## Key classes

`ABCMeta`, `Any`, `BinaryIO`, `Generic`, `GenericAlias`, `IO`, `NamedTupleMeta`, `NewType`, `ParamSpec`, `ParamSpecArgs`, `ParamSpecKwargs`, `Protocol`, `SupportsAbs`, `SupportsBytes`, `SupportsComplex`, `SupportsFloat`, `SupportsIndex`, `SupportsInt`, `SupportsRound`, `Text`, `TextIO`, `TypeAliasType`, `TypeVar`, `TypeVarTuple`, `Union`, `defaultdict`

## Constants / attributes

`AnyStr`, `CT_co`, `EXCLUDED_ATTRIBUTES`, `KT`, `NoDefault`, `T`, `TYPE_CHECKING`, `T_co`, `T_contra`, `VT`, `VT_co`, `V_co`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import typing

def do_work(...):
    """Use typing to accomplish one well-defined task."""
    result = typing.AbstractSet(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `typing` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module typing

NAME
    typing - The typing module: Support for gradual typing as defined by PEP 484 and subsequent PEPs.

MODULE REFERENCE
    https://docs.python.org/3.14/library/typing.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Among other things, the module includes the following:
    * Generic, Protocol, and internal machinery to support generic aliases.
      All subscripted types like X[int], Union[int, str] are generic aliases.
    * Various "special forms" that have unique meanings in type annotations:
      NoReturn, Never, ClassVar, Self, Concatenate, Unpack, and others.
    * Classes whose instances can be type arguments to generic classes and functions:
      TypeVar, ParamSpec, TypeVarTuple.
    * Public helper functions: get_type_hints, overload, cast, final, and others.
    * Several protocols to support duck-typing:
      SupportsFloat, SupportsIndex, SupportsAbs, and others.
    * Special types: NewType, NamedTuple, TypedDict.
    * Deprecated aliases for builtin types and collections.abc ABCs.

    Any name not present in __all__ is an implementation detail
    that may be changed without notice. Use at your own risk!

CLASSES
    builtins.object
        builtins.str
        Any
        Generic
            IO
                BinaryIO
                TextIO
            Protocol
                SupportsAbs
                SupportsBytes
                SupportsComplex
                SupportsFloat
                SupportsIndex
                SupportsInt
                SupportsRound
        NewType
        ParamSpec
        ParamSpecArgs
        ParamSpecKwargs
        TypeAliasType
        TypeVar
        TypeVarTuple
        Union

    class Any(builtins.object)
     |  Any(*args, **kwargs)
     |
     |  Special type indicating an unconstrained type.
     |
     |  - Any is compatible with every type.
     |  - Any assumed to have all methods.
     |  - All values assumed to be instances of Any.
     |
     |  Note that all the above statements are true from the point of view of
     |  static type checkers. At runtime, Any should not be used with instance
     |  checks.
     |
     |  Static methods defined here:
     |
     |  __new__(cls, *args, **kwargs)
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class BinaryIO(IO)
     |  Typed version of the return of open() in binary mode.
     |
     |  Method resolution order:
     |      BinaryIO
     |      IO
     |      Generic
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __enter__(self) -> BinaryIO
     |
     |  write(self, s: bytes | bytearray) -> int
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __orig_bases__ = (typing.IO[bytes],)
     |
     |  __parameters__ = ()
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from IO:
     |
     |  __exit__(self, type, value, traceback) -> None
     |
     |  close(self) -> None
     |
     |  fileno(self) -> int
     |
     |  flush(self) -> None
     |
     |  isatty(self) -> bool
     |
     |  read(self, n: int = -1) -> AnyStr
     |
     |  readable(self) -> bool
     |
     |  readline(self, limit: int = -1) -> AnyStr
     |
     |  readlines(self, hint: int = -1) -> list[AnyStr]
     |
     |  seek(self, offset: int, whence: int = 0) -> int
     |
     |  seekable(self) -> bool
     |
     |  tell(self) -> int
     |
     |  truncate(self, size: int | None = None) -> int
     |
     |  writable(self) -> bool
     |
     |  writelines(self, lines: list[AnyStr]) -> None
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties inherited from IO:
     |
     |  closed
     |
     |  mode
     |
     |  name
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from Generic:
     |
     |  __class_getitem__(...)
     |      Parameterizes a generic class.
     |
     |      At least, parameterizing a generic class is the *main* thing this
     |      method does. For example, for some generic class `Foo`, this is called
     |      when we do `Foo[int]` - there, with `cls=Foo` and `params=int`.
     |
     |      However, note that this method is also called when defining generic
     |      classes in the first place with `class Foo[T]: ...`.
     |
     |  __init_subclass__(...)
     |      Function to initialize subclasses.

    class Generic(builtins.object)
     |  Abstract base class for generic types.
     |
     |  On Python 3.12 and newer, generic classes implicitly inherit from
     |  Generic when they declare a parameter list after the class's name::
     |
     |      class Mapping[KT, VT]:
     |          def __getitem__(self, key: KT) -> VT:
     |              ...
     |          # Etc.
     |
     |  On older versions of Python, however, generic classes have to
     |  explicitly inherit from Generic.
     |
     |  After a class has been declared to be generic, it can then be used as
     |  follows::
     |
     |      def lookup_name[KT, VT](mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
     |          try:
     |              return mapping[key]
     |          except KeyError:
     |            
```

## Related

Other standard-library modules pair well with `typing`; explore the `python` domain of this catalog.
