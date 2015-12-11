'''
Created on Dec 10, 2015

@author: Sameer Adhikari
'''
import math

# A few things to note:
# 1. In a recursive generator use "yield from" (which returns generated values) 
#    Do not just "yield" (which returns only the generator object)
# 2. loop_and_recursion allows a number with up to 1000 factors (at least 2^1000, a 300 digit number)
# 3. only_recursion allows a number subject to 1000 recursions (up to about 4,000,000)

def prime_factors_loop_and_recursion(x):
    if x % 2 == 0:
        yield 2
        if x // 2 > 1:
            yield from prime_factors_loop_and_recursion(x // 2)
        return
    for i in range(3, int(math.sqrt(x) + 0.5) + 1, 2):
        if x % i == 0:
            yield i
            if x // i > 1:
                yield from prime_factors_loop_and_recursion(x // i)
            return
    yield x
    

def prime_factors_only_recursion(x):
    def factor_n(x, n):
        if n * n > x:
            yield x
            return
        if x % n == 0:
            yield n
            if x // n > 1:
                yield from factor_n(x // n, n)
        else:
            yield from factor_n(x, n + 2)
    if x % 2 == 0:
        yield 2
        if x // 2 > 1:
            yield from prime_factors_only_recursion(x // 2)
        return
    yield from factor_n(x, 3)
    
# print([x for x in prime_factors_only_recursion(18)])
                
