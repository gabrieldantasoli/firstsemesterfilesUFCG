def bubblesort(lista):
    for a in range(len(lista)-1):
        ha_trocas = False
        for i in range(len(lista) - 1 - a):
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                ha_trocas = True
        if not ha_trocas: return

