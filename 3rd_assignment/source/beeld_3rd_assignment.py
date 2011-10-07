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
from histogram_intersection import histogram_intersect

def hist_inters_col_model_exercise(model):
    """
    Corresponds to the first exercise of this assignment. Prints a histogram of
    one image for the given colour model; calculates all histograms in the
    "database" of images; calculates and displays a table of intersections of
    all database histograms; calculates and displays a table of intersections of
    the database images against a selection of external images.
    
    """

    print '\nColour histogram and histogram intersection exercise\n'

    bins = (10, 10, 10)
    images = load_images(('db','ext'))
    image = mpimg.imread(images[1][0]+images[0][0][0])
    plt.subplot(1,1,1)

    print '\nSo, we\'re going to build a 3d colour histogram.'
    raw_input '\nLet\'s have a look at the image in question:\n(Press enter)'
    plt.imshow(np.flipud(image))
    plt.show()

    print '\nNow let\'s calculate + view the corresponding histogram printout.'
    press_enter_and_wait()
    print col_hist(image, bins, model)

    print '\nNow we\'ll build a table of histogram intersections for all the'
    print 'images in our database'
    intersections_table(images)
    menu()


def intersections_table(images, with_ext = False):
    """ 
    Returns a table of intersections of database image histograms against
    themselves, or, if "with_ext" == "true", of database histograms against
    "external" image histograms.
    
    """
    print '\nStep 1: calculate histograms'
    press_enter_and_wait()
    db_histograms = []
    for img in images[0][0]:
        image = mpimg.imread(images[1][0]+img)
        db_histograms.append(col_hist(image, bins, model))
    ext_histograms = []
    if with_ext:
        for img in images[0][1]:
        image = mpimg.imread(images[1][1]+img)
        ext_histograms.append(col_hist(image, bins, model))

    print '\nStep 2: build table of intersections'
    press_enter_and_wait()
    db_in_tbl = [['I\\M']]
    for name in images[0][0]:
        db_in_tbl[0].append(name[0:3])
    for name in images[0][0]:
        db_in_tbl.append([name[0:3]])
    for h1 in db_histograms:
        j = 1
        for h2 in db_histograms:
            db_in_tbl[j].append(histogram_intersect(h1, h2))
            j += 1
    raw_input '\nA printout of the resulting table follows:\n(press enter)'
    print db_in_tbl

def press_enter_and_wait():
    raw_input('(Press enter)')
    print 'This may take a while...'


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
