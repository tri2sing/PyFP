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

def divisible_by_n(limit, n):
    ''' Returns a iterator for the subset of integers in [0, limit] divisible by n.
    Please note that this is an example of the use of the cycle() function.
    It is not the most efficient solution to the problem of divisible by n.'''
    cycle_n = (i == 0 for i in cycle(range(n)))
    matches = zip(range(limit + 1), cycle_n)
    return (num for num, match in matches if match == True)
    