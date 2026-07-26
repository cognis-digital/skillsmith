---
name: py-csv-io
description: "Parse and emit delimited data safely with the csv module, including headers via DictReader."
version: 1.0.0
tags: [idiom, programming, python, recipe]
---

    # Python recipe: Reading and writing CSV

    ## Overview

    `csv` handles quoting, delimiters, and newlines correctly — do not split on commas yourself. `DictReader`/`DictWriter` map rows to dicts by header.

    ## When to use

    Parse and emit delimited data safely with the csv module, including headers via DictReader.

    ## Worked examples

    **Read**

```python
import csv
with open('data.csv', newline='') as f:
    for row in csv.DictReader(f):
        print(row['name'], row['age'])
```

**Write**

```python
with open('out.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['name', 'age'])
    w.writeheader(); w.writerow({'name': 'Ada', 'age': 36})
```

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    - Always open CSV files with newline='' to avoid blank rows on Windows.
- Never parse CSV by str.split(',') — quoted fields with commas will break it.

    ## Related

    `python-csv`, `json-io`
