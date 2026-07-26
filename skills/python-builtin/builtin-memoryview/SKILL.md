---
name: builtin-memoryview
description: "Program with Python's built-in memoryview: Create a new memoryview object which references the given object."
version: 1.0.0
tags: [builtin, programming, python]
---

    # Python builtin: `memoryview`

    ## Overview

    `memoryview` is a Python built-in class — always available, no import required.

    Create a new memoryview object which references the given object.

    ## Signature

    ```python
    memoryview(object)
    ```

    ## When to use

    Built-ins are the first tool to reach for: `memoryview` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = memoryview(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    Python Library Documentation: class memoryview in module builtins

class memoryview(object)
 |  memoryview(object)
 |
 |  Create a new memoryview object which references the given object.
 |
 |  Methods defined here:
 |
 |  __buffer__(self, flags, /)
 |      Return a buffer object that exposes the underlying memory of the object.
 |
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |
 |  __enter__(self, /)
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __exit__(self, /, *exc_info)
 |      Release the underlying buffer exposed by the memoryview object.
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
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __release_buffer__(self, buffer, /)
 |      Release the buffer object that exposes the underlying memory of the object.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |
 |  cast(self, /, format, shape=<unrepresentable>)
 |      Cast a memoryview to a new format or shape.
 |
 |  count(self, value, /)
 |      Count the number of occurrences of a value.
 |
 |  hex(self, /, sep=<unrepresentable>, bytes_per_sep=1)
 |      Return the data in the buffer as a str of hexadecimal numbers.
 |
 |        sep
 |          An optional single character or byte to separate hex bytes.
 |        bytes_per_sep
 |          How many bytes between separators.  Positive values count from the
 |          right, negative values count from the left.
 |
 |      Example:
 |      >>> value = memoryview(b'\xb9\x01\xef')
 |      >>> value.hex()
 |      'b901ef'
 |      >>> value.hex(':')
 |      'b9:01:ef'
 |      >>> value.hex(':', 2)
 |      'b9:01ef'
 |      >>> value.hex(':', -2)
 |      'b901:ef'
 |
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return the index of the first occurrence of a value.
 |
 |      Raises ValueError if the value is not present.
 |
 |  release(self, /)
 |      Release the underlying buffer exposed by the memoryview object.
 |
 |  tobytes(self, /, order='C')
 |      Return the data in the buffer as a byte string.
 |
 |      Order can be {'C', 'F', 'A'}. When order is 'C' or 'F', the data of the
 |      original array is converted to C or Fortran order. For contiguous views,
 |      'A' returns an exact copy of the physical memory. In particular, in-memory
 |      Fortran order is preserved. For non-contiguous views, the data is converted
 |      to C first. order=None is the same as order='C'.
 |
 |  tolist(self, /)
 |      Return the data in the buffer as a list of elements.
 |
 |  toreadonly(self, /)
 |      Return a readonly version of the memoryview.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __class_getitem__(object, /)
 |      See PEP 585
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  c_contiguous
 |      A bool indicating whether the memory is C contiguous.
 |
 |  contiguous
 |      A bool indicating whether the memory is contiguous.
 |
 |  f_contiguous
 |      A bool indicating whether the memory is Fortran contiguous.
 |
 |  format
 |      A string containing the format (in struct module style)
 |      for each element in the view.
 |
 |  itemsize
 |      The size in bytes of each element of the memoryview.
 |
 |  nbytes
 |      The amount of space in bytes that the array would use in
 |      a contiguous representation.
 |
 |  ndim
 |      An integer indicating how many dimensions of a multi-dimensional
 |      array the memory represents.
 |
 |  obj
 |      The underlying object of the memoryview.
 |
 |  readonly
 |      A bool indicating whether the memory is read only.
 |
 |  shape
 |      A tuple of ndim integers giving the shape of the memory
 |      as an N-dimensional array.
 |
 |  strides
 |      A tuple of ndim integers giving the size in bytes to access
 |      each element for each dimension of the array.
 |
 |  suboffsets
 |      A tuple of integers used internally for PIL-style arrays.

    ```
