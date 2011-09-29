"""
:synopsis:  Colour histogram building functions.

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import numpy as np


def col2bin(colour, bins, m):
    """ 
    Given a colour-tuple, a colour model and an array describing the number of
    histogram bins for each colour, this function returns a tuple that indexes
    the corresponding bin in the histogram. `m' is a list of the colour models
    supported by this function; the elements of `bin_step' specify the spectral
    `width' of a bin per colour.

    """

    models = ['rgb']
    if m in models:
        index = np.zeros[len(m)]
        bin_step = np.zeros(len(m))
        for i in xrange(len(m)):
            np.append(bin_step, (255 / bins[i]))
            index[i] = (int) (colour[i] / bin_step[i])
        return list(index)
    else:
        return -1


def colHist(image, bins, model):
    """ 
    Given an image; a tuple indicating the number of bins per colour axis; and a
    colour model, this function fills and then returns a colour histogram in the
    form of an array whose rank equals the number of components of the colour
    model. `p' indexes a pixel in the image during iteration. col2bin() is used
    to obtain a histogram bin index for a given colour.
    
    """
    h = np.zeros(bins)
    for p in domainIterator(image):
        h[col2bin(image[p])] += 1
    return h
