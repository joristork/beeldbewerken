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

def interpolation_exercise():
    if "true" == "true":
        print "True"
    else:
        print "False"
    def pV(image, x, y, method):
        interpolatedValue, constantValue = 0 

        if method == "nearest":
            if inImage(image, x, y):
                # do interpolation
                return interpolatedValue
            else:
                # return a constant
                return constantValue
        if method == "linear":
            if inImage(image, x, y):
                # do interpolation
                return interpolatedValue
            else:
                # return a constant
                return constantValue

    def inImage(image, x, y):
        return True



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
            interpolation_exercise()
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
    print '\n*** Second assignment for Beeldbewerken (2011) ***\n'
    menu()

