'''
Created on Feb 10, 2016

@author: Sameer Adhikari
'''

from operator import itemgetter, attrgetter

# This module demonstrates how to use operator module functions instead of lambda.
# The examples here use tuples, but the usage is not restricted to only them.

def lambda_use_nameless(data, func, index):
    '''
    data: list of tuples to operate on using func.
    func: the function to apply on the data (e.g. min, max).
    index: the number to select the item from each tuple.
    '''
    return func(data, key=lambda item: item[index])

def itemgetter_use(data, func, index):
    return func(data, key=itemgetter(index))

def lambda_use_named(data, func, index):
    '''
    data: list of namedtuples to operate on using func.
    func: the function to apply on the data (e.g. min, max).
    index: the number to select the item from each tuple.
    We don't have a way to send the attribute name as 
    a parameter in this case. We can make it a static
    token in the code.
    '''
    # lambda item: item.x would be a static token version
    # assuming that x is an attribute in the namedtuple.
    return func(data, key=lambda item: item[index])    

def attrgetter_use(data, func, attr_name):
    '''
    data: list of namedtuples to operate on using func.
    func: the function to apply on the data (e.g. min, max).
    attr_name: the string to select the item from each tuple.
    '''
    return func(data, key=attrgetter(attr_name))
