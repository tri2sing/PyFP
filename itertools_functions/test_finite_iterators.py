'''
Created on Jan 22, 2016

@author: Sameer Adhikari
'''

from itertools_functions.finite_iterators import running_stats

def test_running_stats():
    rmin, rmax, rprd, rsum = running_stats(range(1,6))
    exprmin = [1, 1, 1, 1, 1]
    exprmax = [1, 2, 3, 4, 5]
    exprprd = [1, 2, 6, 24, 120]
    exprsum = [1, 3, 6, 10, 15]
    assert(exprmin == list(rmin))
    assert(exprmax == list(rmax))
    assert(exprprd == list(rprd))
    assert(exprsum == list(rsum))
    
