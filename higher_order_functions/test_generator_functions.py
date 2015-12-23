'''
Created on Dec 22, 2015

@author: Sameer Adhikari
'''

from higher_order_functions.generator_functions\
    import first_match, is_prime

def test_first_match():
    assert(first_match(lambda x: x % 3 == 0, [2, 3, 4, 5, 6]) == 3)

def test_is_prime():
    assert(is_prime(3) == True)
    assert(is_prime(23) == True)
    assert(is_prime(10) == False)
    assert(is_prime(21) == False)    