#!/usr/bin/env python
"""
:synopsis:  Second assignment for Beeldbewerken (BSc Informatica, UvA): ``Python
            for IP & CV''. In line with the development guidelines on
            http://goo.gl/yvb6B we do not resort to pylab for this script.

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import sys
import interpolation_and_profile as exc1_2
import affine_transformation as exc3
import perspective_transformation as exc4


def interpolation_and_profile_exercise():
    """ First two exercises:  """
    print "\nto be implemented\n"

    menu()


def affine_transformation_exercise():
    """ Third exercise:  """
    print "\nto be implemented\n"

    menu()


def perspective_transformation_exercise():
    """ Fourth exercise:  """
    print "\nto be implemented\n"

    menu()


def menu():
    """ The main menu. ``fails''= number of invalid choices """
    print '\n --- MAIN MENU ---'
    print '\n [1] Interpolation and profile exercises'
    print '\n [2] Affine transformation exercise'
    print '\n [3] Perspective transformation exercise'
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
            interpolation_and_profile_exercise()
        elif choice == '2':
            affine_transformation_exercise()
        elif choice == '3':
            perspective_transformation_exercise()
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

if __name__ == "__main__":
    print '\n*** Second assignment for Beeldbewerken (2011) ***\n'
    menu()

