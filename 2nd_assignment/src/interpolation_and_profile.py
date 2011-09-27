"""
:synopsis:  Algorithms for first exercise of assignment 2 (cf.
            beeld_2nd_assignment.py): interpolation and profile.

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.ndimage.interpolation import zoom
from scipy import array



def inImage(image, x, y):
    """ Returns True if coordinates are within given image domain """
    width, height = image.shape
    return x < width and x >= 0 and y < height and y >= 0 


def nearest_interpolate(image, x, y):
    """ As per lecture notes """
    constantValue = 0.5
    x0 = (int)(x)
    y0 = (int)(y)

    if x - x0 >= 0.5 and y - y0 >= 0.5:
        if inImage(image, x0 + 1, y0 + 1):
            return image[x0 + 1][y0 + 1]
        else:
            return constantValue
    elif x - x0 < 0.5 and y - y0 >= 0.5:
        if inImage(image, x0, y0 + 1):
            return image[x0][y0 + 1]
        else:
            return constantValue
    elif x - x0 >= 0.5 and y - y0 < 0.5:
        if inImage(image,  x0 + 1, y0):
            return image[x0 + 1][y0]
        else:
            return constantValue
    else:
        if inImage(image, x0, y0):
            return image[x0][y0]
        else:
            return contantValue


    

def bilinear_interpolate(image, x, y):
    """ As per lecture notes """
    constantValue = 0.5
    x0 = (int)(x)
    y0 = (int)(y)
    if inImage(image, x0, y0):
        p00 = image[x,y]
    else:
        return constantValue
    if inImage(image, x0, y0 + 1):
        p01 = image[x0, y0 + 1]
    else:
        return constantValue
    if inImage(image, x0 + 1, y0):
        p10 = image[x0 + 1, y0]
    else:
        return constantValue
    if inImage(image, x0 + 1, y0 + 1):
        p11 = image[x0 + 1, y0 + 1]
    else:
        return constantValue

    xdiff = x - x0
    ydiff = y - y0
    y0val = xdiff * p00 + (1 - xdiff) * p01
    y1val = xdiff * p10 + (1 - xdiff) * p11

    return ydiff * y0val + (1 - ydiff) * y1val





def pV(image, x, y, method):
    """ 
    Returns pixel value f(x,y) even for non-integer x, y. Returns -1 is method
    value invalid 
    
    """
    interpolatedValue = 0.1
    constantValue = 0.5     
    if not inImage(image, x, y):
        return constantValue
    elif method == 'nearest':
        return nearest_interpolate(image, x, y)
    elif method == 'linear':
        return bilinear_interpolate(image, x, y)
    else:
        return -1

def profile(image, x0, y0, x1, y1, n, method):
    """
    Profile of an image along line in n points
    """
    return array([pV(image,x,y,method) for (x,y) in zip(np.linspace(x0, x1, n), np.linspace(y0,y1,n))])
