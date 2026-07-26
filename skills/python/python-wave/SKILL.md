---
name: python-wave
description: "Program with Python's wave module: Stuff to parse WAVE files."
version: 1.0.0
tags: [programming, python, stdlib, wave]
---

# Python: `wave`

## Overview

Stuff to parse WAVE files.

Usage.

Reading WAVE files:
      f = wave.open(file, 'r')
where file is either the name of a file or an open file pointer.
The open file pointer must have methods read(), seek(), and close().
When the setpos() and rewind() methods are not used, the seek()
method is not  necessary.

This returns an instance of a class with the following public methods:
      getnchannels()  -- returns number of audio channels (1 for
                         mono, 2 for stereo)
      getsampwidth()  -- returns sample width in bytes
      getframerate()  -- returns sampling frequency
      getnframes()    -- returns number of audio frames
      getcomptype()   -- returns compression type ('NONE' for linear samples)
      getcompname()   -- returns human-readable version of
                         compression type ('not compressed' linear samples)
      getparams()     -- returns a namedtuple consisting of all of the
                         above in the above order
      getmarkers()    -- returns None (for compatibility with the
                         old aifc module)
      getmark(id)     -- raises an error since the mark does not
                         exist (for compatibility with the old aifc module)
      readframes(n)   -- returns at most n frames of audio
      rewind()        -- rewind to the beginning of the audio stream
      setpos(pos)     -- seek to the specified position
      tell()          -- return the current position
      close()         -- close the instance (make it unusable)
The position returned by tell() and the position given to setpos()
are compatible and have nothing to do with the actual position in the
file.
The close() method is called automatically when the class instance
is destroyed.

Writing WAVE files:
      f = wave.open(file, 'w')
where file is either the name of a file or an open file pointer.
The open file pointer must have methods write(), tell(), seek(), and
close().

This returns an instance of a class with the following public methods:
      setnchannels(n) -- set the number of channels
      setsampwidth(n) -- set the sample width
      setframerate(n) -- set the frame rate
      setnframes(n)   -- set the number of frames
      setcomptype(type, name)
                      -- set the compression type and the
                         human-readable compression type
      setparams(tuple)
                      -- set all parameters at once
      tell()          -- return current position in output file
      writeframesraw(data)
                      -- write audio frames without patching up the
                         file header
      writeframes(data)
                      -- write audio frames and patch up the file header
      close()         -- patch up the file header and close the
                         output file
You should set the parameters before the first writeframesraw or
writeframes.  The total number of frames does not need to be set,
but when it is set to the correct value, the header does not have to
be patched up.
It is best to first set all parameters, perhaps possibly the
compression type, and then write audio frames using writeframesraw.
When all frames have been written, either call writeframes(b'') or
close() to patch up the sizes in the header.
The close() method is called automatically when the class instance
is destroyed.

## When to use

Reach for `wave` when your task calls for Stuff to parse WAVE files. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import wave
```

## Key functions

- `wave.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)`
- `wave.open(f, mode=None)`

## Key classes

`Error`, `Wave_read`, `Wave_write`

## Constants / attributes

`KSDATAFORMAT_SUBTYPE_PCM`, `WAVE_FORMAT_EXTENSIBLE`, `WAVE_FORMAT_PCM`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import wave

def do_work(...):
    """Use wave to accomplish one well-defined task."""
    result = wave.namedtuple(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `wave` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module wave

NAME
    wave - Stuff to parse WAVE files.

MODULE REFERENCE
    https://docs.python.org/3.14/library/wave.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Usage.

    Reading WAVE files:
          f = wave.open(file, 'r')
    where file is either the name of a file or an open file pointer.
    The open file pointer must have methods read(), seek(), and close().
    When the setpos() and rewind() methods are not used, the seek()
    method is not  necessary.

    This returns an instance of a class with the following public methods:
          getnchannels()  -- returns number of audio channels (1 for
                             mono, 2 for stereo)
          getsampwidth()  -- returns sample width in bytes
          getframerate()  -- returns sampling frequency
          getnframes()    -- returns number of audio frames
          getcomptype()   -- returns compression type ('NONE' for linear samples)
          getcompname()   -- returns human-readable version of
                             compression type ('not compressed' linear samples)
          getparams()     -- returns a namedtuple consisting of all of the
                             above in the above order
          getmarkers()    -- returns None (for compatibility with the
                             old aifc module)
          getmark(id)     -- raises an error since the mark does not
                             exist (for compatibility with the old aifc module)
          readframes(n)   -- returns at most n frames of audio
          rewind()        -- rewind to the beginning of the audio stream
          setpos(pos)     -- seek to the specified position
          tell()          -- return the current position
          close()         -- close the instance (make it unusable)
    The position returned by tell() and the position given to setpos()
    are compatible and have nothing to do with the actual position in the
    file.
    The close() method is called automatically when the class instance
    is destroyed.

    Writing WAVE files:
          f = wave.open(file, 'w')
    where file is either the name of a file or an open file pointer.
    The open file pointer must have methods write(), tell(), seek(), and
    close().

    This returns an instance of a class with the following public methods:
          setnchannels(n) -- set the number of channels
          setsampwidth(n) -- set the sample width
          setframerate(n) -- set the frame rate
          setnframes(n)   -- set the number of frames
          setcomptype(type, name)
                          -- set the compression type and the
                             human-readable compression type
          setparams(tuple)
                          -- set all parameters at once
          tell()          -- return current position in output file
          writeframesraw(data)
                          -- write audio frames without patching up the
                             file header
          writeframes(data)
                          -- write audio frames and patch up the file header
          close()         -- patch up the file header and close the
                             output file
    You should set the parameters before the first writeframesraw or
    writeframes.  The total number of frames does not need to be set,
    but when it is set to the correct value, the header does not have to
    be patched up.
    It is best to first set all parameters, perhaps possibly the
    compression type, and then write audio frames using writeframesraw.
    When all frames have been written, either call writeframes(b'') or
    close() to patch up the sizes in the header.
    The close() method is called automatically when the class instance
    is destroyed.

CLASSES
    builtins.Exception(builtins.BaseException)
        Error
    builtins.object
        Wave_read
        Wave_write

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

    class Wave_read(builtins.object)
     |  Wave_read(f)
     |
     |  Variables used in this class:
     |
     |  These variables are available to the user though appropriat
```

## Related

Other standard-library modules pair well with `wave`; explore the `python` domain of this catalog.
