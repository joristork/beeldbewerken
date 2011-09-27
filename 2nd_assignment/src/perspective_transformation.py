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
    p1 = [x1,y1]
    p2 = [x2,y2]
    p3 = [x3,y3]
    p4 = [x4,y4]
    
    # M = rijen
    # N = kolommen

    p1b = [0,0]
    p2b = [0,M]
    p3b = [N,M]
    p4b = [N,0]

    m = [[p1[0],p1[1],1,0,0,0,-p1b[0] * p1[0],-p1b[0] * p1[1],-p1b[0]], [
        0,0,0,p1[0],p1[1],1,-p1b[1] * p1[0],-p1b[1] * p1[1],-p1b[1]],[
        
        p1[0],p1[1],1,0,0,0,-p1b[0] * p1[0],-p1b[0] * p1[1],-p1b[0]], [
        0,0,0,p1[0],p1[1],1,-p1b[1] * p1[0],-p1b[1] * p1[1],-p1b[1]],[

        p1[0],p1[1],1,0,0,0,-p1b[0] * p1[0],-p1b[0] * p1[1],-p1b[0]], [
        0,0,0,p1[0],p1[1],1,-p1b[1] * p1[0],-p1b[1] * p1[1],-p1b[1]],[

        p1[0],p1[1],1,0,0,0,-p1b[0] * p1[0],-p1b[0] * p1[1],-p1b[0]], [
        0,0,0,p1[0],p1[1],1,-p1b[1] * p1[0],-p1b[1] * p1[1],-p1b[1]]]

    
    return image
