pini = input()
pini = pini.split()
linha = int(pini[0])
coluna = int(pini[1])

passos = 0
while True:
    jogada = input()
    if jogada == 'X': break
    jogada = jogada.split()
    passos += int(jogada[1])
    if jogada[0] == 'C':
        linha -= int(jogada[1])
    if jogada[0] == 'B':
        linha += int(jogada[1])
    if jogada[0] == 'E':
        coluna -= int(jogada[1])
    if jogada[0] == 'D':
        coluna += int(jogada[1])
    print(f'> {linha} {coluna}')

print(passos)
