
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Nie można dzielić przez zero!"

def power(a, b):
    return a ** b

print(add(3, 4))  
print(subtract(10, 5))  
print(multiply(2, 6)) 
print(divide(8, 2))  
print(power(2, 3))  