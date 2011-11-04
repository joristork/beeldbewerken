"""
:synopsis:  Tests and plots the performance of a function for a series of values
            of parameters to that function.

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import timeit
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import beeld_4th_assignment
import functions

def test_performance(module, statements, functions, nr_calls):
    """ 
    Calls timeit.Timer.timeit() with given parameters; prints and plots results.
    Note that the functions list also serves as an index, and that it should
    match up with the function list in the caller function.
    
    """
    results = []
    print '\nAverage time, by implememtation:'
    print '(%d function calls)\n'%(nr_calls)
    i = 1
    for statement in statements:
        print statement
        results.append(timeit.Timer(statement, 
                "from "+module+" import "+functions[i-1]).timeit(nr_calls))
        print '---> '+statement+': %f' % results[i-1]
        i += 1

    raw_input('\nA plot of performance results follows (press enter):')
    i = 0
    for result in results:
        results[i] = result / nr_calls
        i += 1
    nr_bars = len(statements)
    bars_y = np.arange(nr_bars) + 0.5 
    plt.subplot(111)
    plt.rects = plt.barh(bars_y, results, align='center', color='y')
    plt.yticks(bars_y, (statements))
    plt.xlabel('Mean execution time (seconds)')
    plt.grid(True)
    plt.show()
