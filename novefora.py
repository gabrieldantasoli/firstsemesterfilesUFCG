def noves_fora(lista):
    listaRetorno = []
    while True:
        if len(lista) > 0:
            if lista[0] == 9:
                listaRetorno.append(lista[:])
                lista.pop(0)
            elif lista[0] > 9:
                lista[0] -= 9
            elif lista[0] < 9:
                if len(lista) > 1:
                    lista[0] += lista[1]
                    lista.pop(1)
                for a in range(len(lista)):
                    for b in range(len(lista)-1):
                        if lista[b] < lista[b+1]:
                            lista[b] , lista[b+1] = lista[b+1] , lista[b]
                listaRetorno.append(lista[:])
        if len(lista) <= 1: break
    return ((0,listaRetorno))

print(noves_fora([9])
