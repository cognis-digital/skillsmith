---
name: python-sqlite3
description: "Program with Python's sqlite3 module: The sqlite3 extension module provides a DB-API 2.0 (PEP 249) compliant interface to the SQLite library, and requires SQLite 3.15.2 or newer."
version: 1.0.0
tags: [programming, python, sqlite3, stdlib]
---

# Python: `sqlite3`

## Overview

The sqlite3 extension module provides a DB-API 2.0 (PEP 249) compliant
interface to the SQLite library, and requires SQLite 3.15.2 or newer.

To use the module, start by creating a database Connection object:

    import sqlite3
    cx = sqlite3.connect("test.db")  # test.db will be created or opened

The special path name ":memory:" can be provided to connect to a transient
in-memory database:

    cx = sqlite3.connect(":memory:")  # connect to a database in RAM

Once a connection has been established, create a Cursor object and call
its execute() method to perform SQL queries:

    cu = cx.cursor()

    # create a table
    cu.execute("create table lang(name, first_appeared)")

    # insert values into a table
    cu.execute("insert into lang values (?, ?)", ("C", 1972))

    # execute a query and iterate over the result
    for row in cu.execute("select * from lang"):
        print(row)

    cx.close()

The sqlite3 module is written by Gerhard Häring <gh@ghaering.de>.

## When to use

Reach for `sqlite3` when your task calls for The sqlite3 extension module provides a DB-API 2.0 (PEP 249) compliant interface to the SQLite library, and requires SQL. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import sqlite3
```

## Key functions

- `sqlite3.DateFromTicks(ticks)`
- `sqlite3.TimeFromTicks(ticks)`
- `sqlite3.TimestampFromTicks(ticks)`
- `sqlite3.adapt(...)`
- `sqlite3.complete_statement(statement)`
- `sqlite3.connect(...)`
- `sqlite3.enable_callback_tracebacks(enable, /)`
- `sqlite3.register_adapter(type, adapter, /)`
- `sqlite3.register_converter(typename, converter, /)`

## Key classes

`Binary`, `Blob`, `Connection`, `Cursor`, `DataError`, `DatabaseError`, `Date`, `Error`, `IntegrityError`, `InterfaceError`, `InternalError`, `NotSupportedError`, `OperationalError`, `PrepareProtocol`, `ProgrammingError`, `Row`, `Time`, `Timestamp`, `Warning`

## Constants / attributes

`LEGACY_TRANSACTION_CONTROL`, `PARSE_COLNAMES`, `PARSE_DECLTYPES`, `SQLITE_ABORT`, `SQLITE_ABORT_ROLLBACK`, `SQLITE_ALTER_TABLE`, `SQLITE_ANALYZE`, `SQLITE_ATTACH`, `SQLITE_AUTH`, `SQLITE_AUTH_USER`, `SQLITE_BUSY`, `SQLITE_BUSY_RECOVERY`, `SQLITE_BUSY_SNAPSHOT`, `SQLITE_BUSY_TIMEOUT`, `SQLITE_CANTOPEN`, `SQLITE_CANTOPEN_CONVPATH`, `SQLITE_CANTOPEN_DIRTYWAL`, `SQLITE_CANTOPEN_FULLPATH`, `SQLITE_CANTOPEN_ISDIR`, `SQLITE_CANTOPEN_NOTEMPDIR`, `SQLITE_CANTOPEN_SYMLINK`, `SQLITE_CONSTRAINT`, `SQLITE_CONSTRAINT_CHECK`, `SQLITE_CONSTRAINT_COMMITHOOK`, `SQLITE_CONSTRAINT_FOREIGNKEY`, `SQLITE_CONSTRAINT_FUNCTION`, `SQLITE_CONSTRAINT_NOTNULL`, `SQLITE_CONSTRAINT_PINNED`, `SQLITE_CONSTRAINT_PRIMARYKEY`, `SQLITE_CONSTRAINT_ROWID`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import sqlite3

def do_work(...):
    """Use sqlite3 to accomplish one well-defined task."""
    result = sqlite3.DateFromTicks(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `sqlite3` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: package sqlite3

NAME
    sqlite3

MODULE REFERENCE
    https://docs.python.org/3.14/library/sqlite3.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    The sqlite3 extension module provides a DB-API 2.0 (PEP 249) compliant
    interface to the SQLite library, and requires SQLite 3.15.2 or newer.

    To use the module, start by creating a database Connection object:

        import sqlite3
        cx = sqlite3.connect("test.db")  # test.db will be created or opened

    The special path name ":memory:" can be provided to connect to a transient
    in-memory database:

        cx = sqlite3.connect(":memory:")  # connect to a database in RAM

    Once a connection has been established, create a Cursor object and call
    its execute() method to perform SQL queries:

        cu = cx.cursor()

        # create a table
        cu.execute("create table lang(name, first_appeared)")

        # insert values into a table
        cu.execute("insert into lang values (?, ?)", ("C", 1972))

        # execute a query and iterate over the result
        for row in cu.execute("select * from lang"):
            print(row)

        cx.close()

    The sqlite3 module is written by Gerhard Häring <gh@ghaering.de>.

PACKAGE CONTENTS
    __main__
    dbapi2
    dump

CLASSES
    builtins.Exception(builtins.BaseException)
        Error
            DatabaseError
                DataError
                IntegrityError
                InternalError
                NotSupportedError
                OperationalError
                ProgrammingError
            InterfaceError
        Warning
    builtins.object
        Blob
        Connection
        Cursor
        PrepareProtocol
        Row

    class Blob(builtins.object)
     |  Methods defined here:
     |
     |  __delitem__(self, key, /)
     |      Delete self[key].
     |
     |  __enter__(self, /)
     |      Blob context manager enter.
     |
     |  __exit__(self, type, val, tb, /)
     |      Blob context manager exit.
     |
     |  __getitem__(self, key, /)
     |      Return self[key].
     |
     |  __len__(self, /)
     |      Return len(self).
     |
     |  __setitem__(self, key, value, /)
     |      Set self[key] to value.
     |
     |  close(self, /)
     |      Close the blob.
     |
     |  read(self, length=-1, /)
     |      Read data at the current offset position.
     |
     |        length
     |          Read length in bytes.
     |
     |      If the end of the blob is reached, the data up to end of file will be returned.
     |      When length is not specified, or is negative, Blob.read() will read until the
     |      end of the blob.
     |
     |  seek(self, offset, origin=0, /)
     |      Set the current access position to offset.
     |
     |      The origin argument defaults to os.SEEK_SET (absolute blob positioning).
     |      Other values for origin are os.SEEK_CUR (seek relative to the current position)
     |      and os.SEEK_END (seek relative to the blob's end).
     |
     |  tell(self, /)
     |      Return the current access position for the blob.
     |
     |  write(self, data, /)
     |      Write data at the current offset.
     |
     |      This function cannot change the blob length.  Writing beyond the end of the
     |      blob will result in an exception being raised.

    class Connection(builtins.object)
     |  SQLite database connection object.
     |
     |  Methods defined here:
     |
     |  __call__(self, /, *args, **kwargs)
     |      Call self as a function.
     |
     |  __del__(self, /)
     |      Called when the instance is about to be destroyed.
     |
     |  __enter__(self, /)
     |      Called when the connection is used as a context manager.
     |
     |      Returns itself as a convenience to the caller.
     |
     |  __exit__(self, type, value, traceback, /)
     |      Called when the connection is used as a context manager.
     |
     |      If there was any exception, a rollback takes place; otherwise we commit.
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  backup(self, /, target, *, pages=-1, progress=None, name='main', sleep=0.25)
     |      Makes a backup of the database.
     |
     |  blobopen(self, table, column, row, /, *, readonly=False, name='main')
     |      Open and return a BLOB object.
     |
     |      table
     |        Table name.
     |      column
     |        Column name.
     |      row
     |        Row index.
     |      readonly
     |        Open the BLOB without write permissions.
     |      name
     |        Database name.
     |
     |  close(self, /)
     |      Close the database connection.
     |
     |      Any pending transaction is not committed implicitly.
     |
     |  commit(self, /)
     |      Commit any pending transaction to the database.
     |
     |      If there is no open transaction, this method is a no-op.
     |
     |  create_aggregate(self, /, name, n_arg, aggregate_class)
     |      Creates a new aggregate.
     |
     |      Note: Passing keyword arguments 'name', 'n_arg' and 'aggregate_class'
     |      to _sqlite3.Connection.create_aggregate() is deprecated. Parameters
     |      'name', 'n_arg' and 'aggregate_class' will become positional-only in
     |      Python 3.15.
     |
     |  create_collation(self, name, callback, /)
     |      Creates a collation function.
     |
     |  create_function(self, /, name, narg, func, *, deterministic=False)
     |      Creates a new function.
     |
     |      Note: Passing keyword arguments 'name', 'narg' and 'func' to
     |      _sqlite3.Connection.
```

## Related

Other standard-library modules pair well with `sqlite3`; explore the `python` domain of this catalog.
