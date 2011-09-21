#!/usr/bin/env python
"""
:synopsis:  The AssignmentOne class in this file contains some simple image
            processing implementations and associated introspective functions.
            The operations in question are contrast stretching and linear
            filtering.  This file represents our first assignmemt for the
            Beeldbewerken lab class as part of the BSc in Informatics at the
            University of Amsterdam.


.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg <luuk@noregular.com>

"""
__author__ = "Joris Stork, Lucas Swartsenburg"

import sys
from pylab import *
from numpy import load
import time

class AssignmentOne():
    """

    """


    def __init__(self):
        """ The class remembers the last: histogram, plot and input image """
        self.last_timings_plot = None
        self.last_histogram = None
        self.low_contrast_image = load("../images/lowcontrast.npy")


    def contrast_stretch(self):
        """
        
        
        """
        def cst(f):
            pass
        print '\nContrast stretching assignment (to be implemented)'
        print '\nHere is the picture:'
        imshow(self.low_contrast_image, vmin=0, vmax=1)
        gray()
        title('The low contrast lady')
        savefig('../images/shown_image.png')
        show()
        sys.exit(0)


    def linear_filter(self):
        """
       
        
        """
        print '\nLinear filter assignment (to be implemented)'
        sys.exit(0)


    def menu(self):
        """ The main menu """
        print '\n --- MAIN MENU ---'
        print '\n [1] Contrast stretching exercise'
        print '\n [2] Linear filtering exercise'
        print '\n [3] Exit'
        fails = 0

        def prompt(fails):
            """ note that we ensure ``choice'' is not interpreted as a string """
            choice = 0
            choice = raw_input('\nChoose one:\n>> ')
            router(choice, fails)

        def router(choice, fails):
            if choice == '1':
                self.contrast_stretch()
            if choice == '2':
                self.linear_filter()
            if choice == '3':
                print '\nGoodbye!\n'
                sys.exit(0)
            else:
                tryagain(fails, choice)

        def tryagain(fails, choice):
            fails += 1
            if (fails > 3):
                print '\nToo many wrong choices. Exiting...\n'
                sys.exit(0)
            print '\nSorry, '+choice+' is not a valid choice. Try again.'
            prompt(fails)

        prompt(fails)

if __name__ == "__main__":
    print '\n*** Lucas & Joris\' first assignment for Beeldbewerken (class of 2011) ***\n'    
    assignment = AssignmentOne()
    assignment.menu()

