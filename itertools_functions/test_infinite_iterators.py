'''
Created on Jan 20, 2016

@author: Sameer Adhikari
'''

from itertools_functions.infinite_iterators import custom_enumerate, custom_enumerate_zip_count


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
