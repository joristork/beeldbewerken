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

hatman_rgb = mpimg.imread('../images/hatman.png')
hatman_image = np.mean(hatman_rgb,2)
f = hatman_image


