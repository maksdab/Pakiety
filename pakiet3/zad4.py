def remove_duplicates(nList):
    unikalne_elementy = list(set(nList))
    return unikalne_elementy


new_list = [1,9,2,3,2,3,4,6,6,4,4,5]
unique = remove_duplicates(new_list)
print(unique)