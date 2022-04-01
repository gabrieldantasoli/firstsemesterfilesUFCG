entre = 0 
antes = 0
depois = 0

numeros = []

qnumeros = int(input())

for c in range(qnumeros):
    num = int(input())
    numeros.append(num)

print('---')

primeiracomparacao = int(input())
segundacomparacao = int(input())

for c in numeros:
    if c < primeiracomparacao :
        antes += 1
    elif c > primeiracomparacao and c < segundacomparacao :
        entre += 1
    elif c > segundacomparacao :
        depois += 1

print(f'{antes} antes')
print(f'{entre} entre')
print(f'{depois} depois')
