
def rotate_list(input_list, steps):
    if not input_list:
        return []
    steps %= len(input_list)
    return input_list[-steps:] + input_list[:-steps]


input_list = [1, 2, 3, 4, 5]
steps = 2
print(rotate_list(input_list, steps)) 
