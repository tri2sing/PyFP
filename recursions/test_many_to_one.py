'''
Created on Dec 23, 2015

@author: Sameer Adhikari
'''

from recursions.many_to_one import \
    recursive_product_collection, recursive_product_iterable, tco_product_iterable

def test_product_collection_recursive():
    lst = [1, 2, 3, 4, 5]
    assert(recursive_product_collection(lst) == 120)
    
def test_recursive_product_iterable():
    lst = [1, 2, 3, 4, 5, 6, 7]
    assert(recursive_product_iterable(iter(lst)) == 5040)
    
def test_tco_product_iterable():
    lst = [1, 2, 3, 4, 5, 6]
    assert(tco_product_iterable(iter(lst)) == 720)
    