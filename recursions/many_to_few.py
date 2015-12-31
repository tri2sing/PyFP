'''
Created on Dec 24, 2015

@author: Sameer Adhikari
'''

from collections import Counter, defaultdict

def freq_dist_imperative(data, divisor):
    '''Imperative version of the frequency distribution function.'''
    data_divided = [item //divisor for item in data]
    counter = Counter(data_divided)
    return counter.most_common()


def freq_dist_declarative(data, divisor):
    '''Declarative (functional) version of the frequency distribution function.'''
    data_divided = [item //divisor for item in data]
    sorted_data = iter(sorted(data_divided))
    previous, count = next(sorted_data), 1
    for item in sorted_data:
        if item == previous:
            count += 1
        elif previous is not None:  # and item! = previous
            yield previous, count
            previous, count = item, 1
        else: 
            raise Exception('Bad data; possible design issue?')
        yield previous, count
        

def group_creation_recursive(key_func, data):
    '''Recursive version of the function to group the data using the provided key function.'''
    def group_creator_internal(key_func, collection, output_dict):
        if len(collection) == 0:
            return output_dict
        head, *tail = collection
        output_dict[key_func(head)].append(head)
        return group_creator_internal(key_func, tail, output_dict)
    return group_creator_internal(key_func, data, defaultdict(list))


def group_creation_iterative(key_func, data):
    '''Tail-call-optimized version of the recursive function to group the data using the provided key function.'''
    output_dict = defaultdict(list)
    for item in data:
        output_dict[key_func(item)].append(item)
    return output_dict


def main():
    print(82 * '=')
    divisor = 3  # Divisor for integer division
    print('The divisor for grouping the data is {}'.format(divisor))
    datalist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print('The original list is \n\t{}'.format(datalist))
    
    print(82 * '=')
    print('Frequency distribution of the quantized list using collections.Counter.')
    print('This version uses a stateful object to map the keys to groups.')
    print(freq_dist_imperative(datalist, divisor))

    print(82 * '=')
    print('Frequency distribution of the quantized list using sorting and counting.')
    print('This is a functional programming version that uses a generator function.')
    print(dict(freq_dist_declarative(datalist, divisor)))
    print(82 * '=')
    
    key_func = lambda x: x // divisor  # integer division

    print('Data distribution with actual values in each quanta using recursion')        
    group_result = group_creation_recursive(key_func, datalist)
    for key in group_result:
        print('{}: {}'.format(key, group_result[key]))
    print(82 * '=')
        
    print('Data distribution with actual values in each quanta using iteration (tco of recursion)')        
    group_result_tco = group_creation_iterative(key_func, datalist)
    for key in group_result_tco:
        print('{}: {}'.format(key, group_result_tco[key]))
    print(82 * '=')

    
if __name__ == '__main__':
    main()


            
