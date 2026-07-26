---
name: python-random
description: "Program with Python's random module: Random variable generators."
version: 1.0.0
tags: [programming, python, random, stdlib]
---

# Python: `random`

## Overview

Random variable generators.

    bytes
    -----
           uniform bytes (values between 0 and 255)

    integers
    --------
           uniform within range

    sequences
    ---------
           pick random element
           pick random sample
           pick weighted random sample
           generate random permutation

    distributions on the real line:
    ------------------------------
           uniform
           triangular
           normal (Gaussian)
           lognormal
           negative exponential
           gamma
           beta
           pareto
           Weibull

    distributions on the circle (angles 0 to 2pi)
    ---------------------------------------------
           circular uniform
           von Mises

    discrete distributions
    ----------------------
           binomial


General notes on the underlying Mersenne Twister core generator:

* The period is 2**19937-1.
* It is one of the most extensively tested generators in existence.
* The random() method is implemented in C, executes in a single Python step,
  and is, therefore, threadsafe.

## When to use

Reach for `random` when your task calls for Random variable generators. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import random
```

## Key functions

- `random.betavariate(alpha, beta)`
- `random.binomialvariate(n=1, p=0.5)`
- `random.choice(seq)`
- `random.choices(population, weights=None, *, cum_weights=None, k=1)`
- `random.expovariate(lambd=1.0)`
- `random.gammavariate(alpha, beta)`
- `random.gauss(mu=0.0, sigma=1.0)`
- `random.getrandbits(k, /)`
- `random.getstate()`
- `random.lognormvariate(mu, sigma)`
- `random.main(arg_list: list[str] | None = None) -> int | str`
- `random.normalvariate(mu=0.0, sigma=1.0)`
- `random.paretovariate(alpha)`
- `random.randbytes(n)`
- `random.randint(a, b)`
- `random.random()`
- `random.randrange(start, stop=None, step=1)`
- `random.sample(population, k, *, counts=None)`
- `random.seed(a=None, version=2)`
- `random.setstate(state)`
- `random.shuffle(x)`
- `random.triangular(low=0.0, high=1.0, mode=None)`
- `random.uniform(a, b)`
- `random.vonmisesvariate(mu, kappa)`
- `random.weibullvariate(alpha, beta)`

## Key classes

`Random`, `SystemRandom`

## Constants / attributes

`BPF`, `LOG4`, `NV_MAGICCONST`, `RECIP_BPF`, `SG_MAGICCONST`, `TWOPI`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import random

def do_work(...):
    """Use random to accomplish one well-defined task."""
    result = random.betavariate(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `random` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module random

NAME
    random - Random variable generators.

MODULE REFERENCE
    https://docs.python.org/3.14/library/random.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
        bytes
        -----
               uniform bytes (values between 0 and 255)

        integers
        --------
               uniform within range

        sequences
        ---------
               pick random element
               pick random sample
               pick weighted random sample
               generate random permutation

        distributions on the real line:
        ------------------------------
               uniform
               triangular
               normal (Gaussian)
               lognormal
               negative exponential
               gamma
               beta
               pareto
               Weibull

        distributions on the circle (angles 0 to 2pi)
        ---------------------------------------------
               circular uniform
               von Mises

        discrete distributions
        ----------------------
               binomial


    General notes on the underlying Mersenne Twister core generator:

    * The period is 2**19937-1.
    * It is one of the most extensively tested generators in existence.
    * The random() method is implemented in C, executes in a single Python step,
      and is, therefore, threadsafe.

CLASSES
    _random.Random(builtins.object)
        Random
            SystemRandom

    class Random(_random.Random)
     |  Random(x=None)
     |
     |  Random number generator base class used by bound module functions.
     |
     |  Used to instantiate instances of Random to get generators that don't
     |  share state.
     |
     |  Class Random can also be subclassed if you want to use a different basic
     |  generator of your own devising: in that case, override the following
     |  methods:  random(), seed(), getstate(), and setstate().
     |  Optionally, implement a getrandbits() method so that randrange()
     |  can cover arbitrarily large ranges.
     |
     |  Method resolution order:
     |      Random
     |      _random.Random
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __getstate__(self)
     |      Helper for pickle.
     |
     |  __init__(self, x=None)
     |      Initialize an instance.
     |
     |      Optional argument x controls seeding, as for Random.seed().
     |
     |  __reduce__(self)
     |      Helper for pickle.
     |
     |  __setstate__(self, state)
     |
     |  betavariate(self, alpha, beta)
     |      Beta distribution.
     |
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      Returned values range between 0 and 1.
     |
     |      The mean (expected value) and variance of the random variable are:
     |
     |          E[X] = alpha / (alpha + beta)
     |          Var[X] = alpha * beta / ((alpha + beta)**2 * (alpha + beta + 1))
     |
     |  binomialvariate(self, n=1, p=0.5)
     |      Binomial random variable.
     |
     |      Gives the number of successes for *n* independent trials
     |      with the probability of success in each trial being *p*:
     |
     |          sum(random() < p for i in range(n))
     |
     |      Returns an integer in the range:
     |
     |          0 <= X <= n
     |
     |      The integer is chosen with the probability:
     |
     |          P(X == k) = math.comb(n, k) * p ** k * (1 - p) ** (n - k)
     |
     |      The mean (expected value) and variance of the random variable are:
     |
     |          E[X] = n * p
     |          Var[X] = n * p * (1 - p)
     |
     |  choice(self, seq)
     |      Choose a random element from a non-empty sequence.
     |
     |  choices(self, population, weights=None, *, cum_weights=None, k=1)
     |      Return a k sized list of population elements chosen with replacement.
     |
     |      If the relative weights or cumulative weights are not specified,
     |      the selections are made with equal probability.
     |
     |  expovariate(self, lambd=1.0)
     |      Exponential distribution.
     |
     |      lambd is 1.0 divided by the desired mean.  It should be
     |      nonzero.  (The parameter would be called "lambda", but that is
     |      a reserved word in Python.)  Returned values range from 0 to
     |      positive infinity if lambd is positive, and from negative
     |      infinity to 0 if lambd is negative.
     |
     |      The mean (expected value) and variance of the random variable are:
     |
     |          E[X] = 1 / lambd
     |          Var[X] = 1 / lambd ** 2
     |
     |  gammavariate(self, alpha, beta)
     |      Gamma distribution.  Not the gamma function!
     |
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |
     |      The probability distribution function is:
     |
     |                  x ** (alpha - 1) * math.exp(-x / beta)
     |        pdf(x) =  --------------------------------------
     |                    math.gamma(alpha) * beta ** alpha
     |
     |      The mean (expected value) and variance of the random variable are:
     |
     |          E[X] = alpha * beta
     |          Var[X] = alpha * beta ** 2
     |
     |  gauss(self, mu=0.0, sigma=1.0)
     |      Gaussian distribution.
     |
     |      mu is the mean, and sigma is the standard deviation.  This is
     |      slightly faster than the normalvariate() function.
     |
     |      Not thread-safe without a lock around calls.
     |
     |  getstate(self)
     |      Return internal state; can be passed to setstate() later.
     |
     |  lognormvariate(self, mu, sigma)
     |    
```

## Related

Other standard-library modules pair well with `random`; explore the `python` domain of this catalog.
