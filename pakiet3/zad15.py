def custom_sort(input_list, key_function):
    return sorted(input_list, key=key_function)

input_list = ['pustak', 'beton', 'asfalt', 'okno']
print(custom_sort(input_list, len)) 
