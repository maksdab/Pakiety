def square_number(number):
    return number ** 2

def add_five(number):
    return number + 5

def apply_functions_to_list(numbers_list, *functions):
    result = []
    for number in numbers_list:
        for func in functions:
            number = func(number)
        result.append(number)
    return result

numbers = [1, 2, 3, 4, 5]
print(apply_functions_to_list(numbers, square_number, add_five))  

