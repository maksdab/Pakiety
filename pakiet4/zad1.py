def sum_even_numbers(numbers_list):
    return sum(x for x in numbers_list if x % 2 == 0)


test_list = [1, 2, 3, 4, 5, 6]
print(sum_even_numbers(test_list))
