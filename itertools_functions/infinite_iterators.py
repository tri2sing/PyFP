'''
Created on Jan 20, 2016

@author: Sameer Adhikari
'''

from itertools import count, cycle, repeat

# Example usage of itertools functions (count, cycle, repeat) that work with infinite iterators.

def custom_enumerate(start, step, data_iterator):
    ''' Enumerates a data series with an arithmetic series [start, start + step, start + 2 * step, ...].
    Unlike a regular enumerate() call where the the arithmetic series is [0, 1, 2,...].'''
    return ((start + step * index, item) for index, item in enumerate(data_iterator))

def custom_enumerate_zip_count(start, step, data_iterator):
    ''' Enumerates a data series with an arithmetic series [start, start + step, start + 2 * step, ...].
    Unlike a regular enumerate() call where the the arithmetic series is [0, 1, 2,...].'''
    return zip(count(start, step), data_iterator)

