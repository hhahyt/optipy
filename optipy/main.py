# -*- coding: utf-8 -*-
#
from __future__ import print_function

import numpy
import scipy.optimize


def minimize(fun, x0, jac, get_search_direction, atol):
    '''Generic minimization routine.
    '''
    x = x0.copy()

    old_fx = None
    fx = fun(x)
    grad = jac(x)

    while numpy.dot(grad, grad) > atol**2:
        # get the search direction
        p = get_search_direction(x, grad)

        # Do a line search in direction p
        alpha, _, _, fx, old_fx, _ = scipy.optimize.line_search(
            fun, jac, x, p,
            old_fval=fx,
            old_old_fval=old_fx,
            )
        assert alpha is not None, 'Line search not successful.'

        # update
        x += alpha * p
        grad = jac(x)

    return x
