# -*- coding: utf-8 -*-
#
from __future__ import print_function

from collections import namedtuple

import numpy
import scipy.optimize


def minimize(fun, x0, jac, get_search_direction, atol, maxiter=None):
    '''Generic minimization routine.
    '''
    x = x0.copy()

    old_fx = None
    fx = fun(x)
    grad = jac(x)

    nfev = 0
    nit = 0
    njev = 0

    while numpy.dot(grad, grad) > atol**2:
        assert maxiter is None or nit < maxiter, \
            'Maximum number of iterations reached.'
        nit += 1

        # get the search direction
        p = get_search_direction(x, grad)

        # Do a line search in direction p
        alpha, fc, gc, fx, old_fx, _ = scipy.optimize.line_search(
            fun, jac, x, p,
            old_fval=fx,
            old_old_fval=old_fx,
            )
        assert alpha is not None, 'Line search not successful.'

        nfev += fc
        njev += gc

        # update
        x += alpha * p
        grad = jac(x)

    OptimizeResult = namedtuple(
        'OptimizeResult',
        ['fun', 'jac', 'nfev', 'nit', 'njev', 'status', 'success', 'x']
        )
    sol = OptimizeResult(
        fun=fx, jac=grad,
        nfev=nfev,
        nit=nit,
        njev=njev,
        status=0,
        success=True,
        x=x
        )
    return sol
