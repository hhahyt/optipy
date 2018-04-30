# -*- coding: utf-8 -*-
#
from __future__ import print_function

import numpy
import scipy.optimize


def newton(fun, x0, jac, hess_inv, atol):

    x = x0.copy()
    grad = jac(x)

    fx = fun(x0)

    while numpy.dot(grad, grad) > atol**2:
        # get the search direction
        p = -hess_inv(x, grad)

        # Do a line search in direction p
        alpha, *_ = scipy.optimize.line_search(fun, jac, x, p)
        assert alpha is not None, 'Line search not successful.'

        # update
        x += alpha * p
        grad = jac(x)

    return x
