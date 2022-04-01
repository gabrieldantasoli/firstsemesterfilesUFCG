def diferenca_listas(lista1,lista2):
    for a in range(len(lista2)):
        x=0
        while x < len(lista1):
            if lista2[a] == lista1[x]:
                lista1.pop(x)
            x+=1
