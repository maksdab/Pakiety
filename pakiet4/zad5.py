def split_list(list_to_split, length):
    return [list_to_split[i:i + length] for i in range(0, len(list_to_split), length)]

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(split_list(test_list, 3))
