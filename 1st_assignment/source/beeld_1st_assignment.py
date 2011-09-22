#!/usr/bin/env python
"""
:synopsis:  This file contains some simple image processing implementations and
            associated introspective functions.  The operations in question are
            contrast stretching and linear filtering.  This file represents our
            first assignmemt for the Beeldbewerken lab class as part of the BSc
            in Informatics at the University of Amsterdam.

            In line with the development guidelines on http://goo.gl/yvb6B we do
            not resort to pylab for this script.

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""
__author__ = "Joris Stork, Lucas Swartsenburg"

import sys
import matplotlib.pyplot as plt
import numpy as np


def contrast_stretching_exercise():
    """
    This function displays builds and then displays subplots in a 2x2 arrangment
    to demonstrate an implementation of contrast stretching.  First the low
    contrast image is loaded (with automatic stretching disabled) and set to a
    greyscale colourmap before being plotted top-left. Second, a histogram of
    the greyscale values of loaded image is plotted top-right. Then, our cst
    function is applied to the loaded image, and the resulting image is plotted
    bottom-left. Finally, the corresponding histogram is plotted bottom-right.
    
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
    plt.gray()
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
    choice = raw_input('You will now be taken to the menu (press enter)')
    menu()


def linear_filtering_exercise():
    """
   
    
    """

    def linfilter1(f, w):
        """ First linear filter implementation """
        
        def value(i,j):
            """ Returns value at (i,j) if it's a valid index, else 0 """ 
            if i < 0 or i >= M or j < 0 or j >= N:
                return 0
            return f[i,j]

        g = empty(f.shape, dtype=f.dtype)
        M, N = f.shape
        K, L = (array(w.shape) - 1) / 2

        for j in xrange(N):
            for i in xrange(M):
                summed = 0
                for k in xrange(-K, K+1):
                    for l in xrange(-L, L+1):
                        summed += value(i + k, j + l) * w[k + K, l + L]
                g[i,j] = summed
        return g

    def linfilter2(f, w):
        """ Second linear filter implementation """
        pass

    def linfilter3(f, w):
        """ Third linear filter implementation """
        pass

    def linfilter4(f, w):
        """ Fourth linear filter implementation """
        pass

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
        if choice == '2':
            linear_filtering_exercise()
        if choice == '3':
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
