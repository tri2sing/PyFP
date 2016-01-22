'''
Created on Jan 22, 2016

@author: Sameer Adhikari
'''

from itertools import accumulate, tee
from operator import mul

def running_stats(data_iterator):
    ''' Returns iterators for the running min, max, product, and sum.'''
    # Replicate the input iterator as an iterator can be used only once.
    i1, i2, i3, i4 = tee(data_iterator, 4)
    rmin = accumulate(i1, min)
    rmax = accumulate(i2, max)
    rprd = accumulate(i3, mul)
    rsum  = accumulate(i4)
    return rmin, rmax, rprd, rsum