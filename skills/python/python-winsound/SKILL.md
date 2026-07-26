---
name: python-winsound
description: "Program with Python's winsound module: PlaySound(sound, flags) - play a sound SND_FILENAME - sound is a wav file name SND_ALIAS - sound is a registry sound association name SND_LOOP - Play the sound repeatedly; must also specify SND_ASYNC SND_MEMORY - sound is a memory image of a wav file SND_PURGE - stop all instances of the specified sound SND_ASYNC - PlaySound returns immediately SND_NODEFAULT - Do not play a default beep if the sound can not be found SND_NOSTOP - Do not interrupt any sounds currently playing SND_NOWAIT - Return immediately if the sound driver is busy SND_APPLICATION - sound is an application-specific alias in the registry."
version: 1.0.0
tags: [programming, python, stdlib, winsound]
---

# Python: `winsound`

## Overview

PlaySound(sound, flags) - play a sound
SND_FILENAME - sound is a wav file name
SND_ALIAS - sound is a registry sound association name
SND_LOOP - Play the sound repeatedly; must also specify SND_ASYNC
SND_MEMORY - sound is a memory image of a wav file
SND_PURGE - stop all instances of the specified sound
SND_ASYNC - PlaySound returns immediately
SND_NODEFAULT - Do not play a default beep if the sound can not be found
SND_NOSTOP - Do not interrupt any sounds currently playing
SND_NOWAIT - Return immediately if the sound driver is busy
SND_APPLICATION - sound is an application-specific alias in the registry.
SND_SENTRY - Triggers a SoundSentry event when the sound is played.
SND_SYNC - Play the sound synchronously, default behavior.
SND_SYSTEM - Assign sound to the audio session for system notification sounds.

Beep(frequency, duration) - Make a beep through the PC speaker.
MessageBeep(type) - Call Windows MessageBeep.

## When to use

Reach for `winsound` when your task calls for PlaySound(sound, flags) - play a sound SND_FILENAME - sound is a wav file name SND_ALIAS - sound is a registry sound ass. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import winsound
```

## Key functions

- `winsound.Beep(frequency, duration)`
- `winsound.MessageBeep(type=0)`
- `winsound.PlaySound(sound, flags)`

## Constants / attributes

`MB_ICONASTERISK`, `MB_ICONERROR`, `MB_ICONEXCLAMATION`, `MB_ICONHAND`, `MB_ICONINFORMATION`, `MB_ICONQUESTION`, `MB_ICONSTOP`, `MB_ICONWARNING`, `MB_OK`, `SND_ALIAS`, `SND_APPLICATION`, `SND_ASYNC`, `SND_FILENAME`, `SND_LOOP`, `SND_MEMORY`, `SND_NODEFAULT`, `SND_NOSTOP`, `SND_NOWAIT`, `SND_PURGE`, `SND_SENTRY`, `SND_SYNC`, `SND_SYSTEM`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import winsound

def do_work(...):
    """Use winsound to accomplish one well-defined task."""
    result = winsound.Beep(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `winsound` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module winsound

NAME
    winsound

DESCRIPTION
    PlaySound(sound, flags) - play a sound
    SND_FILENAME - sound is a wav file name
    SND_ALIAS - sound is a registry sound association name
    SND_LOOP - Play the sound repeatedly; must also specify SND_ASYNC
    SND_MEMORY - sound is a memory image of a wav file
    SND_PURGE - stop all instances of the specified sound
    SND_ASYNC - PlaySound returns immediately
    SND_NODEFAULT - Do not play a default beep if the sound can not be found
    SND_NOSTOP - Do not interrupt any sounds currently playing
    SND_NOWAIT - Return immediately if the sound driver is busy
    SND_APPLICATION - sound is an application-specific alias in the registry.
    SND_SENTRY - Triggers a SoundSentry event when the sound is played.
    SND_SYNC - Play the sound synchronously, default behavior.
    SND_SYSTEM - Assign sound to the audio session for system notification sounds.

    Beep(frequency, duration) - Make a beep through the PC speaker.
    MessageBeep(type) - Call Windows MessageBeep.

FUNCTIONS
    Beep(frequency, duration)
        A wrapper around the Windows Beep API.

        frequency
          Frequency of the sound in hertz.
          Must be in the range 37 through 32,767.
        duration
          How long the sound should play, in milliseconds.

    MessageBeep(type=0)
        Call Windows MessageBeep(x).

        x defaults to MB_OK.

    PlaySound(sound, flags)
        A wrapper around the Windows PlaySound API.

        sound
          The sound to play; a filename, data, or None.
        flags
          Flag values, ored together.  See module documentation.

DATA
    MB_ICONASTERISK = 64
    MB_ICONERROR = 16
    MB_ICONEXCLAMATION = 48
    MB_ICONHAND = 16
    MB_ICONINFORMATION = 64
    MB_ICONQUESTION = 32
    MB_ICONSTOP = 16
    MB_ICONWARNING = 48
    MB_OK = 0
    SND_ALIAS = 65536
    SND_APPLICATION = 128
    SND_ASYNC = 1
    SND_FILENAME = 131072
    SND_LOOP = 8
    SND_MEMORY = 4
    SND_NODEFAULT = 2
    SND_NOSTOP = 16
    SND_NOWAIT = 8192
    SND_PURGE = 64
    SND_SENTRY = 524288
    SND_SYNC = 0
    SND_SYSTEM = 2097152

FILE
    c:\python314\dlls\winsound.pyd


```

## Related

Other standard-library modules pair well with `winsound`; explore the `python` domain of this catalog.
