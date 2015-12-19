'''
Created on Dec 18, 2015

@author: Sameer Adhikari
'''

from work_with_collections.sequence_pairs import \
    pairs_zip, pairs_recursion, pairs_loop

def test_pairs_zip():
    l = [1, 2, 3, 4, 5]
    pairs = tuple(pairs_zip(l))
    assert(len(pairs) == 4)
    assert(len(pairs[0]) == 2)    
    
def test_pairs_recursion():
    l = [1, 2, 3, 4, 5]
    # 'list' is not an iterator as it does not implement the 'next' method.
    # So we have to use the 'iter' built-in method to create an iterator.
    pairs = tuple(pairs_recursion(iter(l)))
    assert(len(pairs) == 4)
    assert(len(pairs[0]) == 2)    
    
def test_pairs_loop():
    l = [1, 2, 3, 4, 5]
    pairs = tuple(pairs_loop(iter(l)))
    assert(len(pairs) == 4)
    assert(len(pairs[0]) == 2)    