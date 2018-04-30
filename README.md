# optipy

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/optipy/master.svg)](https://circleci.com/gh/nschloe/optipy)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/optipy.svg)](https://codecov.io/gh/nschloe/optipy)
[![Codacy grade](https://img.shields.io/codacy/grade/2741eedd98a24ee0b65319c1f436f40e.svg)](https://app.codacy.com/app/nschloe/optipy/dashboard)
[![PyPi Version](https://img.shields.io/pypi/v/optipy.svg)](https://pypi.org/project/optipy)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/optipy.svg?logo=github&label=Stars)](https://github.com/nschloe/optipy)

optipy contains a generic optimization/minimization method. Its creation was
motivated by the absence of an implementation of Newton's method with a custom
Hessian solver in SciPy (see [this
bug](https://github.com/scipy/scipy/issues/8756)).


The mandatory Rosenbrock example:
```python
a = 1.0
b = 100.0

def fun(x):
    return (a-x[0])**2 + b*(x[1] - x[0]**2)**2

def jac(x):
    return numpy.array([
        -2*(a-x[0]) - 4*b*(x[1] - x[0]**2) * x[0],
        2*b*(x[1] - x[0]**2)
        ])

def hess_inv(x, grad):
    hess = numpy.array([
        [2 + 8*b*x[0]**2 - 4*b*(x[1] - x[0]**2), -4*b*x[0]],
        [-4*b*x[0], 2*b]
        ])
    return -numpy.linalg.solve(hess, grad)

sol = optipy.minimize(
    fun=fun,
    x0=[-1.0, 3.5],
    jac=jac,
    get_search_direction=hess_inv,
    atol=1.0e-5
    )
```
This is basically the exact Newton method. When setting `get_search_direction`
to `lambda x, grad: -grad`, one gets the steepest descent method. For larger
computations, one will typically replace this with a tailored solver, e.g., a
preconditioned Krylov solver.

The return type is largely compatible with SciPy's generic return type,
[OptmizeResult](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.OptimizeResult.html#scipy.optimize.OptimizeResult).


### Installation

optipy is [available from the Python Package
Index](https://pypi.org/project/optipy/), so simply do
```
pip install -U optipy
```
to install or upgrade. Use `sudo -H` to install as root or the `--user` option
of `pip` to install in `$HOME`.


### Testing

To run the optipy unit tests, check out this repository and type
```
pytest
```

### Distribution
To create a new release

1. bump the `__version__` number,

2. publish to PyPi and tag on GitHub:
    ```
    $ make publish
    ```

### License

optipy is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
