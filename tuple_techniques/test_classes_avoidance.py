'''
Created on Jan 16, 2016

@author: Sameer Adhikari
'''

from tuple_techniques.classes_avoidance import rank, rank_nested_simple

def test_rank_nested_simple():
    data = [0.8, 1.2, 1.2, 2.3, 18]
    returned = list(rank_nested_simple(data))
    expected = [(0, 0.8), (1, 1.2), (2, 1.2), (3, 2.3), (4, 18)]
    assert(returned == expected)
    
    data= ((2, 0.8), (3, 1.2), (5, 1.2), (7, 2.3), (11, 18))
    returned = list(rank_nested_simple(data, key_function=lambda x:x[1]))
    expected = [(0, (2, 0.8)), (1, (3, 1.2)), (2, (5, 1.2)), (3, (7, 2.3)), (4, (11, 18))]
    assert(returned == expected)

    data = expected
    returned = list(rank_nested_simple(data, key_function=lambda x:x[1][0]))
    expected = [(0, (0, (2, 0.8))), (1, (1, (3, 1.2))), (2, (2, (5, 1.2))), (3, (3, (7, 2.3))), (4, (4, (11, 18)))]
    assert(returned == expected)

    
def test_rank():
    data = [0.8, 1.2, 1.2, 2.3, 18]
    returned = list(rank(data))
    expected = [(1.0, 0.8), (2.5, 1.2), (2.5, 1.2), (4.0, 2.3), (5.0, 18)]
    assert(returned == expected)
    
    data = ((2, 0.8), (3, 1.2), (5, 1.2), (7, 2.3), (11, 18))
    returned = list(rank(data, key_function=lambda x:x[1]))
    expected = [(1.0, (2, 0.8)), (2.5, (3, 1.2)), (2.5, (5, 1.2)), (4.0, (7, 2.3)), (5.0, (11, 18))]
    assert(returned == expected)

    data = expected
    returned = list(rank(data, key_function=lambda x:x[1][0]))
    expected = [(1.0, (1.0, (2, 0.8))), (2.0, (2.5, (3, 1.2))), (3.0, (2.5, (5, 1.2))), (4.0, (4.0, (7, 2.3))), (5.0, (5.0, (11, 18)))]
    assert(returned == expected)
