#!/usr/bin/env python
"""
:synopsis:  This file contains the answers to two exercises for the first
            Beeldbewerkan assignment. In line with the development guidelines
            on http://goo.gl/yvb6B we do not resort to pylab for this script.

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import sys
import matplotlib.pyplot as plt
import numpy as np
from linfilters import linfilter
from linfilters import hatman_image
from linfilters import f
from performance_plotter import test_performance


def contrast_stretching_exercise():
    """
    Demonstrates a contrast stretching algorithm using a single figure with four
    subplots: one pre-, and one post- cst image + histogram pair.
    
    """

    def cst(image_array):
        """ The actual contrast stretching algorithm """
        maxval = np.amax(image_array)
        minval = np.amin(image_array)
        return ((image_array-minval) / (maxval-minval))

    print '\nContrast stretching assignment\n'
    raw_input('You will now be shown a figure of results (press enter):')
    plt.subplot(2,2,1)
    plt.title('The low contrast lady')
    image_array = np.load("../images/lowcontrast.npy")
    plt.imshow(image_array, vmin=0, vmax=1)
    plt.subplot(2,2,2)
    plt.title('Her histogram')
    hist_values, bin_edges, patch = plt.hist(image_array.flatten(), bins=40)
    plt.axis([0,1,0,4000])
    plt.subplot(2,2,3)
    plt.title('The lady after cst')
    image_csted = cst(image_array)
    plt.gray()
    plt.imshow(image_csted, vmin=0, vmax=1)
    plt.subplot(2,2,4)
    plt.title('The histogram after cst')
    hist_values, bin_edges, patch = plt.hist(image_csted.flatten(), bins=40)
    plt.axis([0,1,0,4000])
    plt.show()
    plt.close('all')
    raw_input('You will now be taken to the menu (press enter)')
    menu()


def linear_filtering_exercise():
    """
    Demonstrates four different linear filter implementations, first with side
    by side plots of their output by way of functional verification, and second
    with execution time measurements by way of a performance test. Timing is
    done for different neighbourhood sizes.
    
    """

    function_names = ['linfilter1()', 'linfilter2()', 'linfilter3()', 
                         'linfilter4()']

    def draw_plots():
        """ Plots original image alongside linfilter implementation outputs """
        raw_input('\nYou will now be shown graphical results (press enter):')
        plt.subplot(2,4,1)
        plt.title('original image')
        plt.imshow(hatman_image)
        plt.gray()
        i = 5
        for function_nr in xrange(4):
            g = linfilter(function_nr+1, w_size = 25)
            plt.subplot(2,4,i)
            plt.title(function_names[i-5])
            plt.imshow(g)
            plt.gray()
            i += 1    
        plt.show()

    draw_plots()
    w_sizes = ['9', '25', '121']
    for i in xrange (3):
        raw_input('\n\nPerformance tests: %d of 3 to follow (press enter)' % (i+1))
        print '** Performance test for w_size = '+w_sizes[i]+' **'
        test_performance('linfilters', 'linfilter', function_names, 5, 
                         ', w_size = '+w_sizes[i])
    #raw_input('\nPerformance tests: 2 of 3')
    #print '** Performance test for w_size = 25 **'
    #test_performance('linfilters', 'linfilter', function_names, 5, ', w_size = 25')
    #raw_input('\nPerformance tests: 3 of 3')
    #print '** Performance test for w_size = 121 **'
    #test_performance('linfilters', 'linfilter', function_names, 5, ', w_size = 121')
    #raw_input('\nYou will now be taken to the menu (press enter)')
    menu()


def menu():
    """ The main menu. ``fails''= number of invalid choices """
    print '\n --- MAIN MENU ---'
    print '\n [1] Contrast stretching exercise'
    print '\n [2] Linear filtering exercise'
    print '\n [3] Exit'
    fails = 0

    def prompt(fails):
        """Note that we ensure ``choice'' is not interpreted as a string"""
        choice = 0
        choice = raw_input('\nChoose one:\n>> ')
        router(choice, fails)

    def router(choice, fails):
        """ Executes the desired choice, if it is valid """
        if choice == '1':
            contrast_stretching_exercise()
        elif choice == '2':
            linear_filtering_exercise()
        elif choice == '3':
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

if __name__ == "__main__":
    print '\n*** First assignment for Beeldbewerken (2011) ***\n'
    menu()
