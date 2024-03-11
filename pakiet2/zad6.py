def safe_function(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"Error: {e}")
            return None
    return wrapper

@safe_function
def divide(a, b):
    return a / b

result1 = divide(10, 0)  
print(result1)

result2 = divide(10, 2)  
print(result2)
