def double_list_elements(list):
    newlist=[]

    for element in list:
        newlist.append(element * 2)
    
    return newlist

first_list = [1,23,2,4,3,534]
double_list = double_list_elements(first_list)
print(double_list)


    