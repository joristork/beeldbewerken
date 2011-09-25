"""
:synopsis:  Tests and plots the performance of a list of functions callable via
            a ``calling function''. See linfilter() in linfilters.py for an
            example.

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import timeit
from linfilters import linfilter
import numpy as np
import matplotlib.pyplot as plt

def test_performance(module, caller, function_names, nr_calls, other_params):
    """ 
    Calls timeit.Timer.timeit() with given parameters; prints and plots results.
    Note that the function_names also serves as an index, and that it should
    match up with the function list in the caller function.
    
    """
    results = []
    print '\nAverage time, by implememtation:'
    print '(%d function calls)\n'%(nr_calls)
    i = 1
    for function_name in function_names:
        caller_params = ('%d'% i)+other_params 
        results.append(timeit.Timer(caller+'('+caller_params+')', 
                "from "+module+" import "+caller).timeit(nr_calls))
        print '---> '+function_name[0:-2]+': %f' % results[i-1]
        i += 1

    raw_input('\nA plot of performance results follows (press enter):')
    i = 0
    for result in results:
        results[i] = result / nr_calls
        i += 1
    nr_bars = len(function_names)
    bars_y = np.arange(nr_bars) + 0.5 
    plt.subplot(111)
    plt.rects = plt.barh(bars_y, results, align='center', color='y')
    plt.yticks(bars_y, (function_names))
    plt.xlabel('Mean execution time (seconds)')
    plt.grid(True)
    plt.show()
