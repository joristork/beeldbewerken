#!/usr/bin/env python
"""
:synopsis:  This file contains the answers to two exercises for the first
            Beeldbewerkan assignment.

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
    This function demonstrates a contrast stretching algorithm using a single
    figure with four subplots: one pre-, and one post-cst image-histogram pair.
    
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
        g = empty(f.shape, dtype=f.dtype)
        M, N = f.shape
        K, L = (array(w.shape) - 1) / 2

        for j in xrange(N):
            for i in xrange(M):
                ii = minimum(M-1 , maximum(0, arange(i-K, i+K,i+K+1)))
                jj = minimum(N - 1, maximum(0, arange(j - L, j+L + 1)))
                nbh = f[ ix_(ii, jj)]
                g[i,j] = (nbh * w).sum()
        return g

    def linfilter3(f, w):
        """ Third linear filter implementation """
        M, N = f.shape
        K, L = (array(w.shape) - 1) / 2

        di, dj = meshgrid(arange(-L, L+1), arange(-K, K+1))
        didjw = zip( di.flatten(), dj.flatten(), w.flatten())

        def translate(di,dj):
            ii = minimum(M-1, maximum(0, di+arange(M)))
            jj = minimum(N-1, maximum(0, dj+arange(N)))
            return f[ ix_(ii, jj)]

        r = 0 * f
        for di, dj, weight in didgw:
            ir += weight * translate(di,dj)
        return r

        

    def linfilter4(f, w):
        """ Fourth linear filter implementation """
        return correlate(f, w, mode= 'nearest')

    j
    g = linfilter(f, ones((5,5))/25)
    subplot(1,2,1)
    imshow(f)
    subplot(1,2,2)
    imshow(g)
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
