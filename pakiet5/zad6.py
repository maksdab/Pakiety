words_starting_with_a = lambda words_list: list(filter(lambda word: word.startswith('a'), words_list))

words = ['koło', 'kierownica', 'swiatla', 'zderzak', 'alarm']
print(words_starting_with_a(words))




squares = lambda numbers: list(map(lambda x: x ** 2, numbers))

numbers = [1, 2, 3, 4, 5]
print(squares(numbers))