def apply_function_to_list(input_list, function):
    return [function(element) for element in input_list]

test_list = [1, 2, 3, 4, 5]
double_function = lambda x: x * 2
print(apply_function_to_list(test_list, double_function))  
