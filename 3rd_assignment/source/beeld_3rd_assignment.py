#!/usr/bin/env python
"""
:synopsis:  Third assignment for Beeldbewerken (BSc Informatica, UvA): In line
            with the development guidelines on http://goo.gl/yvb6B we do not
            resort to pylab for this script.

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import sys
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from colour_histogram import colHist


def hist_inters_col_model_exercise(model):
    """
    For the given colour model, calculates pairs of histograms and their
    respective intersections from a database of 10 images; displays these
    intersections in a 10x10 table; displays respective intersections of each
    image with some web images. 
    
    
    """

    print '\nColour histogram, histogram intersection exercise\n'
    bins = (10,10,10)
    images = load_images('db')
    print images[1]
    image = mpimg.imread(images[1][0]+images[0][0][0])
    plt.subplot(1,1,1)
    plt.imshow(image)
    plt.show()
    plt.close('all')

    print colHist(image, bins, model)

    menu()


def colour_back_projection_exercise():
    """
    
    """

    menu()


def menu():
    """ The main menu. ``fails''= number of invalid choices """
    print '\n --- MAIN MENU ---'
    print '\n [1] Colour histogram, intersection exercise'
    print '\n [2] As above, but with *FILL_IN* colour model'
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
            hist_inters_col_model_exercise('rgb')
        if choice == '2':
            hist_inters_col_model_exercise('FILL_IN')
        elif choice == '3':
            colour_back_projection_exercise()
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
    return imgs


if __name__ == "__main__":
    print '\n*** Second assignment for Beeldbewerken (2011) ***\n'
    menu()
