def make_multiplier(multiplier):
    return lambda x: x * multiplier

multiply_by_3 = make_multiplier(3)
result = multiply_by_3(5)
print(result)
