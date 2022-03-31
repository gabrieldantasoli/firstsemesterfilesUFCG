def cobrinha(lista):
    qual=0
    retorno = []
    for c in range(len(lista)):
        if qual % 2 != 0:
            for a in range(len(lista[c])-1,-1,-1):
                if lista[c][a] % 2 != 0:
                    retorno.append(lista[c][a])
        else:
            for a in range(len(lista[c])):
                if lista[c][a] % 2 != 0:
                    retorno.append(lista[c][a])
        qual += 1
    return retorno

