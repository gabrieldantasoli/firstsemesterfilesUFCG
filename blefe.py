def blefe(lista):
    diferenca=[]
    for a in range(len(lista)):
        diferenca.append(0)
    for b in range(len(lista)-1):
        if lista[b] < lista[b+1]:
            diferenca[b+1] = lista[b+1]-lista[b]
            lista[b+1] = lista[b]
    return diferenca

