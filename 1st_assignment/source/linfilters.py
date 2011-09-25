"""
:synopsis:  Four linear filter implementations, from fully self-written to a
            simple call to the standard Filter2D function in opencv.

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import numpy as np
import matplotlib.pyplot as plt
import cv
import matplotlib.image as mpimg
#from scipy.ndimage.filters import correlate1d
#from scipy.signal import correlate
from scipy.ndimage.interpolation import zoom

hatman_rgb = mpimg.imread('../images/hatman.png')
hatman_image = np.mean(hatman_rgb,2)
#f = zoom(hatman_image, 0.25)
f = hatman_image

def linfilter1(f,w):
    """ First linear filter implementation: manual (nested loops four deep) """

    def value(i, j):
        """ Returns value at (i,j) if it's a valid index, else 0 """ 
        if i < 0 or i >= M or j < 0 or j >= N:
            return 0
        return f[i,j]

    g = np.empty(f.shape, dtype=f.dtype)
    M, N = f.shape
    K, L = (np.array(w.shape) - 1) / 2

    for j in xrange(N):
        for i in xrange(M):
            summed = 0
            for k in xrange(-K, K+1):
                for l in xrange(-L, L+1):
                    summed += value(i + k, j + l) * w[k + K, l + L]
            g[i,j] = summed
    return g


def linfilter2(f, w):
    """ ... like linfilter1 but numpy function replaces 2 inner nested loops """
    g = np.empty(f.shape, dtype = f.dtype)
    M, N = f.shape
    K, L = (np.array(w.shape) - 1) / 2

    for j in xrange(N):
        for i in xrange(M):
            ii = np.minimum(M - 1 , 
                            np.maximum(0, np.arange(i - K, i + K + 1)))
            jj = np.minimum(N - 1, 
                            np.maximum(0, np.arange(j - L, j + L + 1)))
            nbh = f[np.ix_(ii, jj)]
            g[i, j] = (nbh * w).sum()
    return g


def linfilter3(f, w):
    """ ... like linfilter2, but numpy functions replace remaining two loops """
    M, N = f.shape
    K, L = (np.array(w.shape) - 1) / 2

    di, dj = np.meshgrid(np.arange(-L, L + 1), np.arange(-K, K + 1))
    didjw = zip( di.flatten(), dj.flatten(), w.flatten())

    def translate(di,dj):
        ii = np.minimum(M-1, np.maximum(0, di + np.arange(M)))
        jj = np.minimum(N-1, np.maximum(0, dj + np.arange(N)))
        return f[ np.ix_(ii, jj)]

    r = 0 * f
    for di, dj, weight in didjw:
        r += weight * translate(di,dj)
    return r


def linfilter4(f, w):
    """ Fourth linear filter implementation: entirely opencv driven """
    g = cv.fromarray(np.empty(f.shape, f.dtype))
    cv.Filter2D(cv.fromarray(f), g, cv.fromarray(w), (-1, -1))
    return np.array(g)


def linfilter(function_nr, w_size):
    linfilter_functions = [linfilter1, linfilter2, linfilter3, linfilter4]
    w = np.ones((np.sqrt(w_size), np.sqrt(w_size))) / w_size
    return linfilter_functions[function_nr-1](f, w)
