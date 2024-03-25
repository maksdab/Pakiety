def map_nested(lista, funkcja):
    wynik = [] 
    
    for element in lista:
        if isinstance(element, list):
            wynik.append(map_nested(element, funkcja)) 
        else:
            wynik.append(funkcja(element))  
    
    return wynik

def double(x):
    return x * 2

moja_lista = [1, 2, [3, 4, [5, 6]], 7, [8, 9]]
wynik = map_nested(moja_lista, double)
print(wynik)