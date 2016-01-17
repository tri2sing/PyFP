'''
Created on Jan 11, 2016

@author: Sameer Adhikari
'''

from collections import defaultdict

# In some cases, with the use of a bunch of tuples we can avoid the use of classes.
# The reason to avoid classes it that classes have to maintain state.
# Consider the process of assigning ranks to a sequence using a ranking function.
# The goal is to rank each item along multiple dimensions.

def rank_nested_simple(data, key_function=lambda obj:obj):
    '''Returns nested tuple when ranking along multiple dimensions.
    It does not handle ties as expected in statistical measures.'''
    return (enumerate(sorted(data, key=key_function)))

def rank(data, key_function=lambda obj:obj):
    '''Return a generator with the rank of the data items.
    It uses the key function to extract the key field to rank the items.
    The default key function returns the given item itself as the key.'''
    def create_duplicates_map(data_iterator, key_function):
        '''Iterates through the data sequence and groups duplicates together.
        Returns a dictionary where key maps to a list of the duplicates.
        This is a stateful object (TCO version of a recursion).'''
        duplicates = defaultdict(list)
        for item in data_iterator:
            duplicates[key_function(item)].append(item)
        return duplicates
    
    def generate_ranks(duplicates_map, sorted_key_iterator, base_rank=0):
        '''The function expects a map from the keys to the list of items for the key,
         An iterator for the keys in sorted order, and a base rank to start.'''
        for key in sorted_key_iterator:
            num_dups = len(duplicates_map[key]) # num_dups == 1 => one element, no duplicates
            # yield the rank for each value based on the number of duplicates
            for value in duplicates_map[key]:
                yield (base_rank + 1 + base_rank + num_dups)/2, value
            base_rank += num_dups
            
    duplicates_map = create_duplicates_map(iter(data), key_function)
    return (generate_ranks(duplicates_map, iter(sorted(duplicates_map)), 0))
