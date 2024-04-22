def remove_whitespace(input_list):
    return [word.strip() for word in input_list]

input_list = ['  jabłko  ', 'banan  ', '  pomarańcza', '  kiwi  ']
print(remove_whitespace(input_list)) 
