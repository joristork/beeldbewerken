"""
:synopsis:  Comprises an implementation of Swain and Ballard's 1990 "object
            location via histogram backprojection" algorithm.

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import numpy as np
import cv
from math import pow, sqrt
from colour_histogram import col_hist, col2bin
from histogram_intersection import press_enter_and_wait

def colour_backproject(target, image, bins, model):
    """ 
    Implementation of "object location via histogram backprojection" algorithm
    in Swain and Ballard's 1990 paper. Uses OpenCV library Filter2D to carry out
    covolution.
    
    """

    print '\nFirst, we build the target\'s colour histogram:'
    press_enter_and_wait()
    target_h = col_hist(target, bins, model)
    print target_h

    print '\nNext, we build the image\'s colour histogram:'
    press_enter_and_wait()
    image_h = col_hist(image, bins, model)
    print image_h
    
    print '\nNow, we compute "ratio", the ratio of target/image histograms:'
    press_enter_and_wait()
    ratio = (target_h * 1.0) / image_h
    print ratio

    print '\nNext, we replace each pixel in the image with the value of the',
    print 'bin in "ratio" that the pixel\'s colour indexes (max value: 1).'
    press_enter_and_wait()
    b = np.empty(((image.shape)[0:2]), dtype = float)
    i = 0
    for row in image:
        j = 0
        for pixel in row:
            index = col2bin(pixel, bins, model)
            b[i][j] = min(ratio[index[0]][index[1]][index[2]], 1)
            j += 1
        i += 1
    print b

    print '\nOk, now to convolve a mask with b'
    press_enter_and_wait()
    b_conv = b
    radius = 40
    w = np.zeros((81,81), dtype = float)
    i = 0
    for row in w:
        j = 0
        for element in row:
            if (sqrt(pow((10-i),2)+pow((10-j),2)) < radius):
                w[i][j] = 1
            j += 1
        i += 1
    cv.Filter2D(cv.fromarray(b), cv.fromarray(b_conv), cv.fromarray(w), (-1, -1))
    b_conv = np.array(b_conv)
    print b_conv

    print '\nFinally, we find the location of the peak of the convolved image:'
    press_enter_and_wait()
    print b_conv

    return np.where(b_conv == b_conv.max()), b_conv
