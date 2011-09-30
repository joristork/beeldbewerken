"""
:synopsis:  Algorithms for third exercise of assignment 2 (cf.
            beeld_2nd_assignment.py): affine transformation.

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import numpy as np
from interpolation_and_profile import bilinear_interpolate 

def affineTransform(image, x1, y1, x2, y2, x3, y3, M, N):
    """
    This function takes three points as a input:
        1: the point that should be placed into the upper left corner
        2: the point that should be placed into the lower left corner
        3: the point that should be placed into the lower right corner
        
    M is the height of the resulting image and N is the width

    The return value is a new image with the points placed into the
    correct corners.
    """
    m = np.array([[x1,y1,1,0,0,0],[0,0,0,x1,y1,1],[x2,y2,1,0,0,0],
            [0,0,0,x2,y2,1],[x3,y3,1,0,0,0],[0,0,0,x3,y3,1]])
    
    q = np.array([0,0,0,M,N,M]).transpose()
    A = np.append(np.linalg.lstsq(m, q)[0], np.array((0.0,0.0,1.0), dtype=float)).reshape(3,3)

    Ainv =  np.linalg.inv(A)
    newimage = np.empty((M,N), dtype=float)
    for y in xrange(M):
        for x in xrange(N):
            newx =  np.dot(Ainv, [x,y,1])
            newimage[y][x] = bilinear_interpolate(image, newx[0], newx[1])

    return newimage
