"""
:synopsis:  Functions for converting an image to a different colour model.
            Currently supports RGB to HSV and RGB to YUV conversion.

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import numpy as np


def rgb_to_yuv(pixel):
    """
    Given an RGB pixel, returns its YUV colour model representation.
    Algorithm inspired from http://en.wikipedia.org/wiki/YUV

    """

    transform = np.array([[0.299, 0.587, 0.114],
                         [-0.14713, -0.28886, 0.436],
                         [0.615, -0.51499, -0.10001]])
    return np.dot(transform, pixel)


def rgb_to_hsv(pixel):
    """
    Given an RGB pixel, returns its HSV colour space representation.
    Algorithm inspired from http://paulbourke.net/texture_colour/convert/

    """

    delta = max(pixel) - min(pixel)
    r, g, b = pixel
    v = max(pixel)
    s = 0
    if v > 0:
        s = delta / v
    h = 0
    if delta > 0:
        if (v is r) and (v is not g):
            h += (g - b) / delta
        if (v is g) and (v is not b):
            h += 2 + (b - r) / delta
        if (v is b) and (v is not r):
            h += 4 + (r - g) / delta
        h += 60
    return h, s, v


def set_model(image, in_model = 'rgb', out_model = 'rgb'):
    convertor = None
    if in_model is 'rgb':
        if out_model is 'rgb':
            return image
        elif out_model is 'hsv':
            convertor = rgb_to_hsv
        elif out_model is 'yuv':
            convertor = rgb_to_yuv
        else:
            return -1
    else: return -1
    result = image
    i = 0 
    for row in image:
        j = 0
        for pixel in row:
            result[i][j] = convertor(pixel)
            j += 1
        i += 1
    return result
