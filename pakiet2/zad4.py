numbers = [1,3,6,9,12,15,18,21,24,27,30]

squares = [square for num in numbers if (square := num ** 2) > 10]

print(squares)