'''
Created on Dec 18, 2015

@author: Sameer Adhikari
'''

''' Examples of various methods of creating pairs of items from a given iterable. 
'''

def pairs_zip(iterable):
    return zip(iterable, iterable[1:])

def pairs_recursion(iterator):
    '''Purely FP version'''
    def pairs_recursion_internal(head_item, tail_iterator):
        # Consume one item from the iterator
        next_item = next(tail_iterator)
        yield head_item, next_item
        yield from pairs_recursion_internal(next_item, tail_iterator)
    #Set up the recursion and handle the iterator exhaustion
    try:
        return pairs_recursion_internal(next(iterator), iterator) 
    except StopIteration:
        return 
    
def pairs_loop(iterator):
    '''Replace recursion with generator to perform tail call optimization.
    Uses a for loop with state, but no change from a user perspective.
    Removes the limits of recursion all inevitable in the pure FP version.'''
    begin = next(iterator)
    for end in iterator:
        yield begin, end
        begin = end
    