numeros = []

count = 0
soma = 0

qnumeros = int(input())

for num in range(qnumeros):
    numero = int(input())
    numeros.append(numero)
    if numero % 2 == 0:
        count += 1
        soma += numero

media = soma / count
acimaMedia = 0

for num in range(len(numeros)):
    if numeros[num] > media: 
        acimaMedia += 1

print(f'média dos pares: {media:.1f}')
print(f'acima da média: {acimaMedia}')
