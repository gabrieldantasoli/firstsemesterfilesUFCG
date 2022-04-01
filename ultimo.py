def ultimo_indice(num,lista):
    position = -1
    for a in range(len(lista)):
        if lista[a] == num:
            position = a
    return position


