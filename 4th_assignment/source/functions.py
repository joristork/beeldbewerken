"""
:synopsis:  These are the function implementations required for the exercises
            corresponding to this assignment.

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import scipy.ndimage
import mpl_toolkits.mplot3d.axes3d as plt3
from performance_plotter import test_performance
from cv import Filter2D

cameraman = mpimg.imread('../images/cameraman.png')


def f(X,Y, A = 1, B = 2, V = (6 * np.pi / 201), W = (4 * np.pi / 201)):
    """ Discretisation of f. """
    
    F = A * np.sin(V * X) + B * np.cos(W * Y)
    return F


def fx(X,Y, A = 1, B = 2, V = (6 * np.pi / 201), W = (4 * np.pi / 201)):
    """  Discretisation of partial derivative of f wrt x. """
    
    F = A * V * np.cos(V * X)
    return F


def fy(X,Y, A = 1, B = 2, V = (6 * np.pi / 201), W = (4 * np.pi / 201)):
    """  Discretisation of partial derivative of f wrt y. """

    F = -B * W * np.sin(W * Y)
    return F


def ffx(xx, yy):
    """ x-components of gradient vectors of f """

    return fx(xx, yy)


def ffy(xx, yy):
    """ y-components of gradient vectors of f  """

    return fy(xx, yy)


def gauss(s):
    """ Gaussian kernel with scale s and dimensions s*6+1 by s*6+1  """
    size = s * 3
    x, y = np.meshgrid(np.arange(-size,size + 1), np.arange(-size,size + 1))
    kernel = np.exp(-(x**2 / float(s) + y**2 / float(s)))
    kernel = kernel / kernel.sum()
    
    return x, y, kernel
    

def plot_3d(x, y, z):
    """ Draws a 3D plot of the given discrete function """

    fig = plt.figure()
    axes = plt3.Axes3D(fig)
    axes.plot_wireframe(x,y,z)
    axes.set_xlabel('x')
    axes.set_ylabel('y')
    axes.set_zlabel('z')
    plt.show()
    
    
def time_gauss_convolves(f, s_range, mode='nearest'):
    """   """

    module = 'functions'
    statements = []
    functions = []
    for s in s_range:
        statements.append('convolve('+f+', gauss(%d))' % s)
        print statements[-1]
        functions.append('convolve, gauss, cameraman')
    test_performance(module, statements, functions, 4)

    pass


def gauss1(s):
    """   """
    size = s * 3
    
    x = y = np.arange(-size, size + 1)
    
    ker_x = np.exp(-(x**2 / float(s)))
    ker_x = ker_x / ker_x.sum()    
    ker_y = np.array([[s] for s in ker_x])

    return ker_x, ker_y
    
def time_gauss1_convolves(f, s_range, m='nearest'):
    """   """

    c = cameraman[:,:,0]

    
    ker_x, ker_y = gauss1(12)
    
    convolve1d(c,ker_x)

def gd(f, s, iorder, jorder):
    """   """

    pass


def canny(f, s):
    """   """

    pass


def convolve(f, kernel, mode='nearest'):
    """   """

    result = scipy.ndimage.convolve(f, kernel)
    plt.subplot(1,1,1)
    plt.imshow(result)
    plt.gray()
    plt.show()
    return result
    
def convolve1d(f, ker_x, mode='nearest'):

    newimage_x = scipy.ndimage.convolve1d(c,ker_x, axis=0, mode='nearest')    
    newimage = scipy.ndimage.convolve1d(newimage_x,ker_x,axis=1, mode='nearest')
    plt.imshow(newimage)
    plt.gray()
    plt.show()

    return newimage
