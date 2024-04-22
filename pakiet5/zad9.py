from functools import reduce

find_max = lambda numbers: reduce(lambda x, y: x if x > y else y, numbers)
calculate_average = lambda numbers: reduce(lambda x, y: x + y, numbers) / len(numbers)


numbers = [1, 3, 8, 9, 4, 7, 5]
print(find_max(numbers))
print(calculate_average(numbers))
