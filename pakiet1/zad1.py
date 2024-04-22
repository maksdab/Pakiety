def apply_twice(func, value):
    return func(func(value))

result = apply_twice(lambda x: x * 2, 3)
print(result)  
