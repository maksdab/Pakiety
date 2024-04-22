def merge_dictionaries(*args):
    result = {}
    for dictionary in args:
        for key, value in dictionary.items():
            result[key] = result.get(key, 0) + value
    return result

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dictionaries(dict1, dict2))