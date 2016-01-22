'''
Created on Jan 20, 2016

@author: Sameer Adhikari
'''

from itertools_functions.infinite_iterators import custom_enumerate, custom_enumerate_zip_count, divisible_by_n


def test_custom_enumerate():
    given = [1, 2, 3, 4, 5]
    returned = list(custom_enumerate(1, 3, iter(given)))
    expected = [(1, 1), (4, 2), (7, 3), (10, 4), (13, 5)]
    assert(returned == expected)
    
def test_custom_enumerate_zip_count():
    given = [1, 2, 3, 4, 5]
    returned = list(custom_enumerate_zip_count(1, 3, iter(given)))
    expected = [(1, 1), (4, 2), (7, 3), (10, 4), (13, 5)]
    assert(returned == expected)

def test_divisible_by_n():
    returned = list(divisible_by_n(15, 3))
    expected = [0, 3, 6, 9, 12, 15]
    assert (returned == expected)
    
    returned = list(divisible_by_n(15, 5))
    expected = [0, 5, 10, 15]
    assert (returned == expected)    