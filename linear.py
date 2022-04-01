def busca(seq,valor):
    num = 0
    for a in range(len(seq)):
        if seq[a] == valor:
            num += 1
        if num > 1: return 1
    position = -1
    for a in range(len(seq)):
        if seq[a] == valor:
            position = a
    return position


print(busca([8,9,2,3,6,10,7,9,11],11))
