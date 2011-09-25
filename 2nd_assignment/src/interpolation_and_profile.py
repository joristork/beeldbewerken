"""
:synopsis:  Algorithms for first exercise of assignment 2 (cf.
            beeld_2nd_assignment.py): interpolation and profile.

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import numpy as np
import matplotlib.pyplot as plt
import cv
import matplotlib.image as mpimg
from scipy.ndimage.interpolation import zoom


def inImage(image, x, y):
    """ Returns True if coordinates are within given image domain """
    M, N = image.shape
    if x < 0 or y < 0 or x >= N or y >= M: 
        return False
    return True


def nearest_interpolate(image, x, y):
    """ As per lecture notes """
    best_distance = 2
    x0 = (int)(x)
    y0 = (int)(
    if np.sqrt((x-x0)*(x-x0)+(y-y0)*(y-y0))


def bilinear_interpolate(image, x, y):
    """ As per lecture notes """


def pV(image, x, y, method):
    """ 
    Returns pixel value f(x,y) even for non-integer x, y. Returns -1 is method
    value invalid 
    
    """
    if not inImage(image, x, y):
        return 0
    if method == 'nearest':
        return nearest_interpolate(image, x, y)
    if method == 'linear':
        return bilinear_interpolate(image, x, y)
    else return -1
