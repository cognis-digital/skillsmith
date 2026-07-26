---
name: py-string-io
description: "Treat strings and bytes as file-like objects with io.StringIO / io.BytesIO."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: In-memory text and bytes buffers (io)

    ## Overview

    `io.StringIO`/`io.BytesIO` present an in-memory buffer with the file API, so you can feed string data to code that expects a file, or capture output without touching disk.

    ## When to use

    Treat strings and bytes as file-like objects with io.StringIO / io.BytesIO.

    ## Worked examples

    **Build text like a file**

```python
import io, csv
buf = io.StringIO()
csv.writer(buf).writerow(['a', 'b'])
text = buf.getvalue()
```

**Feed a parser**

```python
import io
parse(io.StringIO(some_text))
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Call getvalue() to retrieve the contents; the buffer's position matters if you also read it.
- Use BytesIO for binary formats (images, gzip), StringIO for text.

    ## Related

    `csv-io`, `context-managers`
