jogadores = 0
while True:
    player = input()
    if player == '-':break
    jogadores += 1

if jogadores == 11:
    print('Modalidade -> Futebol')
if jogadores == 5:
    print('Modalidade -> Basquete')
if jogadores == 6:
    print('Modalidade -> Vôlei')
if jogadores == 7:
    print('modalidade -> Handebol')
