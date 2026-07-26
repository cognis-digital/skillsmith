---
name: python-types
description: "Program with Python's types module: Define names for built-in types that aren't directly accessible as a builtin."
version: 1.0.0
tags: [programming, python, stdlib, types]
---

# Python: `types`

## Overview

Define names for built-in types that aren't directly accessible as a builtin.

## When to use

Reach for `types` when your task calls for Define names for built-in types that aren't directly accessible as a builtin. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import types
```

## Key functions

- `types.coroutine(func)`
- `types.get_original_bases(cls, /)`
- `types.new_class(name, bases=(), kwds=None, exec_body=None)`
- `types.prepare_class(name, bases=(), kwds=None)`
- `types.resolve_bases(bases)`

## Key classes

`AsyncGeneratorType`, `BuiltinFunctionType`, `BuiltinMethodType`, `CapsuleType`, `CellType`, `ClassMethodDescriptorType`, `CodeType`, `CoroutineType`, `DynamicClassAttribute`, `EllipsisType`, `FrameType`, `FunctionType`, `GeneratorType`, `GenericAlias`, `GetSetDescriptorType`, `LambdaType`, `MappingProxyType`, `MemberDescriptorType`, `MethodDescriptorType`, `MethodType`, `MethodWrapperType`, `ModuleType`, `NoneType`, `NotImplementedType`, `SimpleNamespace`, `TracebackType`, `UnionType`, `WrapperDescriptorType`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import types

def do_work(...):
    """Use types to accomplish one well-defined task."""
    result = types.coroutine(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `types` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module types

NAME
    types - Define names for built-in types that aren't directly accessible as a builtin.

MODULE REFERENCE
    https://docs.python.org/3.14/library/types.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.object
        builtins.NoneType
        builtins.NotImplementedType
        builtins.PyCapsule
        builtins.async_generator
        builtins.builtin_function_or_method
        builtins.cell
        builtins.classmethod_descriptor
        builtins.code
        builtins.coroutine
        builtins.ellipsis
        builtins.frame
        builtins.function
        builtins.generator
        builtins.getset_descriptor
        builtins.mappingproxy
        builtins.member_descriptor
        builtins.method
        builtins.method-wrapper
        builtins.method_descriptor
        builtins.module
        builtins.traceback
        builtins.wrapper_descriptor
        DynamicClassAttribute
        GenericAlias
        SimpleNamespace
        typing.Union

    AsyncGeneratorType = class async_generator(object)
     |  Methods defined here:
     |
     |  __aiter__(self, /)
     |      Return an awaitable, that resolves in asynchronous iterator.
     |
     |  __anext__(self, /)
     |      Return a value or raise StopAsyncIteration.
     |
     |  __del__(self, /)
     |      Called when the instance is about to be destroyed.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __sizeof__(self, /)
     |      gen.__sizeof__() -> size of gen in memory, in bytes
     |
     |  aclose(self, /)
     |      aclose() -> raise GeneratorExit inside generator.
     |
     |  asend(self, object, /)
     |      asend(v) -> send 'v' in generator.
     |
     |  athrow(...)
     |      athrow(value)
     |      athrow(type[,value[,tb]])
     |
     |      raise exception in generator.
     |      the (type, val, tb) signature is deprecated,
     |      and may be removed in a future version of Python.
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  __class_getitem__(object, /)
     |      See PEP 585
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  ag_await
     |      object being awaited on, or None
     |
     |  ag_code
     |
     |  ag_frame
     |
     |  ag_running
     |
     |  ag_suspended

    BuiltinFunctionType = class builtin_function_or_method(object)
     |  Built-in subclasses:
     |      builtin_method
     |
     |  Methods defined here:
     |
     |  __call__(self, /, *args, **kwargs)
     |      Call self as a function.
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __reduce__(self, /)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __self__
     |
     |  __text_signature__

    BuiltinMethodType = class builtin_function_or_method(object)
     |  Built-in subclasses:
     |      builtin_method
     |
     |  Methods defined here:
     |
     |  __call__(self, /, *args, **kwargs)
     |      Call self as a function.
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __reduce__(self, /)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __self__
     |
     |  __text_signature__

    CapsuleType = class PyCapsule(object)
     |  Capsule objects let you wrap a C "void *" pointer in a Python
     |  object.  They're a way of passing data through the Python interpreter
     |  without creating your own custom type.
     |
     |  Capsules are used for communication between extension modules.
     |  They provide a way for an extension module to export a C interface
     |  to other extension modules, so that extension modules can use the
     |  Python import mechanism to link to one another.
     |
     |  Methods defined here:
     |
     |  __repr__(self, /)
     |      Return repr(self).

    CellType = class cell(object)
     |  CellType([contents])
     |
     |  Create a new cell object.
     |
     |   contents
     |     the contents of the cell. If not specified, the cell will be empty,
     |     and
     |  further attempts to access its cell_contents attribute will
     |     raise a ValueError.
     |
     |  Methods defined here:
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __gt
```

## Related

Other standard-library modules pair well with `types`; explore the `python` domain of this catalog.
