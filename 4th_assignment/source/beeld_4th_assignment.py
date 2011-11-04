#!/usr/bin/env python
"""
:synopsis:  Fourth assignment for Beeldbewerken (BSc Informatica, UvA): In line
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
from functions import f, fx, fy, gradient_vectors, gauss, convolve, gauss1
from functions import gd, canny


def analytical_local_structure():
    """

    """

    print '\nAnalytical local structure exercises\n'

    print '\nSo, we\'re going to make F, a discrete version of function f.'
    raw_input('\nLet\'s have a look at the result:\n(Press enter)')
    plt.subplot(1,1,1)
    plt.imshow(f())
    plt.show()

    #print '\nNow let\'s generate Fx and Fy: the discretised derivatives.'
    #raw_input('\nLet\'s have a look at the result:\n(Press enter)')
    #plt.subplot(1,1,1)
    #plt.imshow(image)
    #plt.show()

    #print '\nNow we\'ll plot the gradient vectors on F'
    #raw_input('\nLet\'s have a look at the result:\n(Press enter)')
    #plt.subplot(1,1,1)
    #plt.imshow(image)
    #plt.show()

    menu()


def gaussian_convolution():
    """

    """

    #print '\nGaussian convolution exercises\n'

    #print '\nSo, we\'ve implemented a function gauss(s). Note:'
    #print '\nSampling grid size: %d' % 1
    #print '\nSum of kernel values: %d' % 1
    #raw_input('\n(Press enter to continue)')

    #print '\nNow let\'s plot the kernel.'
    #raw_input('\n(Press enter to continue)')
    #plt.subplot(1,1,1)
    #plt.imshow(image)
    #plt.show()

    #print '\nNow we\'ll compute the Gaussian convolution...'
    #print '\nLet\'s time our implementation and plot time against scale s:'
    #raw_input('\n(Press enter)')
    #plt.subplot(1,1,1)
    #plt.imshow(image)
    #plt.show()

    menu()


def separable_gaussian_convolution():
    """

    """

    #print '\nSeparable Gaussian convolution exercises\n'

    #print '\nSo, we\'ve implemented a function gauss1.'
    #print '\nLet\'s time our implementation and plot against scale s.'
    #raw_input('\n(Press enter to continue)')
    #plt.subplot(1,1,1)
    #plt.imshow(image)
    #plt.show()

    menu()


def gaussian_derivatives():
    """

    """

    #print '\nGaussian derivatives exercises\n'

    #print '\nSo, we\'ve implemented a function gD().'
    #print '\nLet\'s look at the 2-jet of the cameraman image.'
    #raw_input('\n(Press enter to continue)')
    #plt.subplot(1,1,1)
    #plt.imshow(image)
    #plt.show()

    menu()


def canny_edge_detector():
    """

    """

    #print '\nCanny edge detector exercise\n'

    #print '\nSo, we\'ve implemented canny() function.'
    #print '\nLet\'s test it on the cameraman image and view the result.'
    #raw_input('\n(Press enter to continue)')
    #plt.subplot(1,1,1)
    #plt.imshow(image)
    #plt.show()

    menu()

def menu():
    """ The main menu. ``fails''= number of invalid choices """

    print '\n --- MAIN MENU ---'
    print '\n [1] Analytical local structure'
    print '\n [2] Gaussian convolution'
    print '\n [3] Separable Gaussian convolution'
    print '\n [4] Gaussian derivatives'
    print '\n [5] Canny edge detector'
    print '\n [6] Exit'
    fails = 0

    def prompt(fails):
        """Note that we ensure ``choice'' is not interpreted as a string"""
        choice = 0
        choice = raw_input('\nChoose one:\n>> ')
        router(choice, fails)

    def router(choice, fails):
        """ Executes the desired choice, if it is valid """
        if choice == '1':
            analytical_local_structure()
        if choice == '2':
            gaussian_convolution()
        elif choice == '3':
            separable_gaussian_convolution()
        elif choice == '4':
            gaussian_derivatives()
        elif choice == '5':
            canny_edge_detector()
        elif choice == '6':
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
    print '\n*** Fourth assignment for Beeldbewerken (2011) ***\n'
    menu()
