def find_max_min_diff(input_list):
    if not input_list:
        return None
    return max(input_list) - min(input_list)

input_list = [1, 5, 9, 2, 8]
print(find_max_min_diff(input_list))
