nomes = ['abreu','antonio','beatriz','cesar','davi','jose','marcos','medeiros','oliveira','silva']


while True:
    nome1 = input('nome 1? ')
    nome2 = input('nome 2? ')
    nome3 = input('nome 3? ')
    indexn1 = 0 
    indexn2 = 0
    indexn3 = 0
    for p in range(len(nomes)):
        print(p)
        if nomes[p] == nome1:
            indexn1 = p
        if nomes[p] == nome2:
            indexn2 = p
        if nomes[p] == nome3:
            indexn3 = p
    if indexn1 < indexn2 and indexn2 < indexn3:
        print(f'{nomes[indexn1]} {nomes[indexn2]} de {nomes[indexn3]}')
        break
    else:
        print('nomes inválidos: tente novamente')
