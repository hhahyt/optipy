# -*- coding: utf-8 -*-
#
import numpy

import optipy


def test_newton():
    a = 1.0
    b = 100.0

    def fun(x):
        return (a-x[0])**2 + b*(x[1] - x[0]**2)**2

    def jac(x):
        return numpy.array([
            -2*(a-x[0]) - 4*b*(x[1] - x[0]**2) * x[0],
            2*b*(x[1] - x[0]**2)
            ])

    def hess_inv(x, rhs):
        hess = numpy.array([
            [2 + 8*b*x[0]**2 - 4*b*(x[1] - x[0]**2), -4*b*x[0]],
            [-4*b*x[0], 2*b]
            ])
        return numpy.linalg.solve(hess, rhs)

    sol = optipy.newton(
        fun=fun,
        x0=[5.0, 4.0],
        jac=jac,
        hess_inv=hess_inv,
        atol=1.0e-5
        )

    assert abs(sol[0] - a) < 1.0e-5
    assert abs(sol[1] - a**2) < 1.0e-5
    return


if __name__ == '__main__':
    test_newton()
