'''
Created on Dec 22, 2015

@author: Sameer Adhikari
'''

import math

def first_match(predicate, collection):
    '''Apply the predicate to every value in the collection.
    Return the first_match value for which the predicate is true. '''
    for x in collection:
        if predicate(x): return x
        

def is_prime(x):
    if x == 2: return True
    if x % 2 == 0: return False
    factor = first_match(lambda n: x % n == 0, range(3, int(math.sqrt(x) + 0.5) + 1, 2))
    return factor is None
