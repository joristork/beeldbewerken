"""
:synopsis:  

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import numpy as np
import matplotlib.pyplot as plt
import cv
import matplotlib.image as mpimg
from scipy.ndimage.interpolation import zoom


def histogram_intersect(h1, h2):
    """
    Returns the intersections of histograms h1 and h2. Algorithm taken from
    Swain and Ballard, 1990. h1 is taken as the "image", h2 as the "model". 

    """

    flat_h1 = h1.flatten()
    flat_h2 = h2.flatten()
    sum_minima = 0
    for pair in zip(flat_h1, flat_h2):
        sum_minima += min(pair)
    model_size = np.sum(flat_h2)
    return sum_minima / model_size
