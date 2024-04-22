def most_frequent_element(input_list):
    return max(set(input_list), key=input_list.count)

test_list = [1, 2, 3, 2, 2, 4, 5, 2]
print(most_frequent_element(test_list))
