'''
Created on Feb 10, 2016

@author: Sameer Adhikari
'''

# An example of a function with strict ordering.
def factorial_strict(n):
    if n == 0: 
        return 1
    elif n == 1: 
        return 1
    else:
        return factorial_strict(n - 1) * n
     

# Same example with relaxation of strict ordering.
# Dictionary keys and lambda are used to mimic the strictly-ordered function.
# At any recursion level there are only two keys in the dictionary: True and False.
def factorial_relaxed(n):
    f = {
         n == 0: lambda n: 1,
         n == 1: lambda n: 1,
         n > 1: lambda n: factorial_relaxed(n - 1) * n
        }[True]
    return f(n)

        
