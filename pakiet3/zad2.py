def filter_long_words(string_list):

    length =[len(s) for s in string_list]

    avg_length = sum(length) / len(length)

    result = [s for s in string_list if len(s) > avg_length]

    return result 

list = ["Sztuczna", "IT", "Python", "Visual STudio", "Java"]
result = filter_long_words(list)
print(result)

