global_variable = 10

def function_with_global_variable():
    global global_variable
    global_variable += 5

def function_with_function_variable():
    local_variable = 5
    
    def inner_function():
        nonlocal local_variable
        local_variable += 10
    
    inner_function()
    return local_variable


function_with_global_variable()
print(global_variable)

print(function_with_function_variable())
