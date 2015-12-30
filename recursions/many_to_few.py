'''
Created on Dec 24, 2015

@author: Sameer Adhikari
'''

from collections import Counter, defaultdict
from pprint import pprint

print(82*'=')
N = 3  # The number of partitions will be either N or N + 1.
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print('The original list is \n\t{}'.format(l1))
l2 = [i // N for i in l1]
print('Integer division by N = {n} gives quantized list\n\t{lst}'.format(n=N, lst=l2))

print(82*'=')
print('Frequency distribution of the quantized list using collections.Counter.')
print('This version uses a stateful object to map the keys to groups.')
ctr = Counter(l2)
print(ctr.most_common())

def frequecy_distribution(data):
    sorted_data = iter(sorted(data))
    previous, count = next(sorted_data), 1
    for item in sorted_data:
        if item == previous:
            count += 1
        elif previous is not None: # and item! = previous
            yield previous, count
            previous, count = item, 1
        else: 
            raise Exception('Bad data; possible design issue?')
        yield previous, count
        
print(82*'=')
print('Frequency distribution of the quantized list using sorting and counting.')
print('This is a functional programming version that uses a generator function.')
print(dict(frequecy_distribution(l2)))
print(82*'=')

quantizer = lambda x: x//N # integer division

def group_creator(keygen_func, data):
    def group_creator_recursive(keygen_func, collection, output_dict):
        if len(collection) == 0:
            return output_dict
        head, *tail = collection
        output_dict[keygen_func(head)].append(head)
        return group_creator_recursive(keygen_func, tail, output_dict)
    return group_creator_recursive(keygen_func, data, defaultdict(list))

print('Data distribution with actual values in each quanta using recursion')        
group_result = group_creator(quantizer, l1)
for key in group_result:
    print('{}: {}'.format(key, group_result[key]))
print(82*'=')
        
def group_creator_tco(keygen_func, data):
    output_dict = defaultdict(list)
    for item in data:
        output_dict[keygen_func(item)].append(item)
    return output_dict

print('Data distribution with actual values in each quanta using iteration (tco)')        
group_result_tco = group_creator_tco(quantizer, l1)
for key in group_result_tco:
    print('{}: {}'.format(key, group_result_tco[key]))
print(82*'=')



            