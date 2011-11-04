"""
:synopsis:  These are the function implementations required for the exercises
            corresponding to this assignment.

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import numpy as np
import matplotlib.image as mpimg


def f(X,Y, A = 1, B = 2, V = (6 * np.pi / 201), W = (4 * np.pi / 201)):
    """ Discretisation of f. """
    
    F = A * np.sin(V * X) + B * np.cos(W * Y)
    return F


def fx(X,Y, A = 1, B = 2, V = (6 * np.pi / 201), W = (4 * np.pi / 201)):
    """   """
    
    F = A * V * np.cos(V * X)
    return F


def fy(X,Y, A = 1, B = 2, V = (6 * np.pi / 201), W = (4 * np.pi / 201)):
    """   """

    F = -B * W * np.sin(W * Y)
    return F


def ffx(xx, yy):
    """   """

    return fx(xx, yy)


def ffy(xx, yy):
    """   """

    return fy(xx, yy)


def gauss(s):
    """   """

    pass


def convolve(f, gauss, mode='nearest'):
    """   """

    pass


def gauss1(s):
    """   """

    pass


def gd(f, s, iorder, jorder):
    """   """

    pass


def canny(f, s):
    """   """

    pass

