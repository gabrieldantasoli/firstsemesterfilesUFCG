reprovados = 0

while True:
    chamada = input()
    if chamada == '-': break
    tamanho = 0
    reprovado = 0
    while True:
        if tamanho == len(chamada): break
        if chamada[tamanho] == 'f':
            reprovado += 1
        if reprovado > 8:
            reprovados += 1
            break
        tamanho += 1

print(f'{reprovados} aluno(s) reprovado(s) por falta.')
