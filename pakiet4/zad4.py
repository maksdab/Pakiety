def power_function(exponent):
    return lambda x: x ** exponent

power_square = power_function(2)
print(power_square(3)) 
