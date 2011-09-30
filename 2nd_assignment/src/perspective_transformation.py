"""
:synopsis:  Algorithms for fourth exercise of assignment 2 (cf.
            beeld_2nd_assignment.py): perspective transformation.

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import numpy as np
from interpolation_and_profile import bilinear_interpolate 

def perspectiveTransform(image, x1, y1, x2, y2, x3, y3, x4, y4, M, N):
    """
    This function takes the coordinates of four points and transforms them to
    the edges of the new picture. This new picture has a NxM resolution.

    The function uses the singe value decomposition to produce a trasposed
    V matrix. The last row of the transposed V matrix is reshaped to a 3x3 
    coefficient matrix that contains the transformation. The transformed points
    still need to be multiplied by a factor 1/s. 
    """
    p1 = [x1,y1]
    p2 = [x2,y2]
    p3 = [x3,y3]
    p4 = [x4,y4]
    
    p1b = [0,0]
    p2b = [0,M]
    p3b = [N,M]
    p4b = [N,0]

    m = np.array((
        [
            [p1[0],p1[1],1,0,0,0,-p1b[0] * p1[0],-p1b[0] * p1[1],-p1b[0]], 
            [0,0,0,p1[0],p1[1],1,-p1b[1] * p1[0],-p1b[1] * p1[1],-p1b[1]],
            
            [p2[0],p2[1],1,0,0,0,-p2b[0] * p2[0],-p2b[0] * p2[1],-p2b[0]], 
            [0,0,0,p2[0],p2[1],1,-p2b[1] * p2[0],-p2b[1] * p2[1],-p2b[1]],
            
            [p3[0],p3[1],1,0,0,0,-p3b[0] * p3[0],-p3b[0] * p3[1],-p3b[0]], 
            [0,0,0,p3[0],p3[1],1,-p3b[1] * p3[0],-p3b[1] * p3[1],-p3b[1]],
            
            [p4[0],p4[1],1,0,0,0,-p4b[0] * p4[0],-p4b[0] * p4[1],-p4b[0]], 
            [0,0,0,p4[0],p4[1],1,-p4b[1] * p4[0],-p4b[1] * p4[1],-p4b[1]]
        ]
        ), dtype=float)

    U,D,VT = np.linalg.svd(m)

    p = VT[-1]

    P = np.linalg.inv(np.reshape(p, (3,3)))

    newimage = np.empty((M,N), dtype=float)
    for y in xrange(M):
        for x in xrange(N):
            newp =  np.dot(P, [x,y,1])
            s = newp / newp[2]
            newimage[y][x] = bilinear_interpolate(image, s[0], s[1])
            
    return newimage

