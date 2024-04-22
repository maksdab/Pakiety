parzyste = lambda lista: list(filter(lambda x: x % 2 == 0, lista))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(parzyste(numbers))
