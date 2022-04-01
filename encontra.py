def encontra_menores(num,lista):
    for c in range(len(lista)):
        if num > lista[c]: 
            return lista[c]
    else:
        return -1

