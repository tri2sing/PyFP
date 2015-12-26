'''
Created on Dec 24, 2015

@author: Sameer Adhikari
'''

from collections import Counter

print(82*'=')
N = 3  # The number of partitions will be either N or N + 1.
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
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


            