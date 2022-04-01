def insere_ordenado_primeiro(lista):
    for a in range(len(lista)-1):
        if lista[a] > lista[a+1]:
            lista[a],lista[a+1] = lista[a+1] , lista[a]
    return lista

print('ok')
