def recursive_sum(nList):
    sum = 0
    
    for element in nList:
        if isinstance(element, list):
            sum += recursive_sum(element)
        else:
            sum += element
    
    return sum

new_list = [4, 6, [2, 5, [3, 1, 3]], 9, [6, 32]]
result = recursive_sum(new_list)
print(result)