'''
Created on Dec 23, 2015

@author: Sameer Adhikari
'''

def recursive_product_collection(collection):
    '''A recursive function that takes a collection and returns a product of the elements.
    This is a fold-right reduction method; operator is applied right-to-left direction.
    Some constraints that it suffers from: 
        Works only with collections as it needs support for len() function.
        Creates a large number of lists in each recursion level due to the [1: ] slice.
        Has the default 1000 depth level limit for recursion.'''
    if len(collection) == 0: return 1
    return collection[0] * recursive_product_collection(collection[1:])

def recursive_product_iterable(interable):
    '''A recursive function that takes an iterable and returns a product of the elements.
    As it uses an iterable, len() function is not defined.
    This is a fold-right reduction method; operator is applied right-to-left direction.'''
    try: 
        head = next(interable)
    except StopIteration:
        return 1
    return head * recursive_product_iterable(interable)

def tco_product_iterable(iterable):
    '''A tail-call optimization for the recursive functions shown above.
    This is a fold-left reduction: the operators are folded into the iterable left-to-right.
    '''    
    prod = 1
    for item in iterable:
        prod *= item
    return prod
