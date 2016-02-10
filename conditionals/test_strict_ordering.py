'''
Created on Feb 10, 2016

@author: Sameer Adhikari
'''

from conditionals.strict_ordering import factorial_strict, factorial_relaxed

def test_factorial_strict():
    assert(factorial_strict(2) == 2)
    assert(factorial_strict(5) == 120)

def test_factorial_relaxed():
    assert(factorial_relaxed(2) == 2)
    assert(factorial_relaxed(5) == 120)
