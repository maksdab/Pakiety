from itertools import permutations

def list_permutations(input_list):
    return list(permutations(input_list))

test_list = [1, 2, 3]
print(list_permutations(test_list)) 
