def maior_slice(lista):
    sublista = ''
    ok = True
    for num in range(len(lista)-1):
        if lista[num] < lista[num+1]:
            sublista += str(lista[num])
        elif lista[num] > lista[num-1]:
            sublista += str(lista[num])
    return sublista


sublista = maior_slice([1,2,3,4,3,4,5,6])

print(sublista)
