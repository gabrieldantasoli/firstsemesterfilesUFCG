def matriz_menor(m1,m2):
    matrizRetorno = []
    linha = []
    for a in range(len(m1)):
        for b in range(len(m1[a])):
            if m1[a][b] <= m2[a][b]:
                linha.append(m1[a][b])
            else:
                linha.append(m2[a][b])
        matrizRetorno.append(linha[:])
        for c in range(len(linha)):
            linha.pop()
    return matrizRetorno
