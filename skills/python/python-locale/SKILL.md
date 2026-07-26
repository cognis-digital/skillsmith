---
name: python-locale
description: "Program with Python's locale module: Locale support module."
version: 1.0.0
tags: [locale, programming, python, stdlib]
---

# Python: `locale`

## Overview

Locale support module.

The module provides low-level access to the C lib's locale APIs and adds high
level number formatting APIs as well as a locale aliasing engine to complement
these.

The aliasing engine includes support for many commonly used locale names and
maps them to values suitable for passing to the C lib's setlocale() function. It
also includes default encodings for all supported locale names.

## When to use

Reach for `locale` when your task calls for Locale support module. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import locale
```

## Key functions

- `locale.atof(string, func=<class 'float'>)`
- `locale.atoi(string)`
- `locale.currency(val, symbol=True, grouping=False, international=False)`
- `locale.delocalize(string)`
- `locale.format_string(f, val, grouping=False, monetary=False)`
- `locale.getdefaultlocale(envvars=('LC_ALL', 'LC_CTYPE', 'LANG', 'LANGUAGE'))`
- `locale.getencoding()`
- `locale.getlocale(category=2)`
- `locale.getpreferredencoding(do_setlocale=True)`
- `locale.localeconv()`
- `locale.localize(string, grouping=False, monetary=False)`
- `locale.normalize(localename)`
- `locale.setlocale(category, locale=None)`
- `locale.str(val)`
- `locale.strcoll(os1, os2, /)`
- `locale.strxfrm(string, /)`

## Key classes

`Error`

## Constants / attributes

`CHAR_MAX`, `LC_ALL`, `LC_COLLATE`, `LC_CTYPE`, `LC_MONETARY`, `LC_NUMERIC`, `LC_TIME`, `locale_alias`, `locale_encoding_alias`, `windows_locale`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import locale

def do_work(...):
    """Use locale to accomplish one well-defined task."""
    result = locale.atof(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `locale` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module locale

NAME
    locale - Locale support module.

MODULE REFERENCE
    https://docs.python.org/3.14/library/locale.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    The module provides low-level access to the C lib's locale APIs and adds high
    level number formatting APIs as well as a locale aliasing engine to complement
    these.

    The aliasing engine includes support for many commonly used locale names and
    maps them to values suitable for passing to the C lib's setlocale() function. It
    also includes default encodings for all supported locale names.

CLASSES
    builtins.Exception(builtins.BaseException)
        Error

    class Error(builtins.Exception)
     |  Method resolution order:
     |      Error
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
     |  Static methods inherited from builtins.Exception:
     |
     |  __new__(*args, **kwargs) class method of builtins.Exception
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

FUNCTIONS
    atof(string, func=<class 'float'>)
        Parses a string as a float according to the locale settings.

    atoi(string)
        Converts a string to an integer according to the locale settings.

    currency(val, symbol=True, grouping=False, international=False)
        Formats val according to the currency settings
        in the current locale.

    format_string(f, val, grouping=False, monetary=False)
        Formats a string in the same way that the % formatting would use,
        but takes the current locale into account.

        Grouping is applied if the third parameter is true.
        Conversion uses monetary thousands separator and grouping strings if
        forth parameter monetary is true.

    getdefaultlocale(envvars=('LC_ALL', 'LC_CTYPE', 'LANG', 'LANGUAGE'))
        Tries to determine the default locale settings and returns
        them as tuple (language code, encoding).

        According to POSIX, a program which has not called
        setlocale(LC_ALL, "") runs using the portable 'C' locale.
        Calling setlocale(LC_ALL, "") lets it use the default locale as
        defined by the LANG variable. Since we don't want to interfere
        with the current locale setting we thus emulate the behavior
        in the way described above.

        To maintain compatibility with other platforms, not only the
        LANG variable is tested, but a list of variables given as
        envvars parameter. The first found to be defined will be
        used. envvars defaults to the search path used in GNU gettext;
        it must always contain the variable name 'LANG'.

        Except for the code 'C', the language code corresponds to RFC
        1766.  code and encoding can be None in case the values cannot
        be determined.

    getencoding()
        Get the current locale encoding.

    getlocale(category=2)
        Returns the current setting for the given locale category as
        tuple (language code, encoding).

        category may be one of the LC_* value except LC_ALL. It
        defaults to LC_CTYPE.

        Except for the code 'C', the language code corresponds to RFC
        1766.  code and encoding can be None in case the values cannot
        be determined.

    getpreferredencoding(do_setlocale=True)
        Return the charset that the user is likely using.

    localeconv()
        Returns numeric and monetary locale-specific parameters.

    normalize(localename)
        Returns a normalized locale code for the given locale
        name.

        The returned locale code is formatted for use with
        setlocale().

        If normalization fails, the original name is returned
        unchanged.

        If the given encoding is not known, the function defaults to
        the default encoding for the locale code just like setlocale()
        does.

    setlocale(category, locale=None)
        Set the locale for the given category.  The locale can be
        a string, an iterable of two strings (language code and encoding),
        or None.

        Iterables are converted to strings using the locale aliasing
        engine.  Locale strings are passed directly to the C lib.

        category may be given as one of the LC_* values.

    str(val)
        Convert float to string, taking the locale into account.

    strcoll(os1, os2, /)
        Compares two strings according to the locale.

    strxfrm(string, /)
  
```

## Related

Other standard-library modules pair well with `locale`; explore the `python` domain of this catalog.
