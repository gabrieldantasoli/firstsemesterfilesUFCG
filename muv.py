#  Velocidade final: 16.30 m/s
#  Velocidade média: 8.80 m/s
#     Posição final: 52.80 m
     
pIni = float(input('Posição inicial? '))
vIni = float(input('Velocidade inicial? '))
time = float(input('Tempo? '))
aceleration = float(input('Aceleração? '))
vFin = vIni + aceleration * time
pFin = pIni + vIni * time + (aceleration * time ** 2) / 2
vMed = (pFin - pIni) / time

print('\nDados da questão')
print('================')

print(f'{"Posição inicial:":>19} {pIni:.2f} m')
print(f'{"Velocidade inicial:":>19} {vIni:.2f} m/s')
print(f'{"Aceleração:":>19} {aceleration:.2f} m/s2')
print(f'{"Tempo:":>19} {time:.2f} s')
print(f'{"Velocidade final:":>19} {vFin:.2f} m/s')
print(f'{"Velocidade média:":>19} {vMed:.2f} m/s')
print(f'{"Posição final:":>19} {pFin:.2f} m')
