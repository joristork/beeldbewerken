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


def pV(image, x, y, method):
    interpolatedValue, constantValue = 0 

    if method == "nearest":
        if inImage(image, x, y):
            return interpolatedValue
        else:
            return constantValue
    if method == "linear":
        if inImage(image, x, y):
            return interpolatedValue
        else:
            return constantValue

def inImage(image, x, y):
    return True
