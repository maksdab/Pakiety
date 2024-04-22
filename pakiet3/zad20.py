def sum_of_squares_of_odds(input_list):
    return sum(x ** 2 for x in input_list if x % 2 != 0)


input_list = [1, 2, 3, 4, 5]
print(sum_of_squares_of_odds(input_list)) 
