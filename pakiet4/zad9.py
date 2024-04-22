def apply_function_to_tuples_list(tuple_list, function):
    return [function(*tuple_element) for tuple_element in tuple_list]

test_tuples = [(1, 2), (3, 4), (5, 6)]
add_function = lambda x, y: x + y
print(apply_function_to_tuples_list(test_tuples, add_function))
