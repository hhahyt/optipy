# optipy

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/optipy/master.svg)](https://circleci.com/gh/nschloe/optipy)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/optipy.svg)](https://codecov.io/gh/nschloe/optipy)
[![Codacy grade](https://img.shields.io/codacy/grade/8ce98e78f7ef427292593d08815c4fa3.svg)](https://app.codacy.com/app/nschloe/optipy/dashboard)
[![awesome](https://img.shields.io/badge/awesome-yes-ff69b4.svg)](https://github.com/nschloe/optipy)
[![PyPi Version](https://img.shields.io/pypi/v/optipy.svg)](https://pypi.org/project/optipy)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/optipy.svg?logo=github&label=Stars)](https://github.com/nschloe/optipy)

optipy is a small collection of optimization/minimization methods. It's
motivated by the absence of an implementation of Newton's method with a custom
Hessian solver in SciPy (see [this
bug](https://github.com/scipy/scipy/issues/8756)).


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
