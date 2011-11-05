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

temp = mpimg.imread('../images/cameraman.png')
cameraman = temp[:,:,0]


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
    kernel = np.exp(-(x**2  + y**2 / float(s)))
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
    """ Calls timing function for convolution using gauss() """

    module = 'functions'
    statements = []
    functions = []
    for s in s_range:
        statements.append('convolve('+f+', gauss(%d)[2])' % s)
        functions.append('convolve, gauss, cameraman')
    test_performance(module, statements, functions, 3)


def gauss1(s):
    """ Returns 1D Gaussian kernel, for separable Gaussian convolution """

    size = s * 3
    
    x = y = np.arange(-size, size + 1)
    
    ker_x = np.exp(-(x**2 / float(s)))
    return ker_x / ker_x.sum()    
    #ker_y = np.array([[s] for s in ker_x])

 
def time_gauss1_convolves(f, s_range, m='nearest'):
    """ Calls timing function for convolution using gauss1() """
    
    module = 'functions'
    statements = []
    functions = []
    for s in s_range:
        statements.append('convolve1d('+f+', gauss1(%d))' % s)
        functions.append('convolve1d, gauss1, cameraman')
    test_performance(module, statements, functions, 3)


def gd(f, s, iorder, jorder):
    """   """
    if iorder + jorder <= 2:
        size = s * 3
        x, y = np.meshgrid(np.arange(-size,size + 1), np.arange(-size,size + 1))
        if iorder == 0 and jorder == 1:
            ker = ((2*y)/float(s)) * np.exp(-(x**2  + y**2 / float(s))) 
        elif iorder == 0 and jorder == 2:
            ker = ((4*y**2 - 2*float(s))/float(s**2)) * np.exp(-(x**2  + y**2 / float(s))) 
        elif iorder == 1 and jorder == 0:
            ker = ((2*x)/float(s)) * np.exp(-(x**2  + y**2 / float(s))) 
        elif iorder == 2 and jorder == 0:
            ker = ((4*x**2 - 2*float(s))/float(s**2)) * np.exp(-(x**2  + y**2 / float(s)))            
        elif iorder == 1 and jorder == 1:
            ker = ((4*x*y)/float(s**2)) * np.exp(-(x**2  + y**2 / float(s)))        
        elif iorder == 0 and jorder == 0:
            ker = np.exp(-(x**2  + y**2 / float(s))) 
            
        return convolve(f, ker)
            
                                                
    
    else:
        print "Invalid order"
        return 0


def canny(f, s):
    """   """

    pass


def convolve(f, kernel, m='nearest'):
    """ Wrapper for scipy's convolve(). Useful for the timeit function. """

    return scipy.ndimage.convolve(f, kernel,mode=m)

    
def convolve1d(f, kernel1d, m='nearest'):
    """ Convolves along one axis, then along the other. """

    newimage_x = scipy.ndimage.convolve1d(f, kernel1d, axis = 0, mode = m)    
    newimage = scipy.ndimage.convolve1d(newimage_x, kernel1d, axis = 1, mode = m)

    return newimage
