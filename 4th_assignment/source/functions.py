"""
:synopsis:  These are the function implementations required for the exercises
            corresponding to this assignment.

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import numpy as np
import matplotlib.image as mpimg


def f():
    """ Discretisation of f. """
    
    x = np.arange(-100,101)
    y = np.arange(-100,101)
    Y, X = np.meshgrid(x,y)
    A = 1
    B = 2
    V = 6 * np.pi / 201
    W = 4 * np.pi / 201
    F = A * np.sin(V * X) + B * np.cos(W * Y)
    return F


def fx():
    """   """

    pass


def fy():
    """   """
    
    pass


def gradient_vectors():
    """   """

    pass


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

