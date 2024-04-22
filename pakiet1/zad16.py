def compose(func1, func2):
    return lambda x: func1(func2(x))

def square(x):
    return x ** 2

def add_one(x):
    return x + 1

composed_function = compose(square, add_one)
result = composed_function(3)
print(result)
