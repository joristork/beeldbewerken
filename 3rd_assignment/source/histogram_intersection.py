"""
:synopsis:  Two functions: the first returns the intersection of two histograms,
            and the second prints a table of intersections between two lists of
            histograms 

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import numpy as np
import matplotlib.image as mpimg
from colour_histogram import col_hist
from model_conversion import set_model


def histogram_intersect(h1, h2):
    """
    Returns the intersections of histograms h1 and h2. Algorithm taken from
    Swain and Ballard, 1990. h1 is taken as the "image", h2 as the "model". 

    """

    flat_h1 = h1.flatten()
    flat_h2 = h2.flatten()
    sum_minima = 0.0
    for pair in zip(flat_h1, flat_h2):
        sum_minima += min(pair)
    model_size = np.sum(flat_h2) * 1.0
    return round((sum_minima / model_size), 3)


def intersections_table(image_paths, bins, model, with_ext = False):
    """ 
    Returns a table of intersections of database image histograms against
    themselves, or, if "with_ext" == "true", of database histograms against
    "external" image histograms.
    
    """

    print '\nStep 1: calculate histograms'
    press_enter_and_wait()
    db_histograms = []
    for img_name in image_paths[0][0]:
        image = set_model(mpimg.imread(image_paths[1][0]+img_name), out_model=model)
        db_histograms.append(col_hist(image, bins, model))
    ext_histograms = []
    if with_ext:
        for img_name in image_paths[0][1]:
            image = set_model(mpimg.imread(image_paths[1][1]+img_name), out_model=model)
            ext_histograms.append(col_hist(image, bins, model))
    else:
        ext_histograms = db_histograms

    print '\nStep 2: build table of intersections'
    press_enter_and_wait()
    intersections_table = [['I\\M ']]
    for name in image_paths[0][0]:
        intersections_table[0].append(name[0:4])
    image_names = image_paths[0][0]
    if with_ext:
        image_names = image_paths[0][1]
    for name in image_names:
        intersections_table.append([name[0:4]])
    i = 1
    for h1 in ext_histograms:
        for h2 in db_histograms:
            rounded_result = '%.2f'%round(histogram_intersect(h1, h2), 2)
            intersections_table[i].append(rounded_result)
        i += 1

    raw_input('\nA printout of the resulting table follows:\n(press enter)')
    for item in intersections_table[0]:
        print '%s '%item,
    print '\n',
    for row in intersections_table[1:]:
        for item in row:
            print '%s '%item,
        print '\n',

def press_enter_and_wait():
    raw_input('(Press enter)')
    print 'This may take a while...\n'
