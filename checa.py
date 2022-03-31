# UNIVERSIDADE FEDERAL DE CAMPINA GRANDE - UFCG
# GABRIEL DANTAS DE OLIVEIRA - 121110669
#//2022 
#Programação 1 - checa sequencia de digitos

digitos = input()
limite = int(input())

digitosImpares = 0
lidos = 0

index = 0
soma = 0
numerosLidos = 0
criterioParada = ''

while True:
    soma += int(digitos[index])
    numerosLidos += 1
    if int(digitos[index]) % 2 != 0: digitosImpares += 1
    if digitosImpares == 6:
        criterioParada = '6 ímpares'
    elif soma >= limite:
        criterioParada = 'limite'
    elif index >= len(digitos) - 1:
        criterioParada = 'final da sequência'
    if soma >= limite or digitosImpares >= 6 or index == len(digitos) - 1: break
    index += 1

print(f'soma: {soma}')
print(f'números lidos: {numerosLidos} de {len(digitos)}')
print(f'critério de parada: {criterioParada}')

