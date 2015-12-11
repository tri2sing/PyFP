'''
Created on Dec 10, 2015

@author: Sameer Adhikari
'''

from features.generators import prime_factors_loop_and_recursion, prime_factors_only_recursion

def test_prime_factors_loop_and_recursion():
    l1 = [x for x in prime_factors_loop_and_recursion(18)]
    assert(l1 == [2, 3, 3])
    l1 = [x for x in prime_factors_loop_and_recursion(27)]
    assert(l1 == [3, 3, 3])
    l1 = [x for x in prime_factors_loop_and_recursion(17)]
    assert(l1 == [17])
    l1 = [x for x in prime_factors_loop_and_recursion(1900)]
    assert(l1 == [2, 2, 5, 5, 19])


def test_prime_factors_only_recursion():
    l1 = [x for x in prime_factors_only_recursion(18)]
    assert(l1 == [2, 3, 3])
    l1 = [x for x in prime_factors_only_recursion(27)]
    assert(l1 == [3, 3, 3])
    l1 = [x for x in prime_factors_only_recursion(17)]
    assert(l1 == [17])
    l1 = [x for x in prime_factors_only_recursion(1900)]
    assert(l1 == [2, 2, 5, 5, 19])
