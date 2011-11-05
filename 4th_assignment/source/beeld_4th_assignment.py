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
from functions import *


def analytical_local_structure():
    """
    Discretises a 2D periodic function and its partial derivatives in each
    dimension, then uses the latter to derive component values for gradient
    vectors of the former, before drawing a quiver plot of the gradient vectors
    over a plot of the original function.

    """

    os.system(['clear','cls'][os.name == 'nt'])
    print '\nAnalytical local structure exercises\n'

    x = np.arange(-100,101)
    y = np.arange(-100,101)
    Y, X = np.meshgrid(x,y)

    print '\nSo, we\'re going to make F, a discrete version of function f.'
    raw_input('\nLet\'s have a look at the result:\n(Press enter)')
    plt.subplot(1,1,1)
    plt.imshow(f(X,Y))
    plt.gray()
    plt.show()
    
    print '\nNow let\'s generate Fx and Fy: the discretised derivatives.'
    raw_input('\nLet\'s have a look at the result:\n(Press enter)')
    plt.subplot(1,2,1)
    plt.imshow(fx(X,Y))
    plt.subplot(1,2,2)
    plt.imshow(fy(X,Y))
    plt.gray()
    plt.show()

    print '\nNow we\'ll plot the gradient vectors on F'
    raw_input('\nLet\'s have a look at the result:\n(Press enter)')
    xx = np.arange(-100, 101, 10)
    yy = np.arange(-100, 101, 10)
    YY, XX = np.meshgrid(yy, xx)
    plt.subplot(1,1,1)
    plt.imshow(f(X,Y))
    plt.gray()
    plt.quiver(yy+100, xx+100, ffy(XX,YY), - ffx(XX,YY), color = 'red')
    plt.show()

    menu()


def gaussian_convolution():
    """
    Demonstrates our implementation of Gaussian convolution using a 2D Gaussian
    kernel with scale (variance) s.

    """

    os.system(['clear','cls'][os.name == 'nt'])
    print '\nGaussian convolution exercises\n'

    x, y, kernel = gauss(4)

    print '\nSo, we\'ve implemented a function gauss(s). Note:'
    print '\nSampling grid size: %d by %d' % kernel.shape
    print '\nSum of kernel values: %d' % kernel.sum()

    print '\n\nNow let\'s plot the kernel.'
    raw_input('\n(Press enter to continue)')
    plot_3d(x, y, kernel)

    print '\nNow we\'ll compute the Gaussian convolution...'
    print '\nLet\'s time our implementation and plot time against scale s:'
    s_range = (1, 2, 3, 5, 7, 9, 11, 15, 19)
    print '\nValues for s: %s' % (s_range,)
    raw_input('\n(Press enter)')

    time_gauss_convolves('cameraman', s_range)

    menu()


def separable_gaussian_convolution():
    """
    Demonstrates our implementation of Gaussian convolution using the
    separability property of the Gauss function.

    """

    print '\nSeparable Gaussian convolution exercises\n'

    print '\nSo, we\'ve implemented a function gauss1 (1D gauss kernels).'
    print '\nLet\'s time our convolve implementation using gauss1() against s.'
    raw_input('\n(Press enter to continue)')
    plt.subplot(1,1,1)
    plt.imshow(image)
    plt.show()

    menu()


def gaussian_derivatives():
    """

    """
    
    temp = mpimg.imread('../images/cameraman.png')
    cameraman = temp[:,:,0]    
    plt.imshow(gd(cameraman, 1, 0, 0))
    plt.gray()
    plt.show()
    
    
    
    
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
    os.system(['clear','cls'][os.name == 'nt'])
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
