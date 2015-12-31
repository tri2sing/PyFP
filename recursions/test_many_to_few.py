'''
Created on Dec 30, 2015

@author: Sameer Adhikari
'''

import pytest

from recursions.many_to_few import \
    freq_dist_imperative, \
    freq_dist_declarative, \
    group_creation_recursive, \
    group_creation_iterative

# A trivial use of fixtures to learn the concept.
@pytest.fixture(scope='module')
def data():
    divisor = 3 
    inlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    return inlist, divisor

def test_freq_dist_imperative(data):
    inlist, divisor = data
    outlist = freq_dist_imperative(inlist, divisor)
    assert len(outlist) == 5
    for key, value in outlist:
        if key == 0:
            assert value == 2
        if key == 4:
            assert value == 1
            
def test_freq_dist_declarative(data):
    inlist, divisor = data
    outdict = dict(freq_dist_declarative(inlist, divisor))
    assert outdict[0] == 2
    assert outdict[4] == 1
    
def test_group_creation_recursive(data):
    inlist, divisor = data
    key_func = lambda x: x // divisor
    outdict = group_creation_recursive(key_func, inlist)
    assert len(outdict[0]) == 2
    assert len(outdict[4]) == 1

def test_group_creation_iterative(data):
    inlist, divisor = data
    key_func = lambda x: x // divisor
    outdict = group_creation_iterative(key_func, inlist)
    assert len(outdict[0]) == 2
    assert len(outdict[4]) == 1
    