# -*- coding: utf-8 -*-
#
import matplotlib.tri
import matplotlib.pyplot as plt
import numpy

import optipy


def test_gradient():
    a = 1.0
    b = 100.0

    def fun(x):
        return (a-x[0])**2 + b*(x[1] - x[0]**2)**2

    def jac(x):
        return numpy.array([
            -2*(a-x[0]) - 4*b*(x[1] - x[0]**2) * x[0],
            2*b*(x[1] - x[0]**2)
            ])

    def get_search_direction(x, grad):
        return -grad

    sol = optipy.minimize(
        fun=fun,
        x0=[-1.0, 3.5],
        jac=jac,
        get_search_direction=get_search_direction,
        atol=1.0e-5
        )

    assert abs(sol[0] - a) < 1.0e-4
    assert abs(sol[1] - a**2) < 1.0e-4
    return


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

    plot(fun, n=100)
    plt.show()
    exit(1)

    assert abs(sol[0] - a) < 1.0e-5
    assert abs(sol[1] - a**2) < 1.0e-5
    return


def plot(f, n=10):
    x = numpy.linspace(-2, +2, n)
    y = numpy.linspace(0, +4, n)
    X, Y = numpy.meshgrid(x, y)
    XY = numpy.stack([X, Y])

    z = numpy.array(f(XY), dtype=float)

    triang = matplotlib.tri.Triangulation(X.flatten(), Y.flatten())
    plt.tripcolor(triang, z.flatten(), shading='flat')
    plt.colorbar()

    plt.set_cmap('viridis')
    plt.gca().set_aspect('equal')
    return


if __name__ == '__main__':
    # test_gradient()
    test_newton()
