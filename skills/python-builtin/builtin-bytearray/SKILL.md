---
name: builtin-bytearray
description: "Program with Python's built-in bytearray: bytearray(iterable_of_ints) -> bytearray bytearray(string, encoding[, errors]) -> bytearray bytearray(bytes_or_buffer) -> mutable copy of bytes_or_buffer bytearray(int) -> bytes array of size given by the parameter initialized with null bytes bytearray() -> empty bytes array Construct a mutable bytearray object from: - an iterable yielding integers in range(256) - a text string encoded using the specified encoding - a bytes or a buffer object - any object implementing the buffer API."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `bytearray`

    ## Overview

    `bytearray` is a Python built-in class — always available, no import required.

    bytearray(iterable_of_ints) -> bytearray
bytearray(string, encoding[, errors]) -> bytearray
bytearray(bytes_or_buffer) -> mutable copy of bytes_or_buffer
bytearray(int) -> bytes array of size given by the parameter initialized with null bytes
bytearray() -> empty bytes array

Construct a mutable bytearray object from:
  - an iterable yielding integers in range(256)
  - a text string encoded using the specified encoding
  - a bytes or a buffer object
  - any object implementing the buffer API.
  - an integer

    ## Signature

    ```python
    bytearray
    ```

    ## When to use

    Built-ins are the first tool to reach for: `bytearray` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = bytearray(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class bytearray in module builtins

class bytearray(object)
 |  bytearray(iterable_of_ints) -> bytearray
 |  bytearray(string, encoding[, errors]) -> bytearray
 |  bytearray(bytes_or_buffer) -> mutable copy of bytes_or_buffer
 |  bytearray(int) -> bytes array of size given by the parameter initialized with null bytes
 |  bytearray() -> empty bytes array
 |
 |  Construct a mutable bytearray object from:
 |    - an iterable yielding integers in range(256)
 |    - a text string encoded using the specified encoding
 |    - a bytes or a buffer object
 |    - any object implementing the buffer API.
 |    - an integer
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __alloc__(self, /)
 |      B.__alloc__() -> int
 |
 |      Return the number of bytes actually allocated.
 |
 |  __buffer__(self, flags, /)
 |      Return a buffer object that exposes the underlying memory of the object.
 |
 |  __contains__(self, key, /)
 |      Return bool(key in self).
 |
 |  __delitem__(self, key, /)
 |      Delete self[key].
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
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
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
 |  __reduce__(self, /)
 |      Return state information for pickling.
 |
 |  __reduce_ex__(self, proto=0, /)
 |      Return state information for pickling.
 |
 |  __release_buffer__(self, buffer, /)
 |      Release the buffer object that exposes the underlying memory of the object.
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
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |
 |  __sizeof__(self, /)
 |      Returns the size of the bytearray object in memory, in bytes.
 |
 |  __str__(self, /)
 |      Return str(self).
 |
 |  append(self, item, /)
 |      Append a single item to the end of the bytearray.
 |
 |      item
 |        The item to be appended.
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
 |  clear(self, /)
 |      Remove all items from the bytearray.
 |
 |  copy(self, /)
 |      Return a copy of B.
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
 |      Decode the bytearray using the codec registered for encoding.
 |
 |      encoding
 |        The encoding with which to decode the bytearray.
 |      errors
 |        The error handling scheme to use for the handling of decoding errors.
 |        The default is 'strict' meaning that decoding errors raise a
 |        UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
 |        as well as any other name registered with codecs.register_error that
 |        can handle UnicodeDecodeErrors.
 |
 |  endswith(self, suffix[, start[, end]], /)
 |      Return True if the bytearray ends with the specified suffix, False otherwise.
 |
 |      suffix
 |        A bytes or a tuple of bytes to try.
 |      start
 |        Optional start position. Default: start of the bytearray.
 |      end
 |        Optional stop position. Default: end of the bytearray.
 |
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |
 |  extend(self, iterable_of_ints, /)
 |      Append all the items from the iterator or sequence to the end of the bytearray.
 |
 |      iterable_of_ints
 |        The iterable of items to append.
 |
 |  find(self, sub[, start[, end]], /)
 |      Return the lowest index in B where subsection 'sub' is found, such that 'sub' is contained within B[start:end].
 |
 |        start
 |          Optional start position. Default: start of the bytes.
 |        end
 |          Optional stop position. Default: end of the bytes.
 |
 |      Return -1 on failure.
 |
 |  hex(self, /, sep=<unrepresentable>, bytes_per_sep=1)
 |      Create a string of hexadecimal numbers from a bytearray object.
 |
 |        sep
 |          An optional single character or byte to separate hex bytes.
 |        bytes_per_sep
 |          How many bytes between separators.  Positive values count from the
 |          right, negative values count from the left.
 |
 |      Example:
 |      >>> value = bytearray([0xb9, 0x01, 0xef])
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
 |      Return the lowest index in B where subsection 'sub' is found, such that 'sub' is contained within B[start:end].
 |
 |     
    ```
