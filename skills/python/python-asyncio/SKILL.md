---
name: python-asyncio
description: "Program with Python's asyncio module: The asyncio package, tracking PEP 3156."
version: 1.0.0
tags: [asyncio, programming, python, stdlib]
---

# Python: `asyncio`

## Overview

The asyncio package, tracking PEP 3156.

## When to use

Reach for `asyncio` when your task calls for The asyncio package, tracking PEP 3156. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import asyncio
```

## Key functions

- `asyncio.all_tasks(loop=None)`
- `asyncio.as_completed(fs, *, timeout=None)`
- `asyncio.capture_call_graph(future: _asyncio.Future | None = None, /, *, depth: int = 1, limit: int | None = None) -> asyncio.graph.FutureCallGraph | None`
- `asyncio.create_eager_task_factory(custom_task_constructor)`
- `asyncio.create_subprocess_exec(program, *args, stdin=None, stdout=None, stderr=None, limit=65536, **kwds)`
- `asyncio.create_subprocess_shell(cmd, stdin=None, stdout=None, stderr=None, limit=65536, **kwds)`
- `asyncio.create_task(coro, **kwargs)`
- `asyncio.current_task(loop=None)`
- `asyncio.eager_task_factory(loop, coro, *, eager_start=True, **kwargs)`
- `asyncio.ensure_future(coro_or_future, *, loop=None)`
- `asyncio.format_call_graph(future: _asyncio.Future | None = None, /, *, depth: int = 1, limit: int | None = None) -> str`
- `asyncio.future_add_to_awaited_by(fut, waiter, /)`
- `asyncio.future_discard_from_awaited_by(fut, waiter, /)`
- `asyncio.gather(*coros_or_futures, return_exceptions=False)`
- `asyncio.get_event_loop()`
- `asyncio.get_event_loop_policy()`
- `asyncio.get_running_loop()`
- `asyncio.iscoroutine(obj)`
- `asyncio.iscoroutinefunction(func)`
- `asyncio.isfuture(obj)`
- `asyncio.new_event_loop()`
- `asyncio.open_connection(host=None, port=None, *, limit=65536, **kwds)`
- `asyncio.print_call_graph(future: _asyncio.Future | None = None, /, *, file: io.Writer[str] | None = None, depth: int = 1, limit: int | None = None) -> None`
- `asyncio.run(main, *, debug=None, loop_factory=None)`
- `asyncio.run_coroutine_threadsafe(coro, loop)`
- `asyncio.set_event_loop(loop)`
- `asyncio.set_event_loop_policy(policy)`
- `asyncio.shield(arg)`
- `asyncio.sleep(delay, result=None)`
- `asyncio.start_server(client_connected_cb, host=None, port=None, *, limit=65536, **kwds)`

## Key classes

`AbstractEventLoop`, `AbstractServer`, `Barrier`, `BaseEventLoop`, `BaseProtocol`, `BaseTransport`, `BoundedSemaphore`, `BrokenBarrierError`, `BufferedProtocol`, `CancelledError`, `Condition`, `DatagramProtocol`, `DatagramTransport`, `Event`, `EventLoop`, `FrameCallGraphEntry`, `Future`, `FutureCallGraph`, `Handle`, `IncompleteReadError`, `InvalidStateError`, `IocpProactor`, `LifoQueue`, `LimitOverrunError`, `Lock`, `PriorityQueue`, `ProactorEventLoop`, `Protocol`, `Queue`, `QueueEmpty`

## Constants / attributes

`ALL_COMPLETED`, `FIRST_COMPLETED`, `FIRST_EXCEPTION`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import asyncio

def do_work(...):
    """Use asyncio to accomplish one well-defined task."""
    result = asyncio.all_tasks(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `asyncio` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: package asyncio

NAME
    asyncio - The asyncio package, tracking PEP 3156.

MODULE REFERENCE
    https://docs.python.org/3.14/library/asyncio.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

PACKAGE CONTENTS
    __main__
    base_events
    base_futures
    base_subprocess
    base_tasks
    constants
    coroutines
    events
    exceptions
    format_helpers
    futures
    graph
    locks
    log
    mixins
    proactor_events
    protocols
    queues
    runners
    selector_events
    sslproto
    staggered
    streams
    subprocess
    taskgroups
    tasks
    threads
    timeouts
    tools
    transports
    trsock
    unix_events
    windows_events
    windows_utils

CLASSES
    asyncio.events._BaseDefaultEventLoopPolicy(asyncio.events._AbstractEventLoopPolicy)
        asyncio.windows_events._WindowsProactorEventLoopPolicy
        asyncio.windows_events._WindowsSelectorEventLoopPolicy
    asyncio.locks._ContextManagerMixin(builtins.object)
        asyncio.locks.Condition(asyncio.locks._ContextManagerMixin, asyncio.mixins._LoopBoundMixin)
        asyncio.locks.Lock(asyncio.locks._ContextManagerMixin, asyncio.mixins._LoopBoundMixin)
        asyncio.locks.Semaphore(asyncio.locks._ContextManagerMixin, asyncio.mixins._LoopBoundMixin)
            asyncio.locks.BoundedSemaphore
    asyncio.mixins._LoopBoundMixin(builtins.object)
        asyncio.locks.Barrier
        asyncio.locks.Condition(asyncio.locks._ContextManagerMixin, asyncio.mixins._LoopBoundMixin)
        asyncio.locks.Event
        asyncio.locks.Lock(asyncio.locks._ContextManagerMixin, asyncio.mixins._LoopBoundMixin)
        asyncio.locks.Semaphore(asyncio.locks._ContextManagerMixin, asyncio.mixins._LoopBoundMixin)
            asyncio.locks.BoundedSemaphore
        asyncio.queues.Queue
            asyncio.queues.LifoQueue
            asyncio.queues.PriorityQueue
    asyncio.proactor_events.BaseProactorEventLoop(asyncio.base_events.BaseEventLoop)
        asyncio.windows_events.ProactorEventLoop
    asyncio.selector_events.BaseSelectorEventLoop(asyncio.base_events.BaseEventLoop)
        asyncio.windows_events._WindowsSelectorEventLoop
    asyncio.streams.FlowControlMixin(asyncio.protocols.Protocol)
        asyncio.streams.StreamReaderProtocol(asyncio.streams.FlowControlMixin, asyncio.protocols.Protocol)
    builtins.BaseException(builtins.object)
        asyncio.exceptions.CancelledError
    builtins.EOFError(builtins.Exception)
        asyncio.exceptions.IncompleteReadError
    builtins.Exception(builtins.BaseException)
        asyncio.exceptions.InvalidStateError
        asyncio.exceptions.LimitOverrunError
        asyncio.queues.QueueEmpty
        asyncio.queues.QueueFull
        asyncio.queues.QueueShutDown
    builtins.OSError(builtins.Exception)
        builtins.TimeoutError
    builtins.RuntimeError(builtins.Exception)
        asyncio.exceptions.BrokenBarrierError
        asyncio.exceptions.SendfileNotAvailableError
    builtins.object
        _asyncio.Future
            _asyncio.Task
        asyncio.events.AbstractEventLoop
            asyncio.base_events.BaseEventLoop
        asyncio.events.AbstractServer
            asyncio.base_events.Server
        asyncio.events.Handle
            asyncio.events.TimerHandle
        asyncio.graph.FrameCallGraphEntry
        asyncio.graph.FutureCallGraph
        asyncio.protocols.BaseProtocol
            asyncio.protocols.BufferedProtocol
            asyncio.protocols.DatagramProtocol
            asyncio.protocols.Protocol
                asyncio.streams.StreamReaderProtocol(asyncio.streams.FlowControlMixin, asyncio.protocols.Protocol)
            asyncio.protocols.SubprocessProtocol
        asyncio.runners.Runner
        asyncio.streams.StreamReader
        asyncio.streams.StreamWriter
        asyncio.taskgroups.TaskGroup
        asyncio.timeouts.Timeout
        asyncio.transports.BaseTransport
            asyncio.transports.DatagramTransport
            asyncio.transports.ReadTransport
                asyncio.transports.Transport(asyncio.transports.ReadTransport, asyncio.transports.WriteTransport)
            asyncio.transports.SubprocessTransport
            asyncio.transports.WriteTransport
        asyncio.windows_events.IocpProactor

    class AbstractEventLoop(builtins.object)
     |  Abstract event loop.
     |
     |  Methods defined here:
     |
     |  add_reader(self, fd, callback, *args)
     |
     |  add_signal_handler(self, sig, callback, *args)
     |
     |  add_writer(self, fd, callback, *args)
     |
     |  call_at(self, when, callback, *args, context=None)
     |
     |  call_exception_handler(self, context)
     |
     |  call_later(self, delay, callback, *args, context=None)
     |
     |  call_soon(self, callback, *args, context=None)
     |
     |  call_soon_threadsafe(self, callback, *args, context=None)
     |
     |  close(self)
     |      Close the loop.
     |
     |      The loop should not be running.
     |
     |      This is idempotent and irreversible.
     |
     |      No other methods should be called after this one.
     |
     |  async connect_accepted_socket(
     |      self,
     |      protocol_factory,
     |      sock,
     |      *,
     |      ssl=None,
     |      ssl_handshake_timeout=None,
     |      ssl_shutdown_timeout=None
     |  )
     |      Handle an accepted connection.
     |
     |      This is used by servers that accept connections outside of
     |      asyncio, but use asyncio to handle connections.
     |
     |      This method is a coroutine.  When completed, the coroutine
     |      returns a (transport, protocol) pair.
     |
     |  async connect_read_pipe(self, protocol_factory, pipe)
     |      Register 
```

## Related

Other standard-library modules pair well with `asyncio`; explore the `python` domain of this catalog.
