'''
Created on Feb 10, 2016

@author: Sameer Adhikari
'''

from collections import namedtuple
from conditionals.lambda_alternative import \
    lambda_use_nameless, itemgetter_use, \
    lambda_use_named, attrgetter_use

def test_lambda_use():
    data = [(1, 5), (0, 9), (4, 8), (3, 7) , (2, 6)]
    assert(lambda_use_nameless(data, min, 1) == (1, 5))
    
def test_itemgetter_use():
    data = [(1, 5), (0, 9), (4, 8), (3, 7) , (2, 6)]
    assert(itemgetter_use(data, min, 1) == (1, 5))

def test_lambda_use_named():
    Point = namedtuple('Point', ('x', 'y'))
    nameless = [(1, 5), (0, 9), (4, 8), (3, 7) , (2, 6)]
    named = list(Point(*item) for item in nameless)
    assert(lambda_use_named(named, max, 0) == (4, 8))

def test_attrgetter_use():
    Point = namedtuple('Point', ('x', 'y'))
    nameless = [(1, 5), (0, 9), (4, 8), (3, 7) , (2, 6)]
    named = list(Point(*item) for item in nameless)
    assert(attrgetter_use(named, max, 'x') == (4, 8))
