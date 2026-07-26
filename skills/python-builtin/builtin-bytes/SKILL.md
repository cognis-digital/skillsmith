---
name: builtin-bytes
description: "Program with Python's built-in bytes: bytes(iterable_of_ints) -> bytes bytes(string, encoding[, errors]) -> bytes bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer bytes(int) -> bytes object of size given by the parameter initialized with null bytes bytes() -> empty bytes object Construct an immutable array of bytes from: - an iterable yielding integers in range(256) - a text string encoded using the specified encoding - any object implementing the buffer API."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `bytes`

    ## Overview

    `bytes` is a Python built-in class — always available, no import required.

    bytes(iterable_of_ints) -> bytes
bytes(string, encoding[, errors]) -> bytes
bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
bytes(int) -> bytes object of size given by the parameter initialized with null bytes
bytes() -> empty bytes object

Construct an immutable array of bytes from:
  - an iterable yielding integers in range(256)
  - a text string encoded using the specified encoding
  - any object implementing the buffer API.
  - an integer

    ## Signature

    ```python
    bytes
    ```

    ## When to use

    Built-ins are the first tool to reach for: `bytes` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = bytes(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class bytes in module builtins

class bytes(object)
 |  bytes(iterable_of_ints) -> bytes
 |  bytes(string, encoding[, errors]) -> bytes
 |  bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
 |  bytes(int) -> bytes object of size given by the parameter initialized with null bytes
 |  bytes() -> empty bytes object
 |
 |  Construct an immutable array of bytes from:
 |    - an iterable yielding integers in range(256)
 |    - a text string encoded using the specified encoding
 |    - any object implementing the buffer API.
 |    - an integer
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __buffer__(self, flags, /)
 |      Return a buffer object that exposes the underlying memory of the object.
 |
 |  __bytes__(self, /)
 |      Convert this value to exact type bytes.
 |
 |  __contains__(self, key, /)
 |      Return bool(key in self).
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getitem__(self, key, /)
 |      Return self[key].
 |
 |  __getnewargs__(self, /)
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __len__(self, /)
 |      Return len(self).
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __mod__(self, value, /)
 |      Return self%value.
 |
 |  __mul__(self, value, /)
 |      Return self*value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __rmod__(self, value, /)
 |      Return value%self.
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __str__(self, /)
 |      Return str(self).
 |
 |  capitalize(self, /)
 |      B.capitalize() -> copy of B
 |
 |      Return a copy of B with only its first character capitalized (ASCII)
 |      and the rest lower-cased.
 |
 |  center(self, width, fillchar=b' ', /)
 |      Return a centered string of length width.
 |
 |      Padding is done using the specified fill character.
 |
 |  count(self, sub[, start[, end]], /)
 |      Return the number of non-overlapping occurrences of subsection 'sub' in bytes B[start:end].
 |
 |      start
 |        Optional start position. Default: start of the bytes.
 |      end
 |        Optional stop position. Default: end of the bytes.
 |
 |  decode(self, /, encoding='utf-8', errors='strict')
 |      Decode the bytes using the codec registered for encoding.
 |
 |      encoding
 |        The encoding with which to decode the bytes.
 |      errors
 |        The error handling scheme to use for the handling of decoding errors.
 |        The default is 'strict' meaning that decoding errors raise a
 |        UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
 |        as well as any other name registered with codecs.register_error that
 |        can handle UnicodeDecodeErrors.
 |
 |  endswith(self, suffix[, start[, end]], /)
 |      Return True if the bytes ends with the specified suffix, False otherwise.
 |
 |      suffix
 |        A bytes or a tuple of bytes to try.
 |      start
 |        Optional start position. Default: start of the bytes.
 |      end
 |        Optional stop position. Default: end of the bytes.
 |
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |
 |  find(self, sub[, start[, end]], /)
 |      Return the lowest index in B where subsection 'sub' is found, such that 'sub' is contained within B[start,end].
 |
 |        start
 |          Optional start position. Default: start of the bytes.
 |        end
 |          Optional stop position. Default: end of the bytes.
 |
 |      Return -1 on failure.
 |
 |  hex(self, /, sep=<unrepresentable>, bytes_per_sep=1)
 |      Create a string of hexadecimal numbers from a bytes object.
 |
 |        sep
 |          An optional single character or byte to separate hex bytes.
 |        bytes_per_sep
 |          How many bytes between separators.  Positive values count from the
 |          right, negative values count from the left.
 |
 |      Example:
 |      >>> value = b'\xb9\x01\xef'
 |      >>> value.hex()
 |      'b901ef'
 |      >>> value.hex(':')
 |      'b9:01:ef'
 |      >>> value.hex(':', 2)
 |      'b9:01ef'
 |      >>> value.hex(':', -2)
 |      'b901:ef'
 |
 |  index(self, sub[, start[, end]], /)
 |      Return the lowest index in B where subsection 'sub' is found, such that 'sub' is contained within B[start,end].
 |
 |        start
 |          Optional start position. Default: start of the bytes.
 |        end
 |          Optional stop position. Default: end of the bytes.
 |
 |      Raise ValueError if the subsection is not found.
 |
 |  isalnum(self, /)
 |      B.isalnum() -> bool
 |
 |      Return True if all characters in B are alphanumeric
 |      and there is at least one character in B, False otherwise.
 |
 |  isalpha(self, /)
 |      B.isalpha() -> bool
 |
 |      Return True if all characters in B are alphabetic
 |      and there is at least one character in B, False otherwise.
 |
 |  isascii(self, /)
 |      B.isascii() -> bool
 |
 |      Return True if B is empty or all characters in B are ASCII,
 |      False otherwise.
 |
 |  isdigit(self, /)
 |      B.isdigit() -> bool
 |
 |      Return True if all characters in B are digits
 |      and there is at least one character in B, False otherwise.
 |
 |  islower(self, /)
 |      B.islower() -> bool
 |
 |      Return True if all cased characters in B are lowercase and there is
 |      at least one cased character in B, False otherwise.
 |
 |  isspace(self, /)
 |      B.isspace() -> bool
 |
 |      Return True if all characters in B are whitespace
 |      and there is at least one character in B, False otherwise.
    ```
