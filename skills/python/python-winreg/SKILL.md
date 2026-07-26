---
name: python-winreg
description: "Program with Python's winreg module: This module provides access to the Windows registry API."
version: 1.0.0
tags: [programming, python, stdlib, winreg]
---

# Python: `winreg`

## Overview

This module provides access to the Windows registry API.

Functions:

CloseKey() - Closes a registry key.
ConnectRegistry() - Establishes a connection to a predefined registry handle
                    on another computer.
CreateKey() - Creates the specified key, or opens it if it already exists.
DeleteKey() - Deletes the specified key.
DeleteValue() - Removes a named value from the specified registry key.
EnumKey() - Enumerates subkeys of the specified open registry key.
EnumValue() - Enumerates values of the specified open registry key.
ExpandEnvironmentStrings() - Expand the env strings in a REG_EXPAND_SZ
                             string.
FlushKey() - Writes all the attributes of the specified key to the registry.
LoadKey() - Creates a subkey under HKEY_USER or HKEY_LOCAL_MACHINE and
            stores registration information from a specified file into that
            subkey.
OpenKey() - Opens the specified key.
OpenKeyEx() - Alias of OpenKey().
QueryValue() - Retrieves the value associated with the unnamed value for a
               specified key in the registry.
QueryValueEx() - Retrieves the type and data for a specified value name
                 associated with an open registry key.
QueryInfoKey() - Returns information about the specified key.
SaveKey() - Saves the specified key, and all its subkeys a file.
SetValue() - Associates a value with a specified key.
SetValueEx() - Stores data in the value field of an open registry key.

Special objects:

HKEYType -- type object for HKEY objects
error -- exception raised for Win32 errors

Integer constants:
Many constants are defined - see the documentation for each function
to see what constants are used, and where.

## When to use

Reach for `winreg` when your task calls for This module provides access to the Windows registry API. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import winreg
```

## Key functions

- `winreg.CloseKey(hkey, /)`
- `winreg.ConnectRegistry(computer_name, key, /)`
- `winreg.CreateKey(key, sub_key, /)`
- `winreg.CreateKeyEx(key, sub_key, reserved=0, access=131078)`
- `winreg.DeleteKey(key, sub_key, /)`
- `winreg.DeleteKeyEx(key, sub_key, access=256, reserved=0)`
- `winreg.DeleteValue(key, value, /)`
- `winreg.DisableReflectionKey(key, /)`
- `winreg.EnableReflectionKey(key, /)`
- `winreg.EnumKey(key, index, /)`
- `winreg.EnumValue(key, index, /)`
- `winreg.ExpandEnvironmentStrings(string, /)`
- `winreg.FlushKey(key, /)`
- `winreg.LoadKey(key, sub_key, file_name, /)`
- `winreg.OpenKey(key, sub_key, reserved=0, access=131097)`
- `winreg.OpenKeyEx(key, sub_key, reserved=0, access=131097)`
- `winreg.QueryInfoKey(key, /)`
- `winreg.QueryReflectionKey(key, /)`
- `winreg.QueryValue(key, sub_key, /)`
- `winreg.QueryValueEx(key, name, /)`
- `winreg.SaveKey(key, file_name, /)`
- `winreg.SetValue(key, sub_key, type, value, /)`
- `winreg.SetValueEx(key, value_name, reserved, type, value, /)`

## Key classes

`HKEYType`, `error`

## Constants / attributes

`HKEY_CLASSES_ROOT`, `HKEY_CURRENT_CONFIG`, `HKEY_CURRENT_USER`, `HKEY_DYN_DATA`, `HKEY_LOCAL_MACHINE`, `HKEY_PERFORMANCE_DATA`, `HKEY_USERS`, `KEY_ALL_ACCESS`, `KEY_CREATE_LINK`, `KEY_CREATE_SUB_KEY`, `KEY_ENUMERATE_SUB_KEYS`, `KEY_EXECUTE`, `KEY_NOTIFY`, `KEY_QUERY_VALUE`, `KEY_READ`, `KEY_SET_VALUE`, `KEY_WOW64_32KEY`, `KEY_WOW64_64KEY`, `KEY_WRITE`, `REG_BINARY`, `REG_CREATED_NEW_KEY`, `REG_DWORD`, `REG_DWORD_BIG_ENDIAN`, `REG_DWORD_LITTLE_ENDIAN`, `REG_EXPAND_SZ`, `REG_FULL_RESOURCE_DESCRIPTOR`, `REG_LEGAL_CHANGE_FILTER`, `REG_LEGAL_OPTION`, `REG_LINK`, `REG_MULTI_SZ`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import winreg

def do_work(...):
    """Use winreg to accomplish one well-defined task."""
    result = winreg.CloseKey(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `winreg` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: built-in module winreg

NAME
    winreg - This module provides access to the Windows registry API.

DESCRIPTION
    Functions:

    CloseKey() - Closes a registry key.
    ConnectRegistry() - Establishes a connection to a predefined registry handle
                        on another computer.
    CreateKey() - Creates the specified key, or opens it if it already exists.
    DeleteKey() - Deletes the specified key.
    DeleteValue() - Removes a named value from the specified registry key.
    EnumKey() - Enumerates subkeys of the specified open registry key.
    EnumValue() - Enumerates values of the specified open registry key.
    ExpandEnvironmentStrings() - Expand the env strings in a REG_EXPAND_SZ
                                 string.
    FlushKey() - Writes all the attributes of the specified key to the registry.
    LoadKey() - Creates a subkey under HKEY_USER or HKEY_LOCAL_MACHINE and
                stores registration information from a specified file into that
                subkey.
    OpenKey() - Opens the specified key.
    OpenKeyEx() - Alias of OpenKey().
    QueryValue() - Retrieves the value associated with the unnamed value for a
                   specified key in the registry.
    QueryValueEx() - Retrieves the type and data for a specified value name
                     associated with an open registry key.
    QueryInfoKey() - Returns information about the specified key.
    SaveKey() - Saves the specified key, and all its subkeys a file.
    SetValue() - Associates a value with a specified key.
    SetValueEx() - Stores data in the value field of an open registry key.

    Special objects:

    HKEYType -- type object for HKEY objects
    error -- exception raised for Win32 errors

    Integer constants:
    Many constants are defined - see the documentation for each function
    to see what constants are used, and where.

CLASSES
    builtins.object
        PyHKEY

    HKEYType = class PyHKEY(builtins.object)
     |  PyHKEY Object - A Python object, representing a win32 registry key.
     |
     |  This object wraps a Windows HKEY object, automatically closing it when
     |  the object is destroyed.  To guarantee cleanup, you can call either
     |  the Close() method on the PyHKEY, or the CloseKey() method.
     |
     |  All functions which accept a handle object also accept an integer --
     |  however, use of the handle object is encouraged.
     |
     |  Functions:
     |  Close() - Closes the underlying handle.
     |  Detach() - Returns the integer Win32 handle, detaching it from the object
     |
     |  Properties:
     |  handle - The integer Win32 handle.
     |
     |  Operations:
     |  __bool__ - Handles with an open object return true, otherwise false.
     |  __int__ - Converting a handle to an integer returns the Win32 handle.
     |  rich comparison - Handle objects are compared using the handle value.
     |
     |  Methods defined here:
     |
     |  Close(self, /)
     |      Closes the underlying Windows handle.
     |
     |      If the handle is already closed, no error is raised.
     |
     |  Detach(self, /)
     |      Detaches the Windows handle from the handle object.
     |
     |      The result is the value of the handle before it is detached.  If the
     |      handle is already detached, this will return zero.
     |
     |      After calling this function, the handle is effectively invalidated,
     |      but the handle is not closed.  You would call this function when you
     |      need the underlying win32 handle to exist beyond the lifetime of the
     |      handle object.
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
     |  __divmod__(self, value, /)
     |      Return divmod(self, value).
     |
     |  __enter__(self, /)
     |
     |  __exit__(self, exc_type, exc_value, traceback, /)
     |
     |  __float__(self, /)
     |      float(self)
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __int__(self, /)
     |      int(self)
     |
     |  __invert__(self, /)
     |      ~self
     |
     |  __lshift__(self, value, /)
     |      Return self<<value.
     |
     |  __mod__(self, value, /)
     |      Return self%value.
     |
     |  __mul__(self, value, /)
     |      Return self*value.
     |
     |  __neg__(self, /)
     |      -self
     |
     |  __or__(self, value, /)
     |      Return self|value.
     |
     |  __pos__(self, /)
     |      +self
     |
     |  __pow__(self, value, mod=None, /)
     |      Return pow(self, value, mod).
     |
     |  __radd__(self, value, /)
     |      Return value+self.
     |
     |  __rand__(self, value, /)
     |      Return value&self.
     |
     |  __rdivmod__(self, value, /)
     |      Return divmod(value, self).
     |
     |  __rlshift__(self, value, /)
     |      Return value<<self.
     |
     |  __rmod__(self, value, /)
     |      Return value%self.
     |
     |  __rmul__(self, value, /)
     |      Return value*self.
     |
     |  __ror__(self, value, /)
     |      Return value|self.
     |
     |  __rpow__(self, value, mod=None, /)
     |      Return pow(value, self, mod).
     |
     |  __rrshift__(self, value, /)
     |      Return value>>self.
     |
     |  __rshift__(self, value, /)
     |      Return self>>value.
     |
     |  __rsub__(self, value, /)
     |      Return value-self.
     |
     |  __rxor__(self, value, /)
     |      Return value^self.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  __sub__(self, value, /)
     |      Return self-value.
     |
     |  __xor__(self, value, /)
     |      Return self^value.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors
```

## Related

Other standard-library modules pair well with `winreg`; explore the `python` domain of this catalog.
