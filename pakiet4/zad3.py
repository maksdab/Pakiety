def filter_even(dictionary):
    return {k: v for k, v in dictionary.items() if v % 2 == 0}


test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(filter_even(test_dict))
