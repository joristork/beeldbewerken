#!/usr/bin/env python
"""
:synopsis:  Third assignment for Beeldbewerken (BSc Informatica, UvA): In line
            with the development guidelines on http://goo.gl/yvb6B we do not
            resort to pylab.

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import sys
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from colour_histogram import col_hist
from histogram_intersection import intersections_table, histogram_intersect
from histogram_intersection import press_enter_and_wait
from model_conversion import set_model
from colour_backprojection import colour_backproject


def hist_inters_and_col_model_exercises(model, bins = (10, 10, 10)):
    """
    Corresponds to the first exercise of this assignment. Prints a histogram of
    one image for the given colour model; calculates all histograms in the
    "database" of images; calculates and displays a table of intersections of
    all database histograms; calculates and displays a table of intersections of
    the database images against a selection of external images.

    """

    print '\nColour histogram and histogram intersection exercise\n'

    image_paths, stored_model = load_images(('db', 'ext'))
    image = set_model(mpimg.imread(image_paths[1][0] + image_paths[0][0][0]), out_model=model)
    plt.subplot(1, 1, 1)

    print '\nSo, we\'re going to build a 3d colour histogram.'
    raw_input('\nLet\'s have a look at the image in question:\n(Press enter)')
    plt.imshow(np.flipud(image))
    plt.show()

    print '\nNow let\'s calculate and view the corresponding histogram printout.'
    press_enter_and_wait()
    print col_hist(image, bins, model)

    print '\nNow we\'ll build a table of histogram intersections for all the'
    print 'images in our database'
    intersections_table(image_paths, bins, model)

    print '\nOk, next we\'ll build a table of intersections for database images'
    print 'against a selection of external images'
    intersections_table(image_paths, bins, model, with_ext = True)

    menu()


def colour_back_projection_exercise(bins, model):
    """
    Uses colour back projection as descibed in Swain and Ballard's 1990 paper,
    to locate a target image within a larger image. Coordinates of best guess.
    
    """

    print '\n\nColour back projection exercise\n'
    raw_input('Let\'s view the image to search & the "target":\n(Press enter)')
    target = mpimg.imread('../images/waldo/waldo_no_bg.tiff')
    image = mpimg.imread('../images/waldo/waldo_env.tiff')
    plt.subplot(1,2,1)
    plt.imshow(np.flipud(image))
    plt.subplot(1,2,2)
    plt.imshow(np.flipud(target))
    plt.show()

    print '\nNow let\'s carry out the back projection...'
    locations, result_image = colour_backproject(target, image, bins, model)
    print '\nThe most likely match location(s):'
    print locations
    plt.subplot(1,1,1)
    plt.imshow(np.flipud(result_image))
    plt.show()

    menu()


def menu():
    """ The main menu. ``fails''= number of invalid choices """

    print '\n --- MAIN MENU ---'
    print '\n [1] Colour histogram, intersection exercise'
    print '\n [2] As above, but with YUV colour model instead of RGB'
    print '\n [3] Colour back projection exercise'
    print '\n [4] Exit'
    fails = 0

    def prompt(fails):
        """Note that we ensure ``choice'' is not interpreted as a string"""
        choice = 0
        choice = raw_input('\nChoose one:\n>> ')
        router(choice, fails)

    def router(choice, fails):
        """ Executes the desired choice, if it is valid """
        if choice == '1':
            hist_inters_and_col_model_exercises('rgb', bins=(10,10,10))
        if choice == '2':
            print '\n\n*** NB: Displayed image in false colour (not adjusted',
            print 'to model) ***'
            hist_inters_and_col_model_exercises('yuv', bins=(10,10,10))
        elif choice == '3':
            colour_back_projection_exercise(bins = (5, 5, 5), model = 'rgb')
        elif choice == '4':
            print '\nGoodbye!\n'
            sys.exit(0)
        else:
            tryagain(fails, choice)

    def tryagain(fails, choice):
        """ Gives the user three chances to enter a valid choice """ 
        fails += 1
        if (fails > 2):
            print '\nToo many wrong choices. Exiting...\n'
            sys.exit(0)
        print '\nSorry, ``'+choice+'\'\' is not a valid choice. Try again.'
        prompt(fails)

    prompt(fails)


def load_images(d):
    """ 
    `d' as in `directory'. Can return a list of image files from the image
    database (pass d='db'), the downloaded images ('ext'), or both ('db',
    'ext'). imgs[0] is a list of directory listings, and imgs[1] is a list of
    corresponding path prefixes
            
    """

    imgs = [[],[]]
    if 'db' in (d):
        imgs[0].append(os.listdir('../images/database/'))
        imgs[1].append('../images/database/')
    if 'ext' in (d):
        imgs[0].append(os.listdir('../images/external/'))
        imgs[1].append('../images/external/')
    if len(imgs[0]) + len(imgs[1]) == 0:
        return -1
    return imgs, 'rgb'


if __name__ == "__main__":
    print '\n*** Second assignment for Beeldbewerken (2011) ***\n'
    menu()
