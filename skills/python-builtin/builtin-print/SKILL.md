---
name: builtin-print
description: "Program with Python's built-in print: Prints the values to a stream, or to sys.stdout by default."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `print`

    ## Overview

    `print` is a Python built-in function — always available, no import required.

    Prints the values to a stream, or to sys.stdout by default.

sep
  string inserted between values, default a space.
end
  string appended after the last value, default a newline.
file
  a file-like object (stream); defaults to the current sys.stdout.
flush
  whether to forcibly flush the stream.

    ## Signature

    ```python
    print(*args, sep=' ', end='\n', file=None, flush=False)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `print` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = print(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: built-in function print in module builtins

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

    ```
