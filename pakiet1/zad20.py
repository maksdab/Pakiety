def process_data(data):
    if isinstance(data, list):
        return [process_data(item) for item in data]
    elif isinstance(data, tuple):
        return tuple(process_data(item) for item in data)
    elif isinstance(data, str):
        return data.upper()
    else:
        return data

data = [1, (2, 3), 'abc', {'a': 1, 'b': 2}]
result = process_data(data)
print(result)
